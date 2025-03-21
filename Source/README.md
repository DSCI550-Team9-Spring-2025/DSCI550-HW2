## Overview

#### Main Source Files
- ```JOIN_COLUMNS.py``` or ```JOIN_COLUMNS.ipynb``` (TBD): final step, joins newly generated columns from ```.../Data/``` to generate ```v2.tsv```
- ```get_spacy_col.py```: extracts name entities using SpaCy and writes to ```spacy.txt``` and parses it to generate ```../Data/spacy.csv```
- ```...```: ...

#### Supplementary Source Files
- ```clean_up_df.ipynb```: cleans dataframe and fixes apparition descriptors from ```v1.tsv``` to ```v2.tsv```
- ```lucene_addToPath.sh```: shell script to add lucene to $PATH env variable (run ```$ source lucene_addToPath.sh```)
- ```...```: ...

<br><br>
###### *** ignored in this directory: lucene-geo-gazetteer (https://github.com/chrismattmann/lucene-geo-gazetteer) ***
