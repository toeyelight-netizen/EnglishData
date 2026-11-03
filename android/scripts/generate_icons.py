"""Generate Android launcher icons from the source logo.

Creates legacy + round launcher icons (mdpi..xxxhdpi), adaptive-icon
foregrounds, and splash art in the app's res/ tree.
"""

import shutil
from pathlib import Path

from PIL import Image, ImageDraw

SRC = Path(r"C:\Users\Farhad\Documents\Qoder\2026-10-31\7e7d90c4\vibe_images\app_logo_medieval_fantasy_1793735473026_751cd83c.png")
RES = Path(__file__).resolve().parent.parent / "app" / "src" / "main" / "res"
DESIGN = Path(__file__).resolve().parent.parent / "design"

DENSITIES = {"mdpi": 1.0, "hdpi": 1.5, "xhdpi": 2.0, "xxhdpi": 3.0, "xxxhdpi": 4.0}
LEGACY_BASE = 48
ADAPTIVE_BASE = 108
BG = (110, 31, 46, 255)  # burgundy #6E1F2E


def scaled(src: Image.Image, size: int) -> Image.Image:
    return src.resize((size, size), Image.LANCZOS)


def circle_masked(src: Image.Image, size: int) -> Image.Image:
    img = scaled(src, size).convert("RGBA")
    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)
    out = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    out.paste(img, (0, 0), mask)
    return out


def adaptive_foreground(src: Image.Image, size: int) -> Image.Image:
    """Art occupies the central safe zone (~62%) on a transparent canvas."""
    canvas = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    art = scaled(src.convert("RGBA"), int(size * 0.62))
    canvas.paste(art, ((size - art.width) // 2, (size - art.height) // 2), art)
    return canvas


def main() -> None:
    src = Image.open(SRC).convert("RGBA")
    shutil.copy2(SRC, DESIGN / "logo_source.png")

    for name, scale in DENSITIES.items():
        folder = RES / f"mipmap-{name}"
        folder.mkdir(parents=True, exist_ok=True)
        legacy = scaled(src, int(LEGACY_BASE * scale))
        legacy.save(folder / "ic_launcher.png", optimize=True)
        circle_masked(src, int(LEGACY_BASE * scale)).save(folder / "ic_launcher_round.png", optimize=True)
        foreground = adaptive_foreground(src, int(ADAPTIVE_BASE * scale))
        foreground.save(folder / "ic_launcher_foreground.png", optimize=True)

    (RES / "drawable-nodpi").mkdir(parents=True, exist_ok=True)
    scaled(src, 768).convert("RGB").save(
        RES / "drawable-nodpi" / "splash_logo.png", optimize=True
    )
    scaled(src, 384).convert("RGB").save(RES / "drawable-nodpi" / "logo_medium.png", optimize=True)

    # Preview for human review
    preview = Image.new("RGB", (1024, 512), BG[:3])
    preview.paste(scaled(src.convert("RGB"), 384), (64, 64))
    preview.paste(circle_masked(src, 192).convert("RGB"), (576, 128))
    preview.save(DESIGN / "icons_preview.png")

    print("Icons written to", RES)


if __name__ == "__main__":
    main()
