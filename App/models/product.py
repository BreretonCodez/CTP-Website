from App.database import db

class Product(db.Model):
    prodId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    desc = db.Column(db.String, nullable=True)
    cost = db.Column(db.Integer, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    supplier = db.Column(db.String, nullable=True)

    def __init__(self, name, cost, stock):
        self.name = name
        self.cost = cost
        self.stock = stock

    def toJSON(self):
        return {
            'prodId': self.prodId,
            'name': self.name,
            'description': self.desc,
            'cost': self.cost,
            'stock': self.stock,
            'supplier': self.supplier
        }

    def get_id(self):
        return str(self.prodId)
