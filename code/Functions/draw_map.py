def draw_map(center, life_line_df):

    """Takes in the epicenter of a storm and returns a map of the life-lines in that area. Life-lines can be clicked on to see category and description."""

    df = life_line_df
    m = Map(center = center, zoom = 15)

    from ipyleaflet import Map,Marker,CircleMarker,Heatmap
    from ipywidgets import HTML
    from ipyleaflet import Popup

    for i in df.index:
        marker = Marker(location = [df.loc[i, "lat"], df.loc[i, "lng"]])
        m.add_layer(marker)
        message1 = HTML()
        message1.value = df.loc[i, 'name']
        message1.description = df.loc[i, "FEMA Lifeline"]
        popup = Popup(
            location=[df.loc[i, "lat"], df.loc[i, "lng"]],
            close_button=True,
            max_width = 400
        )
        m.add_layer(popup)
        marker.popup = message1

    return display(m)
