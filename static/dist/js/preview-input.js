
// Preview image
document.getElementById('id_thumbnail').addEventListener('change', function(event) {
    const input = event.target;
    const file = input.files[0];
    const label = document.getElementById('thumbnail_label');
    const previewContainer = document.getElementById('preview-container');
    const imagePreview = document.getElementById('imagePreview');

    if (file) {
        const reader = new FileReader();

        reader.onload = function(e) {
            imagePreview.style.display = 'block';
            imagePreview.src = e.target.result;
            previewContainer.style.display = 'block';
            label.style.display = 'none';
            document.getElementById('removePreview').style.display = 'block';
        };

        reader.readAsDataURL(file);
    }
});
document.getElementById('removePreview').addEventListener('click', function(event) {
    event.preventDefault();
    const input = document.getElementById('id_thumbnail');
    const label = document.getElementById('thumbnail_label');
    const previewContainer = document.getElementById('preview-container');
    const imagePreview = document.getElementById('imagePreview');
    
    imagePreview.src = '#';
    previewContainer.classList.add('hidden');
    label.style.display = 'flex';
    input.style.display = 'block';
    input.value = '';
    imagePreview.style.display = 'none';
    document.getElementById('removePreview').style.display = 'none';
});


// Preview youtube video
document.getElementById('id_video').addEventListener('input', function(event) {
    updateVideoPreview(event.target.value);
});

window.addEventListener('load', function() {
    const videoInput = document.getElementById('id_video');
    updateVideoPreview(videoInput.value);
});

function updateVideoPreview(videoUrl) {
    const videoPreviewContainer = document.getElementById('video-preview-container');
    const videoPreview = document.getElementById('videoPreview');
    
    const videoId = extractYouTubeVideoID(videoUrl);
    if (videoId) {
        videoPreview.src = `https://www.youtube.com/embed/${videoId}`;
        videoPreviewContainer.classList.remove('hidden');
    } else {
        videoPreview.src = '';
        videoPreviewContainer.classList.add('hidden');
    }
}

function extractYouTubeVideoID(url) {
    const regex = /(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})/;
    const matches = url.match(regex);
    return matches ? matches[1] : null;
}
