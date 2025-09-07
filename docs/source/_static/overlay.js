document.addEventListener("DOMContentLoaded", function () {
    fetch("/dashboard/auth-status/")
        .then(res => res.json())
        .then(data => {
            if (!data.logged_in) {
                document.body.classList.add("locked");

                let main = document.querySelector("div.document");
                if (main) main.id = "main-content";

                let overlay = document.createElement("div");
                overlay.id = "login-overlay";
                overlay.innerHTML = `
                    <h2>🔒 Please log in to view full documentation</h2>
                    <p>You can see a preview, but need to log in to read everything.</p>
                    <a href="/users/signin/">Login to Continue</a>
                `;
                document.body.appendChild(overlay);
            }
        });
});
