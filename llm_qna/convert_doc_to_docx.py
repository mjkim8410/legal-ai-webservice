import subprocess
from pathlib import Path

input_folder = "data/doc"
output_folder = "data/docx"

def convert_doc_to_docx(input_folder, output_folder=None):
    input_folder = Path(input_folder)

    if output_folder is None:
        output_folder = input_folder
    else:
        output_folder = Path(output_folder)
        output_folder.mkdir(parents=True, exist_ok=True)

    doc_files = list(input_folder.glob("*.doc"))

    if not doc_files:
        print("No .doc files found")
        return

    for doc_file in doc_files:
        try:
            subprocess.run([
                "soffice",  # or full path to soffice.exe
                "--headless",
                "--convert-to", "docx",
                "--outdir", str(output_folder),
                str(doc_file)
            ], check=True)

            print(f"Converted: {doc_file.name}")

        except subprocess.CalledProcessError as e:
            print(f"Failed: {doc_file.name} -> {e}")

if __name__ == "__main__":
    convert_doc_to_docx(input_folder, output_folder)