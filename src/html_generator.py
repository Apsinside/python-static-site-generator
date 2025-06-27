from markdown_html import markdown_to_html_node

def extract_title(markdown):
    strings = markdown.split("\n")
    for str in strings:
        if str.startswith("#"):
            return str.strip("#").strip(" ")
    raise Exception("no title found")

def generate_page(from_path, template_path, dest_path):
    with open(template_path) as file:
        template = file.read()
    with open(from_path) as file:
        markdown = file.read()
    title = extract_title(markdown)
    content = markdown_to_html_node(markdown).to_html()

    template = template.replace("{{ Title }}", title).replace("{{ Content }}", content)
    with open(dest_path, "a") as file:
        file.write(template)
