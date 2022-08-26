import matplotlib.pyplot as plt 
import random

def dice_roll()->bool:
    die_1 = random.randint(1, 6)
    die_2 = random.randint(1, 6)

    # Determining if they are the same number
    return True if die_1 == die_2 else False

# Inputs 
num_simulations = 10000
max_num_rolls = 1000
bet = 1

# Tracking vars
win_probability = []
end_balance = []

# Creating the figure to draw the results of each simulation
fig = plt.figure()
plt.title(f"Monte Carlo Dice Game [{num_simulations}] Simulations")
plt.xlabel("Roll Number")
plt.ylabel("Balance [$]")
plt.xlim([0, max_num_rolls])

# The simulation loop
for i in range(num_simulations):
    balance = [1000]
    num_rolls = [0]
    num_wins = 0
    
    # roll dices for 1000 times
    while num_rolls[-1] < max_num_rolls:
        same = dice_roll()
        if same:
            balance.append(balance[-1] + 4 * bet)
            num_wins += 1
        else:
            balance.append(balance[-1] - bet)
        num_rolls.append(num_rolls[-1] + 1)
    
    # storing the results and drawing a line to represent them
    win_probability.append(num_wins / num_rolls[-1])
    end_balance.append(balance[-1])
    plt.plot(num_rolls, balance)

# Displaying the results 
plt.show()

# Averaging win probability and end balance
overall_win_probability = sum(win_probability)/len(win_probability)
overall_end_balance = sum(end_balance)/len(end_balance)
# Displaying the averages
print(f"Average win probability after {num_simulations} runs: {overall_win_probability}")
print(f"Average ending balance after {num_simulations} runs: ${overall_end_balance}")
