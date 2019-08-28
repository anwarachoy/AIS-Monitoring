import socket
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('0.0.0.0', 6789))
serv.listen(5)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 1234))
s.listen(5)
while True:
    conn, addr = serv.accept()
    conns, addrs = s.accept()
    from_client = ''
    while True:
        data = conn.recv(4096)
        if not data: break
        from_client += data
        print (from_client)
        conn.send(data)
        conns.send(data)
    conn.close()
    conns.close()
    print ('client disconnected')
