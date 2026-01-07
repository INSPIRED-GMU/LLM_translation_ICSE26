<div align="center">
  <img src="https://storage.googleapis.com/tf_model_garden/tf_model_garden_logo.png">
</div>

[![Python](https://img.shields.io/pypi/pyversions/tensorflow.svg?style=plastic)](https://badge.fury.io/py/tensorflow)
[![tf-models-official PyPI](https://badge.fury.io/py/tf-models-official.svg)](https://badge.fury.io/py/tf-models-official)

# Willkommen im Model Garden für TensorFlow

Der TensorFlow Model Garden ist ein Repository mit verschiedenen Implementierungen von State-of-the-Art (SOTA) Modellen und Lösungen für TensorFlow-Nutzer. Unser Ziel ist es, Best Practices für das Modellieren zu demonstrieren, damit TensorFlow-Nutzer die Vorteile von TensorFlow für ihre Forschung und Produktentwicklung voll ausschöpfen können.

Um die Transparenz und Reproduzierbarkeit unserer Modelle zu verbessern, stellen wir soweit möglich Trainingsprotokolle auf [TensorBoard.dev](https://tensorboard.dev) zur Verfügung, obwohl nicht alle Modelle dafür geeignet sind.

| Verzeichnis | Beschreibung |
|-------------|--------------|
| [official](official) | • Eine Sammlung von Beispielimplementierungen für SOTA-Modelle mit den neuesten High-Level-APIs von TensorFlow 2<br />• Offiziell von TensorFlow gepflegt, unterstützt und mit den neuesten TensorFlow 2 APIs aktualisiert<br />• Angemessen optimiert für schnelle Leistung bei guter Lesbarkeit<br /> Weitere Details findest du im [Model-Garden-Guide](https://www.tensorflow.org/tfmodels) |
| [research](research) | • Eine Sammlung von Forschungsmodell-Implementierungen in TensorFlow 1 oder 2 von Forschern<br />• Gepflegt und unterstützt von Forschern |
| [community](community) | • Eine kuratierte Liste von GitHub-Repositories mit Machine Learning-Modellen und Implementierungen auf Basis von TensorFlow 2 |
| [orbit](orbit) | • Eine flexible und leichte Bibliothek, die Benutzer einfach nutzen oder forken können, um benutzerdefinierten Trainingscode in TensorFlow 2.x zu schreiben. Sie integriert sich nahtlos mit `tf.distribute` und unterstützt verschiedene Gerätetypen (CPU, GPU und TPU). |

## Installation

Um die aktuelle Version von tensorflow-models zu installieren, folge bitte einer der folgenden Methoden.

#### Methode 1: Installation des TensorFlow Model Garden Pip-Pakets

<details>

**tf-models-official** ist das stabile Model Garden Paket. Schau dir die [Releases](https://github.com/tensorflow/models/releases) an, um verfügbare Module zu sehen.

pip3 installiert automatisch alle Modelle und Abhängigkeiten.

```shell
pip3 install tf-models-official
```

Beispiele:
  - [Grundlegender Bibliotheksimport](https://github.com/tensorflow/models/blob/master/tensorflow_models/tensorflow_models_pypi.ipynb)
  - [NLP-Modellierung](https://github.com/tensorflow/models/blob/master/docs/nlp/index.ipynb)

Um die neuesten Änderungen einzuschließen, kann **tf-models-nightly** installiert werden:

```shell
pip3 install tf-models-nightly
```

</details>

#### Methode 2: Quellcode klonen

<details>

1. Klone das GitHub-Repository:

```shell
git clone https://github.com/tensorflow/models.git
```

2. Füge den ***/models*** Ordner zum Python-Pfad hinzu.

```shell
export PYTHONPATH=$PYTHONPATH:/path/to/models
```

3. Weitere Abhängigkeiten installieren:

```shell
pip3 install --user -r models/official/requirements.txt
```

Optional: Installation von **tensorflow-text-nightly** für NLP-Pakete:

```shell
pip3 install tensorflow-text-nightly
```

</details>

## Ankündigungen

Bitte besuche [diese Seite](https://github.com/tensorflow/models/wiki/Announcements) für aktuelle Ankündigungen.

## Beiträge

Wenn du beitragen möchtest, lies bitte die [Beitragsrichtlinien](https://github.com/tensorflow/models/wiki/How-to-contribute).

## Lizenz

[Apache License 2.0](LICENSE)

## Zitieren des TensorFlow Model Garden

Wenn du TensorFlow Model Garden in deiner Forschung verwendest, zitiere bitte dieses Repository:

```
@misc{tensorflowmodelgarden2020,
  author = {Hongkun Yu und Chen Chen und Xianzhi Du und Yeqing Li und Abdullah Rashwan und Le Hou und Pengchong Jin und Fan Yang
            und Frederick Liu und Jaeyoun Kim und Jing Li},
  title = {{TensorFlow Model Garden}},
  howpublished = {\url{https://github.com/tensorflow/models}},
  year = {2020}
}
```

