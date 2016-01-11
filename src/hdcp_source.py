
import yaml

class HdcpSource:

    def __init__(self, conf_yaml):
        f = open(conf_yaml, "r")
        conf = yaml.load(f)
        f.close()

    def process_request(req):
        msg_type, msg = req



if __name__ == "__main__":
    HdcpSource("yaml/rx1.yaml")

