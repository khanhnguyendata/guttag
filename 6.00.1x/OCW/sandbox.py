# Solving a Diophantine Equation
# Using this theorem, we can write an exhaustive search to find the largest
# number of McNuggets that cannot be bought in exact quantity. The format of
# the search should probably follow this outline:
#
#       Hypothesize possible instances of numbers of McNuggets that cannot be
#           purchased exactly, starting with 1.
#       For each possible instance, called n,
#           Test if there exists non-negative integers a, b, and c, such that
#               6a+9b+20c = n. (This can be done by looking at all feasible
#               combinations of a, b, and c)
#           If not, n cannot be bought in exact quantity, save n
#       When you have found six consecutive values of n that in fact pass the #           test of having an exact solution, the last answer that was saved
#           (not the last value of n that had a solution) is the correct
#           answer, since you know by the theorem that any amount larger can
#           also be bought in exact quantity
#
# ==============================================================================
# Problem 3.
#
# Write an iterative program that finds the largest number of McNuggets that
# cannot be bought in exact quantity. Your program should print the answer in
# the following format (where the correct number is provided in place of <n>):
#
#   “Largest number of McNuggets that cannot be bought in exact quantity: <n>”
#
# Hint: your program should follow the outline above.
# Hint: think about what information you need to keep track of as you loop
# through possible ways of buying exactly n McNuggets. This will guide you in
# deciding what state variables you will need to utilize.
# ==============================================================================

# Converting math equation variables to meaningful program variables
# -------------------------------------------------------------------
# n = totalNuggets
# a = sixPiece
# b = ninePiece
# c = twentyPiece

# Get the range of total number of nuggets to solve for from user and convert answers to integers
minNuggets = input("minimum number of total nuggets? ")
maxNuggets = input("maximum number of total nuggets? ")

minNuggets = int(minNuggets)
maxNuggets = int(maxNuggets)

# Set starting point for totalNuggets calculations at minNuggets
totalNuggets = minNuggets

# Set package variables
twentyPiece = 0
maxTwentyPiece = int(maxNuggets / 20)
# print("maxTwentyPiece = " + str(maxTwentyPiece))

ninePiece = 0
maxNinePiece = int(maxNuggets / 9)
# print("maxNinePiece = " + str(maxNinePiece))

sixPiece = 0
maxSixPiece = int(maxNuggets / 6)
# print("maxSixPiece = " + str(maxSixPiece))

counter = 0

while totalNuggets < maxNuggets:

    if counter < 6:
        twentyPiece = 0

        while twentyPiece <= maxTwentyPiece:
            # print("checking twentyPiece = " + str(twentyPiece))
            ninePiece = 0

            while ninePiece <= maxNinePiece:
                # print("checking ninePiece = " + str(ninePiece))
                sixPiece = 0

                while sixPiece <= maxSixPiece:
                    # print("checking sixPiece = " + str(sixPiece))

                    if (6 * sixPiece) + (9 * ninePiece) + (20 * twentyPiece) == totalNuggets:
                        # print(str(totalNuggets) + " |  " + str(twentyPiece) + " |  " + str(ninePiece) + " |  " + str(sixPiece))
                        print("Found solution for " + str(totalNuggets) + ".")

                        twentyPiece = maxTwentyPiece + 1
                        ninePiece = maxNinePiece + 1
                        sixPiece = maxSixPiece + 1
                        counter += 1
                        print("Counter = " + str(counter))


                    elif (sixPiece == maxSixPiece) and (ninePiece == maxNinePiece) and (twentyPiece == maxTwentyPiece):

                        noSolution = totalNuggets
                        print("No solution for " + str(noSolution) +
                              " nugget(s).")
                        counter = 0
                        sixPiece += 1

                    else:
                        sixPiece += 1

                ninePiece += 1

            twentyPiece += 1

        totalNuggets += 1

    if counter == 6:
        totalNuggets = maxNuggets + 1

print("\nLargest number of McNuggets that cannot be bought in exact quantity: " + str(noSolution) + "\n")