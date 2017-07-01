# Praxiseinstieg Deeo Learning  
Dieses Repository soll ein Praxiseinstieg in die Arbeit mit TensorFlow sein. 
Es enhält alle Quellcodes zu den Beispielen meines Buchs für O'Reilly 
Praxiseinstieg Deep Learning.

## Installation

Um die Beispiele nutzen zu können, muss zu erst [Git](https://git-scm.com) installiert werden. 
Nach der Installation von Git kann dieses Repository geklont werden. Am einfachsten geht
dies über die Kommandozeile eines Terminalprogramms mit Hilfe von 

```
$ cd 
$ git clone https://github.com/rawar/deeplearning.git
$ cd deepleaning
```

erfolgen. 

### Docker Container erstellen

Innerhalb des Projekverzeichnisses liegt ein Dockerfile mit dessen Hilfe sich ein Docker Container 
erstellen lässt, welche die gesammt Software, welche im Buch besprochen wird und alle
Jupyter-Notebook-Beispiele ausführbar enthält. Damit sich ein Docker Container lokal
erstellen lässt, wird je nach Betriebssystem, eine spezielle Docker Laufzeitumgebung
benötigt. Mehr Informationen dazu findet sich auf der Seite von [Docker](https://www.docker.com).

Ist die Docker Laufzeitumgebung installiert, kann der Docker Container zum Buch mit folgenden
Kommandos erstellt werden:

```
$ cd deepleaning
$ cd docker
$ docker build -t deeplearning .
```

### Docker Container von Dockerhub

Eine weitere Möglichkeit an den Docker Container zum Buch zu kommen ist, sich diesen von
[Dockerhub](https://hub.docker.com/r/rawar/deeplearning/) herunter zu laden. Über die
Kommandozeile eines Terminalfensters gelingt dies am einfachsten mit:

```
$ docker search rawar/deeplearning
$ docker pull rawar/deeplearning
```

Darüber hinaus gibt es auch grafische Benutzerschnittstellen wie [Kitematic](https://kitematic.com),
welche die Installation vereinfachen.

## Inhalt des Docker Containers

Der Docker Conatiner zum Buch installiert folgende Softwarepakere:

* Python 2.7
* IPython
* Caffe
* Caffe2
* TensorFlow 1.1.0
* Java 8
* Hadoop 2.7.3
* Spark 2.1.1
* Intel BigDL 0.1.1
* AWS CLI
* Google Cloud SDK

## Nutzung des Docker Containers

### Jupyter-Notebook nutzen

### TensorBoard nutzen

### Cloud-Umgebungen nutzen
