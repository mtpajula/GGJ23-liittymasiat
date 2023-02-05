from engine.components.coordinates.screen import Screen
import geopandas
from lapland_defence.game_objects.game.municipality import Municipality
from lapland_defence.generators.soldier_types import FactionType


class PolyGenerator:

    def __init__(self, data_path):
        self.data_path: str = data_path

    def load_data(self):
        return geopandas.read_file(self.data_path)

    def generate(self, screen: Screen) -> list[Municipality]:
        areas = []
        print("generate poly")
        data_fr = self.load_data()
        data_fr['centroid_column'] = data_fr.centroid

        print(data_fr.info())
        minx, miny, maxx, maxy = data_fr.total_bounds

        height = maxy - miny
        scale = screen.height / height

        miny_scaled = miny * scale
        minx_scaled = minx * scale

        data_fr.geometry = data_fr.geometry.scale(
            xfact=scale, yfact=scale,
            zfact=1.0,
            origin=(-minx_scaled, -miny_scaled)
        )

        for index, row in data_fr.iterrows():
            area = Municipality(name=row["nimi"], polygon=row["geometry"], faction=FactionType.PLAYER)
            areas.append(area)

        self.set_faction_types(areas)

        return areas

    def find_area(self, areas: list[Municipality], name: str):
        for area in areas:
            if area.name == name:
                return area
        return None

    def set_faction_types(self, areas: list[Municipality]):
        nda = self.find_area(areas=areas, name='Enontekiö')
        nda.faction = FactionType.P23G
        self.set_closest_types(areas=areas, base_area=nda)

        sirpa = self.find_area(areas=areas, name='Kuusamo')
        sirpa.faction = FactionType.PIRJO
        self.set_closest_types(areas=areas, base_area=sirpa)

        paula = self.find_area(areas=areas, name='Vaala')
        paula.faction = FactionType.LOL
        self.set_closest_types(areas=areas, base_area=paula)

    def set_closest_types(self, areas: list[Municipality], base_area: Municipality):
        for area in areas:
            # print(area.polygon.distance(base_area.polygon))
            if area.polygon.distance(base_area.polygon) < 0:
                area.faction = base_area.faction
