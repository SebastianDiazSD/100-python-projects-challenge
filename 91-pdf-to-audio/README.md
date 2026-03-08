# 📚 PDF to Audio --- Python Audiobook Generator

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![Project](https://img.shields.io/badge/Project-91%2F100%20Python%20Challenge-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Automation](https://img.shields.io/badge/Automation-PDF%20Processing-orange)
![Made With
Love](https://img.shields.io/badge/Built%20with-%F0%9F%87%A8%F0%9F%87%B4%20Colombian%20Coffee-red)

> Transform any **PDF document into an audiobook** using Python.

Long reports, research papers, and books can now be consumed
**hands-free**.\
This tool extracts text from a PDF file and converts it into natural
speech, producing a complete MP3 audiobook.

Designed as part of the **100 Python Projects Challenge**, this project
demonstrates practical applications of:

-   document processing
-   text-to-speech automation
-   command-line tools
-   audio processing pipelines

------------------------------------------------------------------------

# 🚀 Features

• Extracts text directly from PDF documents\
• Converts text into natural speech\
• Automatically splits large documents into manageable chunks\
• Combines audio segments into a single audiobook file\
• Simple command-line interface for automation workflows

------------------------------------------------------------------------

# 🧰 Tech Stack

-   Python
-   PyPDF2 --- PDF text extraction
-   gTTS --- Text-to-speech engine
-   pydub --- Audio merging and processing
-   tqdm --- Progress visualization

------------------------------------------------------------------------

# 📦 Installation

Clone the repository:

``` bash
git clone https://github.com/SebastianDiazSD/100-python-projects-challenge.git
cd 91-pdf-to-audio
```

Install dependencies:

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

# ⚙️ Usage

Convert a PDF into an audiobook:

``` bash
python pdf_to_audio.py mybook.pdf
```

Output:

    audiobook.mp3

Specify a custom output file:

``` bash
python pdf_to_audio.py mybook.pdf -o my_audiobook.mp3
```

------------------------------------------------------------------------

# 🧪 Example Workflow

1.  Provide a PDF file
2.  Extract text from each page
3.  Split text into API-friendly segments
4.  Generate speech for each segment
5.  Merge audio files into a single audiobook

------------------------------------------------------------------------

# 📂 Project Structure

    91-pdf-to-audio
    │
    ├── pdf_to_audio.py
    ├── requirements.txt
    └── README.md

------------------------------------------------------------------------

# 🔮 Future Enhancements

Planned improvements include:

-   Support for multiple languages
-   Voice selection and speed control
-   Integration with advanced TTS providers
-   Batch processing of multiple PDFs
-   Web interface for uploading documents

------------------------------------------------------------------------

# ☕ Engineering Philosophy

Good software should remove friction from everyday tasks.

Turning reading into listening makes knowledge accessible anywhere ---
during commutes, workouts, or long walks.

Built with focus, discipline, and a bit of **Colombian coffee-powered
engineering** 🇨🇴☕

------------------------------------------------------------------------

# 📜 License

MIT License
