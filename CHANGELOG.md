# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2026-04-25

### Added
- Direct audio file support (MP3, WAV, M4A, FLAC, AAC, OGG, WMA, OPUS)
- Automatic file type detection (video vs audio)
- Enhanced user feedback with file type indicators (📹 video, 🎵 audio)
- Support for 8+ audio formats alongside existing video formats

### Changed
- Updated documentation with audio file examples
- Improved output messages with emoji indicators
- Enhanced README with use cases for both video and audio files

### Fixed
- Better error messages for unsupported file formats

## [1.0.0] - 2026-04-25

### Added
- Initial release
- Video to audio extraction using FFmpeg
- Audio to text transcription using OpenAI Whisper
- Support for multiple Whisper model sizes (tiny, base, small, medium, large)
- Automatic language detection
- Dual output format: plain text and timestamped transcript
- Automated setup script for easy installation
- Comprehensive documentation
- MIT License
- Python 3.10-3.12 support

### Features
- Works completely offline after initial setup
- Supports 99+ languages
- Universal video format support (MP4, MOV, AVI, MKV, FLV, WMV, WEBM, M4V)
- Detailed timestamps for each transcription segment
- High-quality MP3 audio extraction

### Documentation
- Complete README with installation and usage guides
- Contributing guidelines
- Issue templates for bug reports and feature requests
- Changelog
- GitHub publishing guide
