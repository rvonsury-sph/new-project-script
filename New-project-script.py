import os
import shutil
import sys
import tkinter as tk
from tkinter.simpledialog import askstring
from tkinter import filedialog

def get_project_name():
    """
    Function to prompt the user to enter the project name using a dialog box.

    Returns:
        str: The project name entered by the user.
    """
    root = tk.Tk()
    root.withdraw()
    project_name = askstring("Enter Project Name", "Enter the project name here (YYYYMMDD_Project_Name):")
    return project_name

def get_folder_location():
    """
    Function to prompt the user to select the folder where the project will be saved.

    Returns:
        str: The selected folder location.
    """
    root = tk.Tk()
    root.withdraw()
    save_location = filedialog.askdirectory(initialdir=os.getcwd(), title="Select Folder to Save Project")
    return save_location

def create_folder_structure(save_location, project_name):
    """
    Function to create the folder structure for the project.

    Args:
        save_location (str): The path where the project folders will be created.
        project_name (str): The name of the project.
    """
    folders = [
        os.path.join(save_location, project_name),
        os.path.join(save_location, project_name, "0_preproduction"),
        os.path.join(save_location, project_name, "1_media", "1_video", "1_d5m4"),
        os.path.join(save_location, project_name, "1_media", "1_video", "2_iPhone"),
        os.path.join(save_location, project_name, "1_media", "1_video", "3_drone"),
        os.path.join(save_location, project_name, "1_media", "1_video", "4_action-cam"),
        os.path.join(save_location, project_name, "1_media", "1_video", "5_stock"),
        os.path.join(save_location, project_name, "1_media", "1_video", "6_screen-recording"),
        os.path.join(save_location, project_name, "1_media", "1_video", "7_vfx"),
        os.path.join(save_location, project_name, "1_media", "2_audio", "1_original-sound"),
        os.path.join(save_location, project_name, "1_media", "2_audio", "2_music"),
        os.path.join(save_location, project_name, "1_media", "2_audio", "3_voice", "1_layouts"),
        os.path.join(save_location, project_name, "1_media", "2_audio", "3_voice", "2_final"),
        os.path.join(save_location, project_name, "1_media", "2_audio", "4_sfx"),
        os.path.join(save_location, project_name, "1_media", "3_graphics", "1_logos"),
        os.path.join(save_location, project_name, "1_media", "3_graphics", "2_fonts"),
        os.path.join(save_location, project_name, "1_media", "3_graphics", "3_icons"),
        os.path.join(save_location, project_name, "1_media", "3_graphics", "4_pictures"),
        os.path.join(save_location, project_name, "1_media", "3_graphics", "5_psd_ai_indd"),
        os.path.join(save_location, project_name, "2_projects", "1_editing", "_previous-versions"),
        os.path.join(save_location, project_name, "2_projects", "1_editing", "Adobe Premiere Pro Auto-Save"),
        os.path.join(save_location, project_name, "2_projects", "1_editing", "_presets"),
        os.path.join(save_location, project_name, "2_projects", "2_after_effects", "_previous-versions"),
        os.path.join(save_location, project_name, "2_projects", "3_color", "_previous-versions"),
        os.path.join(save_location, project_name, "2_projects", "3_color"),
        os.path.join(save_location, project_name, "2_projects", "4_audio", f"{project_name}_mastering"),
        os.path.join(save_location, project_name, "2_projects", "4_audio", f"{project_name}_mastering", "Session File Backups"),
        os.path.join(save_location, project_name, "2_projects", "4_audio", f"{project_name}_mastering", "Audio Files"),
        os.path.join(save_location, project_name, "3_export", "1_rough", "_archive"),
        os.path.join(save_location, project_name, "3_export", "2_compositing", "for_compositing"),
        os.path.join(save_location, project_name, "3_export", "2_compositing", "from_compositing",),

        os.path.join(save_location, project_name, "3_export", "3_color", "for-color"),
        os.path.join(save_location, project_name, "3_export", "3_color", "from-color"),
        os.path.join(save_location, project_name, "3_export", "4_sound_omf", "for-mastering"),
        os.path.join(save_location, project_name, "3_export", "4_sound_omf", "from-mastering"),
        os.path.join(save_location, project_name, "3_export", "5_srt"),
        os.path.join(save_location, project_name, "3_export", "6_master", "1_ProRes"),
        os.path.join(save_location, project_name, "3_export", "6_master", "2_h264"),
    ]

    for folder in folders:
        os.makedirs(folder, exist_ok=True)

def copy_file(src, dest):
    """
    Function to copy files or directories from source to destination.

    Args:
        src (str): Path of the source file or directory.
        dest (str): Path of the destination directory.
    """
    if os.path.isdir(src):
        shutil.copytree(src, dest)
        print(f"Directory '{src}' copied to '{dest}'")
    elif os.path.isfile(src):
        shutil.copy2(src, dest)
        print(f"File '{src}' copied to '{dest}'")
    else:
        print(f"Warning: '{src}' is neither a file nor a directory. Skipping copy operation.")

def main():
    """
    Main function to orchestrate the project setup process.
    """
    project_name = get_project_name()
    if not project_name:
        print("Error: Project name not provided.")
        sys.exit(1)
    print("Project name:", project_name)

    save_location = get_folder_location()
    if not save_location:
        print("Error: Folder location not provided.")
        sys.exit(1)
    print("Folder location:", save_location)

    create_folder_structure(save_location, project_name)

    # Copy files
    script_dir = os.path.dirname(os.path.realpath(__file__))
    files_to_copy = [
        ("Creative", os.path.join(save_location, project_name, "2_projects", "3_color", "LUTs")),
        ("customer_project_v01.ptx",os.path.join(save_location, project_name, "2_projects", "4_audio", f"{project_name}_mastering")),
        ("customer_project_v01.aep", os.path.join(save_location, project_name, "2_projects", "2_after_effects")),
        ("customer_project_v01.prproj", os.path.join(save_location, project_name, "2_projects", "1_editing"))
    ]

    for file, dest_folder in files_to_copy:
        if file == "Creative":
            # For Creative, simply copy without renaming
            copy_file(os.path.join(script_dir, file), os.path.join(save_location, project_name, dest_folder))
        else:
            # For other files, rename while copying
            copy_file(os.path.join(script_dir, file), os.path.join(save_location, project_name, dest_folder, f"{project_name}_v01{os.path.splitext(file)[1]}"))

print("Folder structure and files copied successfully.")

if __name__ == "__main__":
    main()
