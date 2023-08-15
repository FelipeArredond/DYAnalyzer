# DYAnalyzer

## Como ejecutar el proyecto?

1. Clonar el repositorio

```bash
git clone https://github.com/FelipeArredond/DYAnalyzer.git
```

1. Acceder a la carpeta del proyecto clonado, crear el venv y activarlo

```bash
cd DYAnalyzer
python3 -m venv venv
source venv/bin/activate
```

1. Una vez activado el venv instalamos las dependencias

```bash
pip install -r requirements.txt
```

1. Iniciar el servidor de la app

```bash
python3 manage.py runserver
```

## Funcionamiento

Acceder a la url [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

Alli encontraremos la ventana inicial ⇒ 

![dyhome.png](DYAnalyzerDOC/dyhome.png)

En la esquina superior izquierda iremos a “ Upload File ” para cargar el archivo que deseemos realizar el analisis

![nav.png](DYAnalyzerDOC/nav.png)

Seleccionaremos un archivo y lo cargaremos con el boton upload

![upload.png](DYAnalyzerDOC/upload.png)

Cuando cargamos el archivo deberiamos de poder ver el nombre del archivo

![uploaded.png](DYAnalyzerDOC/uploaded.png)

Cuando presionamos en upload deberiamos poder ver el siguiente mensaje

![readytoscan.png](DYAnalyzerDOC/readytoscan.png)

Cuano presionamos el boton “ Scan File ” el backend de la app empezara a realizar el analisis, veremos que el navegador empezara a cargar, esto significa que se esta procesando la peticion

![scanning.png](DYAnalyzerDOC/scanning.png)

Al finalizar el escaneo podremos ver el output del analisis por pantalla

![result.png](DYAnalyzerDOC/result.png)