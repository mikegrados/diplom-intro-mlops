* Ejecutar tests en el script y explicar detalles
    ```
    $ pytest test_mi_script.py -v 
    ```

* Ejecutar tests en el script y ocultar detalles
    ```
    $ pytest test_mi_script.py -q
    ```

* Ejecutar todos los tests dentro de una carpeta 
    ```
    $ pytest nombre_carpeta/
    ```

* Ejecutar un script test
    ```
    $ pytest nombre_carpeta/test_mi_script.py
    ```

* Ejecutar una sola funcion dentro de un script
    ```
    $ pytest nombre_carpeta/test_mi_script.py::test_tu_funcion
    ```

* Ejecutar una sola funcion dentro de un script con que tenga una marca
    ```
    $ pytest nombre_carpeta/test_mi_script.py -m mi_marca
    ```