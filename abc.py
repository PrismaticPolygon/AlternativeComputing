# Initial food sources are produced for all employed bees
# REPEAT:
#   Each employed bee goes to a food source in her memory and determines a closest source, then evaluate its nectar
#       amount and dances in the hive
#   Each onlooker watches the dance of the employed bees and chooses one of their sources depending on the dances,
#       and goes to that source. After choosing a neighbour around that, she evaluates its nectar amount
#   Abandoned food sources are determined and replaced with the new food sources discovered by scouts
#   The best

S_N = 10    # Amount of foods
limit = 10  # Maximum number of trials before abandoning a source
MFE = 10    # Maximum number of fitness evaluations

num_evaluations = 0

def random_food_source(s):   # Produce initial food sources randomly within the range of the boundaries of the parameters

    return 0


# Blah blah blah.

# What is f(x)?
#

X = list()
f = list()
trials = list()

for s in range(S_N):

    r = random_food_source(s)

    X.append(r)  # Random solution
    f.append(r)
    trials.append(0)    # This is the number of times that we've examined this food source, I believe.

    num_evaluations += 1

for s in range(S_N):

    x = 0   # A new solution produced by equation 2

# I will, infact, just steal this pseudo code.
# It's a lot easier.
# I just have to understand how the thing works.




# Nice. Here's some thorough pseudo-code.
# I'll convert it into my OWN code, and then I'll be in good stead to write it myself.

# void init(int index)
# begin
#   fitness[index] = CalculateFitness(f[index])
#   trial[index] = 0
# end

# void SendScoutBees()

# begin
# if (trial[maxTrialIndex] >= limit) then
#   init(maxTrialIndex)
# end
# end


# Generate a randomly distributed initial population of S_n solutions.

