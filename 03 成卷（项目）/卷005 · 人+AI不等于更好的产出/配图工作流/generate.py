"""
Generate 3 body illustrations using SD 1.5 + ComfyUI + text overlay.
"""
import subprocess, json, os, sys
from pathlib import Path

# Paths
SKILL_DIR = r"E:\hermes\skills\creative\comfyui"
WORK_DIR = r"E:\文境vault\文境Vault\03 成卷（项目）\卷005 · 人+AI不等于更好的产出\配图工作流"
OUTPUT_DIR = os.path.join(WORK_DIR, "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

WORKFLOW_TEMPLATE = os.path.join(WORK_DIR, "sd15_169_body.json")
RUN_WORKFLOW = os.path.join(SKILL_DIR, "scripts", "run_workflow.py")

# Common negative prompt
NEGATIVE = (
    "ugly, blurry, low quality, deformed, distorted, bad anatomy, "
    "watermark, text, signature, letters, words, characters, alphabet, "
    "photograph, photo, realistic, 3d render, digital art smooth, "
    "bright colors, saturated, neon, gradient, shadow, "
    "border, frame, edge decoration, "
    "people, person, human, face, portrait, "
    "cluttered, messy, busy, complex background, "
    "corporate, business, presentation, slide template, "
    "thick lines, heavy marker, childish, cartoon, doodle"
)

# Prompts for each page
PROMPTS = [
    # Page 1: DNA 四级光谱
    (
        "hand-drawn technical illustration on warm off-white paper, "
        "four delicate objects arranged from left to right showing a gradient of completeness, "
        "leftmost: detailed hand-drawn architectural blueprint with fine pencil hatching, "
        "second: similar blueprint but some lines fading into simpler strokes, "
        "third: sparse line drawing with rough outline, "
        "rightmost: barely-there dotted outline dissolving into paper grain, "
        "thin arrow connecting them left to right, "
        "fine black ink lines, delicate crosshatching, "
        "tiny pastel colored sticky notes scattered around: pale blue, sage green, peach, lavender, "
        "small faint grey corner marks, generous negative space, "
        "minimalist composition, centered small diagram, "
        "academic notebook aesthetic, refined, precise, "
        "wide empty margins, calming premium illustration"
    ),
    # Page 2: 共创三指标
    (
        "hand-drawn technical illustration on warm off-white paper, "
        "three small stations arranged horizontally across the middle, "
        "left station: a magnifying glass examining a small detailed object on a desk, "
        "middle station: a simple balance scale with one side heavier, "
        "right station: a small hourglass with a few grains still falling, "
        "thin arrows between stations, "
        "fine black ink lines, delicate pencil hatching, "
        "small pastel marker labels near each station: pale blue, peach, sage green, "
        "faint grey corner grid dots, generous negative space, "
        "minimalist composition, centered small diagram, "
        "academic notebook aesthetic, refined, precise, "
        "wide empty margins, calming premium illustration"
    ),
    # Page 3: 两种自欺
    (
        "hand-drawn technical illustration on warm off-white paper, "
        "left half: a stack of identical blank papers piling up, with a small "
        "mechanical gear beside them - repetitive, hollow productivity, "
        "right half: a single spotlight illuminating an empty stage, tiny empty chairs, "
        "a faint dividing line down the middle, "
        "fine black ink lines, delicate crosshatching, "
        "small pastel sticky notes: peach on left (warm but muted), lavender on right, "
        "faint grey corner marks, generous negative space, "
        "minimalist composition, centered small diagram, "
        "academic notebook aesthetic, refined, precise, "
        "wide empty margins, calming premium illustration"
    ),
]

def generate():
    results = []
    for i, prompt in enumerate(PROMPTS):
        print(f"\n{'='*60}")
        print(f"Generating page {i+1}/3...")
        
        # Load and modify workflow
        with open(WORKFLOW_TEMPLATE, "r") as f:
            workflow = json.load(f)
        
        workflow["3"]["inputs"]["seed"] = 156680208700286 + i * 1000
        workflow["6"]["inputs"]["text"] = prompt
        workflow["7"]["inputs"]["text"] = NEGATIVE
        workflow["9"]["inputs"]["filename_prefix"] = f"page_{i+1:02d}"
        
        # Save temp workflow
        temp_wf = os.path.join(OUTPUT_DIR, f"temp_wf_{i}.json")
        with open(temp_wf, "w") as f:
            json.dump(workflow, f)
        
        # Run
        cmd = [
            sys.executable, RUN_WORKFLOW,
            "--workflow", temp_wf,
            "--output-dir", OUTPUT_DIR,
            "--host", "http://127.0.0.1:8188",
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        print(result.stdout[-500:] if result.stdout else "")
        if result.stderr:
            print("STDERR:", result.stderr[-300:])
        
        results.append(result)
    
    return results

if __name__ == "__main__":
    generate()
