#!/usr/bin/env python
# coding: utf-8

# # QUESTION 1

# A system consists of two subsystems connected in series as shown in the following diagram
# ![](images/question_1.png)
# Each subsystem consists of two components connected in parallel. The AB subsystem fails whenboth A and B have failed. The CD subsystem fails when both C and D have failed. The wholesystem fails as soon as one of the two subsystems fails. Assume that lifetimes of the components,in months, have the following distributions: <br>
# T_a ~ Exponential(lambda = 1)<br>
# T_b ~ Exponential(lambda = 0.1)<br>
# T_c ~ Exponential(lambda = 0.2)<br>
# T_d ~ Exponential(lambda = 0.2)

# In[1]:


# Before we start doing anything, we need to make sure that we have proper modules imported
import numpy


# In[2]:


# Now we specify the number of times we plan to run the simulation
times = int(1e4)


# (a) Write a program to simulaterandom variables that represent the lifetimes of AB and CD subsystems, and the lifetime of the whole system.

# In[3]:


# To generate the A,B,C,D 
A : numpy.ndarray = numpy.random.exponential(scale=1/1, size=times)
B : numpy.ndarray = numpy.random.exponential(scale=1/0.1, size=times)
C : numpy.ndarray = numpy.random.exponential(scale=1/0.2, size=times)
D : numpy.ndarray = numpy.random.exponential(scale=1/0.2, size=times)


# In[4]:


# Now we are looking for which component breaks last in either AB or CD,
# since if one breaks, that doesn't mean that component dies. Both components
# have to die for the entire circuit to die.
AB : numpy.ndarray = numpy.maximum(A, B)
CD : numpy.ndarray = numpy.maximum(C, D)

print("\tLifetime AB: {}         Lifetime CD:{}".format(AB,CD))


# (b) Run 10,000 replications of the simulation and based on the results construct a histogram for the system lifetime.Estimate the average system lifetime.

# In[5]:


# Now, we need to make sure component AB AND CD are operational.
# If one breaks, the entire circuit breaks, thus, here we look for
# the entire lifespan
lifespans : numpy.ndarray = numpy.minimum(AB, CD)

# Now we take the average of all the trials to get
# our average lifespan.
average_lifetime : float = numpy.mean(lifespans)

print("\tThe average lifespan is: {}".format(average_lifetime))


# (c) Estimate the probability that the AB subsystem fails before the CD subsystem fails, usingMonte Carlo simulation.

# In[6]:


# We will generate a new numpy array that is 0 when AB < CD, and 1 otherwise
AB_before_CD : numpy.ndarray =  AB < CD
AB_b_CD_average : float = numpy.mean(AB_before_CD)

# We will print the average
print("\tProb that AB dies before CD: {}".format(AB_b_CD_average))

