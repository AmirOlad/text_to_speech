# 🎙️ Speech-to-Text

> **🇮🇷 [فارسی](README_FA.md)**

A simple and practical **Speech-to-Text** tool that converts spoken audio into written text using Google's online speech recognition service.

The script is designed to handle long audio files, automatically split them into smaller segments, retry failed requests, and save the final transcription as a UTF-8 text file.

---

## ✨ Features

- 🎤 **Speech-to-Text** — Convert spoken audio into written text.
- 📁 **Flexible Input** — Provide a specific audio file or let the script automatically find the latest `pars*.wav` file.
- ⏱️ **Long Audio Support** — Long recordings are automatically split into **30-second segments** to work around limitations of Google's free speech recognition service.
- 🔄 **Automatic Retry** — Failed requests are retried up to **3 times** in case of temporary network issues.
- 💾 **Automatic Saving** — Transcriptions are saved as UTF-8 `.txt` files next to the source audio file.
- 🌍 **Multiple Languages** — Change the recognition language using the `-l` option. The default language is Persian (`fa-IR`).
- 🚫 **Optional Saving** — Disable automatic text file creation with `--no-save`.
- ⚠️ **Detailed Error Messages** — Provides separate messages for missing files, unsupported formats, network problems, and missing audio.
- 🧩 **Simple CLI** — Easy to use directly from the terminal.

---

## 📦 Installation

Make sure you have **Python 3** installed.

Install the required dependency with:

```bash
pip install SpeechRecognition
```

Clone the repository:

```bash
git clone https://github.com/AmirOlad/text_to_speech.git
cd text_to_speech
```

---

## 🚀 Usage

### Basic Usage

Run the script without specifying an input file:

```bash
python transcribe.py
```

In this mode, the script automatically searches for the latest file matching:

```text
pars*.wav
```

This is useful when the audio file was created by another recording script that follows the same naming convention.

---

### Transcribe a Specific File

You can provide the path to an audio file:

```bash
python transcribe.py pars_test.wav
```

Or:

```bash
python transcribe.py my_voice.wav
```

---

### Change the Recognition Language

The default language is:

```text
fa-IR
```

For English speech, use:

```bash
python transcribe.py my_voice.wav -l en-US
```

You can replace the language code with another supported Google Speech Recognition language code.

---

### Specify an Output File

By default, the transcription is saved as a `.txt` file next to the audio file.

You can specify a custom output path:

```bash
python transcribe.py my_voice.wav -l en-US -o result.txt
```

---

### Disable Automatic Saving

If you only want the transcription output without creating a `.txt` file, use:

```bash
python transcribe.py my_voice.wav --no-save
```

---

## 🛠️ Command-Line Options

| Option | Description |
|---|---|
| `FILE` | Path to the input audio file |
| `-l`, `--language` | Speech recognition language. Default: `fa-IR` |
| `-o`, `--output` | Specify the output `.txt` file |
| `--no-save` | Disable saving the transcription to a file |

### Examples

```bash
# Automatically find the latest pars*.wav file
python transcribe.py

# Transcribe a specific file
python transcribe.py pars_test.wav

# Transcribe English audio
python transcribe.py my_voice.wav -l en-US

# Save to a custom output file
python transcribe.py my_voice.wav -l en-US -o result.txt

# Transcribe without saving a text file
python transcribe.py my_voice.wav --no-save
```

---

## ⏱️ Long Audio Processing

Google's free online speech recognition service can have difficulties processing long audio files in a single request.

To handle this, the script automatically divides long recordings into **30-second segments**:

```text
Audio File
    │
    ├── 0–30 seconds
    ├── 30–60 seconds
    ├── 60–90 seconds
    ├── ...
    │
    └── Combined Transcription
```

Each segment is transcribed separately and the resulting text is combined into the final transcription.

This allows the script to process longer recordings more reliably.

---

## 🔄 Automatic Retry

Temporary internet problems can cause individual speech recognition requests to fail.

The script automatically retries failed requests up to **3 times** before reporting an error.

This makes the transcription process more resilient to short network interruptions.

---

## 💾 Output

By default, the generated transcription is saved as a UTF-8 text file next to the source audio.

For example:

```text
my_voice.wav
my_voice.txt
```

The output file contains the recognized speech as plain text.

You can also choose a custom output filename:

```bash
python transcribe.py my_voice.wav -o transcription.txt
```

---

## 🌍 Language Support

The default recognition language is Persian:

```text
fa-IR
```

For example, to recognize English:

```bash
python transcribe.py my_voice.wav -l en-US
```

The language parameter can be changed according to the language of the spoken audio.

---

## ⚠️ Error Handling

The script provides specific error messages for common problems, including:

- ❌ Input file not found
- ❌ Unsupported or invalid audio format
- 🌐 Internet connection problems
- 🔇 No recognizable speech in the audio
- ⚠️ Speech recognition service errors

This makes it easier to identify and troubleshoot problems during transcription.

---

## 🌐 Internet Requirement

This project uses **Google's online Speech Recognition service**, so an active internet connection is required.

The audio is processed through the online recognition service rather than being transcribed completely offline.

> **Note:** Google's free speech recognition service may have limitations, especially when processing very long recordings. This project addresses long recordings by splitting them into 30-second segments.

---

## 📋 Requirements

- Python 3.x
- Internet connection
- `SpeechRecognition`

Install the required package with:

```bash
pip install SpeechRecognition
```

---

## 📂 Project Structure

A simple project structure can look like this:

```text
.
├── Speech_to_text.py
├── README.md
├── README_FA.md
└── pars_test.wav
```

The audio file is only an example and does not need to be included in the repository.

---

## 🔐 Privacy Notice

This project relies on an **online speech recognition service**. Audio data used for transcription is therefore processed through the service rather than entirely on your local machine.

Avoid using sensitive or confidential recordings unless you have reviewed the applicable service's privacy and data-handling policies.

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

If you find a bug or have an idea for improving the project, feel free to open an **Issue** or submit a **Pull Request**.

---

## 📄 License

Add your preferred open-source license here.

For example:

```text
MIT License
```

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

**Built with Python and SpeechRecognition.**
