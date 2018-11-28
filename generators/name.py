from random import choice
from string import Template

from . import BaseGenerator

class Name(BaseGenerator):
        
    def __init__(self, company):
        self.company = company
        
        self.data = self._load_json('name.json')
        self.templates = self.data.pop('templates')
        
        self.nouns = self._load_txt('nouns.txt')
        self.adjectives = self._load_txt('adjectives.txt')
        
        self.founder_data = self._load_json('founder.json')
        
    def generate(self):
        template = Template(self._choose(self.templates))
        elements = {}
        for key, options in self.data.items():
            elements[key] = self._choose(options)
        
        for noun in ['noun', 'noun2']:
            elements[noun] = choice(self.nouns)
            if not elements[noun].isupper():
                elements[noun] = elements[noun].title()
        elements['adjective'] = choice(self.adjectives).title()
        elements['adjective2'] = choice(self.adjectives).title()
        
        fname, lname = self.company.founder.split(' ')
        
        fake = self.company._fake
        
        elements['lname'] = lname
        elements['lname2'] = self._choose(self.founder_data['last_name'])
        elements['lname3'] = self._choose(self.founder_data['last_name'])
        elements['fname'] = fname
        elements['place'] = choice([self.company.city, self.company.state_name])
        elements['fakeword'] = fake.word().title()
        
        if len(elements['fakeword']) <= 3:
            elements['fakeword'] = elements['fakeword'].upper()
        
        if self.company.founder_gender == 'male':
            elements['family'] = elements['family_male']
        else:
            elements['family'] = elements['family_female']
        
        return template.substitute(elements)

