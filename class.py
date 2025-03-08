
class Persona:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome
    
    def saluta(self):
        print("Ciao io sono" + " " + self.nome, self.cognome)

class Insegnante(Persona):
    def __init__(self, nome, cognome, materia):
        super().__init__(nome, cognome)
        self.materia = materia
    
    def saluta(self):
        print("buongiorno sono " + self.nome + " " + self.cognome)

    def dai_voto(self):
        print("voto 9")

perosona1 = Persona("Luca", "Rossi")

insegnante1 = Insegnante("Anna", "Neri", "matematica")

insegnante1.saluta()
insegnante1.dai_voto()