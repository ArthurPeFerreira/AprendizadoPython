# Comando para escrever na tela
print("Hello World!") 

#Recebe oque chamamos de argumento, que é basicamente: print(Argumento)
print(12,34)

#Pode-se utilizar o comando sep="Argumento" para colocar um separador
print(56, 78, sep="-")

#Pode-se utilizar o comando end='Argumento' para dizer oque vai acontecer no final da linha
# \n => Quebra de Linha (LF)
# \r => Coloca o Inicio da Escrita no começo da linha (CR) Explicação => (https://www.youtube.com/watch?v=76qBuowccfg)
#Este é o padrão (CRLF):
print(910, 1112, sep="-",end='\n\r')

#Exemplos:
print(1314, 1516, sep="-",end='##\n')
print(1718, 1920, sep="-",end='\n##')

#Neste Exemplo o \r fez o World! soprepor o Hello pois a escrita foi pro começo da linha
print("\nHello \rWorld!")





