# Uygulama simgelerini üretir (PIL gerekir): python3 kaynak/ikon_yap.py
from PIL import Image, ImageDraw
import os
def ciz(boy):
    k = 4; b = boy * k
    im = Image.new('RGB', (b, b), (21, 22, 20))
    d = ImageDraw.Draw(im)
    # İz çizgisi ve noktalar (ortadaki nokta aktif)
    cy = b // 2
    xs = [0.22, 0.36, 0.50, 0.64, 0.78]
    ys = [0.58, 0.44, 0.52, 0.60, 0.46]
    d.line([(b * x, b * y) for x, y in zip(xs, ys)], fill=(59, 61, 55), width=int(b * 0.012))
    for i, (x, y) in enumerate(zip(xs, ys)):
        r = b * (0.075 if i == 2 else 0.04)
        renk = (255, 125, 82) if i == 2 else (162, 164, 152)
        if i == 2:
            d.ellipse([b * x - b * 0.105, b * y - b * 0.105, b * x + b * 0.105, b * y + b * 0.105], outline=(255, 125, 82), width=int(b * 0.012))
        d.ellipse([b * x - r, b * y - r, b * x + r, b * y + r], fill=renk)
    return im.resize((boy, boy), Image.LANCZOS)
os.makedirs('simge', exist_ok=True)
for ad, boy in (('simge-192.png', 192), ('simge-512.png', 512), ('simge-180.png', 180), ('simge-32.png', 32)):
    ciz(boy).save('simge/' + ad)
print('simgeler hazır')
