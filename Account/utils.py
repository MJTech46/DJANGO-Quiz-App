# This is a file used for keeping utility functions organized in a separate file.

from os.path import join as path_join
from django.utils.deconstruct import deconstructible

#Renaming the user uploaded files in the formate of "UserIcons/{User.uuid}-icon.png"
@deconstructible
class CustomUpload():
    def __call__(self, instance, filename: str):
        #Getting file extention
        ext = filename.split(".")[-1]
        #Create the new file name
        filename = f"{instance.uuid}-icon.{ext}"
        #Returning the new filename
        return path_join('Account/UserIcons/', filename)

custom_upload = CustomUpload()