import os
import glob


def clear_folder(folder_path):
    """Delete all files in the given folder (non-recursive)."""
    if not os.path.exists(folder_path):
        return  # Nothing to clear
    files = glob.glob(os.path.join(folder_path, "*"))
    for f in files:
        try:
            os.remove(f)
        except Exception as e:
            print(f"Could not remove {f}: {e}")
    print(f"Cleared {len(files)} files from {folder_path}.")
