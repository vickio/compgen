from string import Template
from pathlib import Path
from datetime import datetime

from company import Company
from card import Card

class CardPage:
    
    def __init__(self, count=4):
        self.companies = []
        for _ in range(count):
            self.companies.append(Company())
        
        template_file = Path('html/index.template.html')
        self.template = Template(template_file.read_text('utf8'))
    
    @property
    def html(self):
        cards = ''.join([Card(c).html for c in self.companies])
        return self.template.substitute({
            'last_update': datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC'),
            'cards': cards})
