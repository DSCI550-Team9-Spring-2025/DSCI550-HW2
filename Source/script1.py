#University of Southern California
#Spring 2025
#DSCI550
#Assignment 2
#Team 9
#This is the assignment 2 uniformed code (single script file)

#####Start code####

import pandas as pd

#####################################
# MAIN DATAFRAME
df = pd.read_csv("../Data/v1.tsv", sep="\t")
#####################################

# SpaCy NER
#########################
df_spacy = df.copy()
def spacy_col(df: pd.DataFrame):
    """Generates column for df['spacy_entities']"""
    from get_spacy_col import write_spacy, parse_spacy
    print("SpaCy NER")
    print("-" * 15)

    """write_spacy: processes SpaCy entities -> 'spacy.txt'"""
    #write_spacy(df=df, txtfile="spacy.txt") # TAKES 3 MINUTES, 'spacy.txt' already in Source/

    """parse_spacy: parses 'spacy.txt' into csv format -> '../Data/spacy.csv'"""
    parse_spacy(inpath='spacy.txt', outpath='../Data/spacy.csv', size=df.shape[0])

    return pd.read_csv('../Data/spacy.csv')['spacy_entities']

df['spacy_entities'] = spacy_col(df=df_spacy)
print("'spacy_entities' column generated! See df['spacy_entities']")
print("")
#print(df["spacy_entities"])




