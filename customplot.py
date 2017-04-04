#
# First, let us create some utility functions for Plotting
#

from itertools import cycle, islice
from pandas.tools.plotting import parallel_coordinates
import matplotlib.pyplot as plt
import pandas as pd

def pd_centers(featuresUsed, centers):
	colNames = list(featuresUsed)
	colNames.append('prediction')

	# Zip with a column called 'prediction' (index)
	Z = [np.append(A, index) for index, A in enumerate(centers)]

	# Convert to pandas for plotting
	P = pd.DataFrame(Z, columns=colNames)
	P['prediction'] = P['prediction'].astype(int)
	return P

def parallel_plot(data):
	my_colors = list(islice(cycle(['b', 'r', 'g', 'y', 'k']), None, len(data)))
	plt.figure(figsize=(15,8)).gca().axes.set_ylim([-2.5,+2.5])
	parallel_coordinates(data, 'prediction', color = my_colors, marker='o')