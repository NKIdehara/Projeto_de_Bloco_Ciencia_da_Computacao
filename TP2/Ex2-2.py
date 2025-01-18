class Estudante:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def __str__(self):
        return f"Nome: {self.nome}\tNota: {self.nota}"

def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    elemento_pivo = len(lista) // 2
    pivo = lista[elemento_pivo]
    sublista1 = []
    for i in lista:
        if i.nota < pivo.nota:
            sublista1.append(i)
    sublista2 = []
    for i in lista:
        if i.nota == pivo.nota:
            sublista2.append(i)
    sublista3 = []
    for i in lista:
        if i.nota > pivo.nota:
            sublista3.append(i)
    return quick_sort(sublista1) + sublista2 + quick_sort(sublista3)


notas = []
notas.append(Estudante("Alice Silva", 9.7))
notas.append(Estudante("Bruno Costa", 8.4))
notas.append(Estudante("Carlos Oliveira", 7.1))
notas.append(Estudante("Daniela Pereira", 5.8))
notas.append(Estudante("Eduardo Santos", 6.9))
notas.append(Estudante("Fernanda Lima", 8.1))
notas.append(Estudante("Gabriel Souza", 8.8))
notas.append(Estudante("Helena Almeida", 9.8))
notas.append(Estudante("Igor Fernandes", 7.7))
notas.append(Estudante("Juliana Rocha", 6.6))

print("Lista original")
for nota in notas:
    print(nota)

notas = quick_sort(notas)

print("\nLista ordenada")
for nota in notas:
    print(nota)
