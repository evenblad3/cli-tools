#!/usr/bin/env python3
import piexif
import os

files = []

print("=== bulk exif remover ===".title())

while 1:
    askPath = input("Enter path: ")
    try:
        if os.scandir(askPath):
            files = [file for file in os.scandir(askPath) if os.path.isfile(file)]
            ask = input(f"Do you want to display the files in {askPath}?: ")
            if ask.lower().startswith("y"):
                for i in files:
                    print(i.path)
            else:pass
            break
        else:pass
    except Exception as e:
        print(e)
        print("\nWrong directory, please try again.")
        continue

print("\nAttempting to remove the Exif data from the images...")
for file in files:
    currentFile = None
    if file.path.endswith(("jpg", "jpeg", "JPG", "JPEG")):
        currentFile = file.path
        piexif.remove(currentFile)
        print(f"Deleted Exif data from {os.path.split(currentFile)[-1]}")
    else:pass

print("Done.")
