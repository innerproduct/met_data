import tempfile
import os

from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

outdir = './imgs/png/'

pdfs = [s for s in os.listdir('.') if 'pdf' in s]

for pdf in sorted(pdfs):
  print(pdf)
  with tempfile.TemporaryDirectory() as path:
    images_from_path = convert_from_path(pdf, output_folder=path, fmt='jpeg')
    for i,image in enumerate(images_from_path):
      outfilename = pdf.replace('.pdf','_'+str(i).zfill(4)+'.jpg') 
      image.save(os.path.join(outdir, outfilename))
      print(outfilename, 'saved!')

