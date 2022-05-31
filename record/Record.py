import yaml

class Record():
    def __init__(self):
        print('init Record')
        self.ports = self.load_config()
        print(self.ports)

    def load_config(self):
        with open('config/ports.yaml', 'r') as ports:
            ports = yaml.safe_load(ports)
        ports = ports['ports']
        return ports