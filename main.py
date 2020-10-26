#water drinking notification system


import time
from plyer import notification
if __name__ == "__main__":
    while True:
        notification.notify(
            title = "PLEASE DRINK WATER NOW ANANT!!! ",
            message = " DRINKING WATER Keep your temperature normal. Protect your spinal cord and other sensitive tissues. Get rid of wastes through urination, perspiration, and bowel movements.",
            timeout = "12"
        )
        time.sleep(45*45)