"""Generate Android launcher icons from the knight-on-horseback artwork.

Builds a circular gold-framed medallion master from the source painting, then
writes legacy + round launcher icons (mdpi..xxxhdpi), adaptive-icon
foregrounds, and splash art into the app's res/ tree.
"""

import math
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFilter

HERE = Path(__file__).resolve().parent
DESIGN = HERE.parent / "design"
RES = HERE.parent / "app" / "src" / "main" / "res"

SRC = DESIGN / "logo_source_knight.jpg"
MASTER = DESIGN / "logo_master.png"

CROP_BOX = (0, 425, 560)  # left, top, side of the square crop from the portrait painting
MASTER_SIZE = 1024
DISC_R = 470            # painted medallion radius
RING_W = 34             # gold ring thickness

DENSITIES = {"mdpi": 1.0, "hdpi": 1.5, "xhdpi": 2.0, "xxhdpi": 3.0, "xxxhdpi": 4.0}
LEGACY_BASE = 48
ADAPTIVE_BASE = 108
BG = (110, 31, 46, 255)  # burgundy #6E1F2E, matches @color/ic_launcher_bg

GOLD_HI = (246, 222, 156, 255)
GOLD = (217, 164, 65, 255)
GOLD_LO = (150, 104, 36, 255)


def gold_shade(t: float) -> tuple:
    """Vertical gold gradient: highlight -> mid -> shadow."""
    a, b, u = ((GOLD_HI, GOLD, t * 2) if t < 0.5 else (GOLD, GOLD_LO, (t - 0.5) * 2))
    return tuple(round(a[i] + (b[i] - a[i]) * u) for i in range(4))


def build_master() -> Image.Image:
    src = Image.open(SRC).convert("RGB")
    left, top, side = CROP_BOX
    left = max(0, min(left, src.width - side))
    top = max(0, min(top, src.height - side))
    art = src.crop((left, top, left + side, top + side)).resize(
        (MASTER_SIZE, MASTER_SIZE), Image.LANCZOS
    )

    ss = 4  # supersample for smooth ring edges
    n = MASTER_SIZE * ss
    canvas = Image.new("RGBA", (n, n), (0, 0, 0, 0))
    cx = cy = n // 2
    r_disc = DISC_R * ss
    r_out = (DISC_R + RING_W) * ss

    # painted disc
    disc = Image.new("L", (n, n), 0)
    ImageDraw.Draw(disc).ellipse((cx - r_disc, cy - r_disc, cx + r_disc, cy + r_disc), fill=255)
    canvas.paste(art.resize((n, n), Image.LANCZOS), (0, 0), disc)

    # inner vignette so the medallion reads as one piece of metalwork
    soft = disc.filter(ImageFilter.GaussianBlur(r_disc * 0.16))
    vign_alpha = ImageChops.subtract(disc, soft).point(lambda v: int(v * 0.55))
    vign = Image.new("RGBA", (n, n), (26, 8, 12, 255))
    vign.putalpha(vign_alpha)
    canvas = Image.alpha_composite(canvas, vign)

    # gold ring with a vertical sheen
    ring = Image.new("RGBA", (n, n), (0, 0, 0, 0))
    dr = ImageDraw.Draw(ring)
    for y in range(n):
        dr.line((0, y, n, y), fill=gold_shade(y / n))
    mask = Image.new("L", (n, n), 0)
    ImageDraw.Draw(mask).ellipse((cx - r_out, cy - r_out, cx + r_out, cy + r_out), fill=255)
    ImageDraw.Draw(mask).ellipse((cx - r_disc, cy - r_disc, cx + r_disc, cy + r_disc), fill=0)
    canvas = Image.composite(ring, canvas, mask)

    # hairlines and beads
    edge = Image.new("RGBA", (n, n), (0, 0, 0, 0))
    de = ImageDraw.Draw(edge)
    de.ellipse((cx - r_out, cy - r_out, cx + r_out, cy + r_out), outline=(74, 19, 31, 255), width=3 * ss)
    de.ellipse((cx - r_disc, cy - r_disc, cx + r_disc, cy + r_disc), outline=(74, 19, 31, 255), width=2 * ss)
    r_mid = r_disc + 17 * ss
    for k in range(8):
        ang = math.pi * k / 4
        bx, by = cx + r_mid * math.cos(ang), cy + r_mid * math.sin(ang)
        rr = (7 if k % 2 == 0 else 5) * ss
        de.ellipse((bx - rr, by - rr, bx + rr, by + rr), fill=GOLD_HI)
    canvas = Image.alpha_composite(canvas, edge)

    master = canvas.resize((MASTER_SIZE, MASTER_SIZE), Image.LANCZOS)
    master.save(MASTER, optimize=True)
    return master


def scaled(img: Image.Image, size: int) -> Image.Image:
    return img.resize((size, size), Image.LANCZOS)


def on_burgundy(master: Image.Image, size: int) -> Image.Image:
    base = Image.new("RGBA", (size, size), BG)
    art = scaled(master, size)
    base.paste(art, (0, 0), art)
    return base


def circle_masked(master: Image.Image, size: int) -> Image.Image:
    """Round launcher icon: the medallion fills the disc, corners transparent."""
    img = scaled(master, size)
    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, size, size), fill=255)
    out = Image.new("RGBA", (size, size), BG)
    out.paste(img, (0, 0), mask)
    return out


def adaptive_foreground(master: Image.Image, size: int) -> Image.Image:
    """Art occupies the central safe zone (~62%) on a transparent canvas."""
    canvas = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    art = scaled(master, int(size * 0.62))
    canvas.paste(art, ((size - art.width) // 2, (size - art.height) // 2), art)
    return canvas


def main() -> None:
    master = build_master()

    for name, scale in DENSITIES.items():
        folder = RES / f"mipmap-{name}"
        folder.mkdir(parents=True, exist_ok=True)
        size = int(LEGACY_BASE * scale)
        on_burgundy(master, size).save(folder / "ic_launcher.png", optimize=True)
        circle_masked(master, size).save(folder / "ic_launcher_round.png", optimize=True)
        adaptive_foreground(master, int(ADAPTIVE_BASE * scale)).save(
            folder / "ic_launcher_foreground.png", optimize=True
        )

    (RES / "drawable-nodpi").mkdir(parents=True, exist_ok=True)
    on_burgundy(master, 768).convert("RGB").save(RES / "drawable-nodpi" / "splash_logo.png", optimize=True)
    on_burgundy(master, 384).convert("RGB").save(RES / "drawable-nodpi" / "logo_medium.png", optimize=True)

    # previews for human review
    preview = Image.new("RGB", (1024, 512), BG[:3])
    preview.paste(on_burgundy(master, 384).convert("RGB"), (64, 64))
    preview.paste(circle_masked(master, 192).convert("RGB"), (576, 128))
    preview.paste(adaptive_foreground(master, 192).convert("RGB"), (800, 128))
    preview.save(DESIGN / "icons_preview.png")

    master.convert("RGB").save(DESIGN / "logo_preview.png", optimize=True)
    print("master:", MASTER)
    print("icons written to", RES)


if __name__ == "__main__":
    main()
