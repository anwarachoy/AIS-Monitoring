import socket
ais_serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ais_serv.bind(('103.28.13.218', 2101))
ais_serv.listen(5)

ais_fwd1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ais_fwd1.bind(('103.28.13.218', 1234))
ais_fwd1.listen(5)
while True:
    conn, addr = ais_serv.accept()
    conn1, addr1 = ais_fwd1.accept()
    from_client = ''
    while True:
        data = conn.recv(4096)
        if not data: break
        from_client += data
        print (from_client)
        conn.send(data)
        conn1.send(data)
    conn.close()
    conn1.close()
    print ('client disconnected')
