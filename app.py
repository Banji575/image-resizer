from PIL import Image
import os

def resize_images_in_folder(folder_path, output_folder, new_size):
    # Create the output folder if it does not exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through all files in the specified folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        # Check if the file is not a directory and is an image
        if os.path.isfile(file_path) and filename.endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            # Open the image
            img = Image.open(file_path)
            
            # Resize the image
            img = img.resize(new_size, Image.Resampling.LANCZOS)
            
            # Save the resized image to the output folder
            output_path = os.path.join(output_folder, filename)
            img.save(output_path)
            print(f'{filename} resized and saved to {output_path}')
        else:
            print(f'{filename} is not an image file, skipping...')

# Example usage
folder_path = r''  # Path to the folder with images
output_folder = r''  # Path to the output folder
new_size = (256, 256)  # New size for the images

resize_images_in_folder(folder_path, output_folder, new_size)
