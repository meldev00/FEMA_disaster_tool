def fema_tool(data):

    import pandas as pd
    import numpy as np
    import math
    from Functions import distance_formula, draw_heat_map, return_stats
    from ipyleaflet import Map,Heatmap

    lat = float(input("What is the latitude of the center of the distaster?"))
    lng = float(input("What is the longitude of the center of the distaster?"))
    origin = (lat, lng)

    radius = float(input("What is the radius of destruction for the event(in km)?"))

    df = return_stats.return_stats(origin, radius, data)

    draw_heat_map.draw_heat_map(origin, df)

    response = input("Return a table of affected life-lines? Please respond with 'y' or 'n'.")

    if response.lower() == "y":
        return df
    elif response.lower() == "n":
        pass
    else:
        print ("We could not understand your response. Please rerun program to choose again.")
