# Main Source Files
- ```merge_data.ipynb```: final step, joins newly generated columns from ```.../Data/``` to generate ```v2_final.tsv```
- ```create_haunted_images.ipynb```: image generation
- ```generate_image_cap_and_obj.ipynb```: image caption generation
- ```script1.py```: streamlined geotagger and spacy processing
  -  ```tika_geotag_process_code.py```: geotagger processing, generates ```../Data/v2_with_geo.tsv```
  - ```get_spacy_col.py```: extracts name entities using SpaCy and writes to ```spacy.txt``` and parses it to generate ```../Data/spacy.csv```

## Supplementary Source Files
- ```clean_up_df.ipynb```: cleans dataframe and fixes apparition descriptors from ```v1.tsv``` to ```v2.tsv```
- ```lucene_addToPath.sh```: shell script to add lucene to $PATH env variable (run ```source lucene_addToPath.sh```)
- ```spacy_analysis.ipynb```: analysis of SpaCy NER results (for report)
