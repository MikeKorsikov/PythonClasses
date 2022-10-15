import json


class People:
    def __init__(self, first_name=None, last_name=None):
        self.first_name = first_name
        self.last_mname = last_name

    @staticmethod
    def getAll():
        result = []
        with open('db.json') as f:
            data = list(json.loads(f.read()).values())
            #print(data)
            for person in data:
                result.append(People(person['first_name'], person['last_name']))
        return result

    def __str__(self):
        return f"{self.first_name} {self.last_mname}"

    @staticmethod
    def saveAll(people_list):
        pass

