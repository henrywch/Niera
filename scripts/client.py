# client.py
import socket
import pyaudio

HOST = '127.0.0.1'
PORT = 43001
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000

p = pyaudio.PyAudio()
stream = p.open(rate=RATE,
                channels=CHANNELS,
                format=FORMAT,
                input=True,
                input_device_index=0,
                frames_per_buffer=CHUNK)

print("Streaming audio...")
try:
    while True:
        data = stream.read(CHUNK)
        client_socket.sendall(data)
except KeyboardInterrupt:
    print("Stopped")

finally:
    stream.stop_stream()
    stream.close()
    p.terminate()
    client_socket.close()