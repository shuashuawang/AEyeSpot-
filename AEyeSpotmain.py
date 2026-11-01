from PIL import Image, ExifTags
import tkinter as tk
from tkinter import filedialog
import c2pa 
import json

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
print("Selected file:", file_path)


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

# Encountering a problem where No EXIF metadata is found within PNG

# Now, lets search to see if any of the AI Gen tools can be identified.
# Known gen AI image tool list. Notice I include multiple names for the same tool to compensate if metadata is inconsistent.

ai_tools = [
   "midjourney",
    "dall-e",
    "dalle",
    "openai",
    "gpt image",
    "chatgpt",

    "adobe firefly",
    "firefly",

    "nano banana",
    "nano banana 2",
    "gemini",
    "imagen",
    "imagefx",

    "stable diffusion",
    "stability ai",
    "sdxl",

# covers both model name and its developer
    "flux",
    "black forest labs",

    "ideogram",

    "recraft",

    "leonardo ai",
    "leonardo.ai",

    "grok",
    "grok imagine",
    "xai",

    "bing image creator",
    "microsoft designer",

    "canva",
    "magic media",

    "freepik",

    "openart",

    "reve",

    "luma",
    "luma photon",

    "nightcafe",

    "picsart",

    "fotor",

    "playground",

    "getimg.ai",
    "getimg",

    "clipdrop",

    "artbreeder",

    "deep dream generator",

    "generative ai by getty"
]
# starts by assuming no ai tool was found
ai_tool_found = False

# Searches EXIF metadata for known AI tools
for tag_id, value in metadata.items():

    # Converts numerical EXIF tags into readable names
    tag_name = ExifTags.TAGS.get(tag_id, tag_id)

    # Converts the metadata value into lowercase text
    text_to_check = str(value).lower()

    # Checks whether any AI tool names appear in the metadata
    for tool in ai_tools:

        if tool in text_to_check:
            print("Possible AI tool detected:", tool)
            print("Found in EXIF field:", tag_name)
            print("Metadata value:", value)

            ai_tool_found = True

# Displays the final EXIF verification result

if ai_tool_found:
    print("RESULT: Possible AI-related metadata detected.")
    print("WARNING: This does not prove the image was AI-generated.")

# Elif = else if, it allows python to check another condition when the first is false.

elif not metadata:
    print("RESULT: No EXIF metadata found.")
    print("WARNING: Missing EXIF metadata does not mean an image is authentic.")

else:
    print("RESULT: No known AI tool names found in EXIF metadata.")
    print("WARNING: This does not confirm the image is authentic.")


#-------------------
#C2PA INTEGRATION
#-------------------

# Checks for C2PA Content Credentials
reader = c2pa.Reader.try_create(file_path)

if reader is None:
    print("No C2PA Content Credentials found.")
    print("This does not mean the image is authentic.")

else:
    with reader:

        # Converts the JSON text into a Python dictionary
        c2pa_data = json.loads(reader.json())

        # Finds the active C2PA manifest
        # A C2PA manifest is a digitall signed record, containing information on its origin, creation and editing history
        # Think of it like a digital passport for images 
        # Manifests contains: A claim, assertions and a digital signature 

        manifest_id = c2pa_data["active_manifest"]
        manifest = c2pa_data["manifests"][manifest_id]

        # Gets information about the digital signature
        signature = manifest.get("signature_info", {})

        # Displays the important information
        print("C2PA Content Credentials found!")
        print("Image title:", manifest.get("title", "Not provided"))
        print("Software:", manifest.get("claim_generator", "Not provided"))
        print("Signed by:", signature.get("issuer", "Not provided"))

        # Displays the validation state
        print("Validation state:", c2pa_data.get("validation_state", "Unknown"))
       # Retrieves the detailed C2PA validation results
        validation_results = c2pa_data.get("validation_results", {})

       # Retrieves results for the active manifest
        active_results = validation_results.get("activeManifest", {})

       # Retrieves any validation failures
        validation_issues = active_results.get("failure", [])
        if validation_issues:
            print("Validation issues found:")

            for issue in validation_issues:
                print("Issue:", issue["code"])

                if issue["code"] == "signingCredential.untrusted":
                    print("WARNING: Signing certificate is not trusted.")

        else:
            print("No validation issues reported.")
    
        # Displays any actions recorded in the C2PA manifest
        print("\nRecorded image actions:")

        # Starts by assuming no actions were found
        actions_found = False

        # Searches through the manifest's assertions
        for assertion in manifest.get("assertions", []):

            # Checks whether the assertion contains image actions
            if assertion.get("label") == "c2pa.actions.v2":

                # Gets the list of recorded actions
                actions = assertion.get("data", {}).get("actions", [])

                # Displays each recorded action
                for action in actions:
                    print("Action:", action.get("action", "Unknown"))

                    # Checks for extra information about the action
                    parameters = action.get("parameters", {})

                    if "name" in parameters:
                        print("Adjustment type:", parameters["name"])

                    actions_found = True

        # Displays a message if no actions were found
        if not actions_found:
            print("No image actions found in the C2PA manifest.")
    
        # Displays a final C2PA verification summary
        print("\nC2PA Verification Summary:")

        # Gets the validation state - validation state stores the result reported by a C2PA library
        validation_state = c2pa_data.get("validation_state", "Unknown")

        # Assumes the signer is not flagged as untrusted
        untrusted_signer = False

        # Checks whether an untrusted signer was reported
        # For loop searches through validation_issues list to check whether the certificate was flagged as untrusted
        for issue in validation_issues:

            if issue.get("code") == "signingCredential.untrusted":
                untrusted_signer = True

        # Produces a result based on the validation state
        # The if, elif and else statements then decide which message to display
        if validation_state == "Trusted":
            print("RESULT: C2PA credentials validated and signer trusted.")

        # An if statement existing within an elif block = nested conditional statement
        # This means Python will only check nested conditional when validation_state = 'valid'
        elif validation_state == "Valid":

            if untrusted_signer:
                print("RESULT: C2PA checks passed, but signer is untrusted.")

            else:
                print("RESULT: C2PA checks passed. Signer trust not confirmed.")

        elif validation_state == "Invalid":
            print("RESULT: C2PA validation failed. Review the issues above.")

        else:
            print("RESULT: C2PA validation status is unknown.")

        print("NOTE: C2PA does not prove an image depicts a real event.")


