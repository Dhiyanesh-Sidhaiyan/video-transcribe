# Contributing to Video to Text Converter

Thank you for considering contributing to this project! We welcome contributions from everyone.

## 🚀 Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/your-username/video-to-text-converter.git
   cd video-to-text-converter
   ```
3. **Create a branch** for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## 🛠️ Development Setup

1. **Install dependencies**:
   ```bash
   ./setup.sh
   source env/bin/activate
   ```

2. **Make your changes** and test them:
   ```bash
   python video_to_text.py test_video.mp4
   ```

## ✅ Pull Request Guidelines

Before submitting a pull request:

1. **Test your changes** thoroughly
2. **Update documentation** if you've added new features
3. **Follow PEP 8** style guidelines for Python code
4. **Write clear commit messages**:
   ```
   Add feature: Description of what you added
   
   - Detail 1
   - Detail 2
   ```

## 🐛 Reporting Bugs

When reporting bugs, please include:

1. **Python version**: `python --version`
2. **OS and version**: macOS 14, Ubuntu 22.04, etc.
3. **Error message**: Full traceback if available
4. **Steps to reproduce**: Minimal example to reproduce the issue
5. **Expected vs actual behavior**

## 💡 Suggesting Features

We love feature suggestions! Please:

1. Check if the feature has already been requested
2. Clearly describe the use case
3. Explain why this would be useful
4. Provide examples if possible

## 📝 Code Style

- Follow [PEP 8](https://pep8.org/) style guidelines
- Use meaningful variable names
- Add docstrings to functions
- Keep functions focused and small
- Add comments for complex logic

## 🧪 Testing

Before submitting:

```bash
# Test with different video formats
python video_to_text.py test.mp4
python video_to_text.py test.mov
python video_to_text.py test.avi

# Test with different model sizes
python video_to_text.py test.mp4 tiny
python video_to_text.py test.mp4 base
python video_to_text.py test.mp4 small
```

## 📜 License

By contributing, you agree that your contributions will be licensed under the MIT License.

## ❓ Questions?

Feel free to open an issue for any questions about contributing!

Thank you for making this project better! 🎉
