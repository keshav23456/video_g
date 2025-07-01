from flask import Flask, request, jsonify, send_file
from render import render_code_to_video
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "🎥 Manim Video Generator API is running!"

@app.route("/generate", methods=["POST"])
def generate_video():
    data = request.json
    user_code = data.get("code")

    if not user_code:
        return jsonify({"error": "No 'code' provided"}), 400

    video_path = render_code_to_video(user_code)

    if video_path and os.path.exists(video_path):
        return send_file(video_path, as_attachment=True)
    else:
        return jsonify({"error": "Video generation failed"}), 500

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
