import subprocess
import os
import uuid

def render_code_to_video(user_code: str, output_dir="videos"):
    unique_id = str(uuid.uuid4())[:8]
    temp_py_file = f"temp_scene_{unique_id}.py"
    
    # Prepare scene template
    try:
        with open("templates/runner_template.py", "r") as f:
            template = f.read()
    except FileNotFoundError:
        print("🔥 ERROR: Template file 'runner_template.py' not found.")
        return None

    final_code = template.replace("{{USER_CODE}}", user_code)

    # Save temp scene
    with open(temp_py_file, "w") as f:
        f.write(final_code)

    # Build command
    command = [
        "manim", temp_py_file, "MyGeneratedScene",
        "-qk",
        "-o", f"video_{unique_id}.mp4",
        "--media_dir", output_dir
    ]
    print(f"🎬 Running: {' '.join(command)}")

    try:
        result = subprocess.run(command, capture_output=True, text=True)

        print("=== MANIM STDOUT ===")
        print(result.stdout)
        print("=== MANIM STDERR ===")
        print(result.stderr)

        if result.returncode != 0:
            print("❌ Manim rendering failed.")
            return None

        # Construct the real path
        scene_name = temp_py_file.replace(".py", "")
        video_path = os.path.join(output_dir, "videos", scene_name, "480p15", f"video_{unique_id}.mp4")

        print(f"✅ Generated video at: {video_path}")
        return video_path

    except Exception as e:
        print("🔥 Exception during rendering:", str(e))
        return None

    finally:
        if os.path.exists(temp_py_file):
            os.remove(temp_py_file)
