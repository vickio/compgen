from json import JSONDecoder
from pathlib import Path
from random import choices, choice

DATA_PATH = 'data/'

class BaseGenerator:
    
    def __init__(self, company):
        self.company = company
    
    @classmethod    
    def _load_json(cls, file_name):
        data_file = Path(DATA_PATH + file_name)
        return JSONDecoder().decode(data_file.read_text())
    
    @classmethod
    def _load_txt(cls, file_name):
        data_file = Path(DATA_PATH + file_name)
        return data_file.read_text('utf8').split()
    
    @classmethod    
    def _choose(cls, data):
        items = []
        weights = []
        for item, weight in data:
            items.append(item)
            weights.append(weight)
        return choices(items, weights)[0]
