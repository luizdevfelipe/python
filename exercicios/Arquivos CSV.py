import csv
from collections import Counter

with open("file.csv", "r") as file:
    reader = csv.DictReader(file)
    counts = Counter()
    
    for row in reader:
        favorite = row["firs"]
        counts[favorite] +=1
    
for favorite, count in counts.most_common():
    print(f"{favorite}: {counts}")