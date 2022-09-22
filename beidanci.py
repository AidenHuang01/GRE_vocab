#!/usr/bin/python
# -*- coding: utf-8 -*-

from pyexpat import model
import pandas as pd
import os

def learn(df, start):
    total_row = len(df)
    idx = 0
    while idx < len(df):
        index = start + idx
        row = df.loc[index]
        vocab = row["Vocal"]
        meaning = row["Meaning"]
        output = learn_phraser(idx, total_row, vocab, meaning)
        print(output)
        user_input = input(">>")
        print(user_input)
        if user_input == "a":
            if index > 0:
                idx -= 2
            else:
                idx -= 1
        idx += 1 
        os.system('cls' if os.name == 'nt' else 'clear')
    return df

def advanced_learn(df, start):
    total_row = len(df)
    visited = set()
    while len(visited) < total_row:
        idx = 0
        while idx < len(df):
            index = start + idx
            row = df.loc[index]
            vocab = row["Vocal"]
            meaning = row["Meaning"]
            if index not in visited:
                os.system('cls' if os.name == 'nt' else 'clear')
                output = str(idx+1) + "/" + str(total_row) + "\n\n"
                output += vocab + "\n"
                print(output)
                input(">> ")
                os.system('cls' if os.name == 'nt' else 'clear')
                output = learn_phraser(idx, total_row, vocab, meaning)
                print(output)
                user_input = input("\nKnow? Y/[n]: ")
                if user_input == "Y" or user_input == "y":
                    visited.add(index)
            idx += 1
            
                

        
def moxie(df, start):
    total_row = len(df)
    for idx in range(len(df)):
        index = start + idx
        row = df.loc[index]
        vocab = row["Vocal"]
        output = moxie_phraser(idx, total_row, vocab)
        print(output)
        my_meaning = input("::")
        df.loc[index, "Mymeaning"] = my_meaning
        df.loc[index, "Learn"] += 1
        os.system('cls' if os.name == 'nt' else 'clear')

    return df

def pigai(df, start):
    total_row = len(df)
    df_wrong = pd.DataFrame(columns=df.columns)
    for idx in range(len(df)):
        index = start + idx
        row = df.loc[index]
        vocab = row["Vocal"]
        my_meaning = row["Mymeaning"]
        meaning = row["Meaning"]
        output = pigai_phraser(idx, total_row, vocab, my_meaning, meaning)
        print(output)
        key = input("::")
        if key != "":
            df.loc[index, "Wrong"] += 1
            df_wrong.loc[len(df_wrong)] = row
        os.system('cls' if os.name == 'nt' else 'clear')

    return df, df_wrong
        
def store_back(df_partial, df_full):
    df_full.update(df_partial)
    return df_full
        

def learn_phraser(index, total_row, vocab, meaning):
    output = ""
    output += str(index+1) + "/" + str(total_row) + "\n" + "\n"
    output += vocab + "\n" + "\n"
    output += meaning
    return output


def moxie_phraser(index, total_row, vocab):
    output = ""
    output += str(index+1) + "/" + str(total_row) + "\n"
    output += vocab
    return output

def pigai_phraser(index, total_row, vocab, my_meaning, meaning):
    output = ""
    output += str(index+1) + "/" + str(total_row) + "\n"
    output += vocab + "\n"
    output += "Yours:   " + str(my_meaning) + "\n"
    output += "Meaning: " + meaning
    return output

def update_wrong_csv(file_name, df_wrong):
    df_previous = pd.read_csv(file_name)
    df_previous.update(df_wrong)
    df_previous.to_csv(file_name, mode='a', index=False)

def main():
    # Clear screen
    os.system('cls' if os.name == 'nt' else 'clear')

    vocab_df = pd.read_csv("./test.csv", on_bad_lines='skip')
    section = int(input("Enter section [1-41]: "))

    start = 20 * (section - 1)
    end = 20 * section - 1
    if end >= 815:
        end = 814
    
    vocab_df_partial = vocab_df.loc[start:end, :]

    user_input = input("Directly go to advanced learn? y/[N] ")
    if user_input != "Y" and user_input != 'y':
        while True:
            learn(vocab_df_partial, start)
            user_input = input("Go to moxie? [Y]/n")
            if user_input != "n":
                break
    print("check1")

    user_input = input("Skip advanced learning? y/[N]: ")
    print(user_input)
    if user_input != "Y" and user_input != "y":
        advanced_learn(vocab_df_partial, start)

    print("=========== Moxie ===========")
    vocab_df_moxie = moxie(vocab_df_partial, start)

    print("============ Pigai ===========")
    vocab_df_pigai, df_wrong = pigai(vocab_df_moxie, start)

    update_wrong_csv("./wrong.csv", df_wrong)

    df_to_store = store_back(vocab_df_pigai, vocab_df)
    df_to_store.to_csv("./test.csv", index=False)
    


if __name__ == "__main__":
    main()

