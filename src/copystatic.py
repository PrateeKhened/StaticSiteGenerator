import os
import shutil

def copy_static(source, destination, clean=True):
    
    if clean:
        if os.path.exists(destination) and os.path.isdir(destination):
            for filename in os.listdir(destination):
                file_path = os.path.join(destination, filename)
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.remove(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path) 
        elif os.path.exists(destination) and os.path.isfile(destination):
            os.remove(destination)
            os.mkdir(destination)
        elif not os.path.exists(destination):
            os.mkdir(destination)
    
    if not os.path.exists(source):
        raise FileNotFoundError(source)
    
    for name in os.listdir(source):
        src_path = os.path.join(source, name)
        dest_path = os.path.join(destination, name)

        if os.path.isfile(src_path):
            shutil.copy(src_path, dest_path)
            print(f"copied file: {src_path} -> {dest_path}")
        elif os.path.isdir(src_path):
            if not os.path.exists(dest_path):
                os.mkdir(dest_path)
            copy_static(src_path, dest_path, clean=False)