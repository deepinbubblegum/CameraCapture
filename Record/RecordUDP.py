import yaml

class RecordUDP():
    def __init__(self):
       self.ports = self.load_config()

    def load_config(self):
        with open('config/record.yaml', 'r') as ports_file:
            ports = yaml.safe_load(ports_file)['ports']
        return ports

    