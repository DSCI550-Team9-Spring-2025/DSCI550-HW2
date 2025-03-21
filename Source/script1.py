#This is code to extract geo name entities and their metadata using tika geoparser
#USC
#Spring 2025
#Team 9

import csv
import subprocess
import tempfile
import os

# Paths to Tika 2.6.0 setup (command to split)
# java -classpath /root/tika/tika-app-2.6.0.jar:/root/tika/tika-parser-nlp-package-2.6.0.jar:/root/location-ner-model:/root/geotopic-mime org.apache.tika.cli.TikaCLI -m /root/geotopic-mime/cnn.geot

TIKA_APP_JAR = "/root/tika/tika-app-2.6.0.jar"
TIKA_NLP_JAR = "/root/tika/tika-parser-nlp-package-2.6.0.jar"
NER_MODEL_DIR = "/root/location-ner-model"
MIME_CONFIG_DIR = "/root/geotopic-mime"

# Input and output files
INPUT_FILE = "/root/v2.geot"   # <-- Your input TSV file
OUTPUT_FILE = "/root/v2_with_geo.tsv"  # <-- Output file

# Geo fields to extract from Tika output
GEO_FIELDS = [
    "Geographic_LATITUDE",
    "Geographic_LONGITUDE",
    "Geographic_NAME",
    "Optional_LATITUDE1",
    "Optional_LONGITUDE1",
    "Optional_NAME1"
]

def extract_geo_from_description(geot_content):
    """ Runs the Tika CLI on a given .geot content and extracts geo metadata. """
    with tempfile.NamedTemporaryFile(delete=False, suffix=".geot", mode="w") as tmp_file:
        tmp_file.write(geot_content)
        tmp_path = tmp_file.name

    command = [
        "java",
        "-classpath",
        f"{TIKA_APP_JAR}:{TIKA_NLP_JAR}:{NER_MODEL_DIR}:{MIME_CONFIG_DIR}",
        "org.apache.tika.cli.TikaCLI",
        "-m",
        tmp_path
    ]

    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        geo_data = {field: "" for field in GEO_FIELDS}
        for line in result.stdout.splitlines():
            for field in GEO_FIELDS:
                if line.startswith(field + ":"):
                    geo_data[field] = line.split(":", 1)[1].strip()
        return geo_data
    except subprocess.CalledProcessError as e:
        print(f"[!] Tika CLI error: {e}")
        return {field: "" for field in GEO_FIELDS}
    finally:
        os.unlink(tmp_path)

def process_geot_file():
    """ Reads v2.geot, extracts geo metadata, and writes the output file. """
    with open(INPUT_FILE, newline='', encoding='utf-8') as infile, \
         open(OUTPUT_FILE, 'w', newline='', encoding='utf-8') as outfile:

        reader = csv.DictReader(infile, delimiter='\t')
        fieldnames = reader.fieldnames + GEO_FIELDS
        writer = csv.DictWriter(outfile, fieldnames=fieldnames, delimiter='\t')
        writer.writeheader()

        for i, row in enumerate(reader, 1):
            desc = row.get("description", "")
            if desc.strip():
                geo_info = extract_geo_from_description(desc)
                row.update(geo_info)
            else:
                row.update({field: "" for field in GEO_FIELDS})
            writer.writerow(row)

            if i % 50 == 0:
                print(f"[+] Processed {i} rows...")

    print(f"[✓] Done. Output saved to: {OUTPUT_FILE}")

if __name__ == "__main__":
    process_geot_file()
