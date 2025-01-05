import pypdf
import os
import datetime

def save_string_to_file(text: str, file_location: str) -> None:
  """
  Save a string to a text file.

  Required arguments:
      text -- The string you would like to save.
      file_location -- The location of the
       text file to be output. E.g., 'output.txt'
       or 'some_folder/output.txt'.

  This function only saves the file; it
    does not return any output besides None.
  """