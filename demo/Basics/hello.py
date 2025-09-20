def main():

    # Forcer à indiquer deux noms
    stop = False
    while (not stop):
        name = input("Quel est votre prénom et nom ? ")

        # Normalisation du nom
        name = name.strip().title()

        # Séparation prénom / nom
        names = name.split(" ")

        # Si on a deux noms trouvés c'est bon
        if len(names) == 2:
            first_name = names[0]
            last_name = names[1]

            hello(f"M. or Mme. {last_name}")
            # On casse le while
            stop = True
        
        # Sinon on continue
        else:
            print("Veuillez indiquer votre prénom nom.")

def hello(to):
    print(f"Hello, {to}")

main()