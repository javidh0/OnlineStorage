import socket

HOST = '10.5.247.136'
PORT = 42051

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print('Conencted')

def command(clnt, rep):
    ts = "None"
    if(rep == 'r'):
        ts == "REC"
    elif(rep == 'iv'):
        ts == "INV"
    elif(rep == 'v'):
        ts == "VLD"
    clnt.send(ts.encode('utf-8'))
def reply(cmd):
    print(cmd)
    cmd = cmd.decode("utf-8")
    if cmd == '-1':
        return 'break'
def getConfig():
    while True:
        dta = s.recv(1024)
        print(dta)
        if not dta:
            break
def ReqAccess():
    cmd = input("Enter the command : ")
    s.send(cmd.encode('utf-8'))
    buf = s.recv(1024)
    print(buf)
    if buf == b'GET':
        getConfig()
    else:
        print("Invalid")
while False:    
    A = [s.recv(1024)]
    if A[0].decode('utf-8') == 'READY':
        cmd = input("Enter the command : ")
        s.send(cmd.encode('utf-8'))
        print(s.recv(1024))
    elif A[0].decode('utf-8') == 'BREAK':
        break
if(s.recv(1024) == b'READY'):
    ReqAccess()
