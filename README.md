# YouTube Video Summarizer

A Streamlit web application that uses AI to generate summaries and extract key points from YouTube videos using their transcripts.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0%2B-red)
![License](https://img.shields.io/badge/License-MIT-green)

## Features

- 🎥 YouTube video transcript extraction
- 🤖 AI-powered text summarization
- 📝 Key points extraction
- 🎯 Video preview integration
- 💻 User-friendly interface
- ⚡ Real-time processing
- 🔍 Support for various YouTube URL formats

## Installation

1. Clone the repository:
```bash
git clone https://github.com/agneya-1402/youtube-video-summarizer.git
cd youtube-video-summarizer
```

2. Create and activate a virtual environment:
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python -m venv venv
source venv/bin/activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the Streamlit app:
```bash
streamlit run app.py
```

2. Open your web browser and go to `http://localhost:8501`

3. Paste a YouTube video URL into the input field

4. Click the "Summarize" button and wait for the results

## Requirements

- Python 3.8 or higher
- Internet connection for YouTube transcript access
- GPU recommended but not required
- Supported browsers: Chrome, Firefox, Safari, Edge

## How It Works

1. **URL Processing**: The application extracts the video ID from various YouTube URL formats
2. **Transcript Extraction**: Uses the YouTube Transcript API to fetch video captions
3. **Text Summarization**: Implements the BART model from Facebook/Meta for generating concise summaries
4. **Key Points**: Extracts important points from the summary using natural language processing
5. **Display**: Presents the results in a clean, user-friendly interface

## Limitations

- Only works with YouTube videos that have available transcripts/closed captions
- Maximum video length depends on available system memory
- Summarization quality may vary based on transcript quality

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Streamlit](https://streamlit.io/) for the web application framework
- [YouTube Transcript API](https://github.com/jdepoix/youtube-transcript-api) for transcript extraction
- [Hugging Face Transformers](https://huggingface.co/transformers/) for the summarization model
