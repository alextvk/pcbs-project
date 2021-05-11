#! /usr/bin/env python
"""Alexandra Tavakelian - PCBS project Perceptual selection --> article of J. Duncan link + program description """

import random, expyriment

# Experiment parameters
letters="ABCDEFGHKLMNOPQRST"
numbers="1234567890"
ntrials_per_block = 2
DISPLAY_DURATIONS = [60, 90, 120]


# Creating a get_response function in order to resolve the TextInput bug (thank you so much Cédric!!)
def get_response(keyboard, is_only_letters=True):
    keys_to_process = [expyriment.misc.constants.K_RETURN]
    keys_to_process += expyriment.misc.constants.K_ALL_LETTERS
    if not is_only_letters:
        keys_to_process += expyriment.misc.constants.K_ALL_DIGITS
    text_instruction = ("Enter all the LETTERS you remember seeing.\n" if is_only_letters
               else "Enter all the characters - both LETTERS AND NUMBERS - you remember seeing.\n")
    stimulus = expyriment.stimuli.TextBox(text_instruction, size = (400, 200), position = (0,0)) # parametre pos? 
    stimulus.present()
    has_pressed_return = False
    response = ""
    while not has_pressed_return:
        key_pressed, _ = keyboard.wait(keys=keys_to_process)
        has_pressed_return = (key_pressed == expyriment.misc.constants.K_RETURN)
        if not has_pressed_return:
            character = chr(key_pressed)
            response += character.upper()
            stimulus.text = text_instruction + response
            stimulus.present()
    return response


def create_block_of_trials(block_name, ntrials_per_block):
	b = expyriment.design.Block(block_name)
	for _ in range(ntrials_per_block): 
		stim = random.sample(letters, 3) + random.sample(numbers, 3) 
		random.shuffle(stim) 
		stim_str = " ".join(stim)
		t = expyriment.design.Trial()  
		t.set_factor("stim", "".join(stim)) 
		s = expyriment.stimuli.TextLine(stim_str) 
		t.add_stimulus(s)
		b.add_trial(t)
	return b

########################################  MAIN  #################################################
exp = expyriment.design.Experiment(name="Perceptual selection")
expyriment.control.initialize(exp)

blankscreen = expyriment.stimuli.BlankScreen() 
exp.data_variable_names = ["Report_Type", "Display_Duration", "Stim", "Response"]

# PROGRAM EXECUTION	
expyriment.control.start(subject_id= 1, skip_ready_screen = True)

# Add general welcome message + instructions
expyriment.stimuli.TextScreen("Instructions", """Welcome to this experiment. 
We will briefly display a string of 6 alphanumeric characters.
You will be asked to report some or all of them... """).present()
exp.keyboard.wait()

blankscreen.present()

for task in ["Partial", "Whole"]:
	exp.clock.wait(3000)
	for display_duration in DISPLAY_DURATIONS:
		for trial in create_block_of_trials(str(display_duration), ntrials_per_block).trials:
			exp.clock.wait(2000)
			expyriment.stimuli.FixCross().present()
			exp.clock.wait(500)
			blankscreen.present()
			exp.clock.wait(500)
			trial.stimuli[0].present()
			exp.clock.wait(display_duration)
			blankscreen.present()
			response  = get_response(exp.keyboard, task == "Partial")
			exp.data.add([task, display_duration, trial.get_factor("stim"), response])


expyriment.control.end(goodbye_text="Thank you for your participation. Goodbye.", goodbye_delay = 1000)




