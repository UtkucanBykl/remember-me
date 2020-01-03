import random
import json
from abc import ABC, abstractmethod

__all__ = ['JSONFormat', 'Format']


class Format(ABC):
    @abstractmethod
    def parse(self, value):
        pass

    @abstractmethod
    def random(self):
        pass


class JSONFormat(Format):
    def __init__(self, path):
        self._path = path

    def parse(self, value):
        with open(self._path) as f:
            try:
                json_data = json.load(f)
            except:
                json_data = json.loads('{}')
            array_data = json_data.get('data', [])
            array_data.append(value)
            json_data['data'] = array_data
        return json.dumps(json_data)

    def random(self):
        with open(self._path) as f:
            try:
                json_data = json.load(f)
            except:
                json_data = json.loads('{}')
        return random.choice(json_data.get('data', [{}]))