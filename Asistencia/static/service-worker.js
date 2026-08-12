const CACHE_NAME = "asistencia-isfdyt-v1";

const ARCHIVOS = [
    "/",
    "/static/css/estilos.css",
    "/static/manifest.json"
];

self.addEventListener("install", function(event) {

    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(function(cache) {
                return cache.addAll(ARCHIVOS);
            })
    );

    self.skipWaiting();
});


self.addEventListener("activate", function(event) {

    event.waitUntil(
        caches.keys().then(function(nombres) {

            return Promise.all(
                nombres
                    .filter(function(nombre) {
                        return nombre !== CACHE_NAME;
                    })
                    .map(function(nombre) {
                        return caches.delete(nombre);
                    })
            );

        })
    );

    self.clients.claim();
});


self.addEventListener("fetch", function(event) {

    event.respondWith(
        fetch(event.request)
            .catch(function() {
                return caches.match(event.request);
            })
    );

});