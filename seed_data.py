from ejemplo.models import Familiar, Mascota, Automovil

Familiar(nombre="Carlos", direccion="Cordoba 885", numero_pasaporte=123123).save()
Familiar(nombre="Alberto", direccion="Monteagudo 780", numero_pasaporte=890890).save()
Familiar(nombre="Eugenia", direccion="Hernandarias 1098", numero_pasaporte=345345).save()
Familiar(nombre="Yvonne", direccion="Julian Alvarez 585", numero_pasaporte=567567).save()
print("Se cargo con éxito los usuarios de pruebas")

Mascota(propietario="Carlos", nombre="Toto", raza="Dalmata",edad=2).save()

Automovil(propietario="Alberto",marca="Toyota",color="Azul",patente="AA111").save()