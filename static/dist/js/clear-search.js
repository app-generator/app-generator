const clearSearch = () => {
    const urlParams = new URLSearchParams(window.location.search);
    urlParams.delete("search");
    const newUrl = window.location.pathname + (urlParams.toString() ? "?" + urlParams.toString() : "");
    window.history.replaceState({}, document.title, newUrl);
    window.location.reload();
};   

const clearSearchButton = document.getElementById("clear-search");
clearSearchButton && clearSearchButton.addEventListener("click", clearSearch);

