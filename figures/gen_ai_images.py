#!/usr/bin/env python3
"""Generate AI images for AURORA X grant proposal using GPT Image 1."""
import os, sys, json, urllib.request, urllib.error, base64, time

API_KEY = os.environ["OPENAI_API_KEY"]
OUT = os.path.dirname(os.path.abspath(__file__))

PROMPTS = {
    "hero_motor_render": {
        "prompt": (
            "Professional studio photograph of a real aerospace-grade brushless electric motor "
            "for drone propulsion, photographed on a matte black surface. Outer rotor design, "
            "machined aluminum housing with visible CNC milling marks, exposed copper stator "
            "windings with precise lacquer finish, neodymium magnet segments visible inside the "
            "rotor bell. An annular green PCB with tiny surface-mount components wraps around "
            "the stator base. Compact cylindrical form factor, approximately 100mm diameter. "
            "Shot with a Canon EOS R5, 100mm macro lens, f/5.6, controlled studio lighting "
            "with two softboxes and a blue gel rim light. Shallow depth of field, tack-sharp "
            "focus on the copper windings. Real engineering prototype, not a render. "
            "Absolutely no text, no labels, no writing, no watermarks, no annotations anywhere in the image."
        ),
        "size": "1536x1024"
    },
    "exploded_view": {
        "prompt": (
            "Overhead photograph of a disassembled high-performance electric motor laid out "
            "on a clean white anti-static mat in an engineering laboratory. Components arranged "
            "in a neat vertical line from top to bottom: 1) machined aluminum outer rotor bell "
            "with arc-shaped neodymium magnet segments glued inside, 2) laminated silicon-steel "
            "stator core with precision-wound copper wire coils, 3) circular green PCB populated "
            "with tiny GaN transistors and ceramic capacitors, 4) machined aluminum housing "
            "with internal vapor chamber channels visible as polished copper cavities. "
            "Each component casts a soft shadow. Shot from directly above, even diffused lighting, "
            "like a product teardown photograph in a professional review. "
            "Absolutely no text, no labels, no writing, no watermarks, no annotations anywhere in the image."
        ),
        "size": "1024x1024"
    },
    "cooling_cutaway": {
        "prompt": (
            "Close-up photograph of a precision wire-EDM cross-section cut through a real electric "
            "motor housing, revealing the internal two-phase cooling system. The cut surface shows "
            "polished aluminum with sealed copper vapor chamber channels surrounding the stator slot "
            "area. Micro-textured evaporator surfaces visible as fine grooves on the inner copper "
            "walls. Condensation fins machined into the outer housing. The stator laminations and "
            "copper windings are visible in cross-section with clean straight cuts. "
            "Photographed on a laboratory bench with a macro lens, ring light illumination, "
            "showing real metallurgy — grain structure of aluminum, bright copper, dark lamination steel. "
            "Engineering metallography style. "
            "Absolutely no text, no labels, no writing, no watermarks, no annotations anywhere in the image."
        ),
        "size": "1024x1024"
    },
    "evtol_concept": {
        "prompt": (
            "Press photograph of a real full-scale eVTOL air taxi prototype during a test flight, "
            "hovering 30 meters above a modern European airport apron at golden hour. The aircraft "
            "has six tilt-rotor nacelles on a high wing configuration, each nacelle housing a compact "
            "electric motor driving a carbon fiber propeller. Clean white fuselage with subtle blue "
            "accent stripe along the side. Landing gear retracted. Shot with a telephoto lens from "
            "ground level, slight heat shimmer from the rotorwash, motion blur on propeller tips. "
            "Background shows a glass-and-steel terminal building and distant city skyline. "
            "Photojournalistic style, like an Aviation Week or FlightGlobal editorial photograph. "
            "Absolutely no text, no labels, no writing, no watermarks, no annotations anywhere in the image."
        ),
        "size": "1536x1024"
    },
    "technology_infographic": {
        "prompt": (
            "Dramatic overhead photograph of four key electric motor technology components "
            "arranged in a diamond pattern on a dark slate surface, each illuminated by its own "
            "spotlight. Top: a stack of ultra-thin silicon-steel laminations (0.2mm each) with a "
            "mirror finish. Right: a small green PCB populated with GaN power transistors, ceramic "
            "capacitors and copper busbars. Bottom: a machined copper vapor chamber heat sink with "
            "micro-grooved evaporator surface. Left: arc-shaped neodymium magnet segments with "
            "nickel plating showing rainbow magnetization patterns. "
            "Center: thin copper wire coil sample. Shot with controlled studio lighting, "
            "each component sharply focused, shallow depth of field on background. "
            "Real components, real materials, real textures. Editorial product photography style. "
            "Absolutely no text, no labels, no writing, no watermarks, no annotations anywhere in the image."
        ),
        "size": "1536x1024"
    }
}

def generate(name, cfg):
    url = "https://api.openai.com/v1/images/generations"
    payload = json.dumps({
        "model": "gpt-image-1",
        "prompt": cfg["prompt"],
        "n": 1,
        "size": cfg["size"],
        "quality": "high",
        "output_format": "png"
    }).encode()

    req = urllib.request.Request(url, data=payload, headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    })

    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            data = json.loads(resp.read())
            item = data["data"][0]
            b64 = item.get("b64_json") or item.get("b64")
            out_path = os.path.join(OUT, f"ai_{name}.png")
            with open(out_path, "wb") as f:
                f.write(base64.b64decode(b64))
            print(f"  OK  ai_{name}.png ({cfg['size']})")
            return True
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        print(f"  FAIL {name}: HTTP {e.code} -- {body[:300]}")
        return False
    except Exception as e:
        print(f"  FAIL {name}: {e}")
        return False

if __name__ == "__main__":
    print("AURORA X image generation (gpt-image-1, high quality)\n")
    ok = 0
    for i, (name, cfg) in enumerate(PROMPTS.items()):
        print(f"[{i+1}/{len(PROMPTS)}] {name}...")
        if generate(name, cfg):
            ok += 1
        if i < len(PROMPTS) - 1:
            print("  waiting 15s (rate limit)...")
            time.sleep(15)
    print(f"\nDone: {ok}/{len(PROMPTS)}")
