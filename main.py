import logging
import webbrowser
from time import sleep

logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',
                    level=logging.INFO,
                    datefmt='%Y-%m-%d %H:%M:%S')

log_path = "C:/Program Files (x86)/Steam/steamapps/common/Counter-Strike Global Offensive/csgo/console.log"
server_ip = "csgoserveriphere"
dc_msg = "Disconnect: Relog to continue.\n"
timeout_msg = "Server connection timed out.\n"
sleep_sec = 10

def scan():
    logging.info("Scanning " + log_path)
    f = open(log_path,"r", encoding='utf-8', errors='ignore')
    if f.mode == 'r':
        lines = f.readlines()
        for x in lines:
            if x == dc_msg or x == timeout_msg:
                f.close()
                logging.info("Found DC message!")
                connect_to_ip()
                open(log_path, 'w').close()
                return True

        f.close()
        return False
                
def connect_to_ip():
    logging.info("Connecting to IP: " + server_ip)
    webbrowser.open_new("steam://connect/" + server_ip)

def program():
    while 1 == 1:
        scan()
        sleep(sleep_sec)

program()
