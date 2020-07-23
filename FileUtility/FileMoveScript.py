import os
import shutil
import stat

# Create and Move the files to folder


def CreateFolder_and_Move_file(SourceFilepath, filename, extension):
    try:
        IsExtvalid = len(extension) >= 2 and len(extension) <= 6
        if " " in extension:
            IsExtvalid = False
        if IsExtvalid:
            destinationpath = os.path.join(SourceFilepath, extension.upper())
            IsFolderPresent = os.path.exists(destinationpath)
            if not IsFolderPresent:
                os.mkdir(destinationpath)
                print("Folder created "+extension.upper())
                pass
            shutil.move(os.path.join(SourceFilepath, filename),
                        os.path.join(destinationpath, filename))
        pass
    except:
        print("Exception :" + destinationpath)


# Main starts from here

path_to_clean = ["C:\\Users\\HP\\Desktop", "C:\\Users\\HP\\Downloads"]
for path in path_to_clean:
    print("Scanning your directory....")
    entries = os.scandir(path)
    print("Scanning complete....")
    print("Moving Files!!....")
    for items in entries:
        file_stats = os.stat(os.path.join(path, items.name))
        if not stat.S_ISDIR(file_stats[stat.ST_MODE]):
            CreateFolder_and_Move_file(
                path, items.name, items.name.split(".")[-1])

print("Files moved Successfully")
