# conda install -c anaconda flask
from flask import Flask
import folium
import pandas as pd

app = Flask(__name__)


@app.route('/')
def index():
    start_coords = (37.550966, 126.849532)
    folium_map = folium.Map(location=start_coords, zoom_start=14)
    return folium_map._repr_html_()

@app.route('/marker')

def marker():
    coffee_list = pd.read_csv('coffee.csv')

    mapping = folium.Map(location=[coffee_list['위도'].mean(), coffee_list['경도'].mean()], zoom_start=14)

    color_dict = {'스타벅스': 'blue', '이디야커피': 'green', '투썸플레이스': 'red', '빽다방': 'gray'}
    icon_dict = {'스타벅스': 'glyphicon glyphicon-globe', '이디야커피': 'glyphicon glyphicon-unchecked', '투썸플레이스': 'glyphicon glyphicon-heart-empty', '빽다방': 'cloud'}

    for i in coffee_list.index:
        folium.Marker(
        location=[coffee_list['위도'][i], coffee_list['경도'][i]],
        popup=coffee_list['상호명'][i],
        icon=folium.Icon(color=color_dict[coffee_list['상호명'][i]], icon= icon_dict[coffee_list['상호명'][i]])
    ).add_to(mapping)

    folium.CircleMarker(
    location=[coffee_list['위도'].mean(), coffee_list['경도'].mean()],
    radius=500,
    popup='원 그림',
    color='red').add_to(mapping)

    return mapping._repr_html_()

if __name__ == '__main__':
    app.run(debug=True)