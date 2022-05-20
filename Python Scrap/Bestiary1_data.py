import re
import pandas as pd

header = "Creature Level Category TypeTrait Rarity Page"
header = header.split(" ")

def convert(string):
    name = re.findall(r"[\D^-]+(?= -|[0-9]+\D+\d+)", string)[0]
    name = str(name)
    level = re.findall(r"(?=\D)-[0-9]+|[0-9]+(?= )", string)
    level = int(level[0])
    cat = re.findall(r"(?<=[0-9] )\D+(?= \S+ \S+ \d+)", string)
    cat = cat[0]
    typ_trait = re.findall(r"\S+(?= \S+ \d+)", string)[-1]
    typ_trait = str(typ_trait)
    rarity = re.findall(r"\S+(?= \d+)", string)[-1]
    rarity = str(rarity)
    page = re.findall(r"[0-9]+\Z", string)
    page = int(page[0])
    new_string = [name, level, cat, typ_trait, rarity, page]
    return new_string

# convert(b1_creatures[0])

def panda_build(file: str):
    b1_file = open(file)
    b1_data = b1_file.read()
    b1_file.close()
    b1_data.replace("â€“", "-")
    b1_creatures = b1_data.splitlines()

    best1 = []
    for i in range(len(b1_creatures)):
        creature = convert(b1_creatures[i])
        best1.append(creature)

    output = pd.DataFrame(best1, columns = header)
    return output

bestiary1 = panda_build("Bestiary1_data.txt")
bestiary1["Reference"] = " Bestiary 1"
bestiary2 = panda_build("Bestiary2_data.txt")
bestiary2["Reference"] = " Bestiary 2"
bestiary3 = panda_build("Bestiary3_data.txt")
bestiary3["Reference"] = " Bestiary 3"

bestiary = bestiary1.merge(bestiary2, how='outer').merge(bestiary3, how='outer')

for i in range(len(bestiary)):
    name = re.findall(r"[\w ]+", bestiary['Creature'][i])
    bestiary['Creature'][i] = name
    # bestiary['Creature'][i] = bestiary['Creature'][i].strip()
bestiary.to_csv("Bestiary.csv")


re.findall(r"[\w ]+", bestiary['Creature'][i])
bestiary['Creature'][1000].strip()