score = int(input("Note de l'élève: "))

if (score > 100) | (score < 0):
    print("Le score indiqué n'est pas possible")

else:
    if (score <= 100) & (score >= 90):
        print("Score A")

    elif (score < 90) and (score >= 80):
        print("Score B")

    elif (score < 80) and (score >= 70):
        print("Score C")

    else:
        print("Score D")
