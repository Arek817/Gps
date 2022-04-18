from gps_class import GPSVis

vis = GPSVis(data_path='E:/gps.csv',
             map_path='E:/map.png',  # Path to map downloaded from the OSM.
             points=(50.0138, 19.0039, 49.9814, 19.0827)) # Two coordinates of the map (upper left, lower right)

vis.create_image(color=(0, 0, 255))  # Set the color and the width of the GNSS tracks.
vis.plot_map(output='save')

print()