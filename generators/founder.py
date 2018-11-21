from . import BaseGenerator

class Founder(BaseGenerator):
    
    def generate(self):
        fake = self.company._fake
        return ' '.join([fake.first_name(), fake.last_name()])
