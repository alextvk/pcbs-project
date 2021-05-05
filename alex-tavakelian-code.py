# Alexandra Tavakelian - PCBS project Perceptual selection

# Import relevant modules
import random, expyriment

# Alphanumeric characters required for the stimuli
letters="ABCDEFGHKL"
numbers="1234567890"

# Sets of stimuli 
# still need to find a way to compare the user inputs and the stimuli displayed

for _ in range(10): 
	stim = random.sample(letters, 3) + random.sample(numbers, 3) 
	random.shuffle(stim) 
	stim_str = " ".join(s) 
	t.set_factor("stim", stim_str) 
	s = expyriment.stimuli.TextLine(stim_str) 
	t = expyriment.design.Trial() 
	t.add_stimulus(s)

stim1 = random.sample(letters, 3) + random.sample(numbers, 3)
random.shuffle(stim1)
stim_str1 = " ".join(stim1)

stim2 = random.sample(letters, 3) + random.sample(numbers, 3)
random.shuffle(stim2)
stim_str2 = " ".join(stim2)

stim3 = random.sample(letters, 3) + random.sample(numbers, 3)
random.shuffle(stim3)
stim_str3 = " ".join(stim3)

stim4 = random.sample(letters, 3) + random.sample(numbers, 3)
random.shuffle(stim4)
stim_str4 = " ".join(stim4)

stim5 = random.sample(letters, 3) + random.sample(numbers, 3)
random.shuffle(stim5)
stim_str5 = " ".join(stim5)

exp = expyriment.design.Experiment(name="Perceptual selection")
expyriment.control.initialize(exp)

# Instructions for partial and whole report phases
instructions_partial = expyriment.stimuli.TextBox(text="""Welcome to the experiment. 
You will be presented with 6 random alphanumeric characters. 
After each presentation of a combination of letters and numbers, 
please enter ONLY the letters you remember seeing.""", size = (1200, 500))

insutrctions_whole = expyriment.stimuli.TextBox(text="""This is the second phase of the experiment. 
You will be presented with 6 random alphanumeric characters. 
After each presentation of a combination of letters and numbers, 
please enter ALL the letters and numbers you remember seeing.""", size = (1200, 500))

blankscreen = expyriment.stimuli.BlankScreen() 
resp_partial = expyriment.io.TextInput(message="Enter all the letters you remember seeing.")
resp_whole = expyriment.io.TextInput(message="Enter all the characters - both letters and numbers - you remember seeing.")

# First block: 60msec time condition
time_cond_60 = expyriment.design.Block(name="60msec time condition")

# Trial one
trial_one = expyriment.design.Trial()
stimulus1 = expyriment.stimuli.TextLine(stim_str1)
stimulus1.preload()
trial_one.add_stimulus(stimulus1)

# Trial two
trial_two = expyriment.design.Trial()
stimulus2 = expyriment.stimuli.TextLine(stim_str2)
stimulus2.preload()
trial_two.add_stimulus(stimulus2)

# Trial three
trial_three = expyriment.design.Trial()
stimulus3 = expyriment.stimuli.TextLine(stim_str3)
stimulus3.preload()
trial_three.add_stimulus(stimulus3)

# Trial four
trial_four = expyriment.design.Trial()
stimulus4 = expyriment.stimuli.TextLine(stim_str4)
stimulus4.preload()
trial_four.add_stimulus(stimulus4)

# Trial five
trial_five = expyriment.design.Trial()
stimulus5 = expyriment.stimuli.TextLine(stim_str5)
stimulus5.preload()
trial_five.add_stimulus(stimulus5)


# Adding all trials to the 60msec time condition block
time_cond_60.add_trial(trial_one)
time_cond_60.add_trial(trial_two)
time_cond_60.add_trial(trial_three)
time_cond_60.add_trial(trial_four)
time_cond_60.add_trial(trial_five)
exp.add_block(time_cond_60)

# Second block: 90msec time condition
time_cond_90 = expyriment.design.Block(name="90msec time condition")

# Adding all trials to the 90msec time condition block
time_cond_90.add_trial(trial_one)
time_cond_90.add_trial(trial_two)
time_cond_90.add_trial(trial_three)
time_cond_90.add_trial(trial_four)
time_cond_90.add_trial(trial_five)
exp.add_block(time_cond_90)

# Third block: 120msec time condition

expyriment.control.start(subject_id= 1, skip_ready_screen = True)

instructions_partial.present()
exp.clock.wait(5000)

for trial in time_cond_60.trials:
	trial.stimuli[0].present()
	exp.clock.wait(60)
	blankscreen.present()
	exp.clock.wait(500)
	resp_partial.get()
	exp.data.add([time_cond_60.name, trial.id, resp_partial])
	exp.data_variable_names = ["Block", "Trial", "Participant reponse"]

blankscreen.present()
exp.clock.wait(1000)

for trial in time_cond_90.trials:
	trial.stimuli[0].present()
	exp.clock.wait(90)
	blankscreen.present()
	exp.clock.wait(500)
	resp_partial.get()
	exp.data.add([time_cond_90.name, trial.id, resp_partial])
	exp.data_variable_names = ["Block", "Trial", "Participant reponse"]

# for loop with time_cond_120.trials

# instructions_whole.present()
# exp.clock.wait(5000)

# Repeat same loops

expyriment.control.end(goodbye_text="Thank you for your participation. Goodbye.", goodbye_delay = 1000)




# Display 120 msec condition stimuli (10 other stimuli for 120msec + mask)


# Display the instructions for whole report, ask to press a key to display first series of stimuli

# Display 60msec condition stimuli (10 stimuli (each is a random combinations of 6 characters) for 60msec + a blank mask for 500msec after each display)

# Display 90msec condition stimuli (10 other stimuli for 90msec + mask)

# Display 120 msec condition stimuli (10 other stimuli for 120msec + mask)


