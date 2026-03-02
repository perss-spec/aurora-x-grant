#!/usr/bin/env python3
"""Generate AI images for AURORA X grant proposal using DALL-E 3."""
import os, sys, json, urllib.request, urllib.error, base64, time

API_KEY = os.environ["OPENAI_API_KEY"]
OUT = os.path.dirname(os.path.abspath(__file__))

PROMPTS = {
    "hero_motor_render": {
        "prompt": "Photorealistic 3D render of a compact high-tech electric motor for drone propulsion, outer rotor design with visible copper windings, integrated circuit board ring around the stator, blue LED accents, dark studio background with subtle blue rim lighting, engineering product photography style, ultra detailed, 8K quality. The motor is sleek, cylindrical, about 100mm diameter, with visible cooling fins and aerospace-grade materials.",
        "size": "1792x1024"
    },
    "exploded_view": {
        "prompt": "Technical exploded view diagram of an electric motor showing 4 key subsystems separated vertically: 1) outer rotor with Halbach magnet array segments (orange), 2) stator with copper windings (blue), 3) annular green circuit board (GaN inverter), 4) integrated cooling chamber with vapor channels (red). Clean white background, precise engineering illustration style, labeled arrows, professional technical drawing, isometric perspective.",
        "size": "1024x1024"
    },
    "cooling_cutaway": {
        "prompt": "Technical cutaway cross-section illustration of a two-phase thermosyphon cooling system inside an electric motor. Show sealed vapor chamber around stator windings, water vapor bubbles rising from heated copper coils, condensation zone with external fins at top. Blue-to-red thermal gradient colors showing heat flow. Clean technical illustration style, engineering diagram with arrows showing coolant circulation, dark background.",
        "size": "1024x1024"
    },
    "evtol_concept": {
        "prompt": "Futuristic eVTOL air taxi flying over a modern European city skyline at golden hour, 6 electric motors visible on tilting wings, sleek white and blue design, photorealistic rendering, cinematic lighting. The aircraft is clean, modern, with visible propellers driven by compact electric motors. Blue sky with light clouds, sustainable urban air mobility concept.",
        "size": "1792x1024"
    },
    "technology_infographic": {
        "prompt": "Clean modern infographic showing 4 technology pillars as connected hexagonal icons on a dark blue background: 1) electric motor coils icon, 2) semiconductor chip icon, 3) cooling/snowflake icon, 4) magnet horseshoe icon. Connected by glowing blue lines in a network pattern. Minimalist flat design, professional corporate style, suitable for European grant proposal. Title space at top.",
        "size": "1792x1024"
    }
}

def generate(name, cfg):
    url = "https://api.openai.com/v1/images/generations"
    payload = json.dumps({
        "model": "dall-e-3",
        "prompt": cfg["prompt"],
        "n": 1,
        "size": cfg["size"],
        "quality": "hd",
        "response_format": "b64_json"
    }).encode()

    req = urllib.request.Request(url, data=payload, headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    })

    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            data = json.loads(resp.read())
            b64 = data["data"][0]["b64_json"]
            out_path = os.path.join(OUT, f"ai_{name}.png")
            with open(out_path, "wb") as f:
                f.write(base64.b64decode(b64))
            print(f"✓ ai_{name}.png ({cfg['size']})")
            return True
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        print(f"✗ {name}: HTTP {e.code} — {body[:200]}")
        return False
    except Exception as e:
        print(f"✗ {name}: {e}")
        return False

if __name__ == "__main__":
    print("Generating AURORA X AI images...\n")
    ok = 0
    for name, cfg in PROMPTS.items():
        if generate(name, cfg):
            ok += 1
        time.sleep(1)
    print(f"\nDone: {ok}/{len(PROMPTS)} images generated")
