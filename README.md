# Praxiseinstieg Deep Learning  

![book cover](https://www.oreilly.de/common/images/cover_masterid/gross/12840.jpg)

Dieses Repository soll ein Praxiseinstieg in die Arbeit mit TensorFlow und Caffe/Caffe2 sein. 
Es enhält alle Quellcodes zu den Beispielen meines Buchs für O'Reilly 
[Praxiseinstieg Deep Learning](https://www.oreilly.de/buecher/12840/9783960090540-praxiseinstieg-deep-learning.html).

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
* Intel BigDL 0.3.0
* AWS CLI
* Google Cloud SDK

## Nutzung des Docker Containers

Der Docker Container zum Buch lässt sich auf verschiedene Arten nutzen. Um den Container zu starten
und nutzen zu können, lässt sich über die Kommandozeile eines Terminalfensters folgender Befehl nutzen:

```
$ docker run -it -p 8888:8888 -p 6006:6006 rawar/deeplearning:latest bash
```

Ausserdem lässt sich der Docker Container auch über grafische Benutzeroberflächen wie  [Kitematic](https://kitematic.com)
nutzen. 

### Jupyter-Notebook nutzen

Um die Anwendung Jupyter-Notebook mit dem Docker Container zu starten gibt es zwei Möglichkeiten:

* Über die Kommandozeile eines Terminalfensters kann mit Hilfe von

```
$ docker run -it -p 8888:8888 -p 6006:6006 rawar/deeplearning:latest ./run_jupyter.sh
```

direkt die Webanwendung gestartet werden. Oder man nutzt grafische Oberflächen wie [Kitematic](https://kitematic.com)
dafür. 

* Man startet den Docker Container mit

```
$ docker run -it -p 8888:8888 -p 6006:6006 rawar/deeplearning:latest bash
```

und startet die Jupyter-Notebook Anwendung über die Bash mit Hilfe von

```
$ ./run_jupyter
```

Danach lässt sich die Jupyter-Notebook-Anwendung über einen Webbrowser unter `http://localhost:8888` erreichen.
Im Anschluss daran, findet man alle Beispiele zu den Kapiteln im Verzeichnis `notebooks` wieder.

### TensorBoard nutzen

Um die Webanwendung TensorBoard nutzen zu können, muss diese mit Hilfe von

```
$ tensorboard --logdir=path/to/log-directory
```

gestartet werden. Danach lässt sich TensorBoard mit einem Webbrowser unter `http://localhost:6006` erreichen.

### Cloud-Umgebungen nutzen

Der Docker Container zum Buch enthält zwei Schnittstellen zu Cloud Anbietern. Enthalten sind dabei die 
[AWS-Cli](https://aws.amazon.com/de/cli/) für die Nutzung von 
[Amazon Web Service](https://aws.amazon.com/de/) und [Googles Cloud SDK](https://cloud.google.com/sdk/) 
für die Nutzung von [Googles Cloud Platform](https://cloud.google.com). 

Für die Nutzung der Kommandozeilen-Tool sind gültige Accounts nötig. Sollten diese nicht bestehen, kann
man sich sowohl bei AWS als auch GCP kostenlos anmelden. Allein die Nutzung der jeweiligen Dienste kostet
Geld.

Damit der Docker Container die richtigen Anmelde-Daten nutzen kann, sollten diese innerhalb der
Datei `.boto` konfiguriert werden. Wie dies für das GCP SDK erfolgen kann, findet sich 
[hier](https://cloud.google.com/storage/docs/boto-gsutil). Für AWS Cli findest sich ein 
Konfigurationsbeispiel [hier](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html).

