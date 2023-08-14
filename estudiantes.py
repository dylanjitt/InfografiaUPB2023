estudiantes = [
    {
        "nombre completo": "juan perez",
        "edad": 16,
        "notas":{
            "MAT":70,
            "FIS":80,
            "QMC":90,
            "LAB":60
        },
        "asistencia":85
    },
    {
        "nombre completo": "ana luisa",
        "edad": 17,
        "notas":{
            "MAT":40,
            "FIS":50,
            "QMC":60,
            "LAB":100
        },
        "asistencia":85
    }
]

def promedioEstudiante(estudiante:dict)->float:
    total=sum(estudiante["notas"].values())
#    for nota in estudiante["notas"].values():
#        total+=nota
    promedio=total/len(estudiante["notas"])
    return promedio
    



def promedioCurso(listaEstudiantes:list)->float:
    accum=sum([promedioEstudiante(est)for est in listaEstudiantes])
#    accum=0
#    for estudiante in listaEstudiantes:
#        accum += promedioEstudiante(estudiante)
    return accum /len(listaEstudiantes)
    
print(promedioEstudiante(estudiantes[0]))

print(promedioCurso(estudiantes))
