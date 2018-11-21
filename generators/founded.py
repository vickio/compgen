from . import BaseGenerator
from random import randint
from datetime import datetime

class Founded(BaseGenerator):
    
    def __init__(self, company):
        self.data = self._load_json('founded.json')
    
    def generate(self):
        decade = self._choose(self.data['decade'])
        max_year = 9
        if decade == str(datetime.now().year)[:3]:
            max_year = int(str(datetime.now().year)[-1])
        last_digit = str(randint(0, max_year))
        return int(decade + last_digit)
