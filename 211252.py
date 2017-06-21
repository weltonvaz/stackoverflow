nome = "nomedahora"
cpf = "1421241"
departamento = "bsi"
dicProfessor = {nome: {"nome":nome, "cpf":cpf, "departamento":departamento}}
listaProfessores = []
listaProfessores.append(dicProfessor)

for item in listaProfessores:
    print(item[nome])

dicProfessor.clear()