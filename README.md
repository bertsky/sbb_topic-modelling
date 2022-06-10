

## Topic modelling of digitalized collections:

Our topic modeling visualisation is currently derived from the very nice and useful [LDAvis package](https://github.com/cpsievert/LDAvis).

The [sbb_web-integration](https://github.com/qurator-spk/sbb_web-integration) package contains an adapted version of the html/js visualisation interface of LDAvis that has been extended such that 
it can switch between different topic models and provides links into wikidata and the digitalized collections of the SBB.

***

## Installation:

Clone this project, [SBB-utils](https://github.com/qurator-spk/sbb_utils), and
[SBB-web-integration](https://github.com/qurator-spk/sbb_web-integration).

Setup virtual environment:
```
virtualenv --python=python3.6 venv
```

Activate virtual environment:
```
source venv/bin/activate
```

Upgrade pip:
```
pip install -U pip
```

Install packages together with their dependencies in development mode:
```
pip install -e sbb_utils
pip install -e sbb_topic-modelling
```

Additionally for visualization:


```
pip install -e sbb_web-integration
```

***

## Computation of LDA models and visualisation data (JSON):

Complete processing chain can be found in the  [Makefile](Makefile).

## Command-line interface:

### lda-grid-search:


```
lda-grid-search --help

Usage: lda-grid-search [OPTIONS] OUT_FILE CORPUS_FILE DOCS_FILE

  Perform LDA-evaluation in a grid-search over different parameters.

  OUT_FILE: Store results of the grid search as pickled pandas DataFrame in
  this file.

  CORPUS_FILE: Read the text corpus as pickled dataframe from this file.

  DOCS_FILE: Read the documents  as pickled dataframe (required to evalute
  coherence model c_v) from this file.

Options:
  --num-runs INTEGER              Repeat each experiment num-runs times.
                                  Default 10
  --max-passes INTEGER            Max number of passes through the data.
                                  Default 50
  --passes-step INTEGER           Increase number of passes by this step size.
                                  Default 5.
  --max-topics INTEGER            Max number of topics in LDA topic model.
                                  Default 100.
  --topic-step INTEGER            Increase number of topics by this step size.
                                  Default 10.
  --coherence-model [c_v|u_mass]  Which coherence model to use. Default: c_v.
  --processes INTEGER             Number of workers. Default 4.
  --mods-info-file PATH           Read MODS info from this file.
  --gen-vis-data                  Generate visualisation JSON data (LDAvis)
                                  for each tested grid configuration.
  --mini-batch-size INTEGER       Mini-batch size. Default 2048
  --help                          Show this message and exit.

```

### run-lda:

```
run-lda --help

Usage: run-lda [OPTIONS] SQLITE_FILE MODEL_FILE

  Reads entity linking data from SQLITE_FILE. Computes LDA-topic model and
  stores it in MODEL_FILE.

Options:
  --num-topics INTEGER  Number of topics in LDA topic model. Default 10.
  --entities-file TEXT  Knowledge-base of entity linking step.
  --processes INTEGER   Number of workers.
  --corpus-file TEXT    Write corpus to this file.
  --min-proba FLOAT     Minimum probability of counted entities.
  --help                Show this message and exit.

```

### Setup visualization:

Run [sbb_web-integration](https://github.com/qurator-spk/sbb_web-integration) webservice like:

```
env CONFIG=config.json env FLASK_APP=qurator/webapp/app.py env FLASK_ENV=development env flask run --host=0.0.0.0 --port=8000
```

Topic modeling interface can be found at: http://localhost:8000/ldavis.html .

Configuration of displayed topic models is done via [config.json](qurator/webapp/config.json).

### Screenshots:

![sbb-ner-demo example](.screenshots/topicm0.png?raw=true)

![sbb-ner-demo example](.screenshots/topicm1.png?raw=true)

![sbb-ner-demo example](.screenshots/topicm2.png?raw=true)