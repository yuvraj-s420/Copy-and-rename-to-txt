import os
import sys
import shutil


def copyAndRenameTxt(source, target):
    # Source and Target are directories within the cwd, where the files with valid suffixes are to be copied from Source into Target.

    # Form absolute path to directories
    cwd = os.getcwd()
    source_dir = os.path.join(cwd, source)
    target_dir = os.path.join(cwd, target)

    file_names = []
    valid_suffixes = (".cpp", ".c", ".h", ".hpp")
    
    # Walk through source directory
    for root, dirs, files in os.walk(source_dir):

        for file in files:

            if file.endswith(valid_suffixes):
                
                file_names.append(file)

                # Absolute path of file
                file_src = os.path.join(source_dir, file)

                # split file from extension
                file, ext = os.path.splitext(file)

                # Ensure header and cpp files are copied with seperate names (avoid overwrite)
                if ext == ".h" or ext == ".hpp":
                    file_txt = file + "h.txt"
                else:
                    file_txt = file + ".txt"
                
                # Absolute path of desitination .txt file
                file_dst = os.path.join(target_dir, file_txt)

                # Copy the file with .txt suffix to target directory
                shutil.copy(file_src, file_dst)

        break   # Only traverse root of source dir, no subdirectories
    
    print(f"Files copied: {file_names}")



if __name__ == "__main__":

    # Parse arguments
    args = sys.argv

    if len(args) != 3:
        raise Exception("Must only pass source and target directories.")
    
    source = args[1]        # Source to copy files from
    target = args[2]        # target directory to copy to

    copyAndRenameTxt(source, target)