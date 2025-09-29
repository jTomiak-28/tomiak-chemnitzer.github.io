import csv
import os

"""
Given a csv spreadsheet containing the metadata for each piece in the archive,
output one .md file and one .yml file for each piece suitable for use in a Jekyll
collection.
"""

# Path to CSV file
CSV_FILE = "manuscript-archive-master.csv"

# Folder to store generated markdown files
OUTPUT_DIR = "_manuscripts"

# Which columns to include in the front matter
FIELDS = [
    "title",
    "translation",
    "number",
    "key",
    "meter",
    "piece_type",
    "appears_in",
    "composer",
    "arranger",
    "publisher",
    "publication_place",
    "copyright_holder",
    "copyright_year",
    "medium",
    "file_name",
    "notes"
]

def main():

    # make output directory if dne
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with open(CSV_FILE, newline='', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Use a slug from pdf filename or title
            slug = row.get("file_name").replace(".pdf", "")

            # Start front matter
            front_matter = ["---"]

            for field in FIELDS:
                value = row.get(field, "").strip()
                if value:  # only include non-empty values
                    if field == "file_name":
                        # Store as path to assets folder
                        front_matter.append(f'pdf: "/assets/manuscripts/{value}"')
                    else:
                        front_matter.append(f'{field}: "{value}"')

            # Always include layout
            front_matter.append("layout: manuscript")
            front_matter.append("---")
            front_matter.append("")

            # Write file
            output_path = os.path.join(OUTPUT_DIR, f"{slug}.md")
            with open(output_path, "w", encoding="utf-8") as md_file:
                md_file.write("\n".join(front_matter))


if __name__ == "__main__":
    main()