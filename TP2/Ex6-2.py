def sequencia_comum(sequencia1, sequencia2, memoria):
    # encontrar parte da sequencia 1 dentro de sequencia 2
    for i in range(1, len(sequencia1) + 1):
        if sequencia1[:i].lower() in sequencia2.lower():
            memoria[sequencia1[:i]] = i

    # encontrar parte da sequencia 2 dentro de sequencia 1
    for j in range(1, len(sequencia2) + 1):
        if sequencia2[:j].lower() in sequencia1.lower():
            memoria[sequencia2[:j]] = j

    return max(memoria, key=memoria.get)

sequencia1 = "Capitu, apesar daqueles olhos, que o diabo lhe deu, para perder os homens, nao me meteu medo."
sequencia2 = "Narizinho, a menina do nariz arrebitado, vivia no Sitio do Picapau Amarelo com sua avo, Dona Benta."
sequencia = sequencia_comum(sequencia1, sequencia2, {})
print(f"Sequencia 1: {sequencia1}")
print(f"Sequencia 2: {sequencia2}")
print(f"A sequencia comum é \"{sequencia}\" com {len(sequencia)} letras")