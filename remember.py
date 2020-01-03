from recorder import IRe
import subprocess as sp


class Remember(IRe):
    def get_random(self):
        format = self.get_format()
        data = format.random()
        return data

    def remember(self):
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
