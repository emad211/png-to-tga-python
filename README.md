
```markdown
# PNG to TGA Converter

## Description
This repository contains a Python script that converts PNG images to TGA format. The script reads the header of a PNG file, processes the image data, and writes it into a new TGA file. This tool is useful for developers and designers who need to convert image formats for various purposes.

## Features
- Converts PNG images to TGA format.
- Handles Truecolor and Truecolor with alpha (transparency) PNGs.

## Requirements
- Python 3.x

## Installation
To install the required dependencies, run:
```bash
pip install pillow
```

## Usage
To convert a PNG image to TGA format, use the following command:
```bash
python png_to_tga.py input.png output.tga
```
- `input.png`: The path to the PNG file you want to convert.
- `output.tga`: The path where the TGA file will be saved.

## Example
To convert a PNG file named `example.png` to `example.tga`, run:
```bash
python png_to_tga.py example.png example.tga
```

## Script Details
### Functions:
- **`read_png_header(file_path)`**: Reads the header of a PNG file to extract image width, height, bit depth, and color type.
- **`write_tga_header(width, height, color_type)`**: Writes the TGA header based on the image width, height, and color type.
- **`png_to_tga(png_file_path, tga_file_path)`**: Main function that converts a PNG file to TGA format by reading the PNG data and writing it to a new TGA file.





## Contact
For any questions or suggestions, feel free to contact me at emad.k50000@gmail.com
```

