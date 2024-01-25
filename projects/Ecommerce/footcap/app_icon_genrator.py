import os
import sys
import shutil
from PIL import Image, ImageOps
import requests
from io import BytesIO

def create_folder_if_not_exist(path):
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)

def generate_app_icons(icon_path, folder_path):
    # Ensure the folder path has a proper format
    folder_path = os.path.join(folder_path, '')
    create_folder_if_not_exist(folder_path)

    # Open the image
    img = get_image(icon_path)

    # Define the resolutions for different Android icon sizes
    android_sizes = {
        "mipmap-hdpi": (72, 72),
        "mipmap-mdpi": (48, 48),
        "mipmap-xhdpi": (96, 96),
        "mipmap-xxhdpi": (144, 144),
        "mipmap-xxxhdpi": (192, 192)
    }

    # Generate the Play Store icon (512x512)
    playstore_icon_path = os.path.join(folder_path, "playstore.png")
    img.resize((512, 512)).save(playstore_icon_path, format='PNG')

    # Generate Android icons for different resolutions
    android_folder_path = os.path.join(folder_path, "android")
    create_folder_if_not_exist(android_folder_path)

    for size_folder, size in android_sizes.items():
        size_folder_path = os.path.join(folder_path, "android", size_folder)
        create_folder_if_not_exist(size_folder_path)

        android_icon_path = os.path.join(folder_path, "android", size_folder, "ic_launcher.png")
        img.resize(size).save(android_icon_path, format='PNG')

def get_image(path_or_url):
    if path_or_url.startswith(('http://', 'https://')):
        # If the path is a URL, download the image
        response = requests.get(path_or_url)
        response.raise_for_status()  # Check if the request was successful
        img = Image.open(BytesIO(response.content))
    else:
        # If the path is a local file, open it directly
        img = Image.open(path_or_url)

    # Resize the image to 512x512
    img = img.copy()

    # Get the current width and height
    width, height = img.size

    # Check if the image is not in a 1:1 ratio
    if width == height:
        return img.resize((512,512))
    print("NEW TO RESIZE")
    # Find the minimum dimension and create a square canvas
    size = max(width, height)
    new_img = Image.new("RGBA", (size, size), (0,0, 0,0))
    
    # Calculate the position to paste the original image (center it)
    left = (size - width) // 2
    top = (size - height) // 2
    # Paste the  original image onto the square canvas
    new_img.paste(img, (left,top))
    # return   ImageOps.fit(img,(512,512), method = 0,
                #    bleed = 0.0, centering =(0.5, 0.5))

    # Use Image.ANTIALIAS for high-quality downsampling
    return  new_img.resize((512, 512), Image.Resampling.LANCZOS)

def read_parameters():
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) < 3:
        print("Usage: python app_icon_genrator.py input_file output_folder")
        sys.exit(1)

    # Extract input and output paths from command-line arguments
    input_path = sys.argv[1]
    output_path = sys.argv[2]

    return input_path, output_path


if __name__ == "__main__":
    # Example usage with a local file path:
    local_icon_path,    local_folder_path= read_parameters()
    print("ICON PATH : "+local_icon_path)
    print("FOLDER PATH : "+local_folder_path)
    generate_app_icons(local_icon_path, local_folder_path)
    print("APP ICON GENRATED. PATH: " +local_folder_path)
    
