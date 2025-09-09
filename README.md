🎶 Emotion-Based Music Recommender

This project is a Flask + DeepFace application that detects the dominant emotion from a user’s face (via image upload or webcam) and recommends a Spotify playlist that matches their mood.

✨ Features
🧠 AI-Powered Emotion Detection – Uses DeepFace
 to analyze facial expressions.
🎵 Spotify Integration – Maps detected emotions to mood-specific Spotify playlists.
💻 Web Interface – Simple front-end (index.html + style.css) to capture and upload images.
📱 Mobile-Friendly – Flask server can be accessed on the same Wi-Fi network from mobile devices.
🛡 Error Handling – Handles missing files, no face detected, or unexpected errors gracefully.

🗂 Project Structure
.
├── app.py          # Flask backend (API + logic for DeepFace)
├── index.html      # Frontend UI (upload image + view result)
├── style.css       # Styling for the frontend
└── uploads/        # Temporary folder for uploaded images (auto-created)

⚙️ Installation
1. Clone the repository
git clone https://github.com/your-username/emotion-music-recommender.git
cd emotion-music-recommender

2. Create & activate a virtual environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3. Install dependencies
pip install flask deepface opencv-python tensorflow

▶️ Usage
1. Run the Flask app
python app.py
The server will start at:
http://127.0.0.1:5000
To access from mobile on same Wi-Fi:
Replace 127.0.0.1 with your local IP in the browser (e.g. http://192.168.1.5:5000/).

2. Open the Web Interface
Upload a photo (with a visible face).
The system will:
Detect the dominant emotion.
Show a Spotify playlist link matching your mood.

🎭 Emotion → Playlist Mapping
Emotion	Spotify Playlist
Happy	55PVuXcePN1SJUh8yczGuR4
Sad	55PVuXcePN1SJUh8yczGuR5
Angry	55PVuXcePN1SJUh8yczGuR6
Neutral	55PVuXcePN1SJUh8yczGuR7
Surprise	55PVuXcePN1SJUh8yczGuR8
Fear	55PVuXcePN1SJUh8yczGuR9
Disgust	370

(These can be customized in app.py inside the playlists dictionary.)

🖼 Frontend Preview
The UI features a cyberpunk-style design with neon colors.
Webcam/Upload input
"Analyze Emotion" button
Playlist link display
Styled via style.css:

body {
  background:#000;
  color:#0ff;
  text-align:center;
}

🚀 Future Improvements
🎥 Real-time webcam emotion detection.
🎶 Auto-play embedded Spotify player.
📊 Emotion history tracking with graphs.
📱 Mobile app integration.

🤝 Contributing
Pull requests are welcome! If you’d like to suggest features or report bugs, please open an issue.
