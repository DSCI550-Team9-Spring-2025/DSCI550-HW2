# DSCI550-HW2
Large scale data extraction and analysis for haunted places dataset.

## Contributors
SubTeam: Name Entity Recognition (NER)
- Sena London: GeoParser, documentation update for Tika geoparser (readme), configuration, tika_geotag_process_code.py, geoparser_output_analysis.ipynb, script1.py(GeoParser)
- Kevin Sy: merge_data.ipynb (GeoParse,Spacy,GenAI), spacy_analysis.ipynb (NER comparisons location entities), clean_up_df.ipynb, Project management (host team meetings, task assignment, meeting minutes), review/debug
- Andrew Turangan: spaCy NER: get_spacy_col.py, spacy_analysis.ipynb, script1.py(spaCy script)

SubTeam: GenAI Images
- Anneliese Wilkins
- Austin Oliver
- Gideon Nazarian
## Dataset
- ```Data/v2_final.tsv```
## Source Files
- ```Source/merge_data.ipynb```: final step, joins newly generated columns from to generate ```v2_final.tsv```<br>
- ```Source/create_haunted_images.ipynb```: image generation<br>
- ```Source/generate_image_cap_and_obj.ipynb```: image caption generation<br>
- ```Source/script1.py```: geotagger and spacy processing<br>
## Geoparser tool configuration to extract coordinate locations name
see https://github.com/Hibis5946/geotopicparser-utils/blob/master/README_tika_geo_parser.txt<br>
- ```git clone https://github.com/chrismattmann/lucene-geo-gazetteer.git```
- ```cd lucene-geo-gazetteer```
- ```mvn clean package```
- ```mvn install assembly:assembly```
- ```export PATH=$PATH:/root/lucene-geo-gazetteer/src/main/``` (or run ```source Source/lucene_addToPath.sh```)
- ```cd lucene-geo-gazetteer```
- ```curl -O http://download.geonames.org/export/dump/allCountries.zip```
- ```unzip allCountries.zip```
- ```lucene-geo-gazetteer -i geoIndex -b allCountries.txt```
- ```mkdir -p /root/location-ner-model && cd /root/location-ner-model```
- ```curl -O https://opennlp.sourceforge.net/models-1.5/en-ner-location.bin```
- ```mkdir -p org/apache/tika/parser/geo/```
- ```mv en-ner-location.bin org/apache/tika/parser/geo/```
- ```mkdir -p /root/geotopic-mime && cd /root/geotopic-mime```
- ```mkdir -p org/apache/tika/mime```
- ```curl -L -o custom-mimetypes.xml https://raw.githubusercontent.com/chrismattmann/geotopicparser-utils/master/mime/org/apache/tika/mime/custom-mimetypes.xml```
- ```mv custom-mimetypes.xml org/apache/tika/mime```
- ```curl -L -o /root/geotopic-mime/polar.geot https://raw.githubusercontent.com/chrismattmann/geotopicparser-utils/master/geotopics/polar.geot```
- ```curl -L -o /root/geotopic-mime/cnn.geot https://raw.githubusercontent.com/chrismattmann/geotopicparser-utils/master/geotopics/cnn.geot```
- ```cd lucene-geo-gazetteer```
- ```lucene-geo-gazetteer -server```
  ![image](https://github.com/user-attachments/assets/10e4c605-e192-46c0-a886-448e35430964)
##Sample cnn.geot geo metadata
  ![image](https://github.com/user-attachments/assets/23ff8429-68de-4d0c-8183-1afb397afd0d)

##Tika config path
![image](https://github.com/user-attachments/assets/cd2bed09-3489-46db-b079-0053d06559b2)


