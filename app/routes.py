from flask import Blueprint, jsonify
from .system_utils import get_system_stats

main = Blueprint('main', __name__)

@main.route("/stats")
def stats():
    return jsonify(get_system_stats())
