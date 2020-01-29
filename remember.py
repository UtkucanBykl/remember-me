from recorder import IRe
import subprocess as sp
import os

class Remember(IRe):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def running(self) -> bool:
        return os.environ.get('REMEMBER_ME')

    @running.setter
    def running(self, value):
        if isinstance(value, bool):
            os.environ['REMEMBER_ME'] = str(value)

    def get_random(self):
        format = self.get_format()
        data = format.random()
        return data

    def remember(self):
        print(self.running)
        if self.running == 'False' or not self.running:
            return
        data = self.get_random()
        message = data.get('message')
        title = data.get('title')
        subtitle = data.get('subtitle')
        process = sp.Popen(
            ["osascript", "-"],
            stdin=sp.PIPE,
            stderr=sp.PIPE,
            stdout=sp.PIPE,
            universal_newlines=True,
        )
        applescript = f'display notification "{message}" with title "{title}"'
        if subtitle:
            applescript += f' subtitle "{subtitle}"'
        process.communicate(applescript)


if __name__ == "__main__":
    remember = Remember()
    remember.remember()
