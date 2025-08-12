from flask import Flask, render_template, request
import folium

app = Flask(__name__)

@app.route("/")
def index():
    m = folium.Map(location=[-6.200000, 106.816666], zoom_start=12)
    folium.Marker(
        location=[-6.2, 106.816666],
        popup="Jakarta",
        tooltip="Click for more info"
    ).add_to(m)
    map_html = m._repr_html_()
    return render_template("index.html", map_html=map_html)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
