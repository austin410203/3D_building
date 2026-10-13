# TownKit texture additions (exec'd after textures.py helpers in the same namespace)
import numpy as np

def brick(name, c1, c2, cg, seed, nx=4, ny=12):
    """1 tile = 0.9 m: ~22 cm bricks, 7.5 cm courses"""
    mask, tid, bev = tiles(N, nx, ny, 7, offset=True, seed=seed)
    n = fbm(N, seed + 1)
    pits = noise(N, 400, seed=seed + 2)
    col = lerp(c1, c2, 0.45 + 0.18 * n + 0.45 * (tid - 0.5))
    col[pits > 2.2] *= 0.75
    col = lerp(col, cg, mask)
    out(name, col, bev + 0.08 * pits, 5)

def corrugated(name, c, seed, ribs=16, rust=0.25):
    """shipping container / tin sheet, ribs along V"""
    x, y = grid(N, 1, 1)
    prof = np.clip(np.sin(2 * np.pi * x * ribs) * 1.6, -1, 1)
    n = fbm(N, seed)
    streak = noise(N, 40, 3, seed + 3)
    r = noise(N, 12, seed=seed + 4) + 0.5 * noise(N, 90, seed=seed + 5)
    c = np.asarray(c, np.float32)
    col = lerp(c * 1.06, c * 0.78, 0.5 + 0.15 * n + 0.18 * streak + 0.12 * prof)
    rmask = np.clip((r - (2.2 - rust * 3)) * 2, 0, 1)
    col = lerp(col, (0.42, 0.22, 0.12), rmask * 0.85)
    out(name, col, prof + 0.05 * n, 3)

def metal_panel(name, c1, c2, seed, nx=2, ny=2):
    mask, tid, bev = tiles(N, nx, ny, 5, seed=seed)
    x, y = grid(N, 1, 1)
    fx = (x * nx) % 1; fy = (y * ny) % 1
    riv = np.zeros_like(x, bool)
    for cx in (0.04, 0.96):
        for cy in (0.04, 0.5, 0.96):
            riv |= ((fx - cx) ** 2 + (fy - cy) ** 2) < 0.00012 * nx * ny
    n = fbm(N, seed + 1)
    scratch = noise(N, 500, 20, seed + 2)
    col = lerp(c1, c2, 0.5 + 0.2 * n + 0.25 * (tid - 0.5) + 0.05 * scratch)
    col = lerp(col, np.asarray(c2) * 0.5, mask)
    col[riv] *= 1.25
    out(name, col, bev * 0.8 + riv * 0.6 + 0.03 * scratch, 4)

def siding(name, c, seed, boards=8):
    x, y = grid(N, 1, 1)
    fy = (y * boards) % 1
    r = np.random.default_rng(seed).uniform(-0.08, 0.08, boards)[np.floor(y * boards).astype(int) % boards]
    warp = noise(N, 3, 10, seed) * 0.6
    grain = np.sin(2 * np.pi * (x * 6 + warp)) * 0.5 + 0.5
    n = fbm(N, seed + 1)
    peel = (noise(N, 25, seed=seed + 6) + 0.5 * noise(N, 120, seed=seed + 7)) > 1.9
    c = np.asarray(c, np.float32)
    col = lerp(c * 1.08, c * 0.75, 0.45 + 0.15 * grain + 0.15 * n + r + 0.25 * (fy < 0.06))
    col[peel] = col[peel] * 0.5 + np.array((0.45, 0.33, 0.22)) * 0.5
    out(name, col, fy - 0.4 * (fy < 0.04) + 0.05 * grain, 3)

def slate(name, c1, c2, seed):
    mask, tid, bev = tiles(N, 5, 7, 6, offset=True, seed=seed)
    n = fbm(N, seed + 1)
    x, y = grid(N, 1, 1)
    fy = (y * 7) % 1
    col = lerp(c1, c2, 0.5 + 0.2 * n + 0.5 * (tid - 0.5))
    col = lerp(col, np.asarray(c2) * 0.4, mask)
    out(name, col, bev * 0.3 + fy * 0.7 + 0.05 * n, 4)

