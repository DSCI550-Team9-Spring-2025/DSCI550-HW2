# DSCI550-HW2
Large scale data extraction and analysis for haunted places dataset.

## Contributors
SubTeam: Name Entity Recognition (NER)
- Sena London: GeoParser, documentation update for Tika geoparser (readme), configuration, tika_geotag_process_code.py, geoparser_output_analysis.ipynb, script1.py(GeoParser)
- Kevin Sy: merge_data.ipynb (GeoParse,Spacy,GenAI), spacy_analysis.ipynb (NER comparisons location entities), clean_up_df.ipynb, Project management (host team meetings, task assignment, meeting minutes), review/debug
- Andrew Turangan: spaCy NER: get_spacy_col.py, spacy_analysis.ipynb, script1.py(spaCy script)

SubTeam: GenAI Images, Image Docker, Object Recognition Docker (create_haunted_images.ipynb, generate_image_cap_and_obj.ipynb, hw_2_with_images_and_captions.csv, hw2_with_captions_and_objects.csv, image_captions_with_paths_desc.csv, image_captions.csv)
- Anneliese Wilkins
- Austin Oliver
- Gideon Nazarian
## Dataset
- ```Data/v2_final.tsv```
## Source Files
- ```Source/merge_data.ipynb```: final step, joins newly generated columns from to generate ```v2_final.tsv```<br>
- ```Source/create_haunted_images.ipynb```: image generation<br>
- ```Source/generate_image_cap_and_obj.ipynb```: image caption generation and image object recognition<br>
- ```Source/script1.py```: geotagger and spacy processing<br>
## Generated Stable Diffusion Images
see https://drive.google.com/drive/folders/1nHVdrBTWEaS7V7ggoWn3JogsCVurk1_0?usp=sharing
## Geoparser tool configuration to extract coordinate locations name
see https://github.com/Hibis5946/geotopicparser-utils/blob/master/README_tika_geo_parser.txt<br>
 
