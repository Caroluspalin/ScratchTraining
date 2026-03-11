import requests

def hae_numero_fakta(numero):
    url = f"http://numbersapi.com/{numero}?json"
    
    try:
        vastaus = requests.get(url)
        data = vastaus.json()
        return data["text"]
    except:
        return None


def tulosta_raportti(numero):
    fakta = hae_numero_fakta(numero)

    if fakta != None:
        return f"Faktasi on: {fakta}"
    else:
        return f"Numerolla {numero} ei löytynyt faktaa tai syötit kirjaimia."



print("Tervetuloa Fakta-automaattiin! (Kirjoita 'lopeta' sammuttaaksesi)")

while True:
    
    syote = input("\nSyötä numero: ").strip()
    
    
    if syote.lower() == "lopeta":
        print("Heippa!")
        break
        

    raportti = tulosta_raportti(syote)
    print(raportti)