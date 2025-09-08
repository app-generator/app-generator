document.addEventListener("DOMContentLoaded", function () {
    document.documentElement.setAttribute("data-theme", "light");
    document.documentElement.setAttribute("data-mode", "light");
});

document.addEventListener("DOMContentLoaded", function () {
    fetch("/dashboard/auth-status/")
        .then(res => res.json())
        .then(data => {
            if (!data.logged_in) {
                document.body.classList.add("locked");

                let overlay = document.createElement("div");
                overlay.id = "login-overlay";
                overlay.innerHTML = `
                    <h2>Content reserved for authenticated users.</h2>
                    <a href="/users/signin/">Please SignIN.</a>
                `;
                document.body.appendChild(overlay);

                setTimeout(() => {
                    overlay.classList.add("show");
                }, 50);
            }
        });
});
