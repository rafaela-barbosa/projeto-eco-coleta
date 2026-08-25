
document.addEventListener('DOMContentLoaded', function() {
        // Inicializa o mapa centralizado em Vassouras
        const map = L.map('mapa').setView([-22.407651911357682, -43.66121621021201], 16)
        

        // Adiciona as camadas gratuitas do OpenStreetMap
        L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
            maxZoom: 19,
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(map);

        // Exemplo de marcador de teste no Centro
        L.marker([-22.40435633133417, -43.6576533571171]).addTo(map)
            .bindPopup(`
        <div class="popup-coleta">
            <h6 class="fw-bold mb-0 text-dark">Ponto Central de Coleta</h6>
            <p class="mb-0 small">📍 Rua Principal, 100</p>
            <p class="mb-0 small"> ♻️ Pilhas, Baterias</p>
            <p class="mb-0 small text-muted">⏰ Seg-Sex: 8h às 17h</p>
        </div>
            `)
            .openPopup();

        // define pontos no mapa
        var ponto1 = L.marker([-22.407651911357682, -43.66121621021201]).bindPopup('Ponto 1 fica aqui.')
        var ponto2 = L.marker([-22.407651911357682, -43.66121621021201]).bindPopup('Ponto 2 fica aqui.')
        var ponto3 = L.marker([-22.407651911357682, -43.66121621021201]).bindPopup('Ponto 3 fica aqui.')

        // agrupa pontos em camadas separadas
        var pontos = L.layerGroup([ponto1, ponto2, ponto3])

    })