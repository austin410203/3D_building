// WebAudio engine synth (V8-ish firing frequency follows RPM), shift blips, tyre squeal, wind.
export class CarAudio {
  constructor() { this.ctx = null; }
  start() {
    if (this.ctx) return;
    const C = this.ctx = new (window.AudioContext || window.webkitAudioContext)();
    const master = this.master = C.createGain(); master.gain.value = 0.0; master.connect(C.destination);
    // engine: two detuned saws + sub square through a resonant lowpass and soft clip
    this.osc = [C.createOscillator(), C.createOscillator(), C.createOscillator()];
    this.osc[0].type = "sawtooth"; this.osc[1].type = "sawtooth"; this.osc[2].type = "square";
    const shaper = C.createWaveShaper(); const curve = new Float32Array(1024);
    for (let i = 0; i < 1024; i++) { const x = i / 512 - 1; curve[i] = Math.tanh(2.2 * x); } shaper.curve = curve;
    this.filt = C.createBiquadFilter(); this.filt.type = "lowpass"; this.filt.Q.value = 4;
    this.eg = C.createGain(); this.eg.gain.value = 0.2;
    const mix = C.createGain(); mix.gain.value = 0.3;
    this.osc[2].frequency.value = 30;
    for (const o of this.osc) { o.connect(mix); o.start(); }
    mix.connect(shaper); shaper.connect(this.filt); this.filt.connect(this.eg); this.eg.connect(master);
    // noise for tyres + wind
    const buf = C.createBuffer(1, C.sampleRate * 2, C.sampleRate); const d = buf.getChannelData(0);
    for (let i = 0; i < d.length; i++) d[i] = Math.random() * 2 - 1;
    const mk = (type, f, q) => { const s = C.createBufferSource(); s.buffer = buf; s.loop = true; const fl = C.createBiquadFilter(); fl.type = type; fl.frequency.value = f; fl.Q.value = q; const g = C.createGain(); g.gain.value = 0; s.connect(fl); fl.connect(g); g.connect(master); s.start(); return g; };
    this.squeal = mk("bandpass", 1900, 6); this.wind = mk("lowpass", 700, 0.7);
  }
  update(car, active) {
    if (!this.ctx) return;
    const t = this.ctx.currentTime;
    const f = car.rpm / 60 * 4;                                // 8 cylinders, 4-stroke -> 4 pulses / rev
    this.osc[0].frequency.setTargetAtTime(f, t, 0.02);
    this.osc[1].frequency.setTargetAtTime(f * 1.007, t, 0.02);
    this.osc[2].frequency.setTargetAtTime(f / 2, t, 0.02);
    this.filt.frequency.setTargetAtTime(380 + car.rpm * 0.32 + car.throttle * 900, t, 0.03);
    const shiftDip = car.shiftT > 0 ? 0.35 : 1;
    this.eg.gain.setTargetAtTime((0.12 + car.throttle * 0.22) * shiftDip, t, 0.03);
    this.squeal.gain.setTargetAtTime(active ? car.slip * 0.22 : 0, t, 0.05);
    const v = Math.abs(car.vLong);
    this.wind.gain.setTargetAtTime(active ? Math.min(0.35, v * v / 18000) : 0, t, 0.1);
    this.master.gain.setTargetAtTime(active ? 0.55 : 0.0, t, 0.25);
  }
  blip(up) {
    if (!this.ctx) return;
    const t = this.ctx.currentTime;
    this.eg.gain.cancelScheduledValues(t); this.eg.gain.setValueAtTime(up ? 0.05 : 0.35, t); this.eg.gain.linearRampToValueAtTime(0.25, t + 0.18);
  }
}
