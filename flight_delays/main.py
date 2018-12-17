
# coding: utf-8

# os methods for manipulating paths
import os

# Pandas for data management
import pandas as pd


# Bokeh basics
from bokeh.io import curdoc
from bokeh.models.widgets import Tabs
# Using included state data from Bokeh for map
from bokeh.sampledata.us_states import data as states

import flight_delays

# Each tab is drawn by one script
from flight_delays.histogram import histogram_tab
from flight_delays.density import density_tab
from flight_delays.table import table_tab
from flight_delays.draw_map import map_tab
from flight_delays.routes import route_tab


def modify_doc(doc) :
	ifolder = os.path.join(os.path.dirname(__file__), '..', 'data')
	# Read data into dataframes
	flights = pd.read_csv(os.path.join(ifolder, 'flights.csv'), index_col=0).dropna()

	# Formatted Flight Delay Data for map
	map_data = pd.read_csv(os.path.join(ifolder, 'flights_map.csv'), header=[0,1], index_col=0)

	# Create each of the tabs
	tab1 = histogram_tab(flights)
	tab2 = density_tab(flights)
	tab3 = table_tab(flights)
	tab4 = map_tab(map_data, states)
	tab5 = route_tab(flights)

	# Put all the tabs into one application
	tabs = Tabs(tabs = [tab1, tab2, tab3, tab4, tab5])

	# Put the tabs in the current document for display
	doc.add_root(tabs)


def main() :
	modify_doc(curdoc())

if (__name__ == 'main') or (__name__ == 'bk_script_1001') :
    main()

print(__name__)
#main()