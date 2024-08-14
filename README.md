# Python Automation Scripts

<p align="justify">
Welcome! Here you'll find a collection of Python scripts I designed to automate various tasks across different domains. Automation is a key aspect of modern software development and operational workflows, and these scripts aim to streamline repetitive tasks, enhance efficiency, and reduce manual intervention. For questions, please contact: ippc2001@usherbrooke.ca
</p>


## Scripts

- **Image Resizer**
    - This script takes images from a specified folder, resizes them to the desired dimensions, and saves the resized images to a new folder.
    - **How to Run:**
        1. Ensure you have Python installed on your system.
        2. Make sure to install the right Pillow version for your Python version. ```python3 -m pip install Pillow```
        3. Clone or download this repository.
        4. Navigate to the directory containing the `image_resizer.py` script.
        5. Run the script by executing the following command:```bash python3 image_resizer.py```
        6. Follow the on-screen prompts:
            - Enter the name of the folder containing the images you want to resize.
            - Enter the desired width and height for the resized images.
    - The resized images will be saved in a new folder named `<original_folder_name>_resized` in the same directory as the script.
 
- **Youtube Video Downloader**
    - This script allows you to download videos from YouTube using their URLs. It utilizes the Pytube library for video downloading.
    - **How to Run:**
        1. Ensure you have Python installed on your system.
        2. Install the right Pytube library for your system by running: ```pip3 install pytube```.
        3. Clone or download this repository.
        4. Navigate to the directory containing the `youtube_downloader.py` script.
        5. Run the script by executing the following command: ```python3 youtube_video_downloader.py```.
        6. Follow the on-screen prompts:
            - Enter the YouTube URL of the video you want to download.
            - Select the directory where you want to save the downloaded video.
        7. If you have a SSL certificate error:
           - Run ```sudo pip install --upgrade certifi``` in your terminal.
           - Then ```/Applications/Python\ 3.[YOUR VERSION]/Install\ Certificates.command```.
    - The downloaded video will be saved in the specified directory.

- **Excel Files Merger**
    - This script allows you to merge two Excel files based on a specified merge type (e.g., inner, outer, left, right, cross).
    - **How to Run:**
        1. Ensure you have Python installed on your system.
        2. Install the required libraries: ```pip install PyQt5 pandas openpyxl```.
        3. Clone or download this repository.
        4. Navigate to the directory containing the `excel_file_merger.py` script.
        5. Run the script by executing the following command: ```python excel_file_merger.py```.
        6. Follow the on-screen prompts:
            - Select the first Excel file.
            - Select the second Excel file.
            - Choose the merge type from the dropdown menu.
            - Click the `Merge` button.
            - Save de merged file to your desired location.
  
# Contact

For questions, please contact: ippc2001@usherbrooke.ca
