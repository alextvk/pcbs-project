#! /usr/bin/env python
"""Alexandra Tavakelian - PCBS Project Perceptual selection result analysis.
This program analyzes the participants' responses to the Perceptual Selection task.
It will return the number of global hits and the accuracy rate depending on the different report and display duration conditions.
It will also create a data visualization and save the image"""

import pandas as pd
import plotly.express as px
import glob
import numpy as np

# Experiment function
def nb_correct_responses(target, resp):
    result = 0
    if not resp != resp:
        result = len(set(target).intersection(set(resp)))
    return result


#############################################   MAIN   ##################################################

datafiles = glob.glob("data/*.xpd")

for datafile in datafiles:
	df = pd.read_csv(datafile, comment = "#")
	df["hits"] = df.apply(lambda row: nb_correct_responses(row["Stim"], row["Response"]), axis=1)
	df["max_correct_answers"] = df["Report_Type"].apply(lambda x: 6 if x == "Whole" else 3)
	df["Ratio"] = df.apply(lambda row: row["hits"]/row["max_correct_answers"]*100, axis=1)

print(df["hits"].groupby([df["Report_Type"], df["Display_Duration"]]).mean(), df["Ratio"].groupby([df["Report_Type"], df["Display_Duration"]]).mean())

# Data visualization 
stats = df.groupby([df["Report_Type"], df["Display_Duration"]]).agg([("mean", np.mean)]).reset_index()
stats.columns = ["_".join(x) for x in stats.columns]

fig = px.line(stats, x="Display_Duration_", y="Ratio_mean", title='Accuracy Rate per Type of Report', color="Report_Type_", labels={"Display_Duration_": "msec", "Ratio_mean": "Accuracy Rate (%)", "Report_Type_":"Task"})
fig.update_xaxes(type='category')
fig.update_layout(yaxis_range=[0,100])
fig.show()

