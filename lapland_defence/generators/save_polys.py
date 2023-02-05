
import pickle


class SavePolys:

    @staticmethod
    def save(filepath, areas):
        print(f'Write storage to {filepath}')
        serialized = pickle.dumps(areas)
        with open(filepath, 'wb') as file_object:
            file_object.write(serialized)

    @staticmethod
    def load(filepath):
        areas = None
        print(f'Read storage from {filepath}')
        try:
            with open(filepath, 'rb') as file_object:
                raw_data = file_object.read()
            areas = pickle.loads(raw_data)
        except FileNotFoundError:
            print("Cache", "No file")

        return areas
