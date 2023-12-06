import os
import sys
import socket
import argparse
import symmetric
from common import *
from const import *

def main():
    parser = argparse.ArgumentParser(description="test")
    parser.add_argument("--relay", action="store_true", help="enable messsage relay")
    parser.add_argument("--break-heart", action="store_true")
    parser.add_argument("--custom", action="store_true")
    args = parser.parse_args()


    if args.relay:
        perform_relay_attack()

    if args.break_heart:
        perform_heart_breaking_attack()

    if args.custom:
        perform_custom()
        
def perform_relay_attack():
    dialog = Dialog('print')

    socketAlice, aesAlice = setup('bob', BUFFER_DIR, BUFFER_FILE_NAME)
    socketBob, aesBob = setup('alice', BUFFER_DIR, BUFFER_FILE_NAME)

    fromBob = receive_and_decrypt(aesBob, socketBob)
    #dialog.info(fromBob)
    encrypt_and_send(fromBob, aesAlice, socketAlice)

    fromAlice = receive_and_decrypt(aesAlice, socketAlice)
    #dialog.info(fromAlice)
    encrypt_and_send(fromAlice, aesBob, socketBob)

    #tear_down(socketAlice, BUFFER_DIR, BUFFER_FILE_NAME)
    #tear_down(socketBob, BUFFER_DIR, BUFFER_FILE_NAME)
    

def perform_heart_breaking_attack():
    dialog = Dialog('print')

    socketAlice, aesAlice = setup('bob', BUFFER_DIR, BUFFER_FILE_NAME)
    socketBob, aesBob = setup('alice', BUFFER_DIR, BUFFER_FILE_NAME)

    fromBob = receive_and_decrypt(aesBob, socketBob)
    #dialog.info(fromBob)
    toAlice="I hate you!"
    encrypt_and_send(toAlice, aesAlice, socketAlice)

    fromAlice = receive_and_decrypt(aesAlice, socketAlice)
    #dialog.info(fromAlice)
    toBob="You broke my heart..."
    encrypt_and_send(toBob, aesBob, socketBob)

    #tear_down(socketAlice, BUFFER_DIR, BUFFER_FILE_NAME)
    #tear_down(socketBob, BUFFER_DIR, BUFFER_FILE_NAME)

def perform_custom():
    dialog = Dialog('print')

    socketAlice, aesAlice = setup('bob', BUFFER_DIR, BUFFER_FILE_NAME)
    socketBob, aesBob = setup('alice', BUFFER_DIR, BUFFER_FILE_NAME)

    fromBob = receive_and_decrypt(aesBob, socketBob)
    #dialog.info(fromBob)
    dialog.prompt('Please input message...')
    customToAlice = input()
    encrypt_and_send(customToAlice, aesAlice, socketAlice)

    fromAlice = receive_and_decrypt(aesAlice, socketAlice)
    #dialog.info(fromAlice)
    dialog.prompt('Please input message...')
    customToBob = input()
    encrypt_and_send(customToBob, aesBob, socketBob)

    #tear_down(socketAlice, BUFFER_DIR, BUFFER_FILE_NAME)
    #tear_down(socketBob, BUFFER_DIR, BUFFER_FILE_NAME)
    
main()
    
    



    
