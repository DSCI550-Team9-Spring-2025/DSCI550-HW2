import spacy
import pandas as pd
import time

def runtime(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} runtime: {end - start}")
    return wrapper

def ner(text: str , nlp):
    ents = list(nlp(text).ents)
    return [(x.text, x.label_) for x in ents]

@runtime
def ner_column(df: pd.DataFrame) -> list:
    col = list()
    nlp = spacy.load("en_core_web_sm")
    for _, row in df.iterrows():
        col.append(ner(row.description, nlp))
    return col

if __name__ == "__main__":
    print("If you haven't, run", "'python -m spacy download en_core_web_sm'")
    print("")

    print("Spacy NER")
    print("-" * 50)

    df = pd.read_csv("../Data/v2.tsv", usecols=["description"], sep='\t')

    print("Sample")
    print("-" * 25)
    print("decription:", df.description.iloc[0])
    print("")
    nlp = spacy.load("en_core_web_sm")
    sample = ner(df.description.iloc[0], nlp=nlp)
    print("return:", sample)
    print("")

    print("Get spacy_entities column")
    print("-" * 25)
    df['spacy_entities'] = ner_column(df)
    print(df['spacy_entities'])
    print("")