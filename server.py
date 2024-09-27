import socket

# Créer un socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)



# Associer le socket à une adresse IP et un port
server_socket.bind(('0.0.0.0', 666))  # Écouter sur toutes les interfaces, port 666

print("Serveur UDP en écoute sur le port 666...")

#https://docs.simplebackups.com/help-tips--troubleshooting/mQyMDHYQcVeYgoW6VN65u8/how-to-generate-an-rsa-pem-asymmetric-key-pair/bcnQXAqtpBMQSd28UTUEmA

while True:
    data, addressClient = server_socket.recvfrom(1, socket.MSG_PEEK)

    # Afficher les données et l'adresse du client
    print(f"longueur de : {data.decode()}")
    
    data, addressClient = server_socket.recvfrom(int (data.decode()))

    message = data.decode()

    print(f"message : {message}")

    leng = message[0:1]
    
    print(f"lenght : {leng}")
    
    
    # Répondre au client (facultatif)
    # server_socket.sendto(b'Hello from server', client_address)