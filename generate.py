#!/usr/bin/env python3
"""Generate the 20 November 2026 world-news summary image.

Reads news.json (title, subtitle, stories, sources) and renders a
1200x1800 PNG infographic with Pillow. No network access, no external
assets: every element is drawn by this program.
Usage: python3 generate.py [news.json] [output.png]
"""
import json
import sys
import textwrap

from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 1800
BG = (13, 22, 41)          # deep navy
CARD = (24, 37, 66)        # card navy
ACCENT = (255, 196, 66)    # gold
TEXT = (240, 243, 248)
MUTED = (168, 182, 205)
LINE = (52, 71, 110)


def font(size, bold=False):
    for path in (
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold
        else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf" if bold
        else "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    ):
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()


def wrap(draw, text, fnt, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = f"{cur} {w}".strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def main():
    src = sys.argv[1] if len(sys.argv) > 1 else "news.json"
    out = sys.argv[2] if len(sys.argv) > 2 else "news-2026-11-20.png"
    with open(src, encoding="utf-8") as fh:
        data = json.load(fh)

    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W, 10], fill=ACCENT)

    # Header
    d.text((64, 56), "20 NOVEMBER 2026", font=font(30, True), fill=ACCENT)
    d.text((64, 96), data["title"], font=font(58, True), fill=TEXT)
    d.text((64, 168), data["subtitle"], font=font(26), fill=MUTED)
    d.line([(64, 218), (W - 64, 218)], fill=LINE, width=2)

    # Story cards
    y = 248
    card_h = 218
    gap = 20
    for i, s in enumerate(data["stories"], 1):
        d.rounded_rectangle([64, y, W - 64, y + card_h], radius=18, fill=CARD)
        d.rounded_rectangle([64, y, 76, y + card_h], radius=9, fill=ACCENT)
        d.text((100, y + 22), f"{i:02d}", font=font(40, True), fill=ACCENT)
        d.text((170, y + 24), s["tag"], font=font(20, True), fill=ACCENT)
        head_lines = wrap(d, s["headline"], font(30, True), W - 64 - 170 - 40)
        hy = y + 56
        for line in head_lines[:2]:
            d.text((170, hy), line, font=font(30, True), fill=TEXT)
            hy += 38
        sum_lines = wrap(d, s["summary"], font(24), W - 64 - 170 - 40)
        sy = hy + 6
        for line in sum_lines[:2]:
            d.text((170, sy), line, font=font(24), fill=MUTED)
            sy += 32
        y += card_h + gap

    # Footer
    d.line([(64, H - 88), (W - 64, H - 88)], fill=LINE, width=2)
    foot = textwrap.wrap(data["sources"], width=105)
    fy = H - 74
    for line in foot[:2]:
        d.text((64, fy), line, font=font(18), fill=MUTED)
        fy += 24
    img.save(out)
    print(f"Wrote {out} ({W}x{H}) with {len(data['stories'])} stories")


if __name__ == "__main__":
    main()
