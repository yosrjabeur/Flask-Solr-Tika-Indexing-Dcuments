document.addEventListener('DOMContentLoaded', () => {
    const searchForm = document.querySelector('form[action="/search"]');
    const searchResultsDiv = document.getElementById('search-results');

    searchForm.addEventListener('submit', async (event) => {
        event.preventDefault();

        const query = searchForm.querySelector('input[name="q"]').value;
        const response = await fetch(`/search?q=${encodeURIComponent(query)}`);
        const searchResults = await response.json();

        let html = '<h3>Résultats de la recherche :</h3>';
        searchResults.forEach(result => {
            const dotIndex = result.title.lastIndexOf('.');
            if (dotIndex !== -1) {
                const title = result.title.substring(0, dotIndex); 
                const extension = result.title.substring(dotIndex + 1); 

                html += `<div class="list-group-item list-group-item-action">
                            <div class="d-flex w-100 justify-content-between">
                                <h5 class="mb-1">${title}.${extension}</h5>
                                <small>Score : ${result.score}</small>
                            </div>
                        </div>`;
            } else {
                html += `<div class="list-group-item list-group-item-action">
                            <div class="d-flex w-100 justify-content-between">
                                <h5 class="mb-1">${result.title}</h5>
                                <small>Score : ${result.score}</small>
                            </div>
                        </div>`;
            }
        });
        searchResultsDiv.innerHTML = html;
    });
});
