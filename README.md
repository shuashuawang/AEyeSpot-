**General Information**
Assessment 2, AEyeSpot, a image verification tool prototype, designed for helping journalists in investigating the origins of digital images. 

Given my background as a journalism student and someone who is beginning to work within the industry, audiences value
authenticity. Recently, AI has been dominating media landscapes and I am concerned about its potential harm to undermine the credibility of journalism, particularly visual, when Gen AI images are used without proper disclosure.

**Software Used**
• Microsoft Visual Studio Code Version: 1.143.0
• Python 3 — Primary programming language

**Library Dependencies**
Standard libraries:
- Tkinter
- JSON
Third-party libraries:(These must be installed separately)
- Pillow
- c2pa-python

Install the third-party libraries using:
python3 -m pip install Pillow c2pa-python

**Features**
list of ready features:
• Uses Tkinter for file selection
• Uses Pillow to identify image format 
• EXIF metadata analysis
• C2PA content credentials verification 
• Verification results & warnings - displays results in the Python terminal
• Reports missing metadata & C2PA validation issues 
• Explains that missing metadata or Content Credentials does not establish an image's authenticity.

**How to Run AEyeSpot**
1. Download the project files from this GitHub repository.
2. Ensure Python 3 and the required libraries are installed.
3. Open the project folder in Visual Studio Code.
4. Run the main Python file using:

python3 AEyeSpotmain.py

5. Select an image using the file-selection window.
6. View the EXIF metadata and C2PA verification results in the Python terminal.

A sample image, test.png, is provided for testing the prototype.
A second sample of test.jpeg is also provided, of the same image to show a difference in results.
BOTH IMAGES WERE CREATED BY GEN AI

*Note* test.jpeg was converted using Pillow, running this image through AEyeSpot will allow users to see the limitations of EXIF metadata analysis & C2PA content credentials.

**Project Limitations**
AEyeSpot is a proof-of-concept verification tool and is currently unable to deliver reliable results to determine whether an image was generated using artificial intelligence. 

EXIF metadata can be altered, removed or completely void. Similarly, C2PA content credentials are not guaranteed to exist within every image and may be lost during image editing/conversion.

Hence, AEyeSpot should be used as a supplementary investigative tool, rather than a definitive assessment of authenticity.

**Project Status**
- Prototype Complete -

The core EXIF metadata analysis and C2PA verification features have been implemented, integrated and tested.
The prototype demonstrates how beginner-level Python programming can be applied to a real-world challenge within journalism.