def cobble(name, c1, c2, seed, cells=10):
    x, y = grid(N, 1, 1)
    r = np.random.default_rng(seed)
    pts = (np.stack(np.meshgrid(np.arange(cells), np.arange(cells)), -1).reshape(-1, 2)
           + r.uniform(0.2, 0.8, (cells * cells, 2))) / cells
    d1 = np.full(x.shape, 9.0); d2 = np.full(x.shape, 9.0); idx = np.zeros(x.shape, int)
    for k, (px, py) in enumerate(pts):
        for ox in (-1, 0, 1):
            for oy in (-1, 0, 1):
                d = (x - px - ox) ** 2 + (y - py - oy) ** 2
                m = d < d1
                d2 = np.where(m, d1, np.minimum(d2, d)); idx = np.where(m, k, idx); d1 = np.where(m, d, d1)
    edge = np.sqrt(d2) - np.sqrt(d1)
    tint = r.random(len(pts))[idx]
    n = fbm(N, seed + 1)
    col = lerp(c1, c2, 0.4 + 0.5 * (tint - 0.5) + 0.2 * n)
    g = np.clip(edge * cells * 6, 0, 1)
    col = lerp(np.asarray(c2) * 0.45, col, g)
    out(name, col, g ** 0.5 + 0.05 * n, 4)

def marble(name, c1, c2, seed):
    x, y = grid(N, 1, 1)
    w = fbm(N, seed, ((2, .6), (6, .3), (30, .1)))
    v = np.abs(np.sin(2 * np.pi * (x * 2 + y + w * 0.9)))
    vein = np.clip(1 - v * 12, 0, 1)
    col = lerp(c1, c2, 0.15 + 0.15 * w + 0.7 * vein)
    out(name, col, 0.05 * w, 1)

def carpet(name, c, seed):
    n = noise(N, 500, seed=seed) * 0.6 + fbm(N, seed + 1) * 0.4
    c = np.asarray(c, np.float32)
    out(name, lerp(c * 1.1, c * 0.82, 0.5 + 0.3 * n), n, 2)

def sand():
    n = fbm(N, 300)
    g = noise(N, 450, seed=301)
    ripple = np.sin(2 * np.pi * (grid(N, 1, 1)[1] * 14 + noise(N, 3, seed=302))) * 0.5 + 0.5
    col = lerp((0.86, 0.78, 0.60), (0.70, 0.60, 0.42), 0.45 + 0.2 * n + 0.15 * np.tanh(g) + 0.1 * ripple)
    out("sand", col, 0.3 * ripple + 0.2 * g, 2)

def snow():
    n = fbm(N, 310)
    g = noise(N, 450, seed=311)
    col = lerp((0.96, 0.97, 1.0), (0.78, 0.82, 0.90), 0.3 + 0.25 * n + 0.05 * g)
    out("snow", col, 0.5 * n + 0.1 * g, 2)

def mosaic(name, c1, c2, seed):
    """Taiwanese apartment facade: small 4.5 x 9 cm tiles (tile = 0.9 m)"""
    mask, tid, bev = tiles(N, 20, 10, 3, offset=False, seed=seed)
    n = fbm(N, seed + 1)
    streak = noise(N, 30, 2, seed + 2)
    col = lerp(c1, c2, 0.4 + 0.3 * (tid - 0.5) + 0.15 * n + 0.2 * np.clip(streak, 0, 3))
    col = lerp(col, np.asarray(c2) * 0.7, mask)
    out(name, col, bev, 3)

