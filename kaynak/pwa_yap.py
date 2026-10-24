# Derlenmiş uygulamayı (kaynak/metronom.html) kurulabilir web uygulamasına çevirir:
#   python3 kaynak/pwa_yap.py   ->  index.html, manifest.webmanifest, sw.js
import re, json, os
SURUM = os.environ.get('SURUM', '69')
frag = open('kaynak/metronom.html', encoding='utf-8').read()
i = frag.index('</style>') + len('</style>')
bas, govde = frag[:i], frag[i:]
baslik = re.search(r'<title>.*?</title>', bas, re.S).group(0)
stil = re.search(r'<style>.*?</style>', bas, re.S).group(0)
html = f'''<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#f6f6f2" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#151614" media="(prefers-color-scheme: dark)">
<meta name="color-scheme" content="light dark">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Göz Metronomu">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" type="image/png" sizes="32x32" href="simge/simge-32.png">
<link rel="apple-touch-icon" href="simge/simge-180.png">
{baslik}
<style>
  html {{ padding-top: env(safe-area-inset-top, 0px); padding-bottom: env(safe-area-inset-bottom, 0px); }}
  body {{ margin: 0; font: 14px system-ui, -apple-system, "Segoe UI", Roboto, sans-serif; }}
  [hidden] {{ display: none !important; }}
  img {{ max-width: 100%; }}
</style>
{stil}
</head>
<body>
{govde}
<script>
// Kurulabilir uygulama: çevrimdışı çalışma + egzersiz sırasında ekranın kararmasını engelleme
if ('serviceWorker' in navigator) {{
  window.addEventListener('load', () => {{ navigator.serviceWorker.register('sw.js').catch(() => {{}}); }});
}}
(() => {{
  let kilit = null;
  const egzersizVar = () => !!document.querySelector('[id$="-calis"]:not(.hidden)') || (document.getElementById('rt-bar') && document.getElementById('rt-bar').classList.contains('on'));
  const al = async () => {{
    try {{ if (navigator.wakeLock && document.visibilityState === 'visible' && !kilit) {{ kilit = await navigator.wakeLock.request('screen'); kilit.addEventListener('release', () => {{ kilit = null; }}); }} }} catch (e) {{ kilit = null; }}
  }};
  const birak = () => {{ try {{ if (kilit) {{ kilit.release(); }} }} catch (e) {{}} kilit = null; }};
  setInterval(() => {{ if (egzersizVar()) al(); else birak(); }}, 2000);
  document.addEventListener('visibilitychange', () => {{ if (document.visibilityState === 'visible' && egzersizVar()) al(); }});
}})();
</script>
</body>
</html>
'''
open('index.html', 'w', encoding='utf-8').write(html)
json.dump({
  'id': './', 'name': 'Göz Takibi Metronomu', 'short_name': 'Göz Metronomu',
  'description': 'Hızlı okuma ve göz egzersizi uygulaması',
  'lang': 'tr', 'start_url': './', 'scope': './', 'display': 'standalone',
  'background_color': '#151614', 'theme_color': '#151614',
  'icons': [
    {'src': 'simge/simge-192.png', 'sizes': '192x192', 'type': 'image/png', 'purpose': 'any'},
    {'src': 'simge/simge-512.png', 'sizes': '512x512', 'type': 'image/png', 'purpose': 'any'},
    {'src': 'simge/simge-512.png', 'sizes': '512x512', 'type': 'image/png', 'purpose': 'maskable'}
  ]
}, open('manifest.webmanifest', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
sw = f'''// Çevrimiçiyken her zaman en yeni sürümü getirir, çevrimdışıyken kayıtlı kopyayı kullanır.
const ONBELLEK = 'goz-metronomu-v{SURUM}';
const DOSYALAR = ['./', 'index.html', 'manifest.webmanifest', 'simge/simge-192.png', 'simge/simge-512.png', 'simge/simge-180.png', 'simge/simge-32.png'];
self.addEventListener('install', e => {{
  e.waitUntil(caches.open(ONBELLEK).then(c => c.addAll(DOSYALAR)).then(() => self.skipWaiting()));
}});
self.addEventListener('activate', e => {{
  e.waitUntil(caches.keys().then(k => Promise.all(k.filter(x => x !== ONBELLEK).map(x => caches.delete(x)))).then(() => self.clients.claim()));
}});
self.addEventListener('fetch', e => {{
  if (e.request.method !== 'GET' || new URL(e.request.url).origin !== location.origin) return;
  e.respondWith(
    fetch(e.request).then(r => {{
      if (r && r.ok) {{ const kopya = r.clone(); caches.open(ONBELLEK).then(c => c.put(e.request, kopya)); }}
      return r;
    }}).catch(() => caches.match(e.request).then(r => r || caches.match('index.html')))
  );
}});
'''
open('sw.js', 'w', encoding='utf-8').write(sw)
print('PWA hazır, index.html', len(html) // 1024, 'KB')
