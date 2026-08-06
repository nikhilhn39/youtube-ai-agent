import os
from PIL import Image, ImageDraw, ImageFont


def _load_font(font_size):
    try:
        return ImageFont.truetype("arial.ttf", font_size)
    except OSError:
        return ImageFont.load_default()


def _wrap_text(text, draw, font, max_width):
    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        test_line = f"{current_line} {word}".strip()
        width, _ = draw.textsize(test_line, font=font)
        if width <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)
    return lines


def create_thumbnail(text, output_name):
    width, height = 1280, 720
    img = Image.new("RGB", (width, height), color=(24, 24, 24))
    draw = ImageDraw.Draw(img)

    font_title = _load_font(72)
    font_subtitle = _load_font(36)

    padding = 80
    max_text_width = width - padding * 2
    lines = _wrap_text(text.upper(), draw, font_title, max_text_width)

    y = 180
    draw.rectangle([(0, 0), (width, 120)], fill=(220, 20, 60))
    draw.text((padding, 30), "AI Video Builder", fill="white", font=font_subtitle)

    for line in lines:
        line_width, line_height = draw.textsize(line, font=font_title)
        draw.text(((width - line_width) / 2, y), line, fill="white", font=font_title)
        y += line_height + 15

    tagline = "Create, edit, and upload with Python automation"
    tag_width, tag_height = draw.textsize(tagline, font=font_subtitle)
    draw.text(((width - tag_width) / 2, height - tag_height - 60), tagline, fill=(200, 200, 200), font=font_subtitle)

    os.makedirs("outputs", exist_ok=True)
    path = f"outputs/{output_name}_thumbnail.jpg"
    img.save(path)
    return path
