# SSH-Connection-and-Remote-Command-Execution

Este programa en Python permite establecer conexiones SSH y ejecutar comandos en servidores remotos de manera fácil y segura. Utiliza la biblioteca paramiko para gestionar la conexión SSH y proporciona una interfaz sencilla para ejecutar comandos en los hosts remotos.

## Características

* Establece conexiones SSH seguras con servidores remotos.

* Permite ejecutar comandos en los servidores remotos y obtener los resultados.

* Manejo de errores detallado para una mejor depuración y control.

* Implementa gestión de conexiones reutilizables para una mayor eficiencia.

## Requisitos

* Python 3.6 o superior.
* La biblioteca paramiko instalada. Puedes instalarla usando pip install paramiko.

## Uso

1. Clona el repositorio o descarga los archivos en tu máquina local.
2. Importa la clase SSHConnection en tu script de Python.
3. Crea una instancia de SSHConnection proporcionando los detalles del host remoto, como el nombre de host, el puerto, el nombre de usuario y la clave privada.
4. Utiliza el método conectar() para establecer la conexión SSH con el host remoto.
5. Ejecuta los comandos remotos utilizando el método ejecutar_comando().
6. Utiliza el método desconectar() para cerrar la conexión SSH cuando hayas terminado.

## Contribuciones

Las contribuciones son bienvenidas. Si encuentras algún problema o tienes alguna sugerencia de mejora, por favor, abre un issue o envía una pull request.
