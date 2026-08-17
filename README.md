# Text to Speech Converter 🎙️🔊

A lightweight Python Command-Line Interface (CLI) application that converts user-inputted text into speech audio files (`.mp3`) using Google Text-to-Speech (`gTTS`).

---

## 🚀 Features

- **Interactive Menu**: User-friendly console interface to generate speech or exit.
- **Text-to-Speech Conversion**: Instant conversion of typed text into clear spoken audio.
- **MP3 Output**: Automatically saves generated speech as `voice.mp3`.

---

## 📋 Prerequisites

- **Python**: 3.7 or higher installed on your machine.
- **Internet Access**: Required by `gTTS` to communicate with Google Translate's text-to-speech API.

---

## 📦 Installation

1. **Clone or Download the Repository**
   ```bash
   git clone <repository-url>
   cd "Text to Speech"
   ```

2. **Install Required Package**
   Install `gTTS` using `pip`:
   ```bash
   pip install gTTS
   ```

---

## 💻 Usage

Run the Python script from your terminal:

```bash
python main.py
```

### Options:
- **`1`** — Enter text to convert to speech. The generated audio will be saved as `voice.mp3` in the workspace directory.
- **`2`** — Exit the program.

#### Example Output:
```text
Press 1 to convert your text to speech.
Press 2 to exit.
Enter the Choice : 1
Enter the text: Hello, welcome to Text to Speech converter!
audio saved successfully
```

---

## 📁 Project Structure

```
Text to Speech/
├── main.py        # Main CLI script containing TTS logic
└── voice.mp3      # Generated MP3 audio file
```

---

## 🛠️ Built With

- [Python 3](https://www.python.org/)
- [gTTS (Google Text-to-Speech)](https://pypi.org/project/gTTS/)
