#!/usr/bin/env python3
"""Generate a 1920x1080 title/text slide as PNG."""
import argparse
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

W, H = 1920, 1080

def make_slide(title, subtitle=None, body=None, out_path="slide.png", bg=(245,247,250), fg=(30,30,35), accent=(70,130,200)):
    img = Image.new("RGB", (W, H), bg)
    draw = ImageDraw.Draw(img)
    
    # Try to load fonts, fallback to default
    try:
        font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 72)
        font_sub = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 40)
        font_body = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 32)
    except Exception:
        font_title = ImageFont.load_default()
        font_sub = font_body = font_title
    
    y = H // 3
    
    # Title
    bbox = draw.textbbox((0,0), title, font=font_title)
    tw = bbox[2] - bbox[0]
    draw.text(((W - tw) // 2, y), title, fill=fg, font=font_title)
    y += 100
    
    # Subtitle
    if subtitle:
        bbox = draw.textbbox((0,0), subtitle, font=font_sub)
        tw = bbox[2] - bbox[0]
        draw.text(((W - tw) // 2, y), subtitle, fill=accent, font=font_sub)
        y += 80
    
    # Body lines
    if body:
        for line in body.split("\n"):
            bbox = draw.textbbox((0,0), line, font=font_body)
            tw = bbox[2] - bbox[0]
            draw.text(((W - tw) // 2, y), line, fill=fg, font=font_body)
            y += 50
    
    img.save(out_path)
    print(f"Saved {out_path}")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--title", required=True)
    p.add_argument("--subtitle", default=None)
    p.add_argument("--body", default=None)
    p.add_argument("--out", required=True)
    args = p.parse_args()
    make_slide(args.title, args.subtitle, args.body, args.out)
