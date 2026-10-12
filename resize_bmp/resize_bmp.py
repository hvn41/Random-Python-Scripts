import os
import sys
from PIL import Image

TARGET_FOLDER = r"C:\Program Files (x86)\Steam\steamapps\common\Left 4 Dead 2\left4dead2"

def resize_to_bmp_and_save_to_folder(input_path):
    if not os.path.exists(TARGET_FOLDER):
        print(f"Unable to locate {TARGET_FOLDER}. Please check if the folder exists.")
        sys.exit()
    
    try:
        input_path = input_path.strip()

        # Automatically generate name for output image
        filename_only = os.path.basename(input_path)
        filename_without_path = os.path.splitext(filename_only)[0]
        output_filename = f"{filename_without_path}.bmp"

        # Combine folder path and new filename
        final_output_path = os.path.join(TARGET_FOLDER, output_filename)

        # Process and save the image
        with Image.open(input_path) as img:
            resized_img = img.resize((250, 250), Image.Resampling.LANCZOS)
            resized_img.save(final_output_path, format="BMP")

        print(f"\nSuccess: Saved to '{final_output_path}'")

    except FileNotFoundError:
        print(f"\nError: Could not find a file name '{input_path}'. Please check the spelling.")
    except Exception as e:
        print(f"\nError: {e}")

# Ask user input for file name in terminal
user_input = input("Enter the full name of the JPG image (e.g., photo.jpg): ")

# Execute the conversion
resize_to_bmp_and_save_to_folder(user_input)