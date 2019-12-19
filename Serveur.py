import socket

hote = "127.0.0.1"
port = 12800

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((hote, port))
connexion_principale.listen(5)
print("Le serveur écoute à présent sur le port {}".format(port))

connexion_avec_client, infos_connexion = connexion_principale.accept()


msg_recu = int(connexion_avec_client.recv(1024).decode())
msg_recu2 = int(connexion_avec_client.recv(1024).decode())
msg_recu3 = connexion_avec_client.recv(1024).decode()

resultat = ""

if msg_recu3 == "+" :
    resultat = msg_recu + msg_recu2
    print(resultat)
    connexion_avec_client.send(str(resultat).encode())
    print(addition(msg_recu, msg_recu2))
elif msg_recu3 == "*" :
    resultat = msg_recu * msg_recu2
    print(resultat)
    connexion_avec_client.send(str(resultat).encode())
    print(multiplication(msg_recu, msg_recu2))
elif msg_recu3 == "-" :
    resultat = msg_recu - msg_recu2
    print(resultat)
    connexion_avec_client.send(str(resultat).encode())
    print(soustraction(msg_recu, msg_recu2))
else :
    resultat = msg_recu / msg_recu2
    print(resultat)
    connexion_avec_client.send(str(resultat.encode()))
    print(division(msg_recu, msg_recu2))

    # L'instruction ci-dessous peut lever une exception si le message
    # Réceptionné comporte des accents
    print(msg_recu.decode())
    connexion_avec_client.send(b"5 / 5")

print("Fermeture de la connexion")
connexion_avec_client.close()
connexion_principale.close()