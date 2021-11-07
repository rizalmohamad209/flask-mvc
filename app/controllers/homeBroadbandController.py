from app import app
from flask import render_template


@app.route('/homebroadband', methods=['GET'])
def broadband():
    return render_template('homeBroadband.html')
