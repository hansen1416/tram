import os
import subprocess

target_folder = os.path.join("/tram", "videos")

# list all files in `target_folder`
files = os.listdir(target_folder)

for f in files:

    video_path = os.path.join(target_folder, f)

    # List of commands to run
    commands = [
        [
            "python",
            "scripts/estimate_camera.py",
            "--video",
            video_path,
            "--static_camera",
        ],
        ["python", "scripts/estimate_humans.py", "--video", video_path],
        ["python", "scripts/visualize_tram.py", "--video", video_path],
    ]

    for command in commands:
        subprocess.run(command, capture_output=True, text=True, check=True)
