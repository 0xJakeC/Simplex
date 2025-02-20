import os
import random
from flask import Flask, render_template_string, send_from_directory

app = Flask(__name__)

# Define the path to your video files
video_directory = "/your_file_path/"

# Get all video files in the directory
video_files = [f for f in os.listdir(video_directory) if f.endswith(('.mp4'))]

# Function to get a random video
def get_random_video():
    return random.choice(video_files)

# HTML template to display the video
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Random Family Guy Episode</title>
    <style>
        /* Dark mode styling */
        body {
            margin: 0;
            padding: 0;
            background-color: black; /* Dark background */
            color: white; /* Light text */
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            font-family: Arial, sans-serif;
        }
        video {
            width: 80%; /* Adjust video width as needed */
            max-height: 80vh; /* Adjust video height as needed */
        }
        h1 {
            margin-bottom: 20px;
            font-size: 1.5rem; /* Half the default size (default is ~3rem) */
        }
    </style>
    <script>
        function setVolume() {
            const videoElement = document.getElementById("videoPlayer");
            videoElement.volume = 0.5; // Set volume to 50%
        }

        function scrollToBottom() {
            window.scrollTo(0, document.body.scrollHeight); // Scroll to the bottom of the page to help with some devices
        }

        function playNextVideo() {
            // Reload the page to get a new random video
            window.location.reload();
        }
    </script>
</head>
<body onload="setVolume(); scrollToBottom();">
    <h1>Now Playing: {{ video_name }}</h1>
    <video id="videoPlayer" controls autoplay onended="playNextVideo()">
        <source src="{{ video_url }}" type="{{ video_mime_type }}">
        Your browser does not support the video tag.
    </video>
</body>
</html>
"""

@app.route('/')
def index():
    random_video = get_random_video()
    video_url = f"/video/{random_video}"
    video_mime_type = "video/mp4"  # Default MIME type
    if random_video.endswith('.mkv'):
        video_mime_type = "video/x-matroska"
    elif random_video.endswith('.avi'):
        video_mime_type = "video/x-msvideo"
    return render_template_string(html_template, video_name=random_video, video_url=video_url, video_mime_type=video_mime_type)

@app.route('/video/<filename>')
def video(filename):
    mimetype = "video/mp4"  # Default MIME type
    if filename.endswith('.mkv'):
        mimetype = "video/x-matroska"
    elif filename.endswith('.avi'):
        mimetype = "video/x-msvideo"
    return send_from_directory(video_directory, filename, mimetype=mimetype)

if __name__ == '__main__':
    # Run the Flask app, you can delete (host='0.0.0.0', port=5000) if you do not wish to access fom a separate device
    app.run(host='0.0.0.0', port=5000, debug=True)
