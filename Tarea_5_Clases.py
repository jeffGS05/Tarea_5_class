# Tarea
# Basado en el ejemplo anterior, crear un Nieto Humano, basado en las habilidades aprendidas por el abuelo humano y transmitidas al padre Humano.
# Abuelo -> padre -> Nieto
# El abuelo trabaja. El padre es contador y el nieto es analista de negocios
# El nieto tiene que ir a trabajar, sabe de contabilidad es un analista de negocios#

class Abuelo():
    def __init__(self,nombre,esposa,hijos,trabajo):
        self.nombre=nombre
        self.esposa=esposa
        self.hijos=hijos
        self.trabajo=trabajo
    def persona(self):
        print('nombre', self.nombre, 'su esposa se llama ', self.esposa, 'y tienen ', self.hijos, 'hijos , trabajo como ', self.trabajo)

class Padre(Abuelo):
    def __init__(self,n_padre,n_esposa,n_hijos,estudio,n_profesion,n_trabaja):
        super().__init__(n_padre,n_esposa,n_hijos,n_trabaja)
        self.estudio=estudio
        self.n_profesion=n_profesion
    def hijo(self):
        super().persona()
        print('estudio ', self.estudio)

class Nieto(Padre):
    pass

abuelo=Abuelo('Lenin ', 'Marta ', 4, 'panadero')
abuelo.persona()
papa=Padre('Emiliano es hijo de '+abuelo.nombre, 'Sofia', 2, 'administracion','contador','contador')
papa.hijo()
nieto=Nieto('Ernesto es hijo de ' +papa.nombre +'y nieto de '+abuelo.nombre, 'Frida', 0, 'negocios', 'analista de negocios', 'analista de BI')
nieto.hijo()
















