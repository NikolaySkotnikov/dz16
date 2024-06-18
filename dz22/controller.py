from view import View
from model import Model


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def run(self):
        query = None
        while query != '0':
            query = self.view.get_next_query()
            self.execute_query(query)

    def execute_query(self, query):
        if query == '1':
            shoes_data = self.model.get_shoes_data()
            self.view.show_data(shoes_data)
        if query == '2':
            shoes = self.view.add_user_shoes()
            self.model.add_shoes_to_data(shoes)
        if query == '3':
            keywords = self.view.get_keywords()
            shoes = self.model.get_shoes_by(keywords)
            if len(shoes) == 0:
                self.view.get_massage()
                return
            if len(shoes) > 1:
                num_to_del = self.view.get_number(shoes)
                shoes = [shoes[num_to_del - 1]]
            self.model.remove_shoes(shoes[0])
        if query == '4':
            keywords = self.view.get_keywords()
            shoes = self.model.get_shoes_by(keywords)
            self.view.show_data(shoes)
