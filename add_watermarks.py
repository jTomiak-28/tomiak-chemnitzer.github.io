import csv
import fitz  # PyMuPDF
import os


input_folder = r"assets\new_manuscripts3"      # folder containing PDFs
output_folder = r"assets\new_manuscripts"    # folder to save processed PDFs

csv_file = r"manuscript-archive-master.csv"      # CSV

bottom_half_mask_pdf = r"bottom_half_mask.pdf"
full_page_mask_pdf = r"full_page_mask.pdf"
watermark_pdf = r"watermark.pdf"


def overlay_pdf(page, overlay_pdf_path):
    overlay_doc = fitz.open(overlay_pdf_path)
    page.show_pdf_page(page.rect, overlay_doc, 0)
    overlay_doc.close()

def process_pdf(input_path, output_path):
    doc = fitz.open(input_path)
    for i, page in enumerate(doc):
        # Apply masks
        
        if i == 1:
            overlay_pdf(page, bottom_half_mask_pdf)
        elif i > 1:
            overlay_pdf(page, full_page_mask_pdf)

        # Apply watermark on every page
        overlay_pdf(page, watermark_pdf)

    doc.save(output_path)
    doc.close()

# ----------------------------
# MAIN LOOP
# ----------------------------
with open(csv_file, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row.get("publisher") == "Vitak-Elsnic Co.":
            file_name = row.get("file_name")
            if not file_name:
                continue

            input_path = os.path.join(input_folder, file_name)
            output_path = os.path.join(output_folder, file_name)

            if not os.path.exists(input_path):
                print(f"File not found: {input_path}")
                continue

            print(f"Processing {file_name} …")
            process_pdf(input_path, output_path)