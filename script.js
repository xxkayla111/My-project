/* 交互粒子 + 音乐可视化
   功能：
   - 粒子跟随、排斥、爆发
   - 粒子间连线
   - 音频播放（上传本地文件）
   - 使用 Web Audio API 的 AnalyserNode 将频谱映射到粒子属性
   说明：浏览器需要用户交互才能启动 AudioContext，请点击 Play。
*/

(() => {
  const canvas = document.getElementById('canvas');
  const ctx = canvas.getContext('2d');

  let W = canvas.width = innerWidth;
  let H = canvas.height = innerHeight;

  // UI 元素
  const playBtn = document.getElementById('playBtn');
  const pauseBtn = document.getElementById('pauseBtn');
  const audioEl = document.getElementById('audio');
  const fileInput = document.getElementById('audioFile');
  const volumeEl = document.getElementById('volume');
  const spectrumToggle = document.getElementById('spectrumToggle');
  const connectToggle = document.getElementById('connectToggle');
  const resetBtn = document.getElementById('resetBtn');

  // 画布缩放适配
  function resize() {
    W = canvas.width = innerWidth;
    H = canvas.height = innerHeight;
  }
  addEventListener('resize', resize);

  // 鼠标交互
  const mouse = { x: W / 2, y: H / 2, down: false };
  canvas.addEventListener('mousemove', (e) => {
    const rect = canvas.getBoundingClientRect();
    mouse.x = e.clientX - rect.left;
    mouse.y = e.clientY - rect.top;
  });
  canvas.addEventListener('mousedown', (e) => { mouse.down = true; spawnBurst(mouse.x, mouse.y); });
  canvas.addEventListener('mouseup', () => { mouse.down = false; });
  canvas.addEventListener('click', () => { connectToggle.checked = !connectToggle.checked; });

  // 粒子系统参数
  const NUM = Math.floor(Math.max(60, (W * H) / (1600))); // 根据屏幕大小自适应数量
  const particles = [];
  const maxParticleSize = 5;

  class Particle {
    constructor(x, y) {
      this.x = x ?? Math.random() * W;
      this.y = y ?? Math.random() * H;
      const speed = 0.2 + Math.random() * 1.2;
      const angle = Math.random() * Math.PI * 2;
      this.vx = Math.cos(angle) * speed;
      this.vy = Math.sin(angle) * speed;
      this.size = 1 + Math.random() * (maxParticleSize - 1);
      this.baseSize = this.size;
      this.colorHue = Math.floor(Math.random() * 360);
      this.mass = 1 + Math.random() * 2;
      this.alpha = 0.8;
    }
    update(dt, audioFFTVal) {
      // 鼠标吸引力
      const dx = mouse.x - this.x;
      const dy = mouse.y - this.y;
      const dist = Math.sqrt(dx * dx + dy * dy) || 1;
      const maxDist = 200;
      if (dist < maxDist) {
        // 当鼠标按下时产生向外爆发（在 spawnBurst 创建的瞬时速度已设置）
        const force = (1 - dist / maxDist) * 0.6;
        this.vx += (dx / dist) * force / this.mass;
        this.vy += (dy / dist) * force / this.mass;
      } else {
        // 稍微回退到中心的力（避免飘出）
        this.vx += (W/2 - this.x) * 0.00002;
        this.vy += (H/2 - this.y) * 0.00002;
      }

      // 音频联动：audioFFTVal 0-255
      if (audioFFTVal != null) {
        // 根据频谱使粒子大小和颜色变化
        const factor = 1 + audioFFTVal / 120; // 举例放大因子
        this.size = this.baseSize * (0.8 + factor * 0.6);
        this.colorHue = (this.colorHue + audioFFTVal * 0.05) % 360;
        // 加速
        this.vx *= 0.995 + (audioFFTVal / 5000);
        this.vy *= 0.995 + (audioFFTVal / 5000);
      } else {
        // 回到基大小
        this.size += (this.baseSize - this.size) * 0.02;
      }

      // 移动与边界处理
      this.x += this.vx * dt;
      this.y += this.vy * dt;

      if (this.x < -10) this.x = W + 10;
      if (this.x > W + 10) this.x = -10;
      if (this.y < -10) this.y = H + 10;
      if (this.y > H + 10) this.y = -10;
    }
    draw(ctx) {
      ctx.beginPath();
      ctx.fillStyle = `hsla(${this.colorHue}, 80%, 60%, ${this.alpha})`;
      ctx.arc(this.x, this.y, Math.max(0.3, this.size), 0, Math.PI * 2);
      ctx.fill();
    }
  }

  function createParticles(num = NUM) {
    particles.length = 0;
    for (let i = 0; i < num; i++) {
      particles.push(new Particle(Math.random() * W, Math.random() * H));
    }
  }

  function resetParticles() {
    createParticles();
  }

  resetBtn.addEventListener('click', resetParticles);

  // 点击产生爆发
  function spawnBurst(x, y) {
    for (let i = 0; i < 12; i++) {
      const p = new Particle(x, y);
      const angle = Math.random() * Math.PI * 2;
      const speed = 2 + Math.random() * 4;
      p.vx = Math.cos(angle) * speed;
      p.vy = Math.sin(angle) * speed;
      particles.push(p);
      // 限制总数量
      if (particles.length > NUM * 3) particles.shift();
    }
  }

  // 画线连接
  function drawConnections(ctx) {
    const maxDist = Math.min(160, Math.max(80, (W + H) / 20));
    ctx.lineWidth = 0.8;
    for (let i = 0; i < particles.length; i++) {
      const a = particles[i];
      for (let j = i + 1; j < particles.length; j++) {
        const b = particles[j];
        const dx = a.x - b.x;
        const dy = a.y - b.y;
        const d = dx * dx + dy * dy;
        if (d < maxDist * maxDist) {
          const alpha = 0.5 * (1 - d / (maxDist * maxDist));
          ctx.strokeStyle = `rgba(150,200,255,${alpha * 0.8})`;
          ctx.beginPath();
          ctx.moveTo(a.x, a.y);
          ctx.lineTo(b.x, b.y);
          ctx.stroke();
        }
      }
    }
  }

  // 动画循环
  let last = performance.now();
  function loop(now) {
    const dt = (now - last) * 0.06; // 缩放时间步，避免速度过快
    last = now;

    ctx.clearRect(0, 0, W, H);

    // 背景渐变（微弱）
    const g = ctx.createLinearGradient(0, 0, W, H);
    g.addColorStop(0, 'rgba(6,10,20,0.2)');
    g.addColorStop(1, 'rgba(8,12,30,0.2)');
    ctx.fillStyle = g;
    ctx.fillRect(0, 0, W, H);

    // 计算与音频相关的值
    let fftVal = null;
    if (analyser && spectrumToggle.checked) {
      analyser.getByteFrequencyData(freqData);
      // 取一个代表值（例如中高频段的平均）
      const start = Math.floor(freqData.length * 0.1);
      const end = Math.floor(freqData.length * 0.5);
      let sum = 0;
      for (let i = start; i < end; i++) sum += freqData[i];
      const avg = sum / (end - start || 1);
      fftVal = avg;
    }

    // 更新并绘制粒子
    for (let p of particles) {
      p.update(dt, fftVal);
      p.draw(ctx);
    }

    // 连线
    if (connectToggle.checked) drawConnections(ctx);

    requestAnimationFrame(loop);
  }

  // --- 音频设置（Web Audio API）
  let audioCtx = null;
  let sourceNode = null;
  let analyser = null;
  let freqData = null;

  function initAudioContext() {
    if (audioCtx) return;
    audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    analyser = audioCtx.createAnalyser();
    analyser.fftSize = 1024;
    freqData = new Uint8Array(analyser.frequencyBinCount);
    // 创建默认的 source（连接到 audio 元素，或可以用 oscillator）
    sourceNode = audioCtx.createMediaElementSource(audioEl);
    const gain = audioCtx.createGain();
    gain.gain.value = parseFloat(volumeEl.value || '0.6');
    sourceNode.connect(gain).connect(analyser).connect(audioCtx.destination);
    // 音量控制
    volumeEl.addEventListener('input', () => { gain.gain.value = parseFloat(volumeEl.value); });
  }

  // 播放 / 暂停 控制
  playBtn.addEventListener('click', async () => {
    initAudioContext();
    // 必须用户手势才能 resume
    if (audioCtx.state === 'suspended') {
      await audioCtx.resume();
    }
    // 如果没有音频文件则创建一个温和的示例音乐（白噪声 + 旋律示例）——使用 oscillator 合成音
    if (!audioEl.src) {
      // 我们生成一个可听到的循环节奏音（合成），并把它连接到 audioCtx
      // 这里我们直接用 OscillatorNode 来播放示例音
      if (!window._demoOsc) {
        const osc = audioCtx.createOscillator();
        const oscGain = audioCtx.createGain();
        osc.type = 'sine';
        osc.frequency.value = 220;
        oscGain.gain.value = 0.02;
        osc.connect(oscGain).connect(analyser).connect(audioCtx.destination);
        osc.start();
        window._demoOsc = { osc, oscGain };
        // 逐步改变频率制造简单旋律
        let i = 0;
        setInterval(() => {
          const freqs = [220, 246.94, 261.63, 293.66, 329.63, 392.00];
          osc.frequency.linearRampToValueAtTime(freqs[i % freqs.length], audioCtx.currentTime + 0.2);
          i++;
        }, 400);
      }
    } else {
      try {
        await audioEl.play();
      } catch (e) {
        console.warn('播放失败：', e);
      }
      playBtn.disabled = true;
      pauseBtn.disabled = false;
    }
    // 启动动画（若尚未启动）
    if (!window._animStarted) {
      window._animStarted = true;
      last = performance.now();
      requestAnimationFrame(loop);
    }
  });

  pauseBtn.addEventListener('click', () => {
    if (audioEl && !audioEl.paused) audioEl.pause();
    // 如果是 demo oscillator，则停止并清理
    if (window._demoOsc) {
      window._demoOsc.osc.stop();
      window._demoOsc.osc.disconnect();
      window._demoOsc = null;
    }
    playBtn.disabled = false;
    pauseBtn.disabled = true;
  });

  // 处理文件上传
  fileInput.addEventListener('change', () => {
    const file = fileInput.files[0];
    if (!file) return;
    const url = URL.createObjectURL(file);
    audioEl.src = url;
    audioEl.load();
    // 绑定 audio 元素到 audioCtx（如果已经初始化，需要重新创建 source）
    if (audioCtx) {
      try {
        // disconnect old source if present
        // Note: createMediaElementSource cannot be disconnected easily; simplest is to reload audio context by re-init
        // For robustness, create a new context and reconnect
        audioCtx.close().then(() => {
          audioCtx = null;
          sourceNode = null;
          initAudioContext();
          // play immediately
          audioEl.play().then(() => {
            playBtn.disabled = true;
            pauseBtn.disabled = false;
          }).catch(()=>{});
        });
      } catch (e) {
        console.warn('切换文件时发生错误：', e);
      }
    } else {
      // 音频还没有初始化：用户需点击 Play 来启动
    }
  });

  // 初始化粒子并启动动画（动画会在 Play 时启动频谱，但也可以先看到静态动画）
  createParticles();

  // 兼容移动端触摸
  window.addEventListener('touchmove', (e) => {
    const t = e.touches[0];
    mouse.x = t.clientX;
    mouse.y = t.clientY;
  }, { passive: true });
  window.addEventListener('touchstart', (e) => {
    mouse.down = true;
    const t = e.touches[0];
    spawnBurst(t.clientX, t.clientY);
  }, { passive: true });
  window.addEventListener('touchend', () => { mouse.down = false; });

  // 开始动画（轻量运行），频谱连接在 Play 后生效
  requestAnimationFrame(loop);

  // 友好提示：如果用户没有点击 Play，Play 按钮会始终可用
})();
