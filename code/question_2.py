#!/usr/bin/env python
# coding: utf-8

# # QUESTION 2

# ![](images/question_2_text.png)

# ![](images/question_2_parts.png)

# In[ ]:


# Import needed module
import numpy
import random

# For consistent results we seed
random.seed(6)


# In[2]:


# First, we will generate all the computers in the network
num_computers : int = 20
num_infected : int = 0
    
# And specify the chance of infection for infected computer
prob_infect = 0.1

# Keep track of computers
computers : numpy.ndarray = numpy.zeros(num_computers)

# We will also track the total days it takes to irradicate the virus as a sum since
# the average is equal to the sum / trails
days_total = 0

# And we will track the number of times a computer was infected for parts B and D.
times_infected : numpy.ndarray = numpy.zeros(num_computers)
    
# Track average infections per trial
check_already_infected : numpy.ndarray = numpy.zeros(num_computers)
average_infections : list = []


# Now we will need to generate a "turn". To do that, we need to take into account <br>
# the rules that have been given to us in the beggining of the sheet. Namely: <br> <br>
# -(a) Each computer has a 0.1 chance to infect any other uninfected computer <br>
# -(b) Every day technician removed virus from any 5 computers (assume this happens second)

# In[3]:


# First we need to write some helper functions

def infect(index:int, trial:int) -> None:
    # Infects a specific index
    # @return None
    global computers # Have to do it..
    global times_infected
    global num_infected
    computers[index] = 1
    times_infected[index] += 1
    num_infected += 1
    if not check_already_infected[index]: # If we weren't infected this trial
        average_infections[trial] += 1
        check_already_infected[index] = 1

def cure(index:int) -> None:
    # Removes from infected
    # @return None
    global computers 
    global num_infected
    computers[index] =  0 # Find infected in the list and delete it
    num_infected -= 1
    

def get_infected() -> list: # Returns index of infected computers
    global computers
    return [e for e,i in enumerate(computers) if i == 1]

def get_uninfected() -> list: # Returns index of infected computers
    global computers
    return [e for e,i in enumerate(computers) if i == 0]


# In[4]:


# Function (a)
def infect_turn(trial) -> None: # Since computers is global we don't need to pass it in
    # Processes infecting computers
    # @return None
    global computers
    global prob_infect 
    for infed in get_infected(): # for each infected computer
        for uninf in get_uninfected(): # try to infect each uninfected
            if random.random() <= prob_infect: # if infect
                infect(uninf, trial) # then we infect
                
# This has a terrible runtime        


# In[5]:


# Function (b)
def IT_turn(max_fix : int = 5) -> None:
    # Fixes total of max_fix computers
    # @return None
    global computers # Wish I didn't.. ой ой ой
    infected = get_infected() # Get infected computers
    if len(infected) <= max_fix: # If we don't reach max_fix 
        for comp in get_infected(): # Get the infected
            cure(comp) # Cure 'em!
    else: # Otherwise, we need to find max_fix indexes to cure
        cured_indexes = random.sample(infected, max_fix) # Get max_fix indexes are random
        for index in cured_indexes: # For each index
            cure(index) # Cure the computer


# In[6]:


# Now we need to actually process the trials
num_trials = int(1e4)

for trial in range(num_trials):
    # Some resetting before we start
    check_already_infected = numpy.zeros(num_computers) # Reset check
    average_infections.append(0) # Prep for tracking 
    
    # Let's infect a computer
    start_index = random.randrange(0, num_computers, 1) # Pick random computer
    infect(start_index, trial) # Infect it
    
    
    # Now we need to loop through the days
    while num_infected > 0: # While we have infecetd computers
        # We pass the trial so we can properly update "average infections"
        infect_turn(trial = trial)
        IT_turn()
        
        days_total += 1

print("\tExpected time for infected to be cured: {}".      format(days_total/num_trials))
print("\tProbability each computer gets infected at least once: {}".      format( sum(average_infections)/(num_trials * num_computers) ))
print("\tExpected number of computers that get infected: {}".      format( ( times_infected / (days_total) ).mean() * num_computers )) 
# We can use days for the last calculation because it should be equal to 
# the total number of infections. It is used to normalize the array, before
# we take the mean, and then multiply by the max computers

