estudiantes = [
    {
        'nombre': 'juan',
        'apellido': 'perez',
        'notas': {
            'MAT': 30,
            'QMC': 30,
            'FIS': 30,
            'LAB': 30
        },
        'extras': [2, 3, 1, 1, 1],
        'asistencia': 90
    },
    {
        'nombre': 'ana',
        'apellido': 'rivera',
        'notas': {
            'MAT': 98,
            'QMC': 98,
            'FIS': 98,
            'LAB': 98
        },
        'extras': [1],
        'asistencia': 100
    }
]

import csv
class Evaluador:
    """Esta clase implementa diversas funciones para calcular promedios
    de una lista de estudiantes y obtener otros datos adicionales, ademas,
    tambien implementa una funcion para escribir un reporte de notas"""
    def __init__(self, lista_estudiantes, min_asistencia, max_extras):
        self.lista_estudiantes = lista_estudiantes
        self.min_asistencia = min_asistencia
        self.max_extras = max_extras

    def calcular_promedios(self):
        # IMPLEMENTAR METODO
        lista_notas = []
        estudList=self.lista_estudiantes
        promedio=0

        for estudiantes in estudList:
            nombre=estudiantes["nombre"].capitalize()
            apellido=estudiantes["apellido"].capitalize()
            nombComp=nombre+" "+apellido
            print(nombComp)
            if sum(estudiantes["notas"].values()) !=0:
                total=sum(estudiantes["notas"].values())
                promedio=total/len(estudiantes["notas"])
            print(promedio)
        
            if estudiantes["asistencia"]< self.min_asistencia:
                asistencia=0
            else:
                asistencia=estudiantes["asistencia"]
            print(asistencia)

            if len(estudiantes["extras"])!=0:
                totalExtra=sum(estudiantes["extras"])
                pro=promedio
                pro+=totalExtra
                if pro > 100:
                    promedio=100
                else:
                    promedio=pro
            print(promedio)
            lista_notas.append({"nombre completo":nombComp,"promedio":promedio})
            print(lista_notas)
        return lista_notas

    def obtener_mejor_estudiante(self):
        promedios=self.calcular_promedios()
        mejorEstudiante = max(promedios,key=lambda x: x["promedio"])
        return {'nombre completo': mejorEstudiante["nombre completo"], 'promedio': mejorEstudiante["promedio"]}

    def salvar_datos(self, nombre_archivo):
        with open(nombre_archivo,mode='w',newline="")as csvfile:
            casillas=["Nombre Completo","Asistencia","MAT","FIS","QMC","LAB","Total Extras","Promedio Final","Observacion"] 
            writer=csv.DictWriter(csvfile,fieldnames=casillas)
            writer.writeheader()

            for estudiante in self.lista_estudiantes:
                nombcomp=estudiante["nombre"].capitalize()+" "+estudiante["apellido"].capitalize()
                asistencia=estudiante["asistencia"]
                mat=estudiante["notas"]["MAT"] 
                fis=estudiante["notas"]["FIS"] 
                qmc=estudiante["notas"]["QMC"] 
                lab=estudiante["notas"]["LAB"]
                extras=sum(estudiante["extras"])
                promedioFinal=(sum(estudiante["notas"].values()))/len(estudiante["notas"])
                if promedioFinal>50:
                    observacion="APROBADO"
                else:
                    observacion="REPROBADO"
                
                writer.writerow({
                    "Nombre Completo":nombcomp,
                    "Asistencia":asistencia,
                    "MAT":mat,
                    "FIS":fis,
                    "QMC":qmc,
                    "LAB":lab,
                    "Total Extras":extras,
                    "Promedio Final":promedioFinal,
                    "Observacion":observacion
                })
        # IMPLEMENTAR METODO
        print('salvando datos')


# -----------------------------------------#
# ----> NO MODIFICAR DESDE AQUI! <---------#
# -----------------------------------------#
def comparar_archivo_notas(archivo):
    with open('ejemplo_notas.csv', 'r') as archivo_correcto:
        correcto_str = archivo_correcto.read()

    with open(archivo, 'r') as archivo:
        archivo_str = archivo.read()

    return correcto_str == archivo_str


if __name__ == '__main__':
    # datos iniciales
    nombre_archivo = 'notas.csv'
    notas_correcto = [{'nombre completo': 'Juan Perez', 'promedio': 35.0}, {'nombre completo': 'Ana Rivera', 'promedio': 99.0}]
    mejor_correcto = {'nombre completo': 'Ana Rivera', 'promedio': 99.0}

    # Instanciar evaluador
    evaluador = Evaluador(lista_estudiantes=estudiantes, min_asistencia=80, max_extras=5)
    # calcular promedios
    notas = evaluador.calcular_promedios()
    print(f'calcular_promedios: {notas}')
    if notas == notas_correcto:
        print('Calculo de promedios correcto!')
    else:
        print(f'ERROR, lista de promedios esperada: {notas_correcto}')
    # obtener mejor estudiante
    mejor = evaluador.obtener_mejor_estudiante()
    print(f'obtener_mejor_estudiante: {mejor}')
    if mejor == mejor_correcto:
        print('Mejor estudiante correcto!')
    else:
        print(f'ERROR, mejor estudiante esperado: {mejor_correcto}')
    # salvar datos en archivo
    evaluador.salvar_datos(nombre_archivo)
    if comparar_archivo_notas(nombre_archivo):
        print('Generacion de archivo correcta')
    else:
        print('Generacion de archivos incorrecta, ver archivo "ejemplo_notas.csv"')