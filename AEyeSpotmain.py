from PIL import Image, ExifTags
import tkinter as tk
from tkinter import filedialog

print("Welcome to AEyeSpot")
print("AI Image Verification Tool")

# creates a basic Tkinter window
shrub = tk.Tk()

shrub.title("My Image")

# Forces Tkinker to initialize the window - fix to the window problem!

shrub.update()

# Centres the window
shrub.geometry("400x200+500+300")


# open a file-selection window and save the chosen file location inside file_path.
file_path = filedialog.askopenfilename(parent=shrub)


# closes it 
shrub.destroy()

#Use Pillow's Image tool to open the file called test.jpg    
# Image.open(...) is a function
# image = stores the opened image inside the variable called image

image = Image.open(file_path)

# Displays the images format and dimensions
print("Image loaded successfully")
print("Format:", image.format) #e.g. JPEG, PNG, etc
print("Size (Width, Height):", image.size) #e.g. 1920 x 1080
print("Mode:", image.mode) #e.g. RGA, RGBA

#Extracts metadata 
metadata = image.getexif()

if metadata:
    print("Metadata found")

# Displays metadata (In numbers)
    print("Metadata:", metadata)

# Now we need to display those numbers as letters or readable things for the user. We will do this using the for loop.

# ExifTags = Pillow's translation table.

    for tag_id, value in metadata.items():
#tag_id is repeated incase no words are found, the original number ID is still displayed.
     tag_name = ExifTags.TAGS.get(tag_id, tag_id)
    print(tag_name, ":", value)

else:
    print("No EXIF metadata found")

# Now, lets search to see if any of the AI Gen tools can be identified.
# Known gen AI image tool list 

ai_tools = [
   "mid_journey",
   "dall_e",
   "nano_banana",
   "nano_banana_2",
   "openAI",
   "adobe_firefly",
   ""
   
]



