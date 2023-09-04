import socket


class dltDaemon:
    def __init__(self):
        self.HOST = 'fe80::a7da:10d:b51b:e6fa%6'
        self.PORT = 3490

    def __Start__(self):
        global conn
        try:
            # 创建TCP/IP套接字
            s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            # 绑定到指定的IP地址和端口上
            s.bind((self.HOST, self.PORT))
            # 监听传入的连接
            s.listen(100)
            print('Listening on port %s...' % self.PORT)
            while True:
                try:
                    # 建立客户端连接
                    conn, addr = s.accept()
                    print('Connected by', addr)
                    while True:
                        # 循环接收数据并发送到DLT Viewer
                        data = conn.recv(1024)
                        sender=b"e synchronization provider ICAS1 sync slave\x10\x00DLT proxy daemonLOG\x00\x01\x00TYP1\x02\x00.\x00time synchronization provider ICAS1 sync slave\x10\x00DLT proxy daemonLOG\x00\x01\x00TYP1\x02\x00.\x00time synchronization provider ICAS1 sync slave\x10\x00DLT proxy daemonLOG\x00\x01\x00TYP1\x02\x00.\x00time synchronization provider ICAS1 sync slave\x10\x00DLT proxy daemonLOG\x00\x01\x00TYP1\x02\x00.\x00time synchronization provider ICAS1 sync slave\x10\x00DLT proxy daemonLOG\x00\x01\x00TYP1\x02\x00.\x00time synchronization provider ICAS1 sync slave\x10\x00DLT proxy daemonLOG\x00\x01\x00TYP1\x02\x00.\x00time synchronization provider ICAS1sync slave\x10\x00DLT proxy daemonLOG\x00\x01\x00TYP1\x02\x00.\x00time synchronization provider ICAS1 sync slave\x10\x00DLT proxy daemonLOG\x00\x01\x00TYP1\x02\x00.\x00time synchronization provider ICAS1 sync slave\x10\x00DLT proxy daemonLOG\x00\x01\x00TYP1\x02\x00.\x00time synchronization provider ICAS1 sync slave\x10\x00DLT proxy daemonLOG\x00\x00\x00\x10\x00DLT proxy daemonLOG\x00\x01\x00TYP1\x02\x00.\x00time synchronization provider ICAS1 sync slave\x10\x00DLT proxy daemonLOG\x00\x01\x00TYP1\x02\x00.\x00time synchronization provider ICAS1 sync slave\x10\x00DLT proxy daemonLOG\x00\x01\x00TYP1\x02\x00.\x00time synchronization provider ICAS1 sync slave\x10\x00DLT proxy daemonLOG\x00\x01\x00TYP1\x02\x00.\x00time synchronization provider ICAS1 sync slave\x10\x00DLT proxy daemonLOG\x00\x01\x00TYP1\x02\x00.\x00time synchronization provider ICAS1 sync slave\x10\x00DLT proxy daemonLOG\x00\x01\x00TYP1\x02\x00.\x00time synchronization provider ICAS1 sync slave\x10\x00DLT proxy daemonLOG\x00\x00\x00\x10\x00DLT proxy daemonLOG\x00\x01\x00TYP1\x02\x00.\x00time synchronization provider ICAS1 sync slave\x10\x00DLT proxy daemonLOG\x00\x00\x00\x10\x00DLT proxy daemonLOG\x00\x00\x00\x10\x00DLT proxy daemonLOG\x00\x01\x00TYP1\x02\x00.\x00time synchronization provider ICAS1 sync slave\x10\x00DLT proxy daemonLOG\x00\x01\x00TYP1\x02\x00.\x00time synchronization provider ICAS1 sync slave\x10\x00DLT proxy daemonLOG\x00\x01\x00TYP1\x02\x00.\x00time synchronization provider ICAS1 sync slave\x10\x00DLT proxy daemonLOG\x00\x01\x00TYP1\x02\x00.\x00time synchronization provider ICAS1 sync slave\x10\x00DLT proxy daemonLOG\x00\x01\x00TYP1\x02\x00.\x00time synchronization provider ICAS1 sync slave\x10\x00DLT proxy daemonLOG\x00\x01\x00TYP1\x02\x00.\x00time synchronization provider ICAS1 sync slave\x10\x00DLT proxy daemonLOG\x00\x01\x00TYP1\x02\x00.\x00time synchronization provider ICAS1 sync slave\x10\x00DLT proxy daemonLOG\x00\x01\x00TYP1\x02\x00.\x00time synchronization provider ICAS1 sync slave\x10\x00DLT proxy daemonLOG\x00\x00\x00\x10\x00DLT proxy daemonLOG\x00\x01\x00TYP1\x02\x00.\x00time synchronization provider ICAS1 sync slave\x10\x00DLT proxy daemonLOG\x00\x01\x00TYP1\x02\x00.\x00time synchronization provider ICAS1 sync slave\x10\x00DLT proxy daemonLOG\x00\x01\x00TYP1\x02\x00.\x00time synchronization provider ICAS1 sync slave\x10\x00DLT proxy daemonLOG\x00\x01\x00TYP1\x02\x00.\x00time synchronization provider ICAS1 sync slave\x10\x00DLT proxy daemonLOG\x00\x01\x00TYP1\x02\x00.\x00time synchronization provider ICAS1 sync slave\x10\x00DLT proxy daemonremo=t\x00\xa08123\x00\x00\x0b5\x00\x03\xa8\x84A\x01LOG\x00LTDI\x00\x02\x00\x00\x80\x00ContextID 'NOTS' registered for ApID 'LOG', Description=time synchronization provider ICAS1 sync slave without tsyn timestamps\n\x005\x00\x0f\xbd8123\x00\x03\xa8\x8b&\x01LOG\x00LTDC\x03\x00\x00\x00\x07+\x00LOG\x00\x01\x00NOTS\x02\x00F\x00time synchronization provider ICAS1 sync slave without tsyn timestamps\x10\x00DLT proxy daemonLOG\x00\x01\x00NOTS\x02\x00F\x00time synchronization provider ICAS1 sync slave without tsyn timestamps\x10\x00DLT proxy daemonLOG\x00\x01\x00NOTS\x02\x00F\x00time synchronization provider ICAS1 sync slave without tsyn timestamps\x10\x00DLT proxy daemonLOG\x00\x01\x00NOTS\x02\x00F\x00time synchronization provider ICAS1 sync slave without tsyn timestamps\x10\x00DLT proxy daemonLOG\x00\x01\x00NOTS\x02\x00F\x00time synchronization provider ICAS1 sync slavewithout tsyn timestamps\x10\x00DLT proxy daemonLOG\x00\x01\x00NOTS\x02\x00F\x00time synchronization provider ICAS1 sync slave without tsyn timestamps\x10\x00DLT proxy daemonLOG\x00\x01\x00NOTS\x02\x00F\x00time synchronization provider ICAS1 sync slave without tsyn timestamps\x10\x00DLT proxy daemonLOG\x00\x01\x00NOTS\x02\x00F\x00time synchronization provider ICAS1 sync slave without tsyn timestamps\x10\x00DLT proxy daemonLOG\x00\x01\x00NOTS\x02\x00F\x00time synchronization provider ICAS1 sync slave without tsyn timestamps\x10\x00DLT proxy daemonLOG\x00\x01\x00NOTS\x02\x00F\x00time synchronization provider ICAS1 sync slave without tsyn timestamps\x10\x00DLT proxy daemonLOG\x00\x01\x00NOTS\x02\x00F\x00time synchronization provider ICAS1 sync slave without tsyn timestamps\x10\x00DLT proxy daemonLOG\x00\x01\x00NOTS\x02\x00F\x00time synchronization provider ICAS1 sync slave without tsyn timestamps\x10\x00DLT proxy daemonLOG\x00\x01\x00NOTS\x02\x00F\x00time synchronization provider ICAS1 sync slave without tsyn timestamps\x10\x00DLT proxy daemonLOG\x00\x01\x00NOTS\x02\x00F\x00time synchronization provider ICAS1 sync slave without tsyn timestamps\x10\x00DLT proxy daemonLOG\x00\x01\x00NOTS\x02\x00F\x00time synchronizati"
                        if not data:
                            break
                        print(data)
                        while True:
                            response = sender
                            conn.sendall(response)
                except socket.error:
                    break
                finally:
                    # 关闭连接
                    conn.close()
        except Exception as e:
            print('Error:', e)


if __name__ == '__main__':
    dltDaemon().__Start__()