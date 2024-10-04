import socket
import struct

# Créer un socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)

# Associer le socket à une adresse IP et un port
server_socket.bind(('0.0.0.0', 666)) 

print("Serveur UDP en écoute sur le port 666...")

#https://docs.simplebackups.com/help-tips--troubleshooting/mQyMDHYQcVeYgoW6VN65u8/how-to-generate-an-rsa-pem-asymmetric-key-pair/bcnQXAqtpBMQSd28UTUEmA


while True:
    packet, addressClient = server_socket.recvfrom(65565)

    ''' ENTETE IP
    ! : Ordre des octets "network" (big-endian).
    B : Un octet (version et longueur de l'en-tête).
    B : Un octet (type de service).
    H : Un entier sur 2 octets (longueur totale).
    H : Un entier sur 2 octets (identification).
    H : Un entier sur 2 octets (drapeaux et décalage de fragment).
    B : Un octet (TTL).
    B : Un octet (protocole).
    H : Un entier sur 2 octets (checksum).
    4s : Adresse IP source (4 octets).
    4s : Adresse IP destination (4 octets).

    https://en.wikipedia.org/wiki/IPv4#/media/File:IPv4_Packet-en.svg
    + voir image

    '''

    # L'en-tête IP est de 20 octets pour IPv4 lorsqu'il n'y a pas d'option
    RAW_ip_header = packet[:20]

    # Déstructuration de l'en-tête IP
    CLEAN_ip_header = struct.unpack('!BBHHHBBH4s4s', RAW_ip_header)

    #Longueur total
    total_length = CLEAN_ip_header[2]
    
    # Extraction des adresses IP source et destination
    src_ip = socket.inet_ntoa(CLEAN_ip_header[8])
    dest_ip = socket.inet_ntoa(CLEAN_ip_header[9])


    ''' ENTETE IP
    ! : Ordre des octets "network" (big-endian).
    H : Un entier sur 2 octets (Port source)
    H : Un entier sur 2 octets (Port destination)
    H : Un entier sur 2 octets (Longueur UDP, Longueur du segment UDP (en-tête UDP + données UDP).)
    H : Un entier sur 2 octets (Checksum UDP)

    https://fr.wikipedia.org/wiki/User_Datagram_Protocol
    + voir image

    '''

    RAW_udp_header = packet[20:28]
    
    CLEAN_udp_header = struct.unpack('!HHHH', RAW_udp_header)

    src_port = CLEAN_udp_header[0]
    dest_port = CLEAN_udp_header[1]

    print(f'Adresse IP source : {src_ip}:{src_port}, Adresse IP destination : {dest_ip}:{dest_port} pour une longueur : {total_length}')
    print(f'payload : {packet[28:65565].decode()}')