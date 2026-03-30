def check_password(password):
    on_numero = any(m.isdigit() for m in password)
    on_iso = any(m.isupper() for m in password)

    if len(password) < 6:
        return "Heikko"
    if len(password) >= 10 and on_numero and on_iso:
        return "Vahva"
    else: 
        return "Kohtalainen"



print("--- Tehtävä 1 ---")
print(check_password("abc"))          # → heikko
print(check_password("salasana"))     # → kohtalainen
print(check_password("Salasana12"))   # → vahva