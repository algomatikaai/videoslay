# Video Variation Tool - Streamlit Cloud Hosting

This README provides step-by-step instructions for non-coders to host the Video Variation Tool on Streamlit Cloud.

## Prerequisites

1. GitHub Account:
   - If you don't have one, sign up at https://github.com/

2. Streamlit Cloud Account:
   - Sign up at https://streamlit.io/cloud using your GitHub account

## Setup

1. Create a new GitHub repository:
   - Go to https://github.com/new
   - Name your repository (e.g., "video-variation-tool")
   - Choose "Public" for visibility
   - Click "Create repository"

2. Upload files to your repository:
   - Click "uploading an existing file"
   - Drag and drop or select the following files:
     - `video_variation_tool.py`
     - `requirements.txt` (create this file with the content: `streamlit`)
   - Commit the changes

3. Create a `packages.txt` file:
   - In your GitHub repository, click "Add file" > "Create new file"
   - Name the file `packages.txt`
   - Add the following content:     ```
     ffmpeg     ```
   - Commit the new file

## Deploying on Streamlit Cloud

1. Log in to Streamlit Cloud:
   - Go to https://share.streamlit.io/

2. Deploy a new app:
   - Click "New app"
   - Select your GitHub repository, branch (usually "main"), and the `video_variation_tool.py` file
   - Click "Deploy"

3. Wait for the deployment to complete:
   - Streamlit Cloud will install the necessary dependencies and start your app
   - This may take a few minutes

4. Access your app:
   - Once deployment is successful, you'll see a URL for your app
   - Click the URL to open your Video Variation Tool

## Using the Tool

1. Upload a video file using the file uploader

2. Click "Create Variations" to process the video

3. Download the ZIP file containing the video variations

## Troubleshooting

- If you encounter any issues, check the Streamlit Cloud logs for error messages
- Make sure all required files (`video_variation_tool.py`, `requirements.txt`, and `packages.txt`) are present in your GitHub repository
- If problems persist, try redeploying the app or contact Streamlit support

Enjoy using your cloud-hosted Video Variation Tool!
