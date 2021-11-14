import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import random


## ----- part 1 a ------
def load_quantoms():
    for i in range(qA):
        N[random.randint(0, 99)] += 1

## ----- part 1 b ------
def quantoms_exchange(qA, qB):
    qA_track = np.zeros(shape=(100,), dtype=int)
    qB_track = np.zeros(shape=(100,), dtype=int)
    index_counter_qA, index_counter_qB = 0, 0
    for step in range(steps):
        i, j = random.randint(0, 199), random.randint(0, 199)
        if N[i] != 0:
            N[i] -= 1
            N[j] += 1
            if i < 100 and j > 99:  # from A to b
                qB += 1
                qA -= 1
            elif i > 99 and j < 100:  # from b to a
                qA += 1
                qB -= 1
        if step % 1000 == 0:
            qA_track[index_counter_qA] = qA
            index_counter_qA += 1
            qB_track[index_counter_qB] = qB
            index_counter_qB += 1
    plt.plot(np.linspace(0, 100000, 100), qA_track, color='blue', marker='o', linestyle='-', label="q_A")
    plt.plot(np.linspace(0, 100000, 100), qB_track, color='red', marker='o', linestyle='-', label="q_B")
    plt.legend(loc="upper right")
    plt.xlabel("step")
    plt.ylabel("energy quantums")
    plt.title("Energy quantums vs. number of steps in solid quantum exchange")
    plt.show()

## ----- part 2 a - Metropoliuce algorithm -----

def quantum_exchange_for_part_2():
    steps_arr = [2000000 - 1, 4000000 - 1, 6000000 - 1, 8000000 - 1, (10000000 - 1)]
    q_tot_ctr = 0
    q_tot = np.zeros(shape=(steps,))
    q_1_track = np.zeros(shape=(steps,), dtype=int)
    fig, ax = plt.subplots(nrows=2, ncols=3)
    subplts = plt.figure()
    subplt_arr = [ax[0, 0], ax[0, 1], ax[0, 2], ax[1, 0], ax[1, 1]]
    subplt_arr_count = 0
    for step in range(steps):
        i = random.randint(0, 99)
        flip = random.randint(-1, 1) # "coin toss"
        if flip == 1: # == 1
            p = random.random() # float between 0 and 1
            if not (p > np.exp(np.divide(-1, theta))):
                N[i] += 1
                q_tot_ctr += 1
        if flip == -1 :
            if N[i] > 0:
                N[i] -= 1
                q_tot_ctr -= 1
        q_tot[step] = q_tot_ctr
        q_1_track[step] = N[0]
        if step in steps_arr: # create histogram
            print(np.max(N))
            hist, bins = np.histogram(N, bins=range(20))
            print(hist)

            plt.hist(N, bins=range(20), label=str(step + 1), density=True)

            
            subplt_arr[subplt_arr_count].hist(N, bins=range(20), density=True, label=str(step + 1))
            subplt_arr[subplt_arr_count].set_title("Step = " + str(step + 1), size=10)
            subplt_arr[subplt_arr_count].set_xlabel("Energy quantums", fontsize=8)
            subplt_arr[subplt_arr_count].set_ylabel('Particles', fontsize=8)
            subplt_arr_count += 1


    fig.delaxes(ax[1, 2])
    # fig.show()
    plt.title("Histogram of quantums of energy for all particles (Normalized), theta = " + str(theta))
    plt.legend(loc='upper right')
    plt.xlabel("Energy quantums")
    plt.ylabel('Particles')
    # fig.title("Histogram of quantums of energy for all particles (Normalized), theta = " + str(theta))
    plt.show()

    plt.hist(q_1_track, bins=range(np.max(q_1_track) + 1), density=True)
    plt.title ("Histogram of energy quantums of a specific particle, vs steps number to reach them.")
    plt.xlabel("energy quantums")
    plt.ylabel("steps (normalized)")
    plt.show()

    plt.plot(np.linspace(0,10000000, 10000000), q_tot, '-')
    plt.title("q_tot vs. step number")
    plt.xlabel("step")
    plt.ylabel("q_tot")
    plt.show()

if __name__ == "__main__":

    # # part one
    # N = np.zeros(shape=(200,), dtype=int)
    # qA, qB = 300, 0
    # # steps = np.asarray(range(100000), dtype=int)
    # steps = 100000
    # load_quantoms()
    # quantoms_exchange(qA, qB)

    # part two
    N = np.zeros(shape=(100,), dtype=int)
    theta = 2.5
    steps = 10000000
    quantum_exchange_for_part_2()
