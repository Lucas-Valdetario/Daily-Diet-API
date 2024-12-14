class Snack:
    def __init__(self, id, title, description, date, diet=False) -> None:
        self.id = id
        self.title = title
        self.description = description
        self.date = date
        self.diet = diet

    def to_dict(self):
        return {
            "id" : self.id,
            "title" : self.title,
            "description" : self.description,
            "date" : self.date,
            "diet" : self.diet
        } 