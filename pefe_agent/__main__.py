from .consumer import PEFEConsumer
import time
import hashlib

def main():
    class ExampleConsumer(PEFEConsumer):
        def handle_pe_file(self, path):
            return hashlib.sha256(path.encode('utf-8')).digest(), path.encode('utf-8')
    ExampleConsumer(f"AGENT {time.time()}").run()

if __name__ == "__main__":
    main()
