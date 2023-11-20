import pandas as pd
from collections import Counter
import yaml
import time

runfile = open("run.txt", 'r')
sentinel = len(runfile.readlines())
while(sentinel == 0 ):
    time.sleep(3)
    sentinel = len(runfile.readlines())

runfile = open("run.txt", 'r')
params = runfile.readlines()

if(params[0] == "run\n"):
    filename = params[1]

    df = pd.read_excel(filename, sheet_name = 1)

    matchRelScores = Counter(df['Match Rel Score'].tolist())
    matchReview = Counter(df['Match Review'].tolist())
    status = Counter(df['Status'].tolist())

    with open('output.yaml', 'w+') as outfile:
        yaml.dump(matchRelScores, outfile, default_flow_style=False)
        yaml.dump(matchReview, outfile, default_flow_style=False)
        yaml.dump(status, outfile, default_flow_style=False)
