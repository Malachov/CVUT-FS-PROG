class Kotatko:
    def __init__(self, jmeno):
        self.jmeno = jmeno
    def barva(self, barva):
        self.barva=barva

    def zamnoukej(self):
        print(f"{self.jmeno}: Mňau!")

    def snez(self, jidlo):
        print(f"{self.jmeno}: Mňau mňau! {jidlo} mi chutná!")

mourek = Kotatko("mourek")
mourek.zamnoukej()

a=8