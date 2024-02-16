from cryptography.fernet import Fernet #IMPORTA MÓDULO
chave = Fernet.generate_key() #GERA UMA CHAVE RANDÔMICA

file = open('chave.key', 'wb')
file.write(chave)
file.close()

print()
print("A CHAVE ABERTA É: ")
print(chave)
print()

file = open('chave.key', 'rb')
chave_lida = file.read()
file.close()

print()

print("A CHAVE LIDA É: ")
print(chave_lida)
print()
