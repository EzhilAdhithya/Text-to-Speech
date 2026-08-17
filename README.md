# Text to Speech Converter 🎙️🔊

A lightweight Python Command-Line Interface (CLI) application that converts user-inputted text into speech audio files (`.mp3`) using Google Text-to-Speech (`gTTS`).

This repository contains two options:
1. **`main.py`**: Converts text to speech and saves to a single default file (`voice.mp3`).
2. **`MultiVoice.py`**: Allows saving multiple audio recordings with custom filenames or auto-generated timestamped filenames.

---

## 🚀 Features

- **Interactive Menu**: Simple console interface for user choices.
- **Text-to-Speech Engine**: Uses Google Text-to-Speech (`gTTS`) API for speech synthesis.
- **Single-Voice Converter (`main.py`)**: Quickly converts text and outputs to `voice.mp3`.
- **Multi-Voice Converter (`MultiVoice.py`)**: Save as many audio files as you want with custom names (e.g., `my_file.mp3`) or timestamped auto-names (e.g., `voice_YYYYMMDD_HHMMSS.mp3`).

---

## 📋 Prerequisites

- **Python**: 3.7 or higher installed on your machine.
- **Internet Access**: Required by `gTTS` to communicate with Google Translate's TTS API.

---

## 📦 Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/EzhilAdhithya/Text-to-Speech.git
   cd Text-to-Speech
   ```

2. **Install Required Package**
   ```bash
   pip install gTTS
   ```

---

## 💻 Usage

### Option 1: Single Voice Mode (`main.py`)
Run this script to convert text and save it to `voice.mp3`:

```bash
python main.py
```

**Output Example:**
```text
Press 1 to convert your text to speech.
Press 2 to exit.
Enter the Choice: 1
Enter the text: Hello World!
audio saved successfully
```

---

### Option 2: Multi-Voice Mode (`MultiVoice.py`)
Run this script to store multiple audio files with custom or automatic names:

```bash
python MultiVoice.py
```

**Output Example:**
```text
Press 1 to convert your text to speech.
Press 2 to exit.
Enter the Choice: 1
Enter the text: I am a student studying 4th year.
Enter the filename (press Enter for auto-generated name): 
Audio saved successfully as 'voice_20260817_214100.mp3'

Press 1 to convert your text to speech.
Press 2 to exit.
Enter the Choice: 1
Enter the text: Welcome to the project!
Enter the filename (press Enter for auto-generated name): sample_audio
Audio saved successfully as 'sample_audio.mp3'
```

---

## 📁 Project Structure

```
Text to Speech/
├── main.py          # Single voice converter (saves to voice.mp3)
├── MultiVoice.py    # Multi-voice converter (custom / auto timestamped names)
├── voice.mp3        # Sample single output file
└── README.md        # Project documentation
```

---

## 🛠️ Built With

- [Python 3](https://www.python.org/)
- [gTTS (Google Text-to-Speech)](https://pypi.org/project/gTTS/)
