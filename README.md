# PCBS Project: Perceptual Selection based on Alphanumeric Class

The aim of this project was to replicate [J. Duncan (1983) experiment](https://link.springer.com/article/10.3758/BF03202935) on perceptual selection depending on the alphanumeric class of the stimulus. 

The experiment consists in a succession of trials in which a stimulus made of 6 randomized alphanumeric characters is displayed on the screen for a varying amount of time. The participant is asked to either enter only the letters he can remember (e.g. partial report), by typing one the keyboard, or to enter all of the characters (letters and numbers, whole report) he can remember. The responses entered are recorded. 

Duncan's conclusion was that participants perform a perceptual selection based on alphanumeric class: depending on whether it is a letter or a digit that they have to report in the partial report condition, subjects focus on the same class of characters in the whole report condition as well and decrease their global performance in the whole report condition.

### Table of Contents
* [Experiment characteristics](https://github.com/alextvk/pcbs-project-perceptual-selection#experiment-characteristics)
	* [The stimuli](https://github.com/alextvk/pcbs-project-perceptual-selection#the-stimuli)
	* [The report type](https://github.com/alextvk/pcbs-project-perceptual-selection#the-report-type)
	* [The display duration conditions](https://github.com/alextvk/pcbs-project-perceptual-selection#the-display-duration-conditions)
* [Running the experiment](https://github.com/alextvk/pcbs-project-perceptual-selection#running-the-experiment)
* [Analyzing the results](https://github.com/alextvk/pcbs-project-perceptual-selection#analyzing-the-results)
* [Previous coding experience](https://github.com/alextvk/pcbs-project-perceptual-selection#previous-coding-experience)
* [What I learned and what I missed in this PCBS course](https://github.com/alextvk/pcbs-project-perceptual-selection#what-i-learned-and-what-i-missed-in-the-pcbs-course)

## Experiment characteristics

### The stimuli
The stimuli were generated randomly: they consist in 6 alphanumeric characters, 3 capital letters, 3 digits. The order of each character has been randomized at well across trials.

### The report type
There are 2 types of responses expected from participants:
* the partial report consists in the participants reporting only the letters they remember from the stimuli;
* the whole report condition consists in the participants reporting **all** the alphanumeric characters, letters and digits, they remember from the stimuli.
The order of the characters in the reports is not considered. 

### The display duration conditions
3 different display duration conditions were used, following Duncan's own experiment. 
* the first set of stimuli displayed lasts for 60msec; 
* the second one lasts for 90msec;
* the last one lasts for 120 msec;
All displays are followed by a blanck screen for 500msec. 

In total, there are 6 blocked experimental conditions at stake: 2 (partial, whole) x 3 (display duration). There will be 8 trials for each of these 6 blocked conditions.


## Running the experiment

To run the experiment on your computer, you must have Python and the Expyriment module installed. 
Once Python and Expyriment are installed, you can click on [Code](https://github.com/alextvk/pcbs-project-perceptual-selection/blob/main/perceptual-selection-duncan-AT.py) and download the ZIP file attached. Extract it on your computer. 

Then, you can open a Terminal and change the directory to where the file was downloaded. 
Then, type: 
<python perceptual-selection-duncan-AT.py>  



## Analyzing the results
In order to analyze the results of your experiment, you can use the following script: [download this zip file](https://github.com/alextvk/pcbs-project-perceptual-selection/blob/main/result-analysis.py), extract it on your computer. Then, open a Terminal, change the directory to where the file was downloaded and type: 
<python result-analysis.py>

Analyzing the results I got from 3 participants (me included), I can conclude that performance in the partial report task is much better than in the whole report task in the three display duration conditions. However, we can notice that participants improved their global number of correct responses in the whole report condition. 
It would have been nice to add a comparative analysis on the performance of letters report and of digits report in the whole report task. Indeed, we can hypothesize that because we have "conditioned" participants to focus only on letters in the first part of the experiments, their performance at reporting digits in the second part may be altered by this initial 'digits ignorance priming'. 

![Results analysis](https://github.com/alextvk/pcbs-project-perceptual-selection/blob/main/result-table.png)

![Plotting the results](https://github.com/alextvk/pcbs-project-perceptual-selection/blob/main/result-plot.png)


## Previous coding experience
I had followed Datacamp during the first semester, focusing on data analysis and vizualisation using exclusively R. Before that, I had followed a class on how to program VBA for Excel. 
Overall, I was new to Python!



## What I learned and what I missed in the PCBS course
Working on this project had definitely help me progress in programming in general, and has taught me the basics on Python. 

However, the online only format of this class was hard to follow for a beginner like me. The level discrepancies in the class were discouraging and frustrating for me. I wish we had access to Datacamp in parallel, in order to practice with immediate feedback between classes for instance. 

Fortunately, you were very helpful and attentive to keeping everyone on board. I thank you very much for your patience and availability, even outside of class hours! Being guided by your advice and expertise was the most enriching! 

