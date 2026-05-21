class RegistroNotas:

    def __init__(self):
        self.notas = []

    def registrar_nota(self, materia, nota, semestre):
        if nota < 0.0 or nota > 5.0:
            raise ValueError("La nota debe estar entre 0.0 y 5.0")
        for n in self.notas:
            if n["materia"] == materia and n["semestre"] == semestre:
                raise ValueError("Ya existe una nota para esta materia en este semestre")
        self.notas.append({
            "materia": materia,
            "nota": nota,
            "semestre": semestre
        })

    def aprobar(self, materia, semestre):
        for n in self.notas:
            if n["materia"] == materia and n["semestre"] == semestre:
                return n["nota"] >= 3.0
        return False

    def calcular_promedio(self):
        if not self.notas:
            return 0.0
        return sum(n["nota"] for n in self.notas) / len(self.notas)