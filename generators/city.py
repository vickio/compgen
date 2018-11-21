from . import BaseGenerator

class City(BaseGenerator):
    
    def generate(self):
        return self.company._fake.city()
