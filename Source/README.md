## Overview

#### Main source files
- ```JOIN_COLUMNS.py``` or ```JOIN_COLUMNS.ipynb``` (TBD): final step, joins newly generated columns from ```.../Data/``` to generate ```v2.tsv```
- ```spacy_andrew.py```: extracts name entities using SpaCy and writes to ```spacy.txt``` and parses it to generate ```../Data/spacy_andrew.csv```
- ```...```: ...

#### Supplementary source files
- ```clean_up_df.ipynb```: cleans dataframe and fixes apparition descriptors from ```v1.tsv``` to ```v2.tsv```
- ```lucene_addToPath.sh```: shell script to add lucene to $PATH env variable (run ```$ source lucene_addToPath.sh```)
- ```...```: ...

<br><br>
###### *** ignored in this directory: lucene-geo-gazetteer (https://github.com/chrismattmann/lucene-geo-gazetteer) ***
