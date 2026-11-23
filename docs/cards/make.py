# Writes card-<key>.html for each project; render each with readme-header scripts/render-banner.ts -> card-<key>.png
import pathlib

HERE = pathlib.Path(__file__).parent
TEMPLATE = """<!doctype html>
<html lang="th">
<head>
<meta charset="utf-8" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Thai:wght@500;700&display=block" rel="stylesheet" />
<style>
  :root { --bg: #E9EEF3; --ink: #181C27; --muted: #576573; --accent: {accent}; --glow: {glow}; }
  * { box-sizing: border-box; margin: 0; }
  html, body { width: 1280px; height: 640px; overflow: hidden; background: var(--bg); }
  body {
    font-family: "IBM Plex Sans Thai", "Noto Sans Thai", "Inter", sans-serif; color: var(--ink); position: relative;
    background:
      radial-gradient(700px 380px at 50% 100%, var(--glow), transparent 70%),
      radial-gradient(500px 260px at 12% 0%, rgb(255 255 255 / 0.7), transparent 70%),
      linear-gradient(rgb(0 45 116 / 0.05) 1px, transparent 1px) 0 0 / 40px 40px,
      linear-gradient(90deg, rgb(0 45 116 / 0.05) 1px, transparent 1px) 0 0 / 40px 40px,
      var(--bg);
  }
  .top { text-align: center; padding-top: 44px; }
  .brand { display: inline-flex; align-items: center; gap: 12px; font-weight: 700; font-size: 26px; }
  .brand img { height: 44px; border-radius: 11px; }
  h1 { margin-top: 18px; font-size: 48px; line-height: 1.2; font-weight: 700; letter-spacing: -0.01em; }
  h1 em { font-style: normal; color: var(--accent); }
  .checks { margin-top: 14px; display: flex; justify-content: center; gap: 22px; font-size: 19px; font-weight: 500; color: var(--muted); }
  .checks span::before { content: "✔"; color: var(--accent); margin-right: 7px; }
  .shot {
    position: absolute; left: 50%; top: 236px; transform: translateX(-50%);
    width: 1080px; height: 420px; overflow: hidden; padding: 32px 36px 0;
    background: linear-gradient(160deg, var(--accent), {accent2});
    border-radius: 14px 14px 0 0; border: 1px solid rgb(0 45 116 / 0.15); border-bottom: 0;
    box-shadow: 0 -10px 60px var(--glow), 0 0 0 6px rgb(255 255 255 / 0.6);
  }
  .shot img { width: 100%; display: block; border-radius: 12px 12px 0 0; box-shadow: 0 8px 30px rgb(0 45 116 / 0.3); }
</style>
</head>
<body>
  <div class="top">
    <div class="brand"><img src="{icon}" alt="" />{name}</div>
    <h1>{before} <em>{accent_text}</em>{after}</h1>
    <div class="checks">{checks}</div>
  </div>
  <div class="shot"><img src="{shot}" alt="" /></div>
</body>
</html>
"""

CARDS = {
    "rabbit": dict(name="Rabbit Rewards", icon="rabbit-icon.png", shot="rabbit.png",
                   accent="#F28C1E", accent2="#0F2357", glow="rgb(242 140 30 / 0.28)",
                   before="เปลี่ยนทุกการเดินทาง", accent_text="เป็นรางวัล", after="",
                   checks=["สะสมแต้มจาก BTS และบัตร Rabbit", "แลกเที่ยวเดินทางฟรี", "โปรโมชั่นร้านค้าพาร์ทเนอร์"]),
    "opendata": dict(name="Open Data · Urban Ally", icon="ua-teal.png", shot="opendata.png",
                     accent="#22A99A", accent2="#147a70", glow="rgb(34 169 154 / 0.28)",
                     before="ศูนย์รวม", accent_text="ข้อมูลเมืองแบบเปิด", after=" ของอาเซียน",
                     checks=["ภาพรวมสภาพแวดล้อมเมือง", "Geodata สำหรับออกแบบเมือง", "ข้อมูลระดับโลก", "เมือง 15 นาที"]),
    "sonic": dict(name="Sonic Bangkok · Urban Ally", icon="ua-dark.png", shot="sonic.png",
                  accent="#22A99A", accent2="#181C27", glow="rgb(34 169 154 / 0.28)",
                  before="สำรวจย่านเมืองเก่า", accent_text="ผ่านเสียง", after="",
                  checks=["ฐานข้อมูลเสียงแบบเปิด", "แผนที่กรองตามธีมเสียง", "ร่วมกับ Hear&amp;Found"]),
}

for key, c in CARDS.items():
    checks = "".join(f"<span>{x}</span>" for x in c.pop("checks"))
    html = TEMPLATE
    for k, v in {**c, "checks": checks}.items():
        html = html.replace("{" + k + "}", v)
    (HERE / f"card-{key}.html").write_text(html)
    print("wrote", f"card-{key}.html")
