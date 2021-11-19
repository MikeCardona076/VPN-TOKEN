import random
import datetime
class Token_Vpn():

    def __init__(self, area, nombre, apellido_paterno):
        self.empresa = 'SC'
        self.area = area
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.identificador_unico = random.randint(1, 1000000)

    def certificado_vpn(self):
        return self.empresa + self.area + self.nombre + self.apellido_paterno + str(self.identificador_unico) + 'CERT'

    def key_vpn(self):
        return self.empresa + self.area + self.nombre + self.apellido_paterno + str(self.identificador_unico) + 'KEY'




def main():
    try:
        area = input('Ingrese el area: ')
        nombre = input('Ingrese el nombre: ')
        apellido_paterno = input('Ingrese el apellido paterno: ')
        token = Token_Vpn(area, nombre, apellido_paterno)
        txt = open(f'Tokens\{nombre}_Token.txt', 'a')
        txt.write(token.certificado_vpn() + '\n')
        txt.write(token.key_vpn() + '\n')
        txt.write('Creado el ' + str(datetime.datetime.now())) 
        txt.close()
        print('Se ha creado el archivo con el token')
    except Exception as e:
        print(e)
        print('Error al crear el archivo')




if __name__ == '__main__':
    main()

