import hashlib

string_to_encrypt = ""
while string_to_encrypt != "0":
    string_to_encrypt = input("Digite uma string para criptografar ou 0 para sair: ")
    if string_to_encrypt != "0":
        hashObj = hashlib.sha1(string_to_encrypt.encode()).hexdigest()
        print("\n" + hashObj + "\n")
