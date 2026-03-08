import os
import argparse
from PyPDF2 import PdfReader
from gtts import gTTS
from pydub import AudioSegment
from tqdm import tqdm


def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extracts text from a PDF file.
    """
    reader = PdfReader(pdf_path)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    return text


def split_text(text: str, max_chars: int = 4000):
    """
    Splits text into chunks because TTS APIs often have character limits.
    """
    words = text.split()
    chunks = []
    current_chunk = ""

    for word in words:
        if len(current_chunk) + len(word) + 1 <= max_chars:
            current_chunk += " " + word
        else:
            chunks.append(current_chunk.strip())
            current_chunk = word

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks


def text_to_audio(chunks, output_file="audiobook.mp3"):
    """
    Converts text chunks to speech and merges them into one file.
    """
    combined = AudioSegment.empty()

    for i, chunk in enumerate(tqdm(chunks, desc="Generating audio")):
        tts = gTTS(text=chunk, lang="en")

        temp_file = f"chunk_{i}.mp3"
        tts.save(temp_file)

        audio = AudioSegment.from_mp3(temp_file)
        combined += audio

        os.remove(temp_file)

    combined.export(output_file, format="mp3")
    print(f"\nAudiobook saved as: {output_file}")


def main():
    parser = argparse.ArgumentParser(description="Convert PDF to audiobook.")
    parser.add_argument("pdf", help="Path to the PDF file")
    parser.add_argument(
        "-o", "--output",
        default="audiobook.mp3",
        help="Output audio file name"
    )

    args = parser.parse_args()

    if not os.path.exists(args.pdf):
        print("PDF file not found.")
        return

    print("Extracting text from PDF...")
    text = extract_text_from_pdf(args.pdf)

    print("Splitting text into chunks...")
    chunks = split_text(text)

    print("Converting text to speech...")
    text_to_audio(chunks, args.output)


if __name__ == "__main__":
    main()