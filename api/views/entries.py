from datetime import date

from flask import Blueprint, jsonify, request

from api.database.store import diary_entry_db
from api.models.diary import Diary, Helper

helper = Helper()

diary = Blueprint('diary_app', __name__)


@diary.route('/entries', methods=['POST'])
def create_entry():
    json_data = request.get_json()
    title = json_data['title']
    content = json_data['content']

    entry = helper.check_entry(title, content)
    if entry:
        ent_date = date.today()
        ent_id = len(diary_entry_db) + 1
        new_ent = Diary(ent_id, ent_date, title, content)

        diary_entry_db.append(new_ent)
        return jsonify({'Entry created': vars(new_ent)}), 201
    return jsonify(message='No request created'), 400


@diary.route('/entries/<int:entryId>', methods=['GET'])
def get_entry(entryId):
    for ent in diary_entry_db:
        if ent.eid == entryId:
            return jsonify({'Entry found': vars(ent)}), 200
        return jsonify(message='Not found'), 404
