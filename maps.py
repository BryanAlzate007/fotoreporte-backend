
import folium
import branca


m = folium.Map(
    location=(4.812945, -75.705135),
    zoom_start=12,
    )


html = """
    <h1><img src="https://drive.google.com/file/d/1lGh9jti9mQIaXOcy4pExLwR2P74H_zGm/view" title="source: imgur.com" /></h1><br>
    With a few lines of code...
    <p>
    <code>
        from numpy import *<br>
        exp(-2*pi)
    </code>
    </p>
    """
    
folium.Marker(
    location=[4.829599, -75.698683],
    tooltip="Click me!",
    popup=html,
    icon=folium.Icon(color="blue"),
).add_to(m)



m.save("index.html")