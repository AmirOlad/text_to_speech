import argparse
import sys
import time
from pathlib import Path

import speech_recognition as sr

CHUNK_SECONDS = 30
MAX_RETRIES = 3


def parse_args():
    p = argparse.ArgumentParser(description="PARS AI - تبدیل صدا به متن")
    p.add_argument("file", nargs="?", default=None,
                   help="مسیر فایل WAV/FLAC/AIFF (پیش‌فرض: جدیدترین فایل pars*.wav)")
    p.add_argument("-l", "--lang", default="fa-IR",
                   help="زبان تشخیص (پیش‌فرض: fa-IR). مثال: en-US")
    p.add_argument("-o", "--output", default=None,
                   help="ذخیره‌ی متن در فایل (پیش‌فرض: کنار فایل صوتی با پسوند .txt)")
    p.add_argument("--no-save", action="store_true",
                   help="متن در فایل ذخیره نشود")
    return p.parse_args()


def find_default_file():
    candidates = sorted(Path(".").glob("pars*.wav"), key=lambda f: f.stat().st_mtime)
    return candidates[-1] if candidates else None


def recognize_with_retry(recognizer, audio, lang):
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            return recognizer.recognize_google(audio, language=lang)
        except sr.RequestError:
            if attempt == MAX_RETRIES:
                raise
            print(f"   ⚠️ خطای شبکه، تلاش مجدد ({attempt}/{MAX_RETRIES})...")
            time.sleep(2 * attempt)


def transcribe(path, lang):
    recognizer = sr.Recognizer()
    parts = []

    with sr.AudioFile(str(path)) as source:
        total = source.DURATION
        print(f"⏱ مدت فایل: {total:.1f} ثانیه")

        chunks = max(1, int(total // CHUNK_SECONDS) + (1 if total % CHUNK_SECONDS else 0))
        for n in range(chunks):
            audio = recognizer.record(source, duration=CHUNK_SECONDS)
            if chunks > 1:
                print(f"🧠 بخش {n + 1} از {chunks}...")
            try:
                text = recognize_with_retry(recognizer, audio, lang)
                parts.append(text)
            except sr.UnknownValueError:
                print(f"   ❌ در بخش {n + 1} صدای واضحی تشخیص داده نشد.")

    return " ".join(parts).strip()


def main():
    args = parse_args()

    path = Path(args.file) if args.file else find_default_file()
    if path is None or not path.exists():
        print("❌ فایل صوتی پیدا نشد.")
        print("مسیر فایل را بدهید، مثلاً:  python transcribe.py pars_test.wav")
        return 1

    print("🤖 PARS AI")
    print(f"🎧 فایل: {path}")

    try:
        text = transcribe(path, args.lang)
    except sr.RequestError as e:
        print("❌ ارتباط با سرویس تشخیص صدا برقرار نشد.")
        print("اینترنت خود را چک کنید (این سرویس آنلاین است).")
        print(f"جزئیات: {e}")
        return 1
    except ValueError:
        print("❌ فرمت فایل پشتیبانی نمی‌شود. فقط WAV (PCM)، FLAC و AIFF.")
        print("برای MP3 و بقیه، اول با ffmpeg به WAV تبدیل کنید.")
        return 1
    except Exception as e:
        print(f"❌ خطای غیرمنتظره: {e}")
        return 1

    if not text:
        print("❌ هیچ متنی تشخیص داده نشد. میکروفون، ولوم یا زبان انتخابی را چک کنید.")
        return 1

    print("\n✅ متن تشخیص داده شده:")
    print(text)

    if not args.no_save:
        out = Path(args.output) if args.output else path.with_suffix(".txt")
        out.write_text(text, encoding="utf-8")
        print(f"\n💾 متن ذخیره شد: {out.resolve()}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
