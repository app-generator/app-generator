const themeToggleDarkIcon = document.getElementById('theme-toggle-dark-icon');
const themeToggleDarkIcon2 = document.getElementById('theme-toggle-dark-icon-2');
const themeToggleLightIcon = document.getElementById('theme-toggle-light-icon');
const themeToggleLightIcon2 = document.getElementById('theme-toggle-light-icon-2');
const themeToggleBtns = [document.getElementById('theme-toggle'), document.getElementById('theme-toggle-2')];

// Change the icons inside the button based on previous settings
if (localStorage.getItem('color-theme') === 'dark' ||
    (!localStorage.getItem('color-theme') && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    themeToggleLightIcon.classList.remove('hidden');
    themeToggleLightIcon2.classList.remove('hidden');
} else {
    themeToggleDarkIcon.classList.remove('hidden');
    themeToggleDarkIcon2.classList.remove('hidden');
}

let event = new Event('dark-mode');

const toggleTheme = () => {
    // Toggle icons
    themeToggleDarkIcon.classList.toggle('hidden');
    themeToggleDarkIcon2.classList.toggle('hidden');
    themeToggleLightIcon.classList.toggle('hidden');
    themeToggleLightIcon2.classList.toggle('hidden');

    // Toggle theme
    if (localStorage.getItem('color-theme') === 'light' ||
        (!localStorage.getItem('color-theme') && !document.documentElement.classList.contains('dark'))) {
        document.documentElement.classList.add('dark');
        localStorage.setItem('color-theme', 'dark');
    } else {
        document.documentElement.classList.remove('dark');
        localStorage.setItem('color-theme', 'light');
    }

    document.dispatchEvent(event);
};

// Add event listeners to buttons
themeToggleBtns.forEach(btn => btn.addEventListener('click', toggleTheme));
