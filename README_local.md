# Video Variation Tool - Local Hosting

This README provides step-by-step instructions for non-coders to set up and run the Video Variation Tool locally on their computer.

## Prerequisites

1. Install Python:
   - Visit https://www.python.org/downloads/
   - Download and install the latest version of Python for your operating system

2. Install FFmpeg:
   - Windows: 
     - Download from https://ffmpeg.org/download.html
     - Extract the ZIP file and add the `bin` folder to your system PATH
   - macOS:
     - Install Homebrew from https://brew.sh/
     - Open Terminal and run: `brew install ffmpeg`
   - Linux:
     - Open Terminal and run: `sudo apt-get install ffmpeg`

## Setup

1. Download the project:
   - Download the `video_variation_tool.py` file and save it to a new folder on your computer

2. Open a terminal or command prompt:
   - Windows: Press Win+R, type "cmd", and press Enter
   - macOS/Linux: Open the Terminal application

3. Navigate to the project folder:
   - Use the `cd` command to change to the directory where you saved the Python file
   - Example: `cd C:\Users\YourName\Documents\VideoVariationTool`

4. Create a virtual environment:
   - Run: `python -m venv venv`

5. Activate the virtual environment:
   - Windows: Run: `venv\Scripts\activate`
   - macOS/Linux: Run: `source venv/bin/activate`

6. Install required packages:
   - Run: `pip install streamlit`

## Running the Tool

1. Make sure you're in the project folder with the virtual environment activated

2. Run the Streamlit app:
   - Execute: `streamlit run video_variation_tool.py`

3. Your default web browser should open automatically with the Video Variation Tool running

4. Upload a video file, click "Create Variations", and download the resulting ZIP file with the variations

## Troubleshooting

- If you encounter any issues with FFmpeg, make sure it's properly installed and added to your system PATH
- For other problems, try restarting your computer and repeating the setup process

Enjoy using the Video Variation Tool!
