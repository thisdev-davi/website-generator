import os
import shutil
from markdown.markdown_blocks import markdown_to_html_node

def copy_static(source, dest):
    if not os.path.exists(source):
        return
    if not os.path.exists(dest):
        os.mkdir(dest)
    
    for item in os.listdir(source):
        from_path = os.path.join(source, item)
        to_path = os.path.join(dest, item)
        if os.path.isfile(from_path):
            shutil.copy(from_path, to_path)
        else:
            copy_static(from_path, to_path)

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise ValueError("No title found")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path, "r") as f:
        markdown = f.read()
    
    with open(template_path, "r") as f:
        template = f.read()
    
    html_node = markdown_to_html_node(markdown)
    html_content = html_node.to_html()
    
    title = extract_title(markdown)
    
    full_html = template.replace("{{ Title }}", title).replace("{{ Content }}", html_content)
    
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    with open(dest_path, "w") as f:
        f.write(full_html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for item in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, item)
        if os.path.isfile(from_path):
            if from_path.endswith(".md"):
                dest_path = os.path.join(dest_dir_path, item.replace(".md", ".html"))
                generate_page(from_path, template_path, dest_path)
        else:
            new_dest_dir = os.path.join(dest_dir_path, item)
            generate_pages_recursive(from_path, template_path, new_dest_dir)

def main():     
    static_dir = "./static"
    public_dir = "./public"
    content_dir = "./content"
    template_path = "./template.html"

    # Adjust paths if running from src
    if os.getcwd().endswith("src"):
        static_dir = "../static"
        public_dir = "../public"
        content_dir = "../content"
        template_path = "../template.html"

    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)
    
    copy_static(static_dir, public_dir)
    generate_pages_recursive(content_dir, template_path, public_dir)

if __name__ == "__main__":
    main()