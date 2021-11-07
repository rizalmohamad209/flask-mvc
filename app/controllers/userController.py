from app import app
from flask import render_template, request
from app.models.users import db, Mahasiswa


@app.route('/user', methods=['POST', 'GET'])
def user():
    if request.method == 'POST':
        nama = request.form['nama']
        kabupaten = request.form['kabupaten']
        provinsi = request.form['provinsi']
        try:
            mhs = Mahasiswa(nama=nama, kabupaten=kabupaten, provinsi=provinsi)
            db.session.add(mhs)
            db.session.commit()
        except Exception as e:
            print("Failed to add data.")
            print(e)
    listMhs = Mahasiswa.query.all()
    print(listMhs)
    return render_template("users.html", data=enumerate(listMhs, 1))


@app.route('/userCreate', methods=['POST', 'GET'])
def userCreate():

    return render_template("formcreate.html")
