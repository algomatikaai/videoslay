import streamlit as st
import tempfile
import os
import subprocess
import hashlib
import zipfile
import shutil

def process_video(input_file, output_file, preset):
    if preset == 1:
        # Preset 1: Slight Crop & Saturation
        cmd = f'ffmpeg -i "{input_file}" -vf "crop=iw:ih*0.9:0:ih*0.05,eq=saturation=1.1" -c:a copy "{output_file}"'
    elif preset == 2:
        # Preset 2: Resize & Brightness Adjustment
        cmd = f'ffmpeg -i "{input_file}" -vf "scale=iw*0.95:-1,eq=brightness=0.07:saturation=1.1" -c:a copy "{output_file}"'
    elif preset == 3:
        # Preset 3: Time Shift
        cmd = f'ffmpeg -i "{input_file}" -filter:v "setpts=0.97*PTS,eq=saturation=1.1" -filter:a "atempo=1.03" "{output_file}"'
    
    subprocess.run(cmd, shell=True, check=True)

def change_md5(file_path):
    with open(file_path, 'ab') as f:
        f.write(os.urandom(1))  # Append a random byte to change the hash

def create_variation(input_file, output_file, preset):
    # Remove metadata
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.mp4').name
    subprocess.run(f'ffmpeg -i "{input_file}" -map_metadata -1 -c copy "{temp_file}"', shell=True, check=True)
    
    # Apply preset transformation
    process_video(temp_file, output_file, preset)
    
    # Change MD5 hash
    change_md5(output_file)
    
    os.unlink(temp_file)

def main():
    st.title("Video Variation Tool")
    
    uploaded_file = st.file_uploader("Upload a video file", type=['mp4', 'avi', 'mov'])
    
    if uploaded_file is not None:
        st.video(uploaded_file)
        
        if st.button("Create Variations"):
            with tempfile.TemporaryDirectory() as temp_dir:
                input_path = os.path.join(temp_dir, "input.mp4")
                with open(input_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                
                variations = []
                for i in range(1, 4):
                    output_path = os.path.join(temp_dir, f"variation_{i}.mp4")
                    create_variation(input_path, output_path, i)
                    variations.append(output_path)
                
                zip_path = os.path.join(temp_dir, "variations.zip")
                with zipfile.ZipFile(zip_path, 'w') as zipf:
                    for var in variations:
                        zipf.write(var, os.path.basename(var))
                
                with open(zip_path, "rb") as f:
                    st.download_button(
                        label="Download Variations",
                        data=f.read(),
                        file_name="variations.zip",
                        mime="application/zip"
                    )

if __name__ == "__main__":
    main()
