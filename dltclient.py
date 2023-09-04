import socket
import time

# 定义目的IPv6地址和端口号
dest_addr = 'fd53:7cb8:0383:0803:eb01::0010'
dest_port = 3490

# 创建TCP套接字
sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM, socket.IPPROTO_TCP)
# local_ip = socket.gethostbyname(socket.gethostname(), family=socket.AF_INET6)
# print(local_ip)
# 将套接字绑定到本地IPv6地址上

# local_addr = ('fe80::a853:f60b:7760:5c87%20', 8000)
# sock.bind(local_addr)

# 连接到目的IPv6地址
sock.connect((dest_addr, dest_port))

# 发送数据
data = (b'5\x00\x00\x1a8848\n\x1a=\x9e\x16\x01APP\x00CON\x00\x13\x00\x00\x005\x00\x00\x1f8848\n\x1a=\x9e\x16\x01APP'
        b'\x00CON\x00\x11\x00\x00\x00\x04remo5\x00\x00\x1f8848\n\x1a=\x9e\x16\x01APP\x00CON\x00\x12\x00\x00\x00'
        b'\x00remo5\x00\x00\x1b8848\n\x1a=\x9e\x16\x01APP\x00CON\x00\t\x00\x00\x00\x015\x00\x00\x1b8848\n\x1a=\x9e'
        b'\x16\x01APP\x00CON\x00\x0b\x00\x00\x00\x00')
sock.sendall(data)

# 接收数据
while True:
    # 指定文件名
    file_name = "saved_info.txt" # 将信息写入txt文件
    with open(file_name, 'w') as file:
        recv_data = sock.recv(4096)
        print(recv_data)
        file.write(recv_data)
        print(f"信息已保存到 {file_name}")
# sock.close()