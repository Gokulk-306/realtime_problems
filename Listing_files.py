import os
def list_files(folder):
    try:
        files = os.listdir(folder)
        return files, None
    except FileNotFoundError:
        return None, "Folder not found"
    except PermissionError:
        return None, "Permission denied"


def main():
    folders = input("Enter the folder name with spaces :").split()
    for folder in folders:
        files , errors = list_files(folder)
        if files:
            print(f"--- List of files in {folder}---")
            i = 1
            for file in files:
                print(i,":",file)
                i += 1
        else:
            print(f"Error in folder {folder}, {errors}")

if __name__ == "__main__":
    main()
