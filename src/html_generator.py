from markdown_html import markdown_to_html_node
import os

def extract_title(markdown):
    strings = markdown.split("\n")
    for str in strings:
        if str.startswith("#"):
            return str.strip("#").strip(" ")
    raise Exception("no title found")

def generate_page(from_path, template_path, dest_path):
    print("Generating html files from " + from_path + " -> " + dest_path)
    with open(template_path) as file:
        template = file.read()
    with open(from_path) as file:
        markdown = file.read()
    title = extract_title(markdown)
    content = markdown_to_html_node(markdown).to_html()

    template = template.replace("{{ Title }}", title).replace("{{ Content }}", content)
    with open(dest_path, "a") as file:
        file.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if os.path.exists(dir_path_content):
        for dir in os.listdir(dir_path_content):
            source_path = os.path.join(dir_path_content, dir)
            print(source_path)
            target_path = os.path.join(dest_dir_path, dir)
            if os.path.isfile(source_path):
                generate_page(source_path, template_path, target_path.replace(".md", ".html"))
            else:
                os.mkdir(target_path)
                generate_pages_recursive(source_path, template_path, target_path)   