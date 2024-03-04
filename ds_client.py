# Starter code for assignment 3 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Nicole Kwan
# nkwan3@uci.edu
# 76647093
import socket
import json
import time
from ds_protocol import extract_json

def send(server:str, port:int, username:str, password:str, message:str, bio:str=None):
    response = join_server(server, port, username, password)

    if response.type == "error":
        print(response.message)
        return False
    
    token = response.token

    if message:
        if not send_message(server, port, token, "post", message):
            return False
        
    if bio:
        if not send_message(server, port, token, "bio", bio):
            return False
        
    return True

def send_message(server, port, token, entry_type, entry):
    message = {
        "token": token,
        entry_type: {
            "entry": entry,
            "timestamp": time.time()
        }
    }

    message = json.dumps(message)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((server, port))
        send = client.makefile('w')
        recv = client.makefile('r')

        send.write(message + "\r\n")
        send.flush()

        response = recv.readline()
        get_data = extract_json(response)

        if get_data.type == "error":
            print(get_data.message)
            return False
        
        return True

def join_server(server, port, username, password):
    data = {
        "join": {
            "username": username,
            "password": password,
            "token": ""
        }
    }

    # formats as json string
    json_message = json.dumps(data)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((server, port))

        send = client.makefile('w')
        recv = client.makefile('r')

        send.write(json_message + '\r\n')
        send.flush()

        response = recv.readline()
        get_data = extract_json(response)

        print(get_data.message)

    return get_data
    