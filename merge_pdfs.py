import os
from PyPDF2 import PdfMerger

# Step 1: Specify the folder containing the certificate PDFs

folder_path = "./files"  

# Replace with your folder path

# Step 2: Collect all PDF files in the folder
pdf_files = [f for f in os.listdir(folder_path) if f.endswith(".pdf")]

# Sort files alphabetically (optional, for consistent merging order)
pdf_files.sort()

# Step 3: Create a PdfMerger object
merger = PdfMerger()

# Step 4: Append each PDF file to the merger
for pdf in pdf_files:
    file_path = os.path.join(folder_path, pdf)
    print(f"Adding {file_path}...")
    merger.append(file_path)

# Step 5: Define the output file name
output_file = os.path.join(folder_path, "merged_certificates.pdf")

# Write the merged PDF to the output file
merger.write(output_file)
merger.close()

print(f"\nPDFs merged successfully into: {output_file}")


