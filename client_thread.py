import sys
import socket
import logging
import threading
import time

def kirim_data():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 45000)
    sock.connect(server_address)

    try:
        message = 'TIME\r\n'
        sock.sendall(message.encode())
        data = sock.recv(32)
        logging.warning(f"[C] Mengirim.... {message} [S] telah terkirim {data}")
    finally:
        sock.close()
    return

def create_thread():
    t = threading.Thread(target=kirim_data)
    t.start()
    t.join()

if __name__ == '__main__':
    thread_count = 0 
    start_time = time.time()
    while time.time() - start_time < 60:
        create_thread()
        thread_count += 1 
    logging.warning(f"Total requests: {thread_count}")
