import sys
import os

# Add the Plots.py directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'Plots.py'))

from datasets import DatasetLoader
from line_plot import LinePlot


def main():
    # Load the Titanic dataset
    loader = DatasetLoader()
    titanic = loader.load_titanic()

    # Create LinePlot instance and display the plot
    lp = LinePlot(titanic)
    lp.line_plot()


if __name__ == '__main__':
    main()
