# scatter-anim-3D.py

import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation

# Functions

def read_data(filename, speed):
    """
    Arguments:
        filename (string): name of the datafile.
    
    Returns:
        data: list of arrays with dimension (N x 3).
        Each element of the list is an array that corresponds to an instance in time.
        Each array has a dimension of N, with N being the number of particles.
        Each particle is another array of dimension 3, which is their 3D position.
    """
    # obtain number of elements
    with open(filename) as f:
        first_line = f.readline().strip().split(':')
    N = (len(first_line)-1)/3

    start_positions = np.array(map(float, first_line[1:3*N+1])).reshape(N, 3)
    
    # define list of arrays
    data = [start_positions]
    
    ff = open(filename)
    line_counter = 0
    for current_line in ff:
        if line_counter > 0: # prevent first line, that was already read
            if line_counter % speed == 0:
                line_list     = current_line.strip().split(':')
                new_positions = np.array(map(float, line_list[1:3*N+1])).reshape(N, 3)
                data.append(new_positions)
        line_counter = line_counter + 1
    ff.close()
    return data

def animate_scatters(iteration, data, scatters):
    """
    Update the data held by the scatter plot and therefore animates it.

    Args:
        iteration (int): Current iteration of the animation
        data (list): List of the data positions at each iteration.
        scatters (list): List of all the scatters (One per element)

    Returns:
        list: List of scatters (One per element) with new coordinates
    """    
    for i in range(data[0].shape[0]):
        scatters[i]._offsets3d = (data[iteration][i,0:1], data[iteration][i,1:2], data[iteration][i,2:])
    return scatters

def main(data, save=False):
    """
    Creates the 3D figure and animates it with the input data.

    Args:
        data (list): List of the data positions at each iteration.
        save (bool): Whether to save the recording of the animation. (Default to False).
    """

    # Attaching 3D axis to the figure
    fig = plt.figure()
    ax = p3.Axes3D(fig)

    # Initialize scatters
    scatters = [ ax.scatter(data[0][i,0:1], data[0][i,1:2], data[0][i,2:]) for i in range(data[0].shape[0]) ]

    # Number of iterations
    iterations = len(data)
    
    # Setting the axes properties
    ax.set_xlim3d([-0.1, 0.1])
    ax.set_xlabel('X')

    ax.set_ylim3d([-0.1, 0.1])
    ax.set_ylabel('Y')

    ax.set_zlim3d([-0.1, 0.1])
    ax.set_zlabel('Z')

    ax.set_title('3D Animated Scatter Example')

    # Provide starting angle for the view.
    ax.view_init(25, 10) # (azim, elev)

    ani = animation.FuncAnimation(fig, animate_scatters, iterations, fargs=(data, scatters),
                                       interval=1, blit=False, repeat=True)

    if save:
        Writer = animation.writers['ffmpeg']
        writer = Writer(fps=60, metadata=dict(artist='Me'), bitrate=1800, extra_args=['-vcodec', 'libx264'])
        ani.save('3d-scatted-animated.mp4', writer=writer)

    plt.show()

# Program

speed = int(raw_input('choose speed (1 <= int <= 20) : '))
data = read_data('out.txt', speed)
main(data, save=False)
