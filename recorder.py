from format import JSONFormat, Format
from abc import ABC, abstractmethod
import argparse


class IRe:
    def __init__(self, recorder_format='json', save_path='/Users/utkucanbiyikli/Desktop/Projects/remember-me', file_name='remember'):
        self._recorder_format = recorder_format
        self._save_path = save_path
        self._file_name = f'{file_name}.{recorder_format}'

    def get_format(self) -> Format:
        if self._recorder_format == 'json':
            return JSONFormat(f'{self._save_path}/{self._file_name}')


class Recorder(IRe):
    def save(self, value) -> bool:
        format = self.get_format()
        obj = format.parse(value)
        return format.save(obj)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', required=True)
    parser.add_argument('--value', required=True)
    parser.add_argument('--message', required=True)
    args = parser.parse_args()
    recorder = Recorder()
    recorder.save({
        'message': args.message, 'title': args.key, 'subtitle': args.value
    })
