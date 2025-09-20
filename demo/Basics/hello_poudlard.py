def hello(to):
    print(f"Hello, {to}")

def main():
    eleve_griffondor = ["Harry", "Ron", "Hermione"]
    eleve_serpentard = ["Draco", "Crabbe"]
    autres = ["Etienne"]

    for eleve in (eleve_griffondor + eleve_serpentard + autres):
        if eleve in eleve_griffondor:
            hello(eleve + " de griffondor")
        
        elif eleve in eleve_serpentard:
            hello(eleve + " de serpentard")

        else:
            hello(eleve + " sans maison")

main()
