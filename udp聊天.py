import socket

def send_msg(udp_socket):
    """发送消息"""
    dest_ip = input("请输入对方的ip:")
    dest_port = int(input("请输入对方的端口："))
    send_data = input("请输入要发送的数据： ")
    udp_socket.sendto(send_data.encode("gbk"), (dest_ip, dest_port))

def recv_msg(udp_socket):
    """接受消息"""
    recv_data = udp_socket.recvfrom(1024)
    print("%s:%s" % (str(recv_data[1]), recv_data[0].decode("gbk")))
    
def main():
    # 创建一个UDP套接字
    udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    # 绑定信息
    udp_socket.bind(("",7788))
    
    
    while True:
        # 发送
        send_msg(udp_socket)
        # 接收并显示
        recv_msg(udp_socket)
        #套接字可以收发
        #socket套接字是全双工的，但是由于多任务缺少，程序里面体现不出全双工
    udp_socket.close()#socket不用的时候关闭 套接字

if __name__ =='__main__':
    main()









