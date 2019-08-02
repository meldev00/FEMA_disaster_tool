def draw_heat_map(center, df, radius = 16):
    """ Takes in the center as a tuple and returns a heat map of the life lines in the given area."""

    from ipyleaflet import Map,Marker,CircleMarker,Heatmap
    from ipywidgets import HTML
    from ipyleaflet import Popup

    m = Map(center = center, zoom = 11)

    heatmap = Heatmap(
        locations=[(df.loc[i, "lat"], df.loc[i,"lng"]) for i in df.index],
        radius= radius
    )

    m.add_layer(heatmap);

    return display(m)
