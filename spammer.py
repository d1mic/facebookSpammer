import sys
import os
from fbchat import Client
from fbchat.models import *
from dotenv import load_dotenv

load_dotenv()
client = None

def login(email,password):
    global client
    client = Client(email, password)

def logout():
    global client
    client.logout()

def spam(name, msg, n):
    global client
    user = client.searchForUsers(str(name))[0]
    if(not user.is_friend):
        print("This user is not your friend. Don't spam strangers! ")
        return False

    print('Sending messages to: {}'.format(user.name))
    for i in range(n):
        client.send(Message(text=str(msg)), thread_id=user.uid,thread_type=ThreadType.USER)
    print("Messages sent to: {}".format(user.name))
    return True

def main():

    m_email = os.getenv("EMAIL")
    m_password = os.getenv("PASSWORD")
    login(m_email, m_password)

    if(len(sys.argv) != 5):
        print("Usage: python3 spammer.py -s [name] [msg] [numOfMsgs]")

    if(sys.argv[1] == "-s"):
        searchName = str(sys.argv[2])
        spamMsg = str(sys.argv[3])
        numOfSpams = int(sys.argv[4])
        if(not spam(searchName, spamMsg, numOfSpams)):
            print("Failed to send messages to " + searchName)
    
    logout()

if __name__ == "__main__":
    main()