def grime(name, c, seed):
    """dirty painted steel for cyberpunk facades"""
    n = fbm(N, seed)
    streak = noise(N, 50, 2, seed + 1)
    r = noise(N, 10, seed=seed + 2) + 0.6 * noise(N, 80, seed=seed + 3)
    c = np.asarray(c, np.float32)
    col = lerp(c * 1.1, c * 0.55, 0.5 + 0.2 * n + 0.25 * np.clip(streak, -1, 3))
    col = lerp(col, (0.42, 0.26, 0.15), np.clip((r - 1.6) * 1.5, 0, 1) * 0.6)
    out(name, col, 0.3 * n + 0.2 * np.clip(r - 1.6, 0, 2), 3)

def parquet():
    mask, tid, bev = tiles(N, 4, 16, 2, offset=True, seed=320)
    x, y = grid(N, 1, 1)
    grain = np.sin(2 * np.pi * (y * 90 + noise(N, 3, 12, 321) * 0.6)) * 0.5 + 0.5
    col = lerp((0.62, 0.44, 0.28), (0.40, 0.26, 0.15), 0.4 + 0.5 * (tid - 0.5) + 0.2 * grain)
    col = lerp(col, (0.2, 0.13, 0.08), mask)
    out("parquet", col, bev * 0.4 + 0.05 * grain, 3)

brick("brick_red", (0.62, 0.28, 0.20), (0.42, 0.18, 0.12), (0.72, 0.70, 0.66), 400)
brick("brick_dark", (0.30, 0.27, 0.26), (0.18, 0.16, 0.16), (0.45, 0.44, 0.42), 410)
brick("brick_cream", (0.86, 0.80, 0.68), (0.72, 0.64, 0.52), (0.62, 0.60, 0.56), 415)
corrugated("cont_yellow", (0.92, 0.72, 0.10), 420, rust=0.15)
corrugated("cont_blue", (0.12, 0.28, 0.62), 430, rust=0.3)
corrugated("cont_black", (0.10, 0.11, 0.12), 440, rust=0.1)
corrugated("cont_grey", (0.62, 0.64, 0.66), 450, rust=0.35)
corrugated("tin_rust", (0.55, 0.50, 0.46), 455, rust=0.8)
metal_panel("panel_copper", (0.62, 0.36, 0.18), (0.40, 0.22, 0.10), 460)
metal_panel("panel_steel", (0.40, 0.44, 0.48), (0.25, 0.27, 0.30), 470)
metal_panel("panel_dark", (0.16, 0.18, 0.22), (0.08, 0.09, 0.11), 475, 3, 3)
siding("siding_teal", (0.22, 0.55, 0.55), 480)
siding("siding_white", (0.90, 0.88, 0.82), 485)
slate("slate_blue", (0.30, 0.38, 0.46), (0.18, 0.22, 0.28), 490)
slate("slate_dark", (0.22, 0.22, 0.24), (0.12, 0.12, 0.13), 495)
cobble("cobble", (0.62, 0.58, 0.52), (0.40, 0.37, 0.33), 500)
marble("marble_white", (0.95, 0.94, 0.92), (0.55, 0.55, 0.58), 510)
marble("marble_black", (0.10, 0.10, 0.11), (0.70, 0.68, 0.62), 515)
carpet("carpet_grey", (0.42, 0.42, 0.44), 520)
carpet("carpet_red", (0.55, 0.14, 0.12), 525)
mosaic("mosaic_beige", (0.86, 0.80, 0.70), (0.70, 0.64, 0.54), 530)
mosaic("mosaic_pink", (0.85, 0.66, 0.62), (0.68, 0.50, 0.48), 535)
grime("grime_teal", (0.28, 0.38, 0.40), 540)
grime("grime_blue", (0.24, 0.30, 0.38), 545)
parquet(); sand(); snow()
slate("roof_clay", (0.72, 0.30, 0.18), (0.45, 0.16, 0.09), 600)
print("textures2 ->", TEXDIR, len(os.listdir(TEXDIR)))
