#!./venv/bin/python

import re
import csv
from collections import defaultdict

def main():
    
    print("THIS IS UTILITY PROGRAM THAT READS FILE NAME - POSTING.TXT")
    print("AND DISPLAYS THE TOP 20 KEYWORDS SIMILAR TO TAGCROWD")
    print("COMPLETE KEYWORDS AND COUNTS ARE IN WORDCOUNTS.TXT")
    print("------------------------------------------------------")
    print(" Written by Kirk Lim - Ver 1: November 2, 2023")
    print("------------------------------------------------------")
    excluded_words = []

    with open('excluded_words.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            excluded_words.append(row[0])
       
    pattern = re.compile(r'([a-zà-ÿ][a-zà-ÿ’]*)', flags=re.I)

    counts = defaultdict(int)
    
    with open('POSTING.TXT', 'rt') as file:
        for line in file:
            words = re.findall(pattern, line)

            for word in words:
                if len(word)>1 and word.lower() not in excluded_words :
                    counts[word.lower()] += 1

    counts = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))

    with open("wordcounts.txt", 'wt') as file:
        for word, count in counts.items():
            file.write(f'{word},{count}\n')

    limit = 20
    print("Top 20 KEYWORDS")
    for word, count in counts.items():
        print(f'{word},{count}')
        limit-=1
        if limit<=0:
            break
        
    print("\n For complete list of Keywords, open wordcounts.txt")


if __name__ == "__main__":  
    main()
