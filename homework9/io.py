# 2 编写一个接收数据的网络程序，由“网络调试工具”发送数据，你的程序接收数据并打印输出；

# 接收
import socket

def main():
    # 绑定端口信息
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    local_addr = ('', 9999)

    udp_socket.bind(local_addr)
    # 接收数据
    recv_data = udp_socket.recvfrom(1024)  # 1024表示本次接收的最大字节数
    # 打印显示接收到的数据
    print(recv_data)
    # 关闭套接字
    udp_socket.close()


# 发送
# def main():
#     # 1 创建一个udp套接字
#     udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#
#     # 2. 准备接收方的地址 使用udp套接字发送数据:发什么,发给谁
#     # '192.168.1.103'表示目的ip地址
#     # 8080表示目的端口
#     dest_addr = ('192.168.1.103', 8080)  # 注意 是元组，ip是字符串，端口是数字
#
#     # 3. 从键盘获取数据
#     send_data = input("请输入要发送的数据:")
#     # 4. 发送数据到指定的电脑上的指定程序中
#     udp_socket.sendto(send_data.encode('utf-8'), dest_addr)
#     # 5 关闭套接字
#     udp_socket.close()


if __name__ == "__main__":
    main()