import json, sys, os, re, collections
s = sys.argv[1]; base = sys.argv[2]
files = ["metinler-yetiskin.json","metinler-yetiskin-2.json","metinler-yetiskin-hazir.json",
         "metinler-cocuk.json","metinler-cocuk-2.json","metinler-cocuk-hazir.json",
         "metinler-yetiskin-kitap.json","metinler-cocuk-kitap.json","metinler-tekrarli-yeni.json","metinler-meb.json","metinler-halk.json","metinler-yazi.json","metinler-yetiskin-yeni.json"]
DISARI = {"ch01","ch02","ch03","ch04","ch05"}
TEKNIK = {"ck042","ck043","ck044","ck059","ck075","ck076"}
keep = ["id","seviye","baslik","metin","yazar","kaynak","lisans"]
sinifmap = json.load(open(os.path.join(base,"Metinler/metin-sinif.json"), encoding="utf-8"))
liste, ids = [], set()
for f in files:
    p = os.path.join(base, "Metinler", f)
    if not os.path.exists(p): continue
    for m in json.load(open(p, encoding="utf-8")):
        if m["id"] in DISARI or m["id"] in ids: continue
        if m.get("yazarOlum") and m["lisans"] == "Kamu malı" and m["yazarOlum"] > 1954: continue
        # Nasreddin fıkraları: derleyici/telif doğrulanamadı -> uygulamaya alma
        if not m["id"].startswith("halk") and m.get("kaynak", "").startswith("https://tr.wikisource.org") and ("Nasreddin" in m.get("yazar", "") or "fıkra" in m.get("yazar", "").lower() or m.get("yazarOlum") == 1284): continue
        # Çocuk için fazla teknik bulunan Vikipedi parçaları
        if m["id"] in TEKNIK: continue
        ids.add(m["id"])
        r = {k: m[k] for k in keep if k in m}
        if r["seviye"] != "yetiskin":
            g = sinifmap[r["id"]]["grup"]
            if g == "cikar": continue
            r["seviye"] = g
        liste.append(r)
_yk = lambda n: json.load(open(os.path.join(base,"Kelimeler",n), encoding="utf-8"))
_yet = _yk("kelimeler-yetiskin-son.json")
kel = {"yetiskin": _yet, "1-2": _yk("kelimeler-1-2.json"), "3-4": _yk("kelimeler-3-4.json"), "5-6": _yk("kelimeler-5-6.json"), "7-8": _yk("kelimeler-7-8.json")}
dg = {"yetiskin": json.load(open(os.path.join(base,"Kelimeler/neyi-degisti-yetiskin.json"), encoding="utf-8")),
      "cocuk": json.load(open(os.path.join(base,"Kelimeler/neyi-degisti-cocuk.json"), encoding="utf-8"))}
trs = json.load(open(os.path.join(base,"Metinler/tekrarli-sorular.json"), encoding="utf-8"))
trs.update(json.load(open(os.path.join(base,"Metinler/tekrarli-sorular-yazi.json"), encoding="utf-8")))
trs.update(json.load(open(os.path.join(base,"Metinler/tekrarli-sorular-yetiskin.json"), encoding="utf-8")))
trs.update(json.load(open(os.path.join(base,"Metinler/tekrarli-sorular-sinif.json"), encoding="utf-8")))
_ek = os.path.join(base,"Metinler/tekrarli-sorular-ek.json")
trs2 = json.load(open(_ek, encoding="utf-8")) if os.path.exists(_ek) else {}
js = lambda o: json.dumps(o, ensure_ascii=False).replace("</", "<\\/")
t = open(os.path.join(s,"sablon.html"), encoding="utf-8").read().replace("__METINLER__", js(liste)).replace("__KELIMELER__", js(kel)).replace("__DEGISEN__", js(dg)).replace("__TRSORU__", js(trs)).replace("__TRSORU2__", js(trs2))
open(os.path.join(s,"metronom.html"), "w", encoding="utf-8").write(t)
open(os.path.join(s,"metronom.html.js"),"w",encoding="utf-8").write(re.search(r"<script>(.*)</script>", t, re.S).group(1))
print(dict(collections.Counter(m["seviye"] for m in liste)), "toplam", len(liste), "KB", len(t)//1024)
