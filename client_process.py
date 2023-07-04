import sys
import socket
import logging
from multiprocessing import Process
import time 

time.sleep(5)

def kirim_data():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 45000)
    sock.connect(server_address)

    try:
        message = 'TIME\r\n'
        sock.sendall(message.encode())
        data = sock.recv(32)
        logging.warning(f"[C] Mengirim... {message} [S] telah terkirim {data}")
    finally:
        sock.close()
    return

def create_process():
    p = Process(target=kirim_data)
    p.start()
    p.join()

if __name__ == '__main__':
    process_count = 0 
    start_time = time.time()
    while time.time() - start_time < 60:
        create_process()
        process_count += 1 
    logging.warning(f"Total requests: {process_count}")
