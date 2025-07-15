#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PDF Tools – Merge, Split, and Watermark Utility with GUI
---------------------------------------------------------

This tool allows you to:
- Merge multiple PDF files into one.
- Split a single PDF into individual pages.
- Apply a multi-line, diagonal confidentiality watermark to a PDF.
- Load GDPR watermark text from an external JSON file.

Author: [Your Name]
Date: 2025
"""

import os
import json
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinter.simpledialog import askstring
from PyPDF2 import PdfMerger, PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO


def merge_pdfs(pdf_files, output_filename='_merged.pdf'):
    merger = PdfMerger()
    total_files = len(pdf_files)

    progress_window = tk.Toplevel()
    progress_window.title("Merging PDFs")
    tk.Label(progress_window, text="Merging PDFs...").pack(pady=10)
    progress_bar = ttk.Progressbar(progress_window, length=300, mode='determinate', maximum=total_files)
    progress_bar.pack(pady=10)

    file_info = []
    for i, pdf in enumerate(pdf_files):
        reader = PdfReader(pdf)
        file_info.append((os.path.basename(pdf), len(reader.pages)))
        merger.append(pdf)
        progress_bar['value'] = i + 1
        progress_window.update_idletasks()

    merger.write(output_filename)
    merger.close()
    progress_window.destroy()

    result_message = f"Merged {total_files} PDFs into {output_filename}:\n\n"
    for file_name, num_pages in file_info:
        result_message += f"{file_name} - {num_pages} pages\n"
    messagebox.showinfo("Success", result_message)


def split_pdf(pdf_file, output_dir):
    reader = PdfReader(pdf_file)
    base_name = askstring("Nom du fichier", "Nom de base pour les fichiers PDF séparés :")
    if not base_name:
        base_name = "page"

    for i, page in enumerate(reader.pages):
        writer = PdfWriter()
        writer.add_page(page)
        output_filename = os.path.join(output_dir, f"{base_name}_{i + 1}.pdf")
        with open(output_filename, 'wb') as f:
            writer.write(f)
    messagebox.showinfo("Success", f"Split {len(reader.pages)} pages to:\n{output_dir}")


def create_watermark(text):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)

    c.setFont("Helvetica", 10)
    # c.setFillColorRGB(0.7, 0.7, 0.7)
    c.setFillColorRGB(1, 1, 1)

    width, height = letter
    c.saveState()
    c.translate(width / 2, height / 2)
    c.rotate(45)

    # Split text into lines manually using \n
    lines = text.split("\\n")
    line_height = 22

    for i, line in enumerate(lines):
        y_offset = (len(lines) - 1) * line_height / 2 - i * line_height
        c.drawCentredString(0, y_offset, line)

    c.restoreState()
    c.save()
    buffer.seek(0)
    return PdfReader(buffer)


def watermark_pdf(input_pdf_path, output_pdf_path, watermark_text):
    reader = PdfReader(input_pdf_path)
    watermark = create_watermark(watermark_text)
    watermark_page = watermark.pages[0]

    writer = PdfWriter()
    for page in reader.pages:
        page.merge_page(watermark_page)
        writer.add_page(page)

    with open(output_pdf_path, 'wb') as f:
        writer.write(f)


def select_merge():
    files = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])
    if files:
        output_dir = filedialog.askdirectory()
        if output_dir:
            os.chdir(output_dir)
            merge_pdfs(files, os.path.join(output_dir, '_merged.pdf'))


def select_split():
    file = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file:
        output_dir = filedialog.askdirectory()
        if output_dir:
            split_pdf(file, output_dir)


def select_watermark():
    file = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file:
        output_dir = filedialog.askdirectory()
        if output_dir:
            try:
                with open("gdpr_watermark.json", "r", encoding="utf-8") as f:
                    data = json.load(f)
                    watermark_text = data.get("watermark_text", "Confidential")
            except Exception as e:
                messagebox.showerror("Error", f"Could not read watermark text:\n{e}")
                return

            output_file = os.path.join(
                output_dir,
                os.path.splitext(os.path.basename(file))[0] + "_watermarked.pdf"
            )
            watermark_pdf(file, output_file, watermark_text)
            messagebox.showinfo("Success", f"Watermarked file saved as:\n{output_file}")


# ---- GUI Setup ----
root = tk.Tk()
root.title("PDF Tools")

tk.Button(root, text="Merge PDF Files", command=select_merge).pack(pady=10)
tk.Button(root, text="Split Single PDF into Pages", command=select_split).pack(pady=10)
tk.Button(root, text="Add Confidentiality Watermark", command=select_watermark).pack(pady=10)

root.mainloop()


