user = str(input("Usuário: "))
msg = str(input("Digite a frase: "))
key = int(input("Digite a chave: "))
alfabet = ["A","a","B","b","C","c","D","d","E","e","F","f","G","g","H","h","I","i","J","j","K","k","L","l","M","m","N","n","O","o","P","p","Q","q","R","r","S","s","T","t","U","u","V","v","W","w","X","x","Y","y","Z","z"]
result = ""
result2 = ""

print(40*"---")

for character in msg:
    if character in alfabet:
         position = alfabet.index(character)
         position = (position + key) % 52
         result+= alfabet[position]
print("Texto criptografado: {}".format(result))

for character in result:
    if character in alfabet:
         position = alfabet.index(character)
         position = (position - key) % 52
         result2+=alfabet[position]
print("Texto descriptografado: {}".format(result2))        

