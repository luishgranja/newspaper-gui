
# Proyecto Complejidad y Optimización

##### Desarrollo de una interfaz grafica para solucionar la generalización del problema descrito a continuación.
---

*El jefe de edición tiene que preparar el resumen de su periódico, que tiene 10 páginas. Tiene artı́culos organizados en varios temas: noticias internacionales, nacionales, locales, deportes y cultura. Estima que cada página dedicada a un tema dado puede interesar en promedio a cierto número de lectores. El editor debe elegir los temas que se tratarán junto con el número de páginas para atraer el número máximo de lectores. Si decide incluir un tema determinado, debe tener en cuenta un número mı́nimo/máximo de páginas. La Figura 1 muestra los rangos de páginas junto con el número promedio de lectores interesados en cada tema.*

| Tema             | # min pag | # max pag | lectores potenciales (x pag) |
|------------------|-----------|-----------|------------------------------|
| Internacional    | 5         | 9         | 1500                         |
| Nacional         | 4         | 7         | 2000                         |
| Noticias locales | 2         | 5         | 1000                         |
| Deporte          | 2         | 4         | 1500                         |
| Cultura          | 1         | 3         | 750                          |
---
# Requirements

[![python version](https://img.shields.io/badge/python-3.6.8-blue.svg)](https://www.python.org/downloads/release/python-350/) [![minizinc](https://img.shields.io/badge/minizinc-2.3.1-green.svg)](https://www.minizinc.org/) [![tkinter](https://img.shields.io/badge/tkinter-2.3.1-blueviolet.svg)](https://docs.python.org/3.6/library/tkinter.html)

# Install packages
## Install python3.6
`$ apt-get install python3.6 -y`
## Install Tkinter for python3
`$ apt-get install python3-tk`
## Download minizinc from [here](https://www.minizinc.org/software.html)

# Config
### Add minizinc to your path

`$ nano ~/.bashrc`

Add this `PATH=$PATH:/yourpath/MiniZincIDE-2.3.0-bundle-linux/bin` to the bashrc file

`$ source ~/.bashrc`

##### or

`$ echo "PATH=$PATH:/yourpath/MiniZincIDE-2.3.0-bundle-linux/bin" >> ~/.bashrc`

`$ source ~/.bashrc`

# Run
`$ python3 main.py`

