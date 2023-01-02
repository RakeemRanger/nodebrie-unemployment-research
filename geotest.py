import geopandas as gpd
import pandas as pd 

county = gpd.read_file('tl_2016_39_cousub.shp')

county2 = county.cx[:,:]

county2.to_csv('oh_coordinates.csv')

county2[:,:]