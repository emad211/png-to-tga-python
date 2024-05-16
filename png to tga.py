def read_png_header(file_path):
    
    with open(file_path, 'rb') as file:
        # PNG file signature
        signature = file.read(8)
        if signature != b'\x89PNG\r\n\x1a\n':
            raise ValueError("Not a valid PNG file")
        
        # Reading the IHDR chunk
        length = file.read(4)
        chunk_type = file.read(4)
        if chunk_type != b'IHDR':
            raise ValueError("IHDR chunk missing")
        
        ihdr_content = file.read(17)
        width = int.from_bytes(ihdr_content[0:4], 'big')
        height = int.from_bytes(ihdr_content[4:8], 'big')
        bit_depth = ihdr_content[8]
        color_type = ihdr_content[9]
        
        return width, height, bit_depth, color_type

def write_tga_header(width, height, color_type):
    """
    Writes the TGA header based on the image width, height, and PNG color type.
    """
    header = bytearray(18)
    header[2] = 2  # Truecolor image type
    header[12:14] = width.to_bytes(2, 'little')
    header[14:16] = height.to_bytes(2, 'little')
    header[16] = 32 if color_type == 6 else 24  # Bits per pixel
    header[17] = 8 if color_type == 6 else 0   # Alpha channel bits
    return header

def png_to_tga(png_file_path, tga_file_path):
    
    width, height, bit_depth, color_type = read_png_header(png_file_path)
    tga_header = write_tga_header(width, height, color_type)
    
    with open(png_file_path, 'rb') as png_file, open(tga_file_path, 'wb') as tga_file:
        png_file.seek(8 + 4 + 4 + 4 + 17)  

        raw_data = png_file.read()  
        pixel_data = bytearray()
        pixels_to_read = width * height
        bytes_per_pixel = 3 + (1 if color_type == 6 else 0)
        
        for i in range(0, len(raw_data), bytes_per_pixel):
            if len(raw_data) - i < bytes_per_pixel:
                break  
            if color_type in (2, 6):  
                b, g, r = raw_data[i:i+3]
                pixel_data.extend([b, g, r])
                if color_type == 6:
                    pixel_data.append(raw_data[i+3])
        
        tga_file.write(tga_header)
        tga_file.write(pixel_data)

png_to_tga("modern lights.png", "path_to_output_file.tga")
