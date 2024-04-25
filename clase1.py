class persona:
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def getNombre(self):
        return self.nombre
    def getedad(self):
        return self.edad
    def getdni(self):
        return self.dni


    def compara(self):
        if self.edad >= 18:
            return f"{self.nombre} es mayor de edad  "
        else:
            return "no es mayor de edad"\
            

compi = persona("edgar", 19, "30128923");
menor = persona("pedro", 17, "3923029")
print(compi.compara());
print(menor.compara());

class personas2:
    personas = []
    def __init__(self, lis):
        self.personas = lis

    def muestra(self):
        for persona in self.personas:
            if persona.compara():
                print(persona.getNombre())

gente = personas2([persona("kike", 19, "3230434"),persona("fifi", 28, "2489789")]);
gente.muestra();
