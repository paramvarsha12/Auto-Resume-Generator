import pdfkit
from jinja2 import Environment, FileSystemLoader
import os
import tempfile

template_dir = os.path.abspath("templates")
env = Environment(loader=FileSystemLoader(template_dir))

def render_template(data, template_name):
    template_file = f"{template_name}_template.html"
    template = env.get_template(template_file)
    return template.render(data)

def convert_to_pdf(html_content):
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=".html") as tmp:
        tmp.write(html_content.encode("utf-8"))
        tmp_path = tmp.name

    pdf_path = tmp_path.replace(".html", ".pdf")

    
    config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")

    pdfkit.from_file(tmp_path, pdf_path, configuration=config)

    return pdf_path
