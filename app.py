""""
from flask import Flask, request, jsonify
from deepface import DeepFace
import os
import logging

# Configure basic logging to see what's happening
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

# This dictionary holds the playlists for each mood
# updated playlists with a new link for "neutral"
# Final corrected playlists with the correct embed URL format
playlists = {
    "happy": "https://open.spotify.com/playlist/55PVuXcePN1SJUh8yczGuR4",
    "sad": "https://open.spotify.com/playlist/55PVuXcePN1SJUh8yczGuR5",
    "angry": "https://open.spotify.com/playlist/55PVuXcePN1SJUh8yczGuR6",
    "neutral": "https://open.spotify.com/playlist/55PVuXcePN1SJUh8yczGuR7",
    "surprise": "https://open.spotify.com/playlist/55PVuXcePN1SJUh8yczGuR8",
    "fear": "https://open.spotify.com/playlist/55PVuXcePN1SJUh8yczGuR9",
    "disgust": "https://open.spotify.com/playlist/370"
}

@app.route("/analyze", methods=["POST"])
def analyze():
    # Check if a file was sent in the request
    if "file" not in request.files:
        logging.error("No file part in the request")
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files["file"]

    if file.filename == "":
        logging.error("No file selected")
        return jsonify({"error": "No file selected"}), 400

    # Save the file to a temporary folder
    upload_folder = "uploads"
    os.makedirs(upload_folder, exist_ok=True)
    filepath = os.path.join(upload_folder, file.filename)
    file.save(filepath)
    logging.info(f"File saved to {filepath}")

    try:
        # Use DeepFace to analyze the image for emotions
        analysis = DeepFace.analyze(
            img_path=filepath, 
            actions=["emotion"], 
            enforce_detection=True # Ensures it only processes images with a face
        )
        
        # The result can be a list, so we get the first item
        if isinstance(analysis, list):
            analysis = analysis[0]

        # Get the dominant emotion and find its matching playlist
        detected_emotion = analysis.get("dominant_emotion", "neutral").lower()
        playlist_url = playlists.get(detected_emotion, playlists["neutral"]) # Default to neutral
        
        logging.info(f"Detected emotion: {detected_emotion}")

        # Return the final result in JSON format
        return jsonify({
            "emotion": detected_emotion.capitalize(),
            "playlist_url": playlist_url
        })

    except ValueError:
        # This error happens if DeepFace doesn't find a face
        logging.error("ValueError: No face detected in the image.")
        return jsonify({"error": "No face detected in the image."}), 400
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return jsonify({"error": str(e)}), 500
    finally:
        # Clean up by deleting the temporary file
        if os.path.exists(filepath):
            os.remove(filepath)
            logging.info(f"Cleaned up file: {filepath}")

if __name__ == "__main__":
    # Use host='0.0.0.0' to make the API accessible from your Android device 
    # on the same Wi-Fi network.
    app.run(host='0.0.0.0', port=5000)



"""
from flask import Flask, render_template, request, jsonify
from deepface import DeepFace
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    filepath = os.path.join("uploads", file.filename)
    os.makedirs("uploads", exist_ok=True)
    file.save(filepath)

    try:
        # analyze emotions
        analysis = DeepFace.analyze(img_path=filepath, actions=["emotion"], enforce_detection=False)
        
        # sometimes DeepFace returns dict, sometimes list[dict]
        if isinstance(analysis, list):
            analysis = analysis[0]

        detected_emotion = analysis.get("dominant_emotion", "neutral")

        return jsonify({"emotion": detected_emotion})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
