from App.models import Product
from App.database import db

# Creates a new product
def create_prod(name, cost, stock):
    prod = Product(name=name, cost=cost, stock=stock)
    db.session.add(prod)
    db.session.commit()
    return prod

# Updates a product

def update_prod(prodId):
    prod = get_prod_by_id(prodId)
    if prod:
        print(f'Product exists!')
    return None

# Deletes a product

def delete_prod(prodId):
    prod = get_prod_by_id(prodId)
    if prod:
        db.session.delete(prod)
        db.session.commit()
    return None

# Searches for a product

def search_prod(search):
    return Product.query.filter(
        Product.name.like( '%'+search+'%' )
    )

# Product Accessors

def get_prod_by_id(prodId):
    return Product.query.filter_by(prodId=prodId).first()

def get_all_prods():
    return Product.query.all()

def get_all_prods_json():
    prods = Product.query.all()
    if not Product:
        return []
    prods = [prod.toJSON() for prod in prods]
    return prods