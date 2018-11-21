from . import BaseGenerator
from random import choice, randint

class Seed(BaseGenerator):
    
    def __init__(self, company):
        self.nouns = self._load_txt('nouns.txt')
        self.adjectives = self._load_txt('adjectives.txt')
    
    def generate(self):
        return '-'.join([
            choice(self.adjectives),
            choice(self.adjectives),
            choice(self.nouns)])
