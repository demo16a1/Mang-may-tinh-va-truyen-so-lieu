# vd
import socket
# Tạo socket server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket đã được tạo thành công!")
# Gán địa chỉ IP và cổng
server_socket.bind(("127.0.0.1", 5000)) 

# Lắng nghe kết nối (tối đa 5 client)
server_socket.listen(5)
print("Server đang lắng nghe trên cổng 5000...")
while True:
    client_socket, client_address = server_socket.accept()
    print(f"Kết nối từ {client_address}")

    # Nhận dữ liệu từ client
    data = client_socket.recv(1024).decode()
    print(f"Dữ liệu nhận được: {data}")

    # Phản hồi client
    response = "Server đã nhận dữ liệu!"
    client_socket.send(response.encode())

    # Đóng kết nối
    client_socket.close()

    # Điều kiện dừng server khi nhận "exit" từ client
    if data.lower() == "exit":
        print("Server đang tắt...")
        client_socket.close()
        server_socket.close()
    break


