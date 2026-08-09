
document.addEventListener('DOMContentLoaded', function() {
        // Inicializa o mapa centralizado em Vassouras
        const map = L.map('mapa').setView([-22.407651911357682, -43.66121621021201], 14)
        const selectFiltro = document.getElementById('filtro-material')

        selectFiltro.addEventListener('change', function(e) {
        const materialSelecionado = e.target.value; // Retorna 'todos', 'plastico', 'papel', etc.
        
        // Aqui entra a lógica de filtrar os marcadores no mapa
        console.log('Material selecionado:', materialSelecionado)
    })

        // Adiciona as camadas gratuitas do OpenStreetMap
        L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
            maxZoom: 19,
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(map);

        // Exemplo de marcador de teste no Centro
        L.marker([-22.4697, -43.8267]).addTo(map)
            .bindPopup('<b>Ponto Central de Coleta</b><br>Aceita Plástico e Papel.')
            .openPopup();
    })