# Precondiciones
Se asume que ya tiene Python 3+ instalado en su sistema. Si no, por favor, instalelo.  

Revisar este link acorde a su sistema operativo: 
[Python 3 Installation & Setup Guide](https://realpython.com/installing-python/)

# Instalación de ambiente virtual
Abra una terminal, y dirijase a la carpeta raiz del proyecto, e instale `venv` con el siguiente comando.

```
$ pip3 install virtualenv
```
Despues, ejecute los siguientes comandos para crear el entorno virtual.
```
$ python3 -m venv ./venv
```
Active el entorno virtual.
```
$ source env/bin/activate
```

**Nota**: Desactive el entorno virtual usando este comando al terminar su practica.
```
$ deactivate
```

# Instalacion de bibliotecas
Para instalar las bibliotecas necesarias, use este comando:
```
pip3 install -r requirements.txt
```

¡Listo, la configuración está lista para las pruebas!

## Probando el codigo
Cambie de directorio y ejecute el siguiente comando de la siguiente forma
```
cd sesion-3/app
python ejemplo.py
```
Deberia ver la siguiente salida de datos
```
1.5
0.5
2.0
0.5
```


## Ejecutar pruebas unitarias y de integracion
* Pruebas unitarias
```
pytest tests/unit/ -v
```

* Pruebas de integracion
```
pytest tests/integration/ -v
```