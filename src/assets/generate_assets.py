"""
Confoederatio Helvetica - Asset Generation Script
Generates all game assets in Renaissance style using Pillow.
Creates city icons, goods icons, troop icons, title screen, and textures.
"""

import os
from PIL import Image, ImageDraw, ImageFont
import random

def get_font(size=12):
    """Try to load a suitable font, fall back to default."""
    fonts = [
        "arial.ttf",
        "times.ttf",
        "georgia.ttf",
        "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/times.ttf",
        "C:/Windows/Fonts/georgia.ttf",
    ]
    for font_path in fonts:
        try:
            return ImageFont.truetype(font_path, size)
        except (IOError, OSError):
            continue
    return ImageFont.load_default()

# Renaissance color palette
PALETTE = {
    "parchment": (245, 230, 195),
    "dark_parchment": (210, 190, 150),
    "ink": (60, 40, 20),
    "gold": (218, 165, 32),
    "deep_red": (139, 0, 0),
    "forest_green": (34, 100, 34),
    "royal_blue": (65, 105, 225),
    "silver": (192, 192, 192),
    "iron": (105, 105, 105),
    "wood": (139, 90, 47),
    "cream": (255, 253, 208),
}


def create_parchment_background(width, height):
    """Create a parchment-textured background."""
    img = Image.new("RGB", (width, height), PALETTE["parchment"])
    draw = ImageDraw.Draw(img)
    
    # Add subtle texture
    for _ in range(500):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        shade = random.randint(230, 245)
        draw.point((x, y), fill=(shade, shade - 10, shade - 30))
    
    # Add border
    draw.rectangle([2, 2, width - 3, height - 3], outline=PALETTE["ink"], width=2)
    draw.rectangle([5, 5, width - 6, height - 6], outline=PALETTE["gold"], width=1)
    
    return img


def create_city_icon(city_name, color):
    """Create a detailed city icon with Gothic architecture."""
    size = 64
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # City walls
    wall_color = PALETTE["wood"]
    draw.rectangle([8, 35, 56, 58], fill=wall_color, outline=PALETTE["ink"])
    
    # Towers
    for x in [10, 28, 46]:
        draw.rectangle([x, 15, x + 8, 35], fill=color, outline=PALETTE["ink"])
        # Tower top (pointed)
        draw.polygon([(x, 15), (x + 4, 5), (x + 8, 15)], fill=color, outline=PALETTE["ink"])
    
    # Gate
    draw.rectangle([26, 40, 38, 58], fill=PALETTE["ink"])
    draw.arc([26, 30, 38, 42], 180, 0, fill=PALETTE["ink"])
    
    # Windows
    for x in [14, 50]:
        for y in [20, 28]:
            draw.rectangle([x, y, x + 3, y + 4], fill=PALETTE["cream"])
    
    return img


def create_goods_icon(goods_type):
    """Create historical-style goods icons."""
    size = 48
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    if goods_type == "grain":
        # Grain sacks
        for i in range(3):
            x = 8 + i * 12
            draw.ellipse([x, 25, x + 10, 40], fill=PALETTE["wood"], outline=PALETTE["ink"])
    
    elif goods_type == "wine":
        # Wine barrel
        draw.ellipse([10, 15, 38, 35], fill=PALETTE["wood"], outline=PALETTE["ink"])
        draw.rectangle([12, 15, 36, 35], fill=PALETTE["wood"], outline=PALETTE["ink"])
        for y in [18, 25, 32]:
            draw.line([(10, y), (38, y)], fill=PALETTE["iron"], width=2)
    
    elif goods_type == "cheese":
        # Cheese wheel
        draw.ellipse([8, 15, 40, 40], fill=(255, 220, 100), outline=PALETTE["ink"])
        for _ in range(5):
            x = random.randint(12, 36)
            y = random.randint(18, 37)
            draw.ellipse([x - 2, y - 2, x + 2, y + 2], fill=PALETTE["dark_parchment"])
    
    elif goods_type == "wool":
        # Wool balls
        for i in range(3):
            x = 8 + i * 12
            draw.ellipse([x, 20, x + 10, 35], fill=PALETTE["cream"], outline=PALETTE["ink"])
    
    elif goods_type == "iron":
        # Iron bars
        for i in range(3):
            x = 8 + i * 10
            draw.rectangle([x, 20, x + 6, 40], fill=PALETTE["iron"], outline=PALETTE["ink"])
    
    elif goods_type == "silver":
        # Silver coins
        for i in range(4):
            x = 8 + (i % 2) * 16
            y = 15 + (i // 2) * 15
            draw.ellipse([x, y, x + 12, y + 10], fill=PALETTE["silver"], outline=PALETTE["ink"])
    
    return img


def create_troop_icon(troop_type):
    """Create Swiss troop icons in historical dress."""
    size = 48
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    if troop_type == "halberdier":
        # Halberdier with halberd
        draw.rectangle([18, 25, 30, 40], fill=PALETTE["deep_red"], outline=PALETTE["ink"])
        draw.ellipse([20, 15, 28, 25], fill=(220, 190, 160), outline=PALETTE["ink"])
        draw.arc([19, 12, 29, 20], 180, 360, fill=PALETTE["iron"], width=2)
        # Halberd
        draw.line([(35, 5), (35, 45)], fill=PALETTE["wood"], width=2)
        draw.polygon([(33, 5), (37, 5), (35, 12)], fill=PALETTE["iron"])
    
    elif troop_type == "crossbowman":
        # Crossbowman
        draw.rectangle([18, 25, 30, 40], fill=PALETTE["forest_green"], outline=PALETTE["ink"])
        draw.ellipse([20, 15, 28, 25], fill=(220, 190, 160), outline=PALETTE["ink"])
        # Crossbow
        draw.line([(10, 25), (38, 25)], fill=PALETTE["wood"], width=2)
        draw.line([(24, 20), (24, 30)], fill=PALETTE["iron"], width=1)
    
    elif troop_type == "cavalry":
        # Cavalry on horse
        draw.ellipse([10, 30, 38, 42], fill=(160, 120, 80), outline=PALETTE["ink"])
        draw.ellipse([35, 22, 44, 30], fill=(160, 120, 80), outline=PALETTE["ink"])
        # Rider
        draw.rectangle([18, 18, 28, 32], fill=PALETTE["royal_blue"], outline=PALETTE["ink"])
        draw.ellipse([20, 10, 26, 18], fill=(220, 190, 160), outline=PALETTE["ink"])
    
    return img


def create_title_screen():
    """Create decorative Renaissance title screen."""
    width, height = 800, 600
    img = Image.new("RGB", (width, height), PALETTE["parchment"])
    draw = ImageDraw.Draw(img)
    
    # Background texture
    for _ in range(2000):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        shade = random.randint(235, 248)
        draw.point((x, y), fill=(shade, shade - 10, shade - 25))
    
    # Decorative border
    draw.rectangle([10, 10, width - 11, height - 11], outline=PALETTE["gold"], width=4)
    draw.rectangle([20, 20, width - 21, height - 21], outline=PALETTE["ink"], width=2)
    
    # Corner ornaments
    for x, y in [(25, 25), (width - 45, 25), (25, height - 45), (width - 45, height - 45)]:
        draw.ellipse([x, y, x + 20, y + 20], fill=PALETTE["gold"])
    
    # Title text
    title_font = get_font(48)
    subtitle_font = get_font(24)
    
    try:
        draw.text((width // 2, 150), "CONFOEDERATIO",
                 font=title_font, fill=PALETTE["ink"], anchor="mm")
        draw.text((width // 2, 210), "HELVETICA",
                 font=title_font, fill=PALETTE["deep_red"], anchor="mm")
        
        # Decorative line
        draw.line([(200, 260), (600, 260)], fill=PALETTE["gold"], width=3)
        
        draw.text((width // 2, 300), "Eine Schweizer Wirtschaftssimulation",
                 font=subtitle_font, fill=PALETTE["ink"], anchor="mm")
        draw.text((width // 2, 340), "im Renaissance-Stil (1500-1600)",
                 font=subtitle_font, fill=PALETTE["ink"], anchor="mm")
    except Exception:
        pass
    
    return img


def create_map_background():
    """Create parchment-textured map background."""
    width, height = 1024, 768
    img = Image.new("RGB", (width, height), PALETTE["parchment"])
    draw = ImageDraw.Draw(img)
    
    # Parchment texture
    for _ in range(5000):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        shade = random.randint(230, 248)
        draw.point((x, y), fill=(shade, shade - 10, shade - 25))
    
    # Map border
    draw.rectangle([5, 5, width - 6, height - 6], outline=PALETTE["ink"], width=3)
    draw.rectangle([10, 10, width - 11, height - 11], outline=PALETTE["gold"], width=2)
    
    # Grid lines (subtle)
    for x in range(0, width, 64):
        draw.line([(x, 10), (x, height - 11)], fill=(200, 185, 150), width=1)
    for y in range(0, height, 64):
        draw.line([(10, y), (width - 11, y)], fill=(200, 185, 150), width=1)
    
    return img


def generate_all_assets(output_dir="assets"):
    """Generate all game assets and save to output directory."""
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(os.path.join(output_dir, "cities"), exist_ok=True)
    os.makedirs(os.path.join(output_dir, "goods"), exist_ok=True)
    os.makedirs(os.path.join(output_dir, "troops"), exist_ok=True)
    
    print(f"Generating assets to {output_dir}/...")
    
    # City icons
    cities = {
        "zuerich": (PALETTE["deep_red"], "Zürich"),
        "basel": (PALETTE["royal_blue"], "Basel"),
        "geneva": (PALETTE["forest_green"], "Genf"),
        "bern": (PALETTE["gold"], "Bern"),
        "luzern": (PALETTE["iron"], "Luzern"),
    }
    
    for city_id, (color, name) in cities.items():
        icon = create_city_icon(name, color)
        path = os.path.join(output_dir, "cities", f"{city_id}.png")
        icon.save(path)
        print(f"  Created {path}")
    
    # Goods icons
    goods_types = ["grain", "wine", "cheese", "wool", "iron", "silver"]
    for goods_type in goods_types:
        icon = create_goods_icon(goods_type)
        path = os.path.join(output_dir, "goods", f"{goods_type}.png")
        icon.save(path)
        print(f"  Created {path}")
    
    # Troop icons
    troop_types = ["halberdier", "crossbowman", "cavalry"]
    for troop_type in troop_types:
        icon = create_troop_icon(troop_type)
        path = os.path.join(output_dir, "troops", f"{troop_type}.png")
        icon.save(path)
        print(f"  Created {path}")
    
    # Title screen
    title = create_title_screen()
    title_path = os.path.join(output_dir, "title_screen.png")
    title.save(title_path)
    print(f"  Created {title_path}")
    
    # Map background
    map_bg = create_map_background()
    map_path = os.path.join(output_dir, "map_background.png")
    map_bg.save(map_path)
    print(f"  Created {map_path}")
    
    print("Asset generation complete!")
    return output_dir


if __name__ == "__main__":
    generate_all_assets()
