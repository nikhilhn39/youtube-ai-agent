# 🎬 YouTube AI Agent

An AI-powered YouTube automation tool that streamlines content creation by generating scripts, titles, descriptions, hashtags, voiceovers, thumbnails, and videos with minimal manual effort.

---

## 🚀 Features

- 📝 AI Script Generation
- 🎙️ AI Voice Generation
- 🎥 Automatic Video Creation
- 🖼️ AI Thumbnail Generation
- 🏷️ SEO-Friendly Titles
- 📄 Video Description Generation
- 🔖 Hashtag Generation
- 📁 Automatic Output Organization
- ☁️ Optional YouTube Upload Support

---

## 📂 Project Structure

```
youtube_ai_agent/
│
├── assets/
├── modules/
│   ├── script_generator.py
│   ├── voice_generator.py
│   ├── video_fetcher.py
│   ├── video_editor.py
│   ├── thumbnail_generator.py
│   ├── metadata_generator.py
│   └── uploader.py
│
├── outputs/
├── scripts/
├── .env
├── .gitignore
├── main.py
└── README.md
```

---

## 🛠 Technologies Used

- Python 3.10+
- OpenAI API
- ElevenLabs API (Optional)
- FFmpeg
- MoviePy
- Pillow
- Requests
- python-dotenv

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/nikhilhn39/youtube-ai-agent.git
cd youtube-ai-agent
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file.

Example:

```env
OPENAI_API_KEY=your_openai_api_key
ELEVENLABS_API_KEY=your_elevenlabs_api_key
PEXELS_API_KEY=your_pexels_api_key
YOUTUBE_CLIENT_SECRET=client_secret.json
```

---

## ▶️ Usage

Generate a complete YouTube video:

```bash
python main.py --topic "Artificial Intelligence"
```

Example with custom output name:

```bash
python main.py --topic "Python Tutorial" --output_name python_video
```

---

## 📦 Output

The generated files are saved inside the **outputs/** folder.

Example:

```
outputs/
│
├── script.txt
├── voice.mp3
├── video.mp4
├── thumbnail.png
└── metadata.txt
```

---

## 📈 Workflow

1. Enter a video topic
2. Generate AI script
3. Generate AI voice
4. Fetch stock videos
5. Edit and combine clips
6. Generate thumbnail
7. Generate metadata
8. Export final video
9. Upload to YouTube (Optional)

---

## 📌 Future Improvements

- Multi-language support
- AI-generated subtitles
- Trending topic detection
- Automatic Shorts generation
- Background music selection
- Social media publishing
- AI video quality enhancement

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Added new feature"
```

4. Push the branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Nikhil H N**

- GitHub: https://github.com/nikhilhn39
- LinkedIn: https://www.linkedin.com/in/nikhil-h-n

---

⭐ If you found this project useful, consider giving it a star on GitHub!
