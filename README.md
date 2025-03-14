Simplex

###########################################################################################################

Simple Netflix. This Python script creates a simple web-based video player that randomly
selects and plays episodes from whatever dir full of videos you want. The application is built with
Flask and features:

- **Random Episode Selection**: Automatically picks a random episode from
which ever TV Show you want, you can add as many TV Shows as you want, just to be sure to update available_folders.
- **Saves Previoulsy Chosen TV Show**: If you choose _**Show F**_ one night and the next night, reload your site, _**Show F**_ will still be selected.
- **Responsive HTML Template**: Includes a dark mode (bc who wants to get blinded), full-screen
viewing, and basic controls.
- **Volume Control**: Adjusts the video volume to 22% upon page load, this can be changed but some of my .mp4s were loud.
- **Autoplay Feature**: Continuously plays the next episode after the current
one finishes.

**Key Features:**
- Uses Flask for rendering and serving web content
- Dark mode on by default
- Auto-scrolls to the bottom of the page to help with viewing on TVs (not sure if this is necessary for you but it helped me with the viewing experience on my own personal TV)

**Note:** This script is intended for local use. Pls don't host publicly!!

###########################################################################################################

**Prerequisites**

  Flask

pip install flask
