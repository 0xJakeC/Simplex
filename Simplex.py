import os
import random
from flask import Flask, render_template_string, request, redirect, url_for, send_from_directory

app = Flask(__name__)

# Base directory
base_directory = "Enter_the_Path_to_all_of_your_TV_Show_Folders"

# Predefined list of folders, rename how you want
available_folders = {
    "Name 1": "Name_1_Folder",
    "Name 2": "Name_2_Folder",
    etc
    
}

# Default folder for when the page first loads or the service or script is restarted
selected_folder = "Name_1_Folder"

# HTML template that I found and modified to display the video and folder selection form
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Random Video Player</title>
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
            font-size: 1.5rem; /* Half the default size because the text was too big */
        }
        form {
            margin-bottom: 20px;
        }
        select, input[type="submit"] {
            padding: 5px;
            font-size: 1rem;
            background-color: rgba(0, 0, 0, 0.7);
            color: white;
            border: 2px solid white;
            border-radius: 5px;
            cursor: pointer;
        }
        select {
            width: 200px;
        }
        input[type="submit"]:hover {
            background-color: rgba(255, 255, 255, 0.1);
        }
    </style>
    <script>
        function setVolume() {
            const videoElement = document.getElementById("videoPlayer");
            // You can delete or change the setVolume function, my files were just loud
            videoElement.volume = 0.22; // Set volume to 22%
        }

        function playNextVideo() {
            // Reload the page to get a new random video
            window.location.reload();
        }
    </script>
</head>
// scrollToBottom can also be deleted if not needed but it helps when I use my TV to access Simplex
<body onload="setVolume(); scrollToBottom();">
    <h1>Now Playing: {{ video_name }}</h1>
    <form action="/set_folder" method="post">
        <label for="folder">Select TV Show:</label>
        <select id="folder" name="folder">
            {% for name, folder in available_folders.items() %}
                <option value="{{ folder }}" {% if folder == selected_folder %}selected{% endif %}>{{ name }}</option>
            {% endfor %}
        </select>
        <input type="submit" value="Play">
    </form>
    <video id="videoPlayer" controls autoplay onended="playNextVideo()">
        <source src="{{ video_url }}" type="{{ video_mime_type }}">
        Your browser does not support the video tag.
    </video>
</body>
</html>
"""

@app.route('/')
def index():
    global selected_folder
    # Create the full directory path
    video_directory = os.path.join(base_directory, selected_folder)

    # Get all video files in the directory
    video_files = [f for f in os.listdir(video_directory) if f.endswith(('.mp4', '.mkv', '.avi', '.mov'))]
    if not video_files:
        return "No video files found in the directory."

    # Randomly select a video file
    random_video = random.choice(video_files)
    video_url = f"/video/{random_video}"
    video_mime_type = "video/mp4"  # Default MIME type
    if random_video.endswith('.mkv'):
        video_mime_type = "video/x-matroska"
    elif random_video.endswith('.avi'):
        video_mime_type = "video/x-msvideo"
    return render_template_string(html_template, video_name=random_video, video_url=video_url, video_mime_type=video_mime_type, available_folders=available_folders, selected_folder=selected_folder)

@app.route('/set_folder', methods=['POST'])
#Send the selected TV show back to the Pi
def set_folder():
    global selected_folder
    selected_folder = request.form['folder']
    return redirect(url_for('index'))

@app.route('/video/<filename>')
def video(filename):
    global selected_folder
    # Create the full directory path
    video_directory = os.path.join(base_directory, selected_folder)

    mimetype = "video/mp4"  # Default MIME type
    if filename.endswith('.mkv'):
        mimetype = "video/x-matroska"
    elif filename.endswith('.avi'):
        mimetype = "video/x-msvideo"
    return send_from_directory(video_directory, filename, mimetype=mimetype)

if __name__ == '__main__':
    # Run the Flask app, you can delete (host='0.0.0.0', port=5000) if you do not want to access fom a separate device
    app.run(host='0.0.0.0', port=5000, debug=True)
