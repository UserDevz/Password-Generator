# Criador: UserDevz
# Gerador de senhas fortes!
# modo de uso:
#    •python Password-Generator.py <numero de caracteres>

# importando as bibliotecas necessarias:
import random

# Definindo os caracteres para a senha:
letras = "abcdefghijklmnopqrstuvwxyz"
numero = "0123456789"
caracteres = "[]{};:*'+-&_$#@()?!"
letras_A = letras.upper()

# Tamanho da senha desejada:
tamanho = 16

# Gerando a senha:
geral = letras + numero + caracteres + letras_A
password = "".join(random.sample(geral, tamanho))

print(f'Senha gerada: {password}\n')
