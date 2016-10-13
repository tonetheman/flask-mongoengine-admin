from flask import Blueprint, render_template, abort, request, redirect
from app import app
from models import Tag, Category, Item

import json

def json_response(data):
    return json.dumps(data)


admin = Blueprint('admin', __name__, template_folder='templates')

@admin.route('/')
def index():
    return redirect('/admin/')


@admin.route("/admin/")
def admin_ui():
    return render_template('/admin/index.html')
