#!/usr/bin/env python3
"""
Extract audio from video/audio files and convert to text using Whisper AI.
Supports both video files (MP4, MOV, AVI) and audio files (MP3, WAV, M4A, FLAC).
"""

import os
import sys
from pathlib import Path
import whisper
import subprocess


# Supported file extensions
VIDEO_EXTENSIONS = {'.mp4', '.mov', '.avi', '.mkv', '.flv', '.wmv', '.webm', '.m4v'}
AUDIO_EXTENSIONS = {'.mp3', '.wav', '.m4a', '.flac', '.aac', '.ogg', '.wma', '.opus'}


def is_video_file(file_path: str) -> bool:
    """Check if file is a video file based on extension."""
    return Path(file_path).suffix.lower() in VIDEO_EXTENSIONS


def is_audio_file(file_path: str) -> bool:
    """Check if file is an audio file based on extension."""
    return Path(file_path).suffix.lower() in AUDIO_EXTENSIONS


def extract_audio(video_path: str, output_audio_path: str) -> None:
    """Extract audio from video file using ffmpeg."""
    print(f"Extracting audio from {video_path}...")

    cmd = [
        'ffmpeg',
        '-i', video_path,
        '-vn',  # No video
        '-acodec', 'libmp3lame',
        '-q:a', '2',  # High quality
        '-y',  # Overwrite output file
        output_audio_path
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"Error extracting audio: {result.stderr}")
        sys.exit(1)

    print(f"Audio saved to {output_audio_path}")


def transcribe_audio(audio_path: str, model_name: str = "base") -> dict:
    """Transcribe audio file to text using Whisper AI.

    Args:
        audio_path: Path to audio file
        model_name: Whisper model size (tiny, base, small, medium, large)
                   - tiny: fastest, least accurate
                   - base: good balance (default)
                   - small: better accuracy
                   - medium/large: best accuracy, slower

    Returns:
        Dictionary with 'text' and 'segments' keys
    """
    print(f"\nLoading Whisper model '{model_name}'...")
    model = whisper.load_model(model_name)

    print(f"Transcribing audio from {audio_path}...")
    print("This may take a few minutes depending on audio length...")

    result = model.transcribe(audio_path, verbose=True)

    return result


def main():
    if len(sys.argv) < 2:
        print("Usage: python video_to_text.py <file_path> [model_size]")
        print("")
        print("Supports:")
        print("  - Video files: MP4, MOV, AVI, MKV, FLV, WMV, WEBM, M4V")
        print("  - Audio files: MP3, WAV, M4A, FLAC, AAC, OGG, WMA, OPUS")
        print("")
        print("Model sizes: tiny, base (default), small, medium, large")
        sys.exit(1)

    input_path = sys.argv[1]
    model_size = sys.argv[2] if len(sys.argv) > 2 else "base"

    if not os.path.exists(input_path):
        print(f"Error: File not found: {input_path}")
        sys.exit(1)

    # Determine file type
    is_video = is_video_file(input_path)
    is_audio = is_audio_file(input_path)

    if not is_video and not is_audio:
        print(f"Error: Unsupported file format: {Path(input_path).suffix}")
        print(f"Supported video formats: {', '.join(sorted(VIDEO_EXTENSIONS))}")
        print(f"Supported audio formats: {', '.join(sorted(AUDIO_EXTENSIONS))}")
        sys.exit(1)

    # Create output paths
    base_name = Path(input_path).stem
    text_output = f"{base_name}_transcript.txt"
    detailed_output = f"{base_name}_transcript_detailed.txt"

    # Handle video or audio file
    if is_video:
        print(f"📹 Detected video file: {Path(input_path).name}")
        audio_path = f"{base_name}_audio.mp3"
        extract_audio(input_path, audio_path)
    else:
        print(f"🎵 Detected audio file: {Path(input_path).name}")
        audio_path = input_path

    # Transcribe
    result = transcribe_audio(audio_path, model_size)

    # Save full transcript
    with open(text_output, 'w', encoding='utf-8') as f:
        f.write(result['text'])

    # Save detailed transcript with timestamps
    with open(detailed_output, 'w', encoding='utf-8') as f:
        f.write("DETAILED TRANSCRIPT WITH TIMESTAMPS\n")
        f.write("=" * 50 + "\n\n")

        for segment in result['segments']:
            start_time = segment['start']
            end_time = segment['end']
            text = segment['text'].strip()

            f.write(f"[{start_time:.2f}s - {end_time:.2f}s] {text}\n")

    print(f"\n{'='*50}")
    print(f"✅ Transcription complete!")
    print(f"{'='*50}")
    print(f"📄 Full transcript: {text_output}")
    print(f"⏱️  Detailed transcript with timestamps: {detailed_output}")

    if is_video:
        print(f"🎵 Extracted audio: {audio_path}")

    print(f"\n📝 Preview:\n{result['text'][:300]}...")


if __name__ == "__main__":
    main()
