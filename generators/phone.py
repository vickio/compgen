from . import BaseGenerator
from random import randint

class Phone(BaseGenerator):
    
    def __init__(self, company):
        self.company = company
        self.data = self._load_json('phone.json')
    
    def generate(self):
        area_code = self._choose(self.data['area_code'])
        if area_code == 'xxx':
            area_code = str(randint(1, 999)).zfill(3)
        phone = f'({area_code}) '
        phone += str(randint(1, 999)).zfill(3) + '-'
        phone += str(randint(1, 9999)).zfill(4)
        return phone
