<div align="center">
  <img src="https://storage.googleapis.com/tf_model_garden/tf_model_garden_logo.png">
</div>

[![Python](https://img.shields.io/pypi/pyversions/tensorflow.svg?style=plastic)](https://badge.fury.io/py/tensorflow)
[![tf-models-official PyPI](https://badge.fury.io/py/tf-models-official.svg)](https://badge.fury.io/py/tf-models-official)


# Willkommen im Model Garden für TensorFlow

Der TensorFlow Model Garden ist ein Repository mit verschiedenen Implementierungen von State-of-the-Art (SOTA) Modellen und Modelllösungen für TensorFlow-Nutzer. Unser Ziel ist es, Best Practices für die Modellierung zu demonstrieren, damit TensorFlow-Nutzer TensorFlow optimal für ihre Forschung und Produktentwicklung nutzen können.

Um die Transparenz und Reproduzierbarkeit unserer Modelle zu verbessern, werden soweit möglich auch Trainingsprotokolle auf [TensorBoard.dev](https://tensorboard.dev) bereitgestellt, auch wenn nicht alle Modelle dafür geeignet sind.

| Verzeichnis | Beschreibung |
|-----------|-------------|
| [official](official) | • Eine Sammlung von Beispielimplementierungen für SOTA-Modelle unter Verwendung der neuesten High-Level-APIs von TensorFlow 2<br />• Offiziell von TensorFlow gewartet, unterstützt und mit den neuesten TensorFlow 2 APIs aktualisiert<br />• Angemessen optimiert für schnelle Leistung bei gleichzeitiger guter Lesbarkeit<br /> Weitere Details zu den Funktionen finden Sie im Leitfaden zum [Model-garden](https://www.tensorflow.org/tfmodels)|
| [research](research) | • Eine Sammlung von Forschungsmodell-Implementierungen in TensorFlow 1 oder 2 von Forschern<br />• Von Forschern gewartet und unterstützt |
| [community](community) | • Eine kuratierte Liste von GitHub-Repositories mit maschinellen Lernmodellen und Implementierungen, die von TensorFlow 2 unterstützt werden |
| [orbit](orbit) | • Eine flexible und leichtgewichtige Bibliothek, die Benutzer beim Schreiben von angepasstem Trainingsschleifencode in TensorFlow 2.x einfach verwenden oder forken können. Sie integriert sich nahtlos mit `tf.distribute` und unterstützt die Ausführung auf verschiedenen Gerätetypen (CPU, GPU und TPU). |

## Installation

Um die aktuelle Version von tensorflow-models zu installieren, folgen Sie bitte einer der unten beschriebenen Methoden.

#### Methode 1: Installation des TensorFlow Model Garden pip-Pakets

<details>

**tf-models-official** ist das stabile Model Garden-Paket. Bitte prüfen Sie die [Releases](https://github.com/tensorflow/models/releases), um zu sehen, welche Module verfügbar sind.

pip3 installiert alle Modelle und Abhängigkeiten automatisch.

```shell
pip3 install tf-models-official
```

Bitte schauen Sie sich unsere Beispiele an:
  - [grundlegende Bibliotheksimporte](https://github.com/tensorflow/models/blob/master/tensorflow_models/tensorflow_models_pypi.ipynb)
  - [NLP-Modellentwicklung](https://github.com/tensorflow/models/blob/master/docs/nlp/index.ipynb)
um zu lernen, wie man ein PIP-Paket verwendet.

Beachten Sie, dass **tf-models-official** möglicherweise nicht die neuesten Änderungen im Master-Branch dieses
GitHub-Repositories enthält. Um die neuesten Änderungen einzubeziehen, können Sie **tf-models-nightly**
installieren, das täglich automatisch als Nightly Model Garden-Paket erstellt wird.

```shell
pip3 install tf-models-nightly
```

</details>


#### Methode 2: Quellcode klonen

<details>

1. Klonen Sie das GitHub-Repository:

```shell
git clone https://github.com/tensorflow/models.git
```

2. Fügen Sie den obersten ***/models*** Ordner zum Python-Pfad hinzu.

```shell
export PYTHONPATH=$PYTHONPATH:/path/to/models
```

Wenn Sie in einer Windows-Umgebung arbeiten, müssen Sie möglicherweise den folgenden Befehl mit PowerShell verwenden:
```shell
$env:PYTHONPATH += ":\path\to\models"
```

Wenn Sie ein Colab-Notebook verwenden, setzen Sie bitte den Python-Pfad mit os.environ.

```python
import os
os.environ['PYTHONPATH'] += ":/path/to/models"
```

3. Installieren Sie weitere Abhängigkeiten

```shell
pip3 install --user -r models/official/requirements.txt
```

Wenn Sie NLP-Pakete verwenden, installieren Sie bitte auch
**tensorflow-text-nightly**:

```shell
pip3 install tensorflow-text-nightly
```

</details>


## Ankündigungen

Bitte prüfen Sie [diese Seite](https://github.com/tensorflow/models/wiki/Announcements) für aktuelle Ankündigungen.

## Beiträge

[![help wanted:paper implementation](https://img.shields.io/github/issues/tensorflow/models/help%20wanted%3Apaper%20implementation)](https://github.com/tensorflow/models/labels/help%20wanted%3Apaper%20implementation)

Wenn Sie beitragen möchten, lesen Sie bitte die [Beitragsrichtlinien](https://github.com/tensorflow/models/wiki/How-to-contribute).

## Lizenz

[Apache License 2.0](LICENSE)

## Zitieren des TensorFlow Model Garden

Wenn Sie den TensorFlow Model Garden in Ihrer Forschung verwenden, zitieren Sie bitte dieses Repository.

```
@misc{tensorflowmodelgarden2020,
  author = {Hongkun Yu and Chen Chen and Xianzhi Du and Yeqing Li and Abdullah Rashwan and Le Hou and Pengchong Jin and Fan Yang
            and Frederick Liu and Jaeyoun Kim and Jing Li},
  title = {{TensorFlow Model Garden}},
  howpublished = {\url{https://github.com/tensorflow/models}},
  year = {2020}
}
```