from engine.components.coordinates.screen import Screen
from engine.components.types.area_object import AreaObject
import geopandas
import matplotlib.pyplot as plt


class PolyGenerator:

    def __init__(self, data_path):
        self.data_path: str = data_path

    def load_data(self):
        return geopandas.read_file(self.data_path)

    def generate(self, screen: Screen) -> list[AreaObject]:
        areas = []
        print("generate poly")
        data_fr = self.load_data()
        data_fr['centroid_column'] = data_fr.centroid

        print(data_fr.info())
        minx, miny, maxx, maxy = data_fr.total_bounds

        width = maxx - minx
        height = maxy - miny
        scale = screen.height / height
        # data_fr["game_x"] = (data_fr["geometry"].bounds["minx"] - minx) * scale
        # data_fr["game_y"] = screen.height - (data_fr["geometry"].bounds["miny"] - miny) * scale

        miny_scaled = miny * scale
        minx_scaled = minx * scale

        print(data_fr.loc[data_fr['nimi'] == 'Rovaniemi']["geometry"])
        data_fr.geometry = data_fr.geometry.scale(xfact=scale, yfact=scale, zfact=1.0, origin=(-minx_scaled, -miny_scaled))

        # data_fr["game_x"] = data_fr["geometry"].bounds["minx"]
        # data_fr["game_y"] = screen.height - data_fr["geometry"].bounds["miny"]

        print(data_fr.loc[data_fr['nimi'] == 'Rovaniemi']["geometry"])
        # minx, miny, maxx, maxy = data_fr.total_bounds
        # data_fr.geometry = data_fr.geometry.scale(xfact=1.0, yfact=1.0, zfact=1.0, origin=(minx, miny))

        # data_fr.plot()
        # plt.show()

        for index, row in data_fr.iterrows():
            area = AreaObject(name=row["nimi"], polygon=row["geometry"])
            # area.position = int(row['game_x']), int(row['game_y'])
            print(f'{area.name} {area.position}')
            # print(row["geometry"].geoms[0].bounds)
            # print(row['centroid_column'].x)
            # print(row['centroid_column'].y)
            areas.append(area)

        return areas
