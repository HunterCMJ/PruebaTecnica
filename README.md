Prueba Técnica: Mini-Proyecto de Pipeline de Datos de CARLOS MAQUEDA JIMENEZ

# Primera Parte: GitHub

- Tienes que crear una cuenta de GitHub si no la tienes. Es gratuito, así que no debería de haber problema.
- Crea un repositorio nuevo. Tiene que ser público para que lo podamos revisar (nos tendrás que pasar el enlace al repo).
- A partir de ahora deberás hacer los ejercicios a continuación. Cada apartado numerado debería de ser un único commit (el mensaje que pongas en cada uno es libre, pero como sugerencia puedes poner el nombre del ejercicio y el número del apartado), pero puedes hacer tantos commits como necesites.

# Segunda Parte: Python + GCP + BQ

- Tienes que crear un script de Python que se conecte a una API y se descargue los datos (con 100 registros más que suficiente).

Tiene que haber una clase para descargar de la API y otra para subirla a BigQuery. Haz un commit con esta parte y súbelo al repositorio como "parte2" (puedes hacer los commits que quieras pero indicando cada parte)

- Los resultados de la conexión a la API los tienes que cargar en un DATASET que te crees en Bigquery.
  - El Dataset que reciba los datos de la API debe seguir esta nomenclatura: SANDBOX\_&lt;nombre de tu aplicación&gt;

Para esta parte, cuando lo tengas, puedes adjuntar captura de pantalla y subir el fichero que genera la tabla al repositorio.

- Vas a transformar los datos del sandbox. Dentro del repositorio, debe haber una carpeta sql/ con al menos un archivo:
- **transform.sql**: Este archivo debe contener una única consulta SQL que:
  - Lea los datos de la tabla almacenada en SANDBOX\_&lt;nombre de tu aplicación&gt;
  - Realice alguna transformación simple. Por ejemplo: eliminar posibles duplicados del día, añadir una columna con la fecha en que se ejecuta la transformación…
  - Inserte el resultado transformado en la tabla INTEGRATION.integration_prueba_tecnica.
  - **Requisito clave:** La consulta debe ser **idempotente**. Es decir, si se ejecuta varias veces sobre los mismos datos crudos del día, el resultado en la tabla final debe ser el mismo (no debe generar duplicados).

_Puntos a tener en cuenta:_

- _GCP te va a pedir siempre una tarjeta para poder darte de alta. Forma parte de la verificación. No harán ningún cargo pues es todo libre de coste._
- _Autenticación del Script: El script de Python necesita credenciales para poder interactuar con BigQuery. El método estándar es: Crear una Cuenta de Servicio (Service Account). Asignarle los roles de IAM necesarios (ej. Editor de datos de BigQuery y Usuario de trabajos de BigQuery). Descargar la clave de la cuenta de servicio en formato JSON. Configurar la variable de entorno GOOGLE_APPLICATION_CREDENTIALS para que apunte a la ruta de ese archivo JSON._

# Tercera Parte: Airflow

Para esta prueba vas a necesitar tener el módulo Airflow instalado en local o en una máquina de docker para poder lanzarlo.

- 1. Define un DAG llamado **test** que se ejecuta cada día a las 3:00 UTC, con los siguientes argumentos por defecto:

from datetime import datetime, timedelta 

default_args = {
'owner': 'airflow', 
'depends_on_past': False, 
'start_date': datetime(1900, 1, 1),
'retries': 1,
'retry_delay': timedelta(seconds=5)
}

- 2. Incluye las tareas **start** y **end** como **DummyOperator** y que end vaya detrás de start en el DAG.
  - Define una lista de tareas dummy **task_n** con **N** tareas, donde cada tarea con **n**

par dependa de todas las tareas impares.

- 3. Define un nuevo operador **TimeDiff** que parta del **BaseOperator,** que reciba una fecha (**diff_date)** como entrada y muestre la diferencia con la actual. Crea una tarea nueva con el operador.
  - ¿Qué es un Hook? ¿En qué se diferencia de una conexión? Puedes responder en un comentario dentro del código.



Entorno virtual gesiotnado por UV. 
pip install uv 

