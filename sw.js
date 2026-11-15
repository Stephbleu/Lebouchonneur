// Le Bouchonneur v6.1 — service worker
// - pages et données (data/) : réseau d'abord, cache en secours hors ligne
// - autres fichiers (images, icônes, manifest) : cache d'abord
const CACHE = 'bouchonneur-v6-1';
const FILES = ['./', './index.html', './manifest.webmanifest', './assets/bandeau.jpg', './assets/icon-192.png', './assets/icon-512.png'];

self.addEventListener('install', e => {
  self.skipWaiting();
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(FILES)));
});

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys()
      .then(keys => Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', e => {
  const req = e.request;
  const url = new URL(req.url);
  if (req.method !== 'GET' || url.origin !== location.origin) return;

  const isData = url.pathname.includes('/data/');
  const networkFirst = isData || req.mode === 'navigate' || url.pathname.endsWith('/index.html');

  // Pour les données, la clé de cache ignore le paramètre ?t= ajouté par l'application.
  const key = isData ? url.origin + url.pathname : req;

  if (networkFirst) {
    e.respondWith(
      fetch(req)
        .then(res => {
          if (res.ok) {
            const copy = res.clone();
            caches.open(CACHE).then(c => c.put(key, copy));
          }
          return res;
        })
        .catch(() => caches.match(key).then(r => r || caches.match('./index.html')))
    );
    return;
  }

  e.respondWith(
    caches.match(req).then(r => r || fetch(req).then(res => {
      if (res.ok) {
        const copy = res.clone();
        caches.open(CACHE).then(c => c.put(req, copy));
      }
      return res;
    }))
  );
});
