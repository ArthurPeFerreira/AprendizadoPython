#Converter tipos de dados (str, float, int, bool)

#String
print("Conversão String para outros tipos:")
#Conversão String para Int
print("1", type("1"), int("1"), type(int("1")))
print(int("1") + 1)

#Conversão String para Float
print("1.1", type("1.1"), float("1.1"), type(float("1.1")))
print(float("1.1") + 1.1)

#Conversão String para Bool
print("True", type("True"), bool("True"), type(bool("True")))
print(bool("True") & True)

#Float
print("\nConversão Float para outros tipos:")
#Conversão Float para Int
print(1.0, type(1.0), int(1.0), type(int(1.0)))
print(int(1.0) + 1)

#Conversão Float para String
print(1.1, type(1.1), str(1.1), type(str(1.1)))
print("O número é: " + str(1.1))

#Conversão Float para Bool
print(1.0, type(1.0), bool(1.0), type(bool(1.0)))
print(0.0, type(0.0), bool(0.0), type(bool(0.0)))
print(bool(1.0) & True)

#Int
print("\nConversão Int para outros tipos:")
#Conversão Int para Float
print(1, type(1), float(1), type(float(1)))
print(float(1) + 1.1)

#Conversão Int para String
print(1, type(1), str(1), type(str(1)))
print("O número é: " + str(1))

#Conversão Int para Bool
print(1, type(1), bool(1), type(bool(1)))
print(0, type(0), bool(0), type(bool(0)))
print(bool(1) & True)

#Bool
print("\nConversão Bool para outros tipos:")
#Conversão Bool para Float
print(True, type(True), float(True), type(float(True)))
print(float(True) + 1.1)

#Conversão Bool para String
print(True, type(True), str(True), type(str(True)))
print("O estado é: " + str(True))

#Conversão Bool para Int
print(True, type(True), int(True), type(int(True)))
print(False, type(False), int(False), type(int(False)))
print(int(True) + 1)