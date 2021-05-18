from pathlib import Path
from sklearn.model_selection import train_test_split

def lireText(fichier):
    with open(fichier) as f:
        return f.readlines()
        
lines  = lireText("conversation.txt")
lines = [line[:-1] for line in lines]

# nombre de messages par conversation
number_lines = 6
data = []

# regroupe les message par conversation
for i in range(len(lines)//number_lines) :
  start = i*number_lines
  if len(lines[start:]) > number_lines:
    end = start + number_lines
    data.append(''.join(lines[start:end]))
  else :
    data.append(''.join(lines[start:]))

data_train, data_test, _, _ = train_test_split(data, data, test_size=0.33)

with open("train.txt", "w") as f:
  f.write('\n'.join(data_train))

with open("test.txt", "w") as f:
  f.write('\n'.join(data_test))