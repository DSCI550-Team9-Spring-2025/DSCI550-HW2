import spacy
import pandas as pd
import time
import os

def runtime(func):
    """Wrapper function decorator to calculate runtime in seconds."""
    def wrapper(*args, **kwargs) -> None:
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} runtime: {end - start:.2f} seconds.")
    return wrapper

def ner(text: str , nlp) -> str:
    """Run SpaCy NER on description. Returns 'ent.text, ent.label_' for each ent"""
    ents = list(nlp(text).ents)
    res = ""
    for x in ents:
        res += f"{x.text}, {x.label_}\n"
    return res

@runtime
def write_spacy(df: pd.DataFrame, txtfile: str="spacy.txt"):
    """Iterates through df.description and writes result of ner() to txtfile."""
    with open(txtfile, 'w') as file:
        nlp = spacy.load("en_core_web_sm")
        for index, row in df.iterrows():
            entities = ner(row.description, nlp)
            file.write(str(index) + "...\n")
            file.write(entities)
            file.write("\n")

@runtime
def parse_spacy(inpath: str="spacy.txt", outpath: str='../Data/spacy.csv', size: int=0):
    """Parses input txt into output csv."""
    if not os.path.exists(inpath):
        print(f"Error: {inpath} does not exist.")
        return
    
    # read line by line
    with open(inpath, 'r') as file:
        lines = file.readlines()

    # populate parsed_data
    parsed_data = [""] * size
    index = None
    for line in lines:
        # empty line
        if not line:
            continue

        # index line
        if line[0].isdigit() and '...' in line:
            index = int(line.split('...')[0])
        # entity line
        elif index is not None:
            parsed_data[index] += line.strip() + '\n'

    # generate output csv
    df = pd.DataFrame(parsed_data, columns=["spacy_entities"])
    df.to_csv(outpath, index=False)
    print(outpath + " created!")

def main():
    print("IF YOU HAVEN'T, run", "'python -m spacy download en_core_web_sm'")
    print("")

    print("Spacy NER with '../Data/v2.tsv'")
    print("-" * 50)
    df = pd.read_csv("../Data/v2.tsv", usecols=["description"], sep='\t')

    # create spacy.txt: takes 2-3 minutes on andrew's machine
    if not os.path.exists("spacy.txt"):
        print("Sample")
        print("-" * 25)
        print("decription:\n", df.description.iloc[0])
        print("")
        nlp = spacy.load("en_core_web_sm")
        sample = ner(df.description.iloc[0], nlp=nlp)
        print("return:\n", sample)
        print("")

        print("Get spacy_entities column")
        print("-" * 25)
        print("Writing to 'spacy.txt'...")
        write_spacy(df)
        print("Done!")
        print("")

    # parse spacy.txt
    print("Parse 'spacy.txt'")
    print("-" * 25)
    print("Parsing 'spacy.txt'...")
    parse_spacy(size=df.shape[0])
    print("Done!")
    print("")

    # spacy_andrew.csv sample
    print("Result Sample")
    print("-" * 25)
    spacy_df = pd.read_csv("../Data/spacy.csv")
    print("spacy_df.iloc[0]['spacy_entities']")
    print("-" * 15)
    print(spacy_df.iloc[0]['spacy_entities'])
    print("spacy_df")
    print("-" * 15)
    print(spacy_df)
    print("")


if __name__ == "__main__":
    main()