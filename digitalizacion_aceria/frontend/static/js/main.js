document.addEventListener('DOMContentLoaded', function () {
    // Función para actualizar los datos en tiempo real
    function updateRealTimeData() {
        fetch('/')
            .then(response => response.text())
            .then(html => {
                document.getElementById('real-time-data').innerHTML = html;
            })
            .catch(error => console.error('Error:', error));
    }

    // Actualizar los datos cada 5 segundos
    setInterval(updateRealTimeData, 5000);

    // Manejar el formulario de consulta histórica
    const historicalForm = document.getElementById('historical-form');
    if (historicalForm) {
        historicalForm.addEventListener('submit', function (event) {
            event.preventDefault();
            const startDate = document.getElementById('start-date').value;
            const endDate = document.getElementById('end-date').value;

            fetch(`/historical?start_date=${startDate}&end_date=${endDate}`)
                .then(response => response.text())
                .then(html => {
                    document.getElementById('historical-data').innerHTML = html;
                })
                .catch(error => console.error('Error:', error));
        });
    }
});