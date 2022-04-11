from format import Format, JSONFormat
import argparse


class IRe:
    def __init__(self, recorder: Format):
        self.recorder = recorder

    def get_format(self) -> Format:
        return self.recorder


class Recorder(IRe):
    def save(self, value) -> bool:
        format = self.get_format()
        obj = format.parse(value)
        return format.save(obj)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--key", required=True)
    parser.add_argument("--value", required=True)
    parser.add_argument("--message", required=True)
    args = parser.parse_args()
    recorder = Recorder(JSONFormat(path="./remember.json"))
    recorder.save({"message": args.message, "title": args.key, "subtitle": args.value})
