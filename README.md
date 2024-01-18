# Archiver

## Program Description

This program is designed to encode and decode textual data with the ability to achieve efficient compression using the Huffman algorithm.

## Environment Requirements

- Python 3.x
- Required libraries: `pickle`, `sys`, `Counter`

## Running the Program

The program is executed from the command line with the following arguments:

- For encoding: 
  ```bash
  python main.py -e example.txt
- For decoding:
  ```bash
  python main.py -d example.par
## Program Output

The output of the program is a new file with the extension .par for encoded data and a decrypted file for decoding. The filenames correspond to the original filenames. For example, if the original file is abc.txt, the encoded file will be abc.par.