from collections import Counter
import pandas as pd

data=pd.read_csv("C:/Users/zahra/Desktop/data.csv", usecols=["text"])
str = data.text. to_list()
list=[]

for my_str in str:
    try:
            last_word_without_pre=my_str.split()[-1]
            if last_word_without_pre.endswith("." ):
                last_word_without_pre=last_word_without_pre[:-1]
            elif last_word_without_pre.endswith("?"):
                last_word_without_pre=last_word_without_pre[:-1]
            list.append(last_word_without_pre)
    except:
        pass

counts = Counter(list)
print(counts)
