import spacy
import pandas as pd
import time

def runtime(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} runtime: {end - start:.2f} seconds.")
    return wrapper

def ner(text: str , nlp):
    ents = list(nlp(text).ents)
    res = ""
    for x in ents:
        res += f"{x.text}, {x.label_}\n"
    return res

@runtime
def ner_column(df: pd.DataFrame):
    with open("spacy.txt", 'w') as file:
        nlp = spacy.load("en_core_web_sm")
        for index, row in df.iterrows():
            entities = ner(row.description, nlp)
            file.write(str(index) + "...\n")
            file.write(entities)
            file.write("\n")

if __name__ == "__main__":
    print("If you haven't, run", "'python -m spacy download en_core_web_sm'")
    print("")

    print("Spacy NER")
    print("-" * 50)

    df = pd.read_csv("../Data/v2.tsv", usecols=["description"], sep='\t')

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
    print("Writing to 'spacy.txt'")
    ner_column(df)
    print("Done!")
    print("")