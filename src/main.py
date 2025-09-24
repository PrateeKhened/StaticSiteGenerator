import sys
from copystatic import copy_static
from generate_page import generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"

def main():
    
    print("Deleting public directory...")
    print("Copying static files to public directory...")
    copy_static(dir_path_static, dir_path_public)

    base_path = sys.argv[1] if len(sys.argv) > 1 else "/"

    print("Generating page...")
    generate_pages_recursive(
        dir_path_content,
        template_path,
        dir_path_public,
        base_path,
    )

if __name__ == "__main__":
    main()