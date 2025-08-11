# resize_tool.py
import os
from PIL import Image

def get_user_input():
    """Gathers all necessary information from the user interactively."""
    print("--- Welcome to the Professional Image Resizer Tool ---")
    
    input_folder = input("Enter the path to the input folder (e.g., 'input_images'): ")
    output_folder = input("Enter the path for the output folder (e.g., 'output_images'): ")
    
    while True:
        try:
            max_width = int(input("Enter the maximum width for resizing: "))
            max_height = int(input("Enter the maximum height for resizing: "))
            break
        except ValueError:
            print("Invalid input. Please enter whole numbers for dimensions.")

    output_format = input("Enter desired output format (e.g., jpg, png) or press Enter to keep original: ").lower()
    
    return input_folder, output_folder, (max_width, max_height), output_format

def process_images(input_folder, output_folder, size, output_format):
    """
    Resizes and converts all images in a folder based on user-defined parameters.
    """
    if not os.path.exists(output_folder):
        print(f"Output folder '{output_folder}' not found. Creating it...")
        os.makedirs(output_folder)

    # List of common image file extensions
    image_extensions = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')
    
    processed_count = 0
    skipped_count = 0

    try:
        files = os.listdir(input_folder)
    except FileNotFoundError:
        print(f"\n[ERROR] The input folder '{input_folder}' was not found. Please check the path and try again.")
        return

    print("\n--- Starting Image Processing ---")
    for filename in files:
        # Check if the file is an image
        if not filename.lower().endswith(image_extensions):
            print(f"-> Skipping '{filename}' (not a recognized image file).")
            skipped_count += 1
            continue

        input_path = os.path.join(input_folder, filename)
        
        try:
            with Image.open(input_path) as img:
                # Use thumbnail to resize while maintaining aspect ratio.
                # It resizes the image to fit within the specified (width, height) box.
                img.thumbnail(size)
                
                # Determine the output filename and format
                original_name, original_ext = os.path.splitext(filename)
                
                if output_format:
                    # If a new format is specified, use it
                    new_filename = f"{original_name}_resized.{output_format}"
                else:
                    # Otherwise, keep the original format
                    new_filename = f"{original_name}_resized{original_ext}"

                output_path = os.path.join(output_folder, new_filename)
                
                # Save the image. If the format is JPG, ensure it's converted to RGB.
                if output_format == 'jpg' and img.mode != 'RGB':
                    img = img.convert('RGB')
                
                img.save(output_path)
                print(f"-> Successfully resized and saved '{filename}' as '{new_filename}'.")
                processed_count += 1

        except Exception as e:
            print(f"[ERROR] Could not process '{filename}'. Reason: {e}")
            skipped_count += 1
            
    print("\n--- Processing Complete ---")
    print(f"Successfully processed: {processed_count} images.")
    print(f"Skipped: {skipped_count} files.")

if __name__ == "__main__":
    input_dir, output_dir, resize_dim, out_format = get_user_input()
    process_images(input_dir, output_dir, resize_dim, out_format)