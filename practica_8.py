from suds.client import Client

# url = 'http://localhost:7000/ws/EstudianteWebServices'
url = 'http://localhost:7000/ws/EstudianteWebServices?wsdl'

client = Client(url)

# print(client)

# Crear estudiantes
client.service.crearEstudiante(20158711, 'Papolo', 'MED')
client.service.crearEstudiante(20143220, 'Alan', 'EST')

print("\nLista de estudiantes:")
estudiantes = client.service.getListaEstudiantes()
for estudiante in estudiantes:
    print('Matrícula: ' + str(estudiante['matricula']) + ' Nombre: ' + estudiante['nombre'] + ' Carrera: ' + estudiante['carrera'])

print("\nConsultar un estudiante con matrícula 20143220:")
estudiante = client.service.getEstudiante(20143220)
print('Matrícula: ' + str(estudiante['matricula']) + ' Nombre: ' + estudiante['nombre'] + ' Carrera: ' + estudiante['carrera'])

print("\nEstudiante con matrícula 20143220 borrado")
client.service.borrarEstudiante(20143220)

print("\nLista de estudiantes restantes:")
estudiantes = client.service.getListaEstudiantes()
for estudiante in estudiantes:
    print('Matrícula: ' + str(estudiante['matricula']) + ' Nombre: ' + estudiante['nombre'] + ' Carrera: ' + estudiante['carrera'])