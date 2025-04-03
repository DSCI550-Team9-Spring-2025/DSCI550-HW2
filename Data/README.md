# Main Datasets
- ```v1.tsv```: initial main dataset from HW1 (read-only recommended: ```chmod 444 v1.tsv```)<br>
- ```v2.tsv```: main dataset that will have new features added to it.<br>
- ```v2_with_all_features.tsv```: large dataset with all features, many of which were intermediary in debugging and analysis like tokenization, POS, lemma, etc. <br>
- ```v2_final.tsv```: dataset with all relevant features filtered and prepped for HW3 visualizations<br>
   - Corrections from "v1.tsv" to "v2.tsv, "clean_up_df.ipynb" added "apparition_adj_str" and fixed keyword_dictionary for Apparition_Descriptors and added in Apparition_Adjectives. <br>

## New column data
- ```spacy.csv```: SpaCy NER<br>
- ```v2_with_geo.tsv```: geotagger<br>
- ```merged_spacy_and_geo_v2.csv```: SpaCy-Geotagger merge<br>
- ```hw2_with_captions_and_objects.csv```: GenAI image and caption features with "v2.tsv" merged in.<br>

#### Supplementary Data
```keywords_dictionary_v2.csv```: updated keyword bank for text matching schemas.<br>
```spacy_loc_analysis.csv```: intermediary outputs used to see analysis of NER entity label summary counts related to location.
