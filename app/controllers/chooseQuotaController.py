from app import app
from flask import render_template


@app.route('/choose', methods=['GET'])
def choose():
    return render_template('chooseQuota.html')
