
# coding: utf-8

# os methods for manipulating paths
import os

# pandas and numpy for data manipulation
import numpy as np
import pandas as pd


# Bokeh plotting tools
from bokeh.models import ColumnDataSource, Panel
from bokeh.models.widgets import TableColumn, DataTable, Tabs


# Draw a table with summary statistics by airline
def table_tab(flights):

	# Calculate summary stats for table
	carrier_stats = flights.groupby('name')['arr_delay'].describe()
	columns = {'name': 'airline', 'count': 'flights', '50%': 'median'}
	carrier_stats = carrier_stats.reset_index().rename(columns=columns)
	# Round statistics for display
	carrier_stats['mean'] = carrier_stats['mean'].round(2)
	carrier_src = ColumnDataSource(carrier_stats)

	# Columns of table
	table_columns = [TableColumn(field='airline', title='Airline'),
					 TableColumn(field='flights', title='Number of Flights'),
					 TableColumn(field='min', title='Min Delay'),
					 TableColumn(field='mean', title='Mean Delay'),
					 TableColumn(field='median', title='Median Delay'),
					 TableColumn(field='max', title='Max Delay')]

	carrier_table = DataTable(source=carrier_src, 
							  columns=table_columns, width=1000)

	tab = Panel(child = carrier_table, title = 'Summary Table')

	return tab


def modify_doc(doc) :
	ifolder = os.path.join(os.path.dirname(__file__), '..', 'data')
	# Read data into dataframes
	# Flights and Airlines
	flights = pd.read_csv(os.path.join(ifolder, 'flights.csv'), index_col=0).dropna()

	# Create the tabs and put the tabs into one application
	tabs = Tabs(tabs = [table_tab(flights)])

	# Put the tabs in the current document for display
	# Map of Flight Delays
	doc.add_root(tabs)


def main() :
	modify_doc(curdoc())
