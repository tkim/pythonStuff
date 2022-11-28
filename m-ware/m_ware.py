import os

# find files
files = []

for file in os.listdir():
    # skip the file that runs the m-ware
    if file == "m_ware.py":
          continue
    files.append(file)

print(files)

