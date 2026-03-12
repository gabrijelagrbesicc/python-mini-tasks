lozinka = "python123"

unos = input("Unesi lozinku: ")

while unos != lozinka:
    print("Lozinka nije tocna. Pokusaj opet!")
    unos = input("Unesi lozinku ")

print("Uspjesna prijava")