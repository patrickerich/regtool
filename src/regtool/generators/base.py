#!/usr/bin/env python3
from typing import Dict
from mako.template import Template 
from pathlib import Path

class BaseGenerator:
    def __init__(self, template_dir: Path):
        self.template_dir = template_dir
        
    def load_template(self, template_name: str) -> Template:
        template_path = self.template_dir / template_name
        return Template(filename=str(template_path))
        
    def render(self, template_name: str, context: Dict) -> str:
        template = self.load_template(template_name)
        return template.render(**context)
