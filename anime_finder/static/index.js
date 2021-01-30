const searchInput = document.getElementById("search-input")

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');


if (searchInput) {
    searchInput.addEventListener("change", () => {
        searchForm = document.getElementById("search-div").innerHTML;
        document.getElementById("search-div").innerHTML = `
            <div class="loading-container">
            <div class="loading">
                <div>
                    <div>
                        <div>
                            <div>
                                <div>
                                    <div>
                                        <div>
                                            <div>
                                                <div> </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        `;

        let formData = new FormData();
        formData.append('image', searchInput.files[0]);

        fetch("/search/",
            {
                body: formData,
                method: "post",
                credentials: 'same-origin',
                headers: {
                    "X-CSRFToken": csrftoken
                }
            }).then(response => response.json())
            .then(data => {
                if (data.success){
                    document.getElementById("search-result").innerHTML = `
                        <div class="row justify-content-center">
                            <div class="col-lg-8 d-flex">
                                <div class="search-result-image" style="background-image: url(${data.anime_thumbnail})">
                                </div>
                                <div class="search-result-info">
                                    <h1>${data.anime_name}</h1>
                                    <div>
                                        <span><i class="uil uil-apps"></i>Part ${data.pard}</span>
                                        <span><i class="uil uil-calender"></i>Year ${data.year}</span>
                                        <span><i class="uil uil-chart-pie-alt"></i>similarity ${data.similarity}%</span>
                                    </div>
                                    <div class="source">
                                        <a href="${data.source}" target="_blank">Source</a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    `;
                    document.getElementById("search-div").innerHTML = searchForm;
                }
            })
    })
}



