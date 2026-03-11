def tallenna_lokikirjaan(teksti):
    with open("lokikirja.txt", "a", encoding="utf-8") as tiedosto:
        tiedosto.write(teksti + "\n")
        

print("Tervetuloa Muistioon! (kirjoita 'lopeta' sulkeaksesi)")

while True:
    syote = input("\nMitä haluat tallentaa?")

    if syote == "lopeta":
        print("Heippa")
        break

    tallenna_lokikirjaan(syote)
    print("\nTallennettu!")
 
    