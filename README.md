# edm-tool

En este repositorio podrá ejecutar los modelo propuestos en el paper “An Educational Data Mining Model based on Auto Machine Learning and Interpretable Machine Learning”.

Los mismo podrán ser ejecutados de dos maneras: a través de Google Colab o ejecutando un script de Python.

En el caso de optar por Google Colab deberá tener una cuenta de Gmail,  descargar el archivo Unvime2020y2021GitHub.ipynb y guardarlo dentro de la carpeta Colab Notebooks dentro del Drive. Realizar doble click sobre el archivo y se ejecutara el cuaderno dentro de Google Colab. Ejecute las celdas siguiendo los comentarios.

La segunda opción es ejecutando un script en Python, para el cual se deberá tener instalado los siguientes requerimientos mínimos.

Requerimientos mínimos:  (https://automl.github.io/auto-sklearn/master/installation.html)

- Linux operating system (for example Ubuntu) (get Linux here)
- Python (>=3.7) (get Python here),
- C++ compiler (with C++11 supports) (get GCC here).

In case you try to install Auto-sklearn on a system where no wheel files for the pyrfr package are provided (see here for available wheels) you also need:

SWIG (get SWIG here).

Ahora descargar del repositorio los siguientes archivos.

- unvimestatistics.py
- unvimestatistics&shap.py
- unvimestatistics&pi.py
- requeriments.txt

Abrir la consola o terminal de Ubuntu y colocar los siguientes comandos y posicionarse en la carpeta en donde se encuentran los archivos descargados.
```bash
sudo apt install python3-pip
pip install -r requirements1.txt
python3 unvimestatistics.py ( para ver las estadísticas como accuracy, recall , f1, etc..)
python3 unvimestatistics&shap.py ( para ver estadísticas y la interpreatbilidad local de los resultados con SHAP)
python3 unvimestatistics&pi.py ( para ver estadísticas y la interpreatbilidad global de los resultados con importance permutation)
```
