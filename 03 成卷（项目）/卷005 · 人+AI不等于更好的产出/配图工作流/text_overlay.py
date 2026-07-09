"""
Post-processing: overlay Chinese text on generated hand-drawn illustrations.
Matches ian-handdrawn-ppt Visual DNA V6 typography style.
"""
from PIL import Image, ImageDraw, ImageFont
import os

# Font paths (Windows)
KAITI = "C:/Windows/Fonts/simkai.ttf"  # 楷体 - closest to hand-drawn
HEITI = "C:/Windows/Fonts/simhei.ttf"  # 黑体

def add_text_overlay(image_path, output_path, config):
    """
    config = {
        "title": "标题文字",
        "subtitle": "副标题",
        "labels": [{"text": "标签", "x": 0.3, "y": 0.5, "color": "blue"}],
        "page_number": "01 / 03",
    }
    Coordinates are 0-1 fractions of image size.
    """
    img = Image.open(image_path).convert("RGBA")
    w, h = img.size
    
    # Create overlay layer
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    
    # Title font (centered, medium)
    title_size = int(h * 0.06)
    try:
        title_font = ImageFont.truetype(KAITI, title_size)
    except:
        title_font = ImageFont.truetype(HEITI, title_size)
    
    # Page number (upper left, small)
    pn_size = int(h * 0.025)
    try:
        pn_font = ImageFont.truetype(KAITI, pn_size)
    except:
        pn_font = ImageFont.load_default()
    
    # Label font
    label_size = int(h * 0.03)
    try:
        label_font = ImageFont.truetype(KAITI, label_size)
    except:
        label_font = ImageFont.load_default()
    
    # Page number
    if config.get("page_number"):
        draw.text((int(w * 0.06), int(h * 0.05)), config["page_number"], 
                  fill=(60, 60, 60, 255), font=pn_font)
    
    # Title (centered)
    title = config.get("title", "")
    if title:
        bbox = draw.textbbox((0, 0), title, font=title_font)
        tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
        tx = (w - tw) // 2
        ty = int(h * 0.08)
        draw.text((tx, ty), title, fill=(30, 30, 30, 255), font=title_font)
        # Pale blue underline
        ul_y = ty + th + int(h * 0.008)
        draw.line([(tx, ul_y), (tx + tw, ul_y)], 
                  fill=(150, 190, 220, 180), width=max(1, int(h * 0.003)))
    
    # Subtitle
    subtitle = config.get("subtitle", "")
    if subtitle:
        sub_size = int(h * 0.035)
        try:
            sub_font = ImageFont.truetype(KAITI, sub_size)
        except:
            sub_font = label_font
        bbox = draw.textbbox((0, 0), subtitle, font=sub_font)
        sw = bbox[2] - bbox[0]
        sx = (w - sw) // 2
        sy = int(h * 0.16)
        draw.text((sx, sy), subtitle, fill=(80, 80, 80, 255), font=sub_font)
    
    # Labels with pastel backgrounds
    colors = {
        "blue": (180, 210, 240, 120),
        "green": (180, 220, 190, 120),
        "peach": (240, 200, 180, 120),
        "lavender": (210, 190, 230, 120),
    }
    text_colors = {
        "blue": (40, 60, 100, 255),
        "green": (40, 80, 50, 255),
        "peach": (100, 50, 30, 255),
        "lavender": (60, 40, 100, 255),
    }
    
    for label in config.get("labels", []):
        text = label["text"]
        lx = int(w * label["x"])
        ly = int(h * label["y"])
        color_key = label.get("color", "blue")
        
        bbox = draw.textbbox((0, 0), text, font=label_font)
        lw, lh = bbox[2] - bbox[0], bbox[3] - bbox[1]
        
        pad = int(h * 0.01)
        # Draw pastel background
        draw.rounded_rectangle(
            [(lx - pad, ly - pad), (lx + lw + pad, ly + lh + pad)],
            radius=4, fill=colors.get(color_key, colors["blue"])
        )
        # Draw text
        draw.text((lx, ly), text, fill=text_colors.get(color_key, text_colors["blue"]), font=label_font)
    
    # Composite and save
    result = Image.alpha_composite(img, overlay)
    result = result.convert("RGB")
    result.save(output_path, "PNG")
    return output_path


# ========== Page-specific configs ==========

BASE = r"E:\文境vault\文境Vault\03 成卷（项目）\卷005 · 人+AI不等于更好的产出\配图工作流"

PAGE_CONFIGS = [
    {
        # Page 1: DNA四级光谱
        "title": "你的产出里，有几成是你",
        "subtitle": "任务模式 · DNA 四级光谱",
        "page_number": "01 / 03",
        "labels": [
            {"text": "A级：你的骨架", "x": 0.08, "y": 0.55, "color": "green"},
            {"text": "B级：混合DNA", "x": 0.28, "y": 0.55, "color": "blue"},
            {"text": "C级：AI骨架", "x": 0.48, "y": 0.55, "color": "peach"},
            {"text": "D级：纯AI生成", "x": 0.68, "y": 0.55, "color": "lavender"},
            {"text": "溯源链断了 →", "x": 0.45, "y": 0.72, "color": "peach"},
            {"text": "就是你放手的地方", "x": 0.58, "y": 0.78, "color": "lavender"},
        ]
    },
    {
        # Page 2: 共创三指标
        "title": "协作中，你在变强吗",
        "subtitle": "共创模式 · 三个检测指标",
        "page_number": "02 / 03",
        "labels": [
            {"text": "追问深度", "x": 0.10, "y": 0.50, "color": "blue"},
            {"text": "跳出AI框架", "x": 0.10, "y": 0.60, "color": "blue"},
            {"text": "推翻率", "x": 0.38, "y": 0.50, "color": "peach"},
            {"text": "认知推翻≠修辞推翻", "x": 0.38, "y": 0.60, "color": "peach"},
            {"text": "残留率", "x": 0.66, "y": 0.50, "color": "green"},
            {"text": "关掉AI后脑中的回响", "x": 0.66, "y": 0.60, "color": "green"},
        ]
    },
    {
        # Page 3: 两种自欺
        "title": "最危险的两种自欺",
        "subtitle": "",
        "page_number": "03 / 03",
        "labels": [
            {"text": "高产幻觉", "x": 0.15, "y": 0.55, "color": "peach"},
            {"text": "产出多≠有你在里面", "x": 0.15, "y": 0.65, "color": "peach"},
            {"text": "讨论幻觉", "x": 0.55, "y": 0.55, "color": "lavender"},
            {"text": "AI的独白，你在鼓掌", "x": 0.55, "y": 0.65, "color": "lavender"},
        ]
    }
]
