from jinja2 import Environment, FileSystemLoader
import importlib.resources as pkg_resources

class TemplateHandler:
    def __init__(self, template_dir):
        self.env = Environment(
            loader=FileSystemLoader(pkg_resources.files(f'regtool.templates.{template_dir}')),
            trim_blocks=True,
            lstrip_blocks=True
        )

    def render(self, template_name, context):
        template = self.env.get_template(template_name)
        return template.render(**context)
