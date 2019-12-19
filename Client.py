import socket

hote = "127.0.0.1"
port = 12800


connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion.connect((hote, port))
print("Connexion établie avec le serveur sur le port {}".format(port))


valeur1 = input()
valeur2 = input()
signe = input()

    # Peut planter si vous tapez des caractères spéciaux
valeur1 = valeur1.encode()
valeur2 = valeur2.encode()
signe = signe.encode()

    # On envoie le message
connexion.send(valeur1)
connexion.send(valeur2)
connexion.send(signe)

msg_recu = connexion.recv(1024)
print(msg_recu.decode()) # Là encore, peut planter s'il y a des accents

print("Fermeture de la connexion")
connexion.close()