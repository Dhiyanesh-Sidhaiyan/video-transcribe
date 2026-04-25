#!/bin/bash
# Setup script for video-to-text converter

echo "Setting up video-to-text converter..."

# Remove old virtual environment if it exists
if [ -d "env" ]; then
    echo "Removing old virtual environment..."
    rm -rf env
fi

# Create new virtual environment with Python 3.12
echo "Creating virtual environment with Python 3.12..."
python3.12 -m venv env

# Activate virtual environment
echo "Activating virtual environment..."
source env/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install requirements
echo "Installing requirements..."
pip install openai-whisper torch torchaudio

echo ""
echo "Setup complete!"
echo ""
echo "To activate the environment, run:"
echo "  source env/bin/activate"
echo ""
echo "To run the script:"
echo "  python video_to_text.py <video_file>"
