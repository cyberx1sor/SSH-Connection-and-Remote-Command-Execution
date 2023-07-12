import paramiko
import logging

logging.basicConfig(level=logging.INFO)  # Configuración básica de registro

class SSHConnection:
    def __init__(self, host, puerto, usuario, clave_privada):
        self.host = host
        self.puerto = puerto
        self.usuario = usuario
        self.clave_privada = clave_privada
        self.ssh_client = None

    def conectar(self):
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            self.ssh_client.connect(
                hostname=self.host,
                port=self.puerto,
                username=self.usuario,
                key_filename=self.clave_privada,
                timeout=10
            )
            logging.info(f'Conexión SSH establecida con {self.host}:{self.puerto}')

        except paramiko.AuthenticationException:
            logging.error(f'Error de autenticación en {self.host}')
            raise
        except paramiko.SSHException as e:
            logging.error(f'Error en la conexión SSH con {self.host}: {e}')
            raise
        except Exception as e:
            logging.error(f'Error desconocido en la conexión SSH con {self.host}: {e}')
            raise

    def desconectar(self):
        if self.ssh_client is not None:
            self.ssh_client.close()
            logging.info(f'Conexión SSH cerrada con {self.host}:{self.puerto}')

    def ejecutar_comando(self, comando):
        try:
            _, stdout, stderr = self.ssh_client.exec_command(comando, timeout=10)
            resultado = stdout.read().decode()
            errores = stderr.read().decode()

            if errores:
                logging.error(f'Error al ejecutar el comando en {self.host}: {errores}')

            return resultado

        except paramiko.SSHException as e:
            logging.error(f'Error al ejecutar el comando en {self.host}: {e}')
            raise
        except Exception as e:
            logging.error(f'Error desconocido al ejecutar el comando en {self.host}: {e}')
            raise

# Ejemplo de uso
hosts_remotos = [
    {
        'host': 'ejemplo1.com',
        'puerto': 22,
        'usuario': 'usuario1',
        'clave_privada': '/ruta/a/clave_privada1.pem',
        'comandos': ['ls -l', 'whoami']
    },
    {
        'host': 'ejemplo2.com',
        'puerto': 22,
        'usuario': 'usuario2',
        'clave_privada': '/ruta/a/clave_privada2.pem',
        'comandos': ['df -h', 'uptime']
    }
]

for host_info in hosts_remotos:
    try:
        conexion_ssh = SSHConnection(
            host=host_info['host'],
            puerto=host_info['puerto'],
            usuario=host_info['usuario'],
            clave_privada=host_info['clave_privada']
        )
        conexion_ssh.conectar()

        for comando in host_info['comandos']:
            resultado_comando = conexion_ssh.ejecutar_comando(comando)
            logging.info(f'Resultado del comando en {conexion_ssh.host}: {resultado_comando}')

    except Exception as e:
        logging.error(f'Error en la conexión SSH con {host_info["host"]}: {e}')

    finally:
        if conexion_ssh is not None:
            conexion_ssh.desconectar()
