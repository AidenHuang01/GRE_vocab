#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import os





def learn(df):
    total_row = len(df)
    index = 0
    while index < len(df):
        row = df.loc[index]
        vocab = row["Vocal"]
        meaning = row["Meaning"]
        output = learn_phraser(index, total_row, vocab, meaning)
        print(output)
        user_input = input(">>")
        print(user_input)
        if user_input == "a":
            if index > 0:
                index -= 2
            else:
                index -= 1
        index += 1 
        os.system('cls' if os.name == 'nt' else 'clear')

    return df
        
def moxie(df):
    total_row = len(df)
    for index in range(len(df)):
        row = df.loc[index]
        vocab = row["Vocal"]
        output = moxie_phraser(index, total_row, vocab)
        print(output)
        my_meaning = input("::")
        df.loc[index, "Mymeaning"] = my_meaning
        df.loc[index, "Learn"] += 1
        os.system('cls' if os.name == 'nt' else 'clear')

    return df

def pigai(df):
    total_row = len(df)
    for index in range(len(df)):
        row = df.loc[index]
        vocab = row["Vocal"]
        my_meaning = row["Mymeaning"]
        meaning = row["Meaning"]
        output = pigai_phraser(index, total_row, vocab, my_meaning, meaning)
        print(output)
        key = input("::")
        if key != "":
            df.loc[index, "Wrong"] += 1
        os.system('cls' if os.name == 'nt' else 'clear')

    return df
        
def store_back(df_partial, df_full):
    df_full.update(df_partial)
    return df_full
        

def learn_phraser(index, total_row, vocab, meaning):
    output = ""
    output += str(index) + "/" + str(total_row) + "\n" + "\n"
    output += vocab + "\n" + "\n"
    output += meaning
    return output

def moxie_phraser(index, total_row, vocab):
    output = ""
    output += str(index) + "/" + str(total_row) + "\n"
    output += vocab
    return output

def pigai_phraser(index, total_row, vocab, my_meaning, meaning):
    output = ""
    output += str(index) + "/" + str(total_row) + "\n"
    output += vocab + "\n"
    output += "Yours:   " + str(my_meaning) + "\n"
    output += "Meaning: " + meaning
    return output

def main():
    # Clear screen
    os.system('cls' if os.name == 'nt' else 'clear')

    vocab_df = pd.read_csv("./GRE_vocab_1.csv", on_bad_lines='skip')
    section = int(input("Enter section [1-41]: "))

    start = 20 * (section - 1)
    end = 20 * section - 1
    
    if end >= 815:
        end = 814

    vocab_df_partial = vocab_df.loc[start:end, :]

    user_input = input("Directly go to Moxie? y/[N] ")
    if user_input != "Y" and user_input != 'y':
        while True:
            learn(vocab_df_partial)
            user_input = input("Go to moxie? [Y]/n")
            if user_input != "n":
                break

    print("=========== Moxie ===========")
    vocab_df_moxie = moxie(vocab_df_partial)

    print("============ Pigai ===========")
    vocab_df_pigai = pigai(vocab_df_moxie)

    df_to_store = store_back(vocab_df_pigai, vocab_df)
    df_to_store.to_csv("./test.csv")

if __name__ == "__main__":
    main()
