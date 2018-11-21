from string import Template
from pathlib import Path

class Card:
    
    def __init__(self, company):
        self.company = company
        template_file = Path('html/card.template.html')
        self.template = Template(template_file.read_text('utf8'))
    
    @property
    def html(self):
        data = {
            'seed': self.company.seed,
            'name': self.company.name + self.company.suffix,
            'url': self.company.url,
            'phone': self.company.phone,
            'address': self.company.street_address,
            'city': ', '.join([self.company.city, self.company.state]),
            'founded': f'Founded {self.company.founded} by {self.company.founder}'
        }
        return self.template.substitute(data)
