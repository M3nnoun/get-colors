from PIL import Image, ImageDraw
import csv
import os
import time

def hex_to_rgb(hex_color):
    # Convert a hex color code (e.g., "#RRGGBB") to an RGB tuple
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def create_rectangle_image(width, height, border_size=4, border_color="#FFFFFF", fill_color="#000000"):
    border_color_rgb = hex_to_rgb(border_color)
    fill_color_rgb = hex_to_rgb(fill_color)
    
    # Create a new image with a white background
    image = Image.new("RGB", (width, height), border_color_rgb)
    draw = ImageDraw.Draw(image)
    rect_x = border_size
    rect_y = border_size
    rect_width = width - 2 * border_size
    rect_height = height - 2 * border_size
    
    # Draw the filled rectangle
    draw.rectangle([rect_x, rect_y, rect_x + rect_width, rect_y + rect_height], fill=fill_color_rgb)
    
    return image

def read_data_from_csv(file_path):
    data = []
    
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            name = row['Name']
            color = row['Color']
            data.append((name, color))
    
    return data

# Example usage:
file_path = 'data.csv'
data = read_data_from_csv(file_path)
count=1
for name, color in data:
    print(f"Info of item {count}")
    count+=1
    image = create_rectangle_image(237, 79, border_color="#ffffff", fill_color=color)
    image.save(os.path.join("output-png", f"{name}.png"))
    time.sleep(1)



