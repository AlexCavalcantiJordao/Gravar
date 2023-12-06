arquivo = open('arqText.txt', 'w')

arquivo.write("Curso em Python \n")
arquivo.write("Aula Prática")
arquivo.close()

# Leitura do arquivo texto

leitura = open("arqText.txt", "r")
print(leitura.read())
leitura.close()