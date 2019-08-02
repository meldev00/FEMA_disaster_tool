def return_stats(origin, radius, life_line_df):

    """ Takes in the epicenter of a storm as a tuple, the radius of the area affected in kilometers, and the dataframe of life-lines in the given city. Returns a breakdown of the life-lines in the affected area by catergory."""

    import pandas as pd
    import numpy as np
    from Functions import distance_formula

    #creating a new dataframe to manipulate
    life_line = life_line_df.copy()

    #this will be the list of distances from the origin
    distances = []

    #runs through each life-line and finds the distance from the origin
    for i in life_line.index:
         distances.append(distance_formula.distance(origin,(life_line.loc[i,"lat"],life_line.loc[i,"lng"])))

    #adds the distance column to the life-line dataframe
    life_line["distance"] = distances

    #creating a new dataframe of the affected area
    affected_area_df = life_line[life_line["distance"] <= radius]

    #creating a list of life-lines in df
    lines = []
    for i in affected_area_df["FEMA Lifeline"].value_counts().index:
        lines.append(i)

    #calculate the total life lines in the zone
    total_life_lines = affected_area_df.shape[0]

    #returns the numerical data of potentially affected buildings to user
    print (f"The total amount of life lines in this area is: {total_life_lines}.")
    print (f"Below is a list of the types of life-lines and how many are in the affected area:")

    #goes through the life lines and counts how many places belong to each category
    for i in lines:
        num_places = affected_area_df["FEMA Lifeline"].value_counts()[i]
        print (f"{i}: {num_places}")

    affected_area_df = affected_area_df.drop(["geometry", "types"], axis = 1)

    return affected_area_df
