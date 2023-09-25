jmeno = 'Lucie'
jmeno = jmeno.lower()
email = f"{jmeno}@czechitas.cz"
print(email)

jmeno_a_prijmeni = input("Jak se jmenuješ? Napiš celé jméno: ")
print(jmeno_a_prijmeni)

print(jmeno_a_prijmeni.upper())
print(jmeno_a_prijmeni.lower())
print(jmeno_a_prijmeni.title())
print('. '.join(jmeno_a_prijmeni.split()[0][0].upper() + jmeno_a_prijmeni.split()[1][0]).upper() + '.')
if len(jmeno_a_prijmeni.split()[0]) > 5:
  print(jmeno_a_prijmeni.split()[0][0] + '. ' + jmeno_a_prijmeni.split()[1])
else: 
  print(jmeno_a_prijmeni.title())