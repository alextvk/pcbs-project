import pandas as pd
import glob

def nb_correct_responses(target, resp):
	return len(set(target).intersection(set(resp)))

datafiles = glob.glob("data/*.xpd")
datafiles = ["data/test.xpd"]

for datafile in datafiles:
	df = pd.read_csv(datafile, comment = "#")
	hits = []
	for index, r in df.iterrows():
		hits.append(nb_correct_responses(r["Stim"], r["Response"]))
	df["hits"] = hits

	print(df["hits"].groupby([df["Report_Type"], df["Display_Duration"]]).mean())
