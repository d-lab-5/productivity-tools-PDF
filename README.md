
# 📄 productivity-tools-PDF

**productivity-tools-PDF** is a cross-platform, open-source utility for day-to-day PDF manipulation on Windows and Linux desktops. Built with Python and Tkinter, it provides a simple graphical interface for merging, splitting, and watermarking PDF files—ideal for personal productivity or professional workflows involving sensitive documents.

---

## ✨ Features

- 🔗 **Merge PDFs** – Combine multiple PDF files into one, with progress indication.
- ✂️ **Split PDFs** – Extract every page of a PDF as separate files with custom file naming.
- 🛡️ **Add Watermarks** – Automatically add a diagonal confidentiality watermark, loaded from an external GDPR-compliant JSON template.
- 🖥️ **Simple GUI** – Lightweight Tkinter interface, no need to touch the command line.

---

## 📥 Example: GDPR Watermark

The watermark text is loaded from `gdpr_watermark.json` and applied diagonally across each page:

```
Document strictement confidentiel – transmis uniquement pour instruction du dossier,
 conformément au Règlement Général sur la Protection des Données (RGPD).
Merci de le supprimer après usage.
```

---

## 🛠️ Requirements

- Python 3.8+
- [PyPDF2](https://pypi.org/project/PyPDF2/)
- [reportlab](https://pypi.org/project/reportlab/)
- Tkinter (usually bundled with Python)

Install dependencies:

```bash
pip install PyPDF2 reportlab
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/productivity-tools-PDF.git
cd productivity-tools-PDF
```

### 2. Run the tool

```bash
python pdf_tools.py
```

This will open a simple GUI window with three buttons:
- Merge PDF Files
- Split Single PDF into Pages
- Add Confidentiality Watermark

---

## 🗂️ Project Structure

```
productivity-tools-PDF/
├── pdf_tools.py              # Main GUI tool
├── gdpr_watermark.json       # GDPR watermark text (editable)
├── README.md
```

---

## 🧩 Modular Expansion

Future planned tools for this repo:
- 🗜️ PDF compression
- 🖼️ PDF to image conversion
- 🔄 Image to PDF conversion
- 🔍 OCR with Tesseract
- 📑 Metadata viewer/editor

---

## 📄 License

MIT License — Free to use, modify, and distribute.
