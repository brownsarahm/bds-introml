from matplotlib.colors import LinearSegmentedColormap
import seaborn as sns

colors = ['purple', 'green', 'blue', 'pink' , 'brown', 'red', 'teal' , 'orange',
          'yellow', 'lilac', 'hot pink', 'dark purple', 'sky blue', 'grey']
color_list = sns.xkcd_palette(colors)
color_map = lambda N : LinearSegmentedColormap.from_list('xkcdmap', color_list[:N], N=N)


def plot_pts(x,z, ax=None):
    """
    plot scatter points from a clustering problem, colored by cluster

    Parameters
    -------------
    x : list of 2xN
        points in 2d
    z: list of integers
        assignemnts

    Returns
    ---------
    plt

    """

    if ax is None:
        ax = plt.gca()

    plt_pts =  plt.scatter(__, __,s = 50, c = z, marker = 'x',
                       cmap=color_map(max(z)+1))
    plt.axis([-15,15,-15,15])


    return plt_pts
