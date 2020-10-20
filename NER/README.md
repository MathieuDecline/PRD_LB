# Named Entity Recognition
BERT Model - google colab - NER

https://colab.research.google.com/drive/1ulJlyB4jnImWuorUAfDdM7l1Y7CwCQXL?usp=sharing

# Data repository for BERT model.

Dataset_0 : 
Each text line represent a line from the receipt.
Each line is associated to a label : 'company', 'date', 'address', 'total', '0' (Unknown).

Dataset_1 : 
Each text line represent a line from the receipt.
All lines with unkown label were removed.
Each line is associated to a label : 'company', 'date', 'address', 'total'

Dataset_2 : 
Each text line represent a word from the receipt.
Each word is associated to a label : 'company', 'date', 'address', 'total', '0' (Unknown).

Dataset_3 : 
Each text line represent 3 word from the receipt: [previous word, word labelled, next word].
Each word is associated to a label : 'company', 'date', 'address', 'total', '0' (Unknown).
