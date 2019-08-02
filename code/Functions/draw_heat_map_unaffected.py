def not_affected_heatmap(affected_df, original_df):

    """ This returns a heatmap of life-lines listed in the dataset that are NOT in the reported affected area.""" 

    from Functions import draw_heat_map

    life_lines_not_affected = original_df.drop(affected_df.index)

    draw_heat_map.draw_heat_map((29.9511, -90.0715), life_lines_not_affected)
