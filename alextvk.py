# Alexandra Tavakelian - PCBS project Perceptual selection

# Import relevant modules
import random, expyriment

# Creating a get_response function in order to resolve the TextInput bug (thank you so much Cédric!!)
def get_response(keyboard, is_only_letters=True):
    keys_to_process = [expyriment.misc.constants.K_RETURN]
    keys_to_process += expyriment.misc.constants.K_ALL_LETTERS
    if not is_only_letters:
        keys_to_process += expyriment.misc.constants.K_ALL_DIGITS
    text_instruction = ("Enter all the letters you remember seeing.\n" if is_only_letters
               else "Enter all the characters - both letters and numbers - you remember seeing.\n")
    stimulus = expyriment.stimuli.TextBox(text_instruction, size=(400, 200))
    stimulus.present()
    has_pressed_return = False
    response = ""
    while not has_pressed_return:
        key_pressed, _ = keyboard.wait(keys=keys_to_process)
        has_pressed_return = (key_pressed == expyriment.misc.constants.K_RETURN)
        if not has_pressed_return:
            character = chr(key_pressed)
            response += character
            stimulus.text = text_instruction + response
            stimulus.present()
    return response

# Alphanumeric characters required for the stimuli
letters="ABCDEFGHKLMNOPQRST"
numbers="1234567890"

exp = expyriment.design.Experiment(name="Perceptual selection")
expyriment.control.initialize(exp)

blankscreen = expyriment.stimuli.BlankScreen() 


# First block: 60msec time condition
time_cond_60 = expyriment.design.Block(name="60msec time condition")

# Randomized sets of stimuli for 60ms time condition
for _ in range(10): 
	stim_60 = random.sample(letters, 3) + random.sample(numbers, 3) 
	random.shuffle(stim_60) 
	stim_str_60 = " ".join(stim_60)
	t_60 = expyriment.design.Trial()  
	t_60.set_factor("stim_60", stim_str_60) 
	s_60 = expyriment.stimuli.TextLine(stim_str_60) 
	t_60.add_stimulus(s_60)
	time_cond_60.add_trial(t_60)
	exp.add_block(time_cond_60)


# Second block: 90msec time condition
time_cond_90 = expyriment.design.Block(name="90msec time condition")

# Randomized sets of stimuli for 90ms time condition
for _ in range(10): 
	stim_90 = random.sample(letters, 3) + random.sample(numbers, 3) 
	random.shuffle(stim_90) 
	stim_str_90 = " ".join(stim_90)
	t_90 = expyriment.design.Trial()  
	t_90.set_factor("stim_90", stim_str_90) 
	s_90 = expyriment.stimuli.TextLine(stim_str_90) 
	t_90.add_stimulus(s_90)
	time_cond_90.add_trial(t_90)
	exp.add_block(time_cond_90)
	

# Third block: 120msec time condition
time_cond_120 = expyriment.design.Block(name="120msec time condition")

# Randomized sets of stimuli for 120ms time condition
for _ in range(10): 
	stim_120 = random.sample(letters, 3) + random.sample(numbers, 3) 
	random.shuffle(stim_120) 
	stim_str_120 = " ".join(stim_120)
	t_120 = expyriment.design.Trial()  
	t_120.set_factor("stim_120", stim_str_120) 
	s_120 = expyriment.stimuli.TextLine(stim_str_120) 
	t_120.add_stimulus(s_120)
	time_cond_120.add_trial(t_120)
	exp.add_block(time_cond_120)


# PROGRAM EXECUTION	
expyriment.control.start(subject_id= 1, skip_ready_screen = True)

# PARTIAL REPORT
#instructions_partial.present()
exp.clock.wait(5000)


# 60msec time condition
for trial in time_cond_60.trials:
	trial.stimuli[0].present()
	exp.clock.wait(60)
	blankscreen.present()
	exp.clock.wait(500)
	response_only_letters = get_response(exp.keyboard, is_only_letters=True)
	print("First response:", response_only_letters)
	#exp.data.add([time_cond_60.name, trial.id, response_only_letters])
	#exp.data_variable_names = ["Block", "Trial", "Partial Report Reponse"]

blankscreen.present()
exp.clock.wait(1000)

# 90msec time condition
for trial in time_cond_90.trials:
	trial.stimuli[0].present()
	exp.clock.wait(90)
	blankscreen.present()
	exp.clock.wait(500)
	response_only_letters = get_response(exp.keyboard, is_only_letters=True)
	print("First response:", response_only_letters)
	#exp.data.add([time_cond_90.name, trial.id, response_only_letters])
	#exp.data_variable_names = ["Block", "Trial", "Partial Report Reponse"]

blankscreen.present()
exp.clock.wait(1000)

# 120msec time condition
for trial in time_cond_120.trials:
	trial.stimuli[0].present()
	exp.clock.wait(120)
	blankscreen.present()
	exp.clock.wait(500)
	response_only_letters = get_response(exp.keyboard, is_only_letters=True)
	print("First response:", response_only_letters)
	#exp.data.add([time_cond_120.name, trial.id, response_only_letters])
	#exp.data_variable_names = ["Block", "Trial", "Partial Report Reponse"]


# WHOLE REPORT
#instructions_whole.present()
exp.clock.wait(5000)

# 60msec time condition
for trial in time_cond_60.trials:
	trial.stimuli[0].present()
	exp.clock.wait(60)
	blankscreen.present()
	exp.clock.wait(500)
	response_letters_and_digits = get_response(exp.keyboard, is_only_letters=False)
	print("Second response:", response_letters_and_digits)
	#exp.data.add([time_cond_60.name, trial.id, response_letters_and_digits])
	#exp.data_variable_names = ["Block", "Trial", "Whole Report Reponse"]

blankscreen.present()
exp.clock.wait(1000)

# 90msec time condition
for trial in time_cond_90.trials:
	trial.stimuli[0].present()
	exp.clock.wait(90)
	blankscreen.present()
	exp.clock.wait(500)
	response_letters_and_digits = get_response(exp.keyboard, is_only_letters=False)
	print("Second response:", response_letters_and_digits)
	#exp.data.add([time_cond_90.name, trial.id, response_letters_and_digits])
	#exp.data_variable_names = ["Block", "Trial", "Whole Report Reponse"]

blankscreen.present()
exp.clock.wait(1000)

# 120msec time condition
for trial in time_cond_120.trials:
	trial.stimuli[0].present()
	exp.clock.wait(120)
	blankscreen.present()
	exp.clock.wait(500)
	response_letters_and_digits = get_response(exp.keyboard, is_only_letters=False)
	print("Second response:", response_letters_and_digits)
	# exp.data.add([time_cond_120.name, trial.id, response_letters_and_digits])
	#exp.data_variable_names = ["Block", "Trial", "Whole Report Reponse"]

expyriment.control.end(goodbye_text="Thank you for your participation. Goodbye.", goodbye_delay = 1000)


