# 🎥 Video to Text Converter

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenAI Whisper](https://img.shields.io/badge/Powered%20by-OpenAI%20Whisper-412991.svg)](https://github.com/openai/whisper)

A simple yet powerful tool to extract audio from video files and convert speech to text using OpenAI's Whisper AI. Works completely offline after initial setup!

## ✨ Features

- 🎯 **High Accuracy**: Uses OpenAI's state-of-the-art Whisper model
- 🔒 **Offline**: Works without internet after initial model download
- ⚡ **Fast Processing**: Multiple model sizes for speed/accuracy tradeoff
- 📝 **Dual Output**: Plain text + timestamped transcript
- 🎬 **Universal Format Support**: Works with MP4, MOV, AVI, MKV, and more
- 🌍 **Multi-language**: Supports 99+ languages (auto-detection)

## 📋 Table of Contents

- [Quick Start](#-quick-start)
- [Installation](#-installation)
- [Usage](#-usage)
- [How It Works](#-how-it-works)
- [Dependencies](#-dependencies)
- [Examples](#-examples)
- [Contributing](#-contributing)
- [License](#-license)

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/video-to-text-converter.git
cd video-to-text-converter

# Run automated setup
./setup.sh

# Activate virtual environment
source env/bin/activate

# Convert your video
python video_to_text.py path/to/your/video.mp4
```

Extract audio from video files and convert to text using speech recognition.

## Dependencies

### Python Packages

1. **openai-whisper (20240930)**
   - OpenAI's Whisper automatic speech recognition (ASR) model
   - State-of-the-art speech-to-text conversion
   - Works offline after initial model download
   - Supports multiple languages and accents
   - Functionality: Transcribes audio with high accuracy and provides timestamps
   - Model sizes available: tiny, base, small, medium, large (larger = more accurate but slower)

2. **torch & torchaudio**
   - PyTorch deep learning framework and audio processing library
   - Required dependencies for Whisper to run
   - Handles neural network operations and audio tensor manipulation
   - Functionality: Provides the ML backend for Whisper model inference

### System Dependencies

**ffmpeg** - Required for audio extraction
- Multimedia framework for audio/video processing
- Handles video decoding and audio extraction
- Converts video files to audio format
- Must be installed separately on your system

## 🛠️ Installation

### Prerequisites

**Python 3.10 - 3.12** (Python 3.13+ has compatibility issues with some dependencies)

**FFmpeg** (required for video processing):

| Platform | Installation Command |
|----------|---------------------|
| **macOS** | `brew install ffmpeg` |
| **Ubuntu/Debian** | `sudo apt-get install ffmpeg` |
| **Windows** | Download from [ffmpeg.org](https://ffmpeg.org/download.html) |
| **Arch Linux** | `sudo pacman -S ffmpeg` |

### Automated Setup (Recommended)

```bash
# Clone the repository
git clone https://github.com/yourusername/video-to-text-converter.git
cd video-to-text-converter

# Run setup script (creates virtual environment with Python 3.12)
chmod +x setup.sh
./setup.sh

# Activate the environment
source env/bin/activate
```

### Manual Setup

```bash
# Create virtual environment
python3.12 -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## 📖 Usage

### Basic Usage

```bash
# Use default 'base' model (good balance of speed and accuracy)
python video_to_text.py path/to/video.mp4
```

### Advanced Usage

```bash
# Specify model size for better accuracy
python video_to_text.py path/to/video.mp4 small

# For best accuracy (slower)
python video_to_text.py path/to/video.mp4 large
```

### Model Size Options

| Model | Speed | Accuracy | RAM Required | Best For |
|-------|-------|----------|--------------|----------|
| `tiny` | ~32x realtime | Lower | ~1 GB | Quick drafts, testing |
| `base` | ~16x realtime | Good | ~1 GB | **Default - balanced** |
| `small` | ~6x realtime | Better | ~2 GB | Professional transcripts |
| `medium` | ~2x realtime | High | ~5 GB | Technical content |
| `large` | ~1x realtime | Best | ~10 GB | Critical accuracy needs |

### Processing Pipeline

When you run the script, it will:

1. ✅ **Extract audio** from video using FFmpeg
2. ✅ **Download Whisper model** (first run only, ~150MB for 'base')
3. ✅ **Detect language** automatically
4. ✅ **Transcribe** with timestamps
5. ✅ **Generate outputs** (2 text files + audio)

### Output Files

After processing, you'll get three files:

```
your_video_audio.mp3                    # Extracted audio (MP3 format)
your_video_transcript.txt               # Clean, continuous text
your_video_transcript_detailed.txt      # Text with timestamps
```

**Example detailed output:**
```
[0.00s - 7.00s] Hello everyone, welcome to today's presentation.
[7.00s - 15.50s] Today we'll discuss the architecture of our system.
[15.50s - 23.80s] The first component is the data ingestion layer.
```

## 💡 Examples

### Example 1: Conference Recording
```bash
python video_to_text.py conference_2024.mp4 base
# Output: conference_2024_transcript.txt (with speaker content)
```

### Example 2: Interview Transcription
```bash
python video_to_text.py interview.mov small
# Better accuracy for multi-speaker content
```

### Example 3: Lecture Notes
```bash
python video_to_text.py lecture_week3.mp4 tiny
# Fast transcription for quick notes
```

## 🎯 Use Cases

- 📚 **Education**: Transcribe lectures, tutorials, online courses
- 🎙️ **Podcasts**: Convert video podcasts to text blogs
- 🎬 **Content Creation**: Generate subtitles, captions
- 📝 **Documentation**: Meeting notes, interviews, presentations
- ♿ **Accessibility**: Create text versions of video content
- 🔍 **SEO**: Make video content searchable

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. 🍴 Fork the repository
2. 🌱 Create a feature branch (`git checkout -b feature/amazing-feature`)
3. 💾 Commit your changes (`git commit -m 'Add amazing feature'`)
4. 📤 Push to the branch (`git push origin feature/amazing-feature`)
5. 🎉 Open a Pull Request

Please ensure your code:
- Follows Python PEP 8 style guidelines
- Includes appropriate comments
- Updates documentation if needed

## 🐛 Known Issues

- **Python 3.13+**: Not currently supported due to dependency issues (use 3.10-3.12)
- **Large files**: Videos over 2 hours may require the `large` model for best results
- **Heavy accents**: Consider using `small` or larger models for better accuracy

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [OpenAI Whisper](https://github.com/openai/whisper) - The amazing speech recognition model
- [FFmpeg](https://ffmpeg.org/) - Multimedia processing framework
- All contributors who help improve this tool

## 📞 Support

- 🐛 **Issues**: [GitHub Issues](https://github.com/yourusername/video-to-text-converter/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/yourusername/video-to-text-converter/discussions)

---

**Made with ❤️ by developers, for developers**