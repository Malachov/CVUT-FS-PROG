class Kotatko:
    def __init__(self, jmeno):
        self.jmeno = jmeno
    def barva(self, barva):
        self.barva=barva

    def povaha(self, povaha):
        self.povaha = povaha
    def zamnoukej(self):
        print(f"{self.jmeno}: Mňau!")

    def snez(self, jidlo):
        print(f"{self.jmeno}: Mňau mňau! {jidlo} mi chutná!")

mourek = Kotatko("mourek")

mourek.barva("cerna")

mourek.josef="barva"

setattr(mourek, mourek.josef, "oranzova")

mourek.zamnoukej()

print('1 + 2', end=' ')     # Místo přechodu na nový řádek jen napiš mezeru
print('=', end=' ')
print(1 + 2, end='!')
print()

a=8