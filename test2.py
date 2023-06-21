
        #elif option == "d":
         #   record_id = input("Enter record #: ")
          #  with open(r"c:\Users\training.user\Downloads\record.txt", "r") as f:
           #     lines = f.readlines()
            #with open(r"c:\Users\training.user\Downloads\record.txt", "w") as file:
             #   for line in lines:
              #      if not line.startswith(record_id):
               #         file.write(line)
           # print("Record deleted")

import os
import sys
from pathlib import Path
def delete_line(file_name, line_number):
    with open(file_name, "r") as f:
        lines = f.readlines()
    with open(file_name, "w") as f:
        for i in range(len(lines)):
            if i != line_number:
                f.write(lines[i])
if __name__ == "__main__":
    file_name = r"c:\Users\training.user\Downloads\record.txt"
    line_number = int(input("Enter the line number to delete: "))
    delete_line(file_name, line_number)
