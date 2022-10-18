import matplotlib.pyplot as plt
from matplotlib.pyplot import savefig, subplots
from matplotlib import use
from json import loads
from numpy import arange, gradient
from math import sqrt


def draw_speed_graph():
    use('TkAgg')
    with open('log.json', 'r') as f:
        sim_results = loads(f.read())

    t = arange(0, sim_results["frame_count"] + 1, 1)
    plt.Figure(dpi=300)
    fig, ax = subplots(2, 1)
    speeds = []
    for i in range(sim_results["body_count"]):
        speeds.append([])
        for j in range(sim_results["frame_count"] + 1):
            speed = sqrt(pow(sim_results["velocities"][str(j)][i][0], 2) +
                         pow(sim_results["velocities"][str(j)][i][1], 2))
            speeds[i].append(speed)

        ax[0].plot(t, speeds[i], linewidth=2.0)
        ax[1].plot(t, gradient(speeds[i]))

    ax[0].set_ylabel("Скорость")
    ax[1].set_ylabel("Ускорение")
    ax[1].set_xlabel("Шаги симуляции")

    savefig("speed_plot.jpg", )


def draw_x_y_graph():
    use('TkAgg')
    with open('log.json', 'r') as f:
        sim_results = loads(f.read())

    t = arange(0, sim_results["frame_count"] + 1, 1)
    fig, ax = subplots(2, 1)
    pos_x = []
    pos_y = []

    shift_x = sim_results["frame_size"][0] / 2
    shift_y = sim_results["frame_size"][1] / 2

    for i in range(sim_results["body_count"]):
        pos_x.append([])
        pos_y.append([])
        for j in range(sim_results["frame_count"] + 1):
            pos_x[i].append(sim_results["positions"][str(j)][i][0]-shift_x)
            pos_y[i].append(sim_results["positions"][str(j)][i][1]-shift_y)

        ax[0].plot(t, pos_x[i])
        ax[1].plot(t, pos_y[i])

    ax[0].set_ylabel("X координата")
    ax[1].set_ylabel("Y координата")
    ax[1].set_xlabel("Шаги симуляциии")
    savefig("xyplot.jpg")
