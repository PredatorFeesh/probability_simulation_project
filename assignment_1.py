import numpy 

# In random.exponential , scale = 1 / lambda, so lambda = 1 / beta

# Number of trials to run the simulation
times = int(1e4)

# To generate the A,B,C,D 
A = numpy.random.exponential(scale=1/1, size=times)
B = numpy.random.exponential(scale=1/0.1, size=times)
C = numpy.random.exponential(scale=1/0.2, size=times)
D = numpy.random.exponential(scale=1/0.2, size=times)


# Now we are looking for which component breaks last in either AB or CD,
# since if one breaks, that doesn't mean that component dies. Both components
# have to die for the entire circuit to die.
AB = numpy.maximum(A, B)
CD = numpy.maximum(C, D)


# Now, we need to make sure component AB AND CD are operational.
# If one breaks, the entire circuit breaks, thus, here we look for
# the entire lifespan
lifespans = numpy.minimum(AB, CD)


# Now we take the average of all the trials to get
# our average lifespan.
average_lifetime = numpy.average(lifespans)

print(average_lifetime)
