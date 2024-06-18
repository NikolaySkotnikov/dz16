import json


class Shoes:

    shoes_parameters = ['Тип обуви',
                        'Вид обуви',
                        'Цвет',
                        'Цена',
                        'Производитель',
                        'Размер']

    def __init__(self, type_shoes, view_shoes, color, price, manufacturer, size):
        self.type_shoes = type_shoes
        self.view_shoes = view_shoes
        self.color = color
        self.price = price
        self.manufacturer = manufacturer
        self.size = size

    def __str__(self):
        result = {}
        for key, par in zip(self.shoes_parameters, self.__dict__.values()):
            result[key] = par
        return (f'{self.view_shoes.capitalize()}\n\t' +
                '\n\t'.join(f'{key}: {value}' for key, value in result.items()))


class JsonWork:
    @staticmethod
    def load_json(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    @staticmethod
    def dump_json(filename, data):
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2)


class Model:
    def __init__(self):
        self.filename = 'data.json'
        try:
            data = JsonWork.load_json(self.filename)
            self.shoes = {}
            for key, value in data.items():
                self.shoes[key] = Shoes(*value.values())
        except FileNotFoundError:
            JsonWork.dump_json(self.filename, {})
            self.shoes = {}
        except json.decoder.JSONDecodeError:
            self.shoes = {}

    def get_shoes_data(self):
        return self.shoes.values()

    def add_shoes_to_data(self, data):
        shoes = Shoes(*data.values())
        if len(self.shoes) == 0:
            key_dict = 1
        else:
            key_dict = len(self.shoes.keys()) + 1
        self.shoes[f'shoes{key_dict}'] = shoes
        dict_shoes = JsonWork.load_json(self.filename)
        dict_shoes[f'shoes{key_dict}'] = shoes.__dict__
        JsonWork.dump_json(self.filename, dict_shoes)

    def get_shoes_by(self, keywords):
        words = list(map(str.strip, keywords.split(',')))
        shoes = []
        for word in words:
            for sh in self.shoes.values():
                if word.lower() in " ".join(map(str, sh.__dict__.values())).lower() and sh not in shoes:
                    shoes.append(sh)
        return shoes

    def remove_shoes(self, shoes):
        print(self.shoes.values())
        shoes_list = [i for i in self.shoes.values()]
        shoes_list.remove(shoes)
        self.shoes.clear()
        for i in range(len(shoes_list)):
            self.shoes[f'shoes{i + 1}'] = shoes_list[i]
        dict_shoes = {}
        for key, val in self.shoes.items():
            dict_shoes[key] = val.__dict__
        JsonWork.dump_json(self.filename, dict_shoes)
