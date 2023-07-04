import sys
import socket
import logging
from concurrent.futures import ThreadPoolExecutor
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

if __name__ == '__main__':
    with ThreadPoolExecutor() as executor:
        start_time = time.time()
        request_count = 0
        futures = set()

        while time.time() - start_time < 60:
            future = executor.submit(kirim_data)
            futures.add(future)

            completed_futures = {f for f in futures if f.done()}
            request_count += len(completed_futures)
            futures -= completed_futures

        for future in futures:
            future.result()

        logging.warning(f"Total requests: {request_count}")
