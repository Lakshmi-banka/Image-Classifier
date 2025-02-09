#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Lakshmi Banka
# DATE CREATED: 10-11-2024                               
# REVISED DATE: 09-02-2025
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
import os
from os import listdir

#       Define get_pet_labels function below.
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    try:
        in_files = os.listdir(image_dir)
    except FileNotFoundError:
        print(f"Error: Directory '{image_dir}' not found.")
        return {}
    results_dic = dict()
    for filename in in_files:
        # Ignore hidden files or non-image files
        if filename.startswith("."):
            continue

        # Construct full file path and check if it is a file
        file_path = os.path.join(image_dir, filename)
        if not os.path.isfile(file_path):
            continue

        # Extract pet label from filename
        words = filename.lower().split('_')
        pet_label = " ".join([word for word in words if word.isalpha()])

        # Add filename and label to the dictionary
        if filename not in results_dic:
            results_dic[filename] = [pet_label]
        else:
            print("** Warning: Duplicate files exist in directory:", filename)
    return results_dic
