
import re
import yaml

class HdcpSink:

    def __init__(self, conf_file):

        f = open(conf_file, "r")
        conf = yaml.load(f)
        f.close()

        cert_bin = self.__hex2bin(conf["cert_hex"])

        priv = conf["priv_key"]
        P_bin           = self.__hex2bin(priv["P_hex"])
        Q_bin           = self.__hex2bin(priv["Q_hex"])
        d_mod_p_1_bin   = self.__hex2bin(priv["d_mod_p-1_hex"])
        d_mod_q_1_bin   = self.__hex2bin(priv["d_mod_q-1_hex"])
        inv_q_mod_p_bin = self.__hex2bin(priv["inv_q_mod_p_hex"])

        self.__cert_bin   = cert_bin
        self.__priv_key_P = int.from_bytes(P_bin, "big")
        self.__priv_key_Q = int.from_bytes(Q_bin, "big")
        self.__priv_key_d_mod_p_1   = int.from_bytes(d_mod_p_1_bin, "big")
        self.__priv_key_d_mod_q_1   = int.from_bytes(d_mod_q_1_bin, "big")
        self.__priv_key_inv_q_mod_p = int.from_bytes(inv_q_mod_p_bin, "big")


        f = open("yaml/global.yaml", "r")
        conf = yaml.load(f)
        f.close()

        global_constant_hex = re.sub(r'\s', "", conf["global_constant"])
        self.__global_constant_bin = bytes.fromhex(global_constant_hex)

    def __hex2bin(self, hex_str):
        ret_bin = bytes.fromhex(re.sub(r'\s', "", hex_str))
        return ret_bin

    def process_request(self, request):
        (msg_type, msg) = request

    def test(self):
        print("P is ... " + str(self.__priv_key_P))
        print("Q is ... " + str(self.__priv_key_Q))

if __name__ == "__main__":
    rx1 = HdcpSink("yaml/rx1.yaml")
    rx1.test()

