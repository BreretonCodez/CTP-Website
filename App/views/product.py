from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt import jwt_required, current_identity

from App.controllers import (
    create_prod,
    update_prod,
    search_prod,
    delete_prod,
    get_all_prods,
    get_all_prods_json,
    get_prod_by_id,
)

prod_views = Blueprint('prod_views', __name__, template_folder='../templates')

# JINJA ROUTES

@prod_views.route('', methods=[])

@prod_views.route('', methods=[])

@prod_views.route('', methods=[])

# API ROUTES