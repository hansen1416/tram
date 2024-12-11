import os
import subprocess

target_folder = os.path.join("/tram", "videos")
results_folder = os.path.join("/tram", "results")

# list all files in `target_folder`
files = os.listdir(target_folder)

print(f"got {len(files)} files")

for f in files:

    file_name = f.split(".")[0]

    video_name = os.path.join(results_folder, file_name, "tram_output.mp4")

    if os.path.exists(video_name):
        print(f"{f} video already processed")
        continue
    else:
        print(f"{f} video in process")

    # # check if the results already exists
    # if os.path.exists(os.path.join(results_folder, file_name)):
    #     print(f"{f} already processed")
    #     continue
    # else:
    #     print(f"{f} in process")

    video_path = os.path.join(target_folder, f)

    # List of commands to run
    commands = [
        # ["python", "scripts/estimate_camera.py", "--video", video_path],
        # ["python", "scripts/estimate_humans.py", "--video", video_path],
        ["python", "scripts/visualize_tram.py", "--video", video_path],
    ]

    for command in commands:
        subprocess.run(command, check=True)
