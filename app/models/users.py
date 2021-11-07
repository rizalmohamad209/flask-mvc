from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)


class Mahasiswa(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False)
    nama = db.Column(db.String(100), nullable=False)
    kabupaten = db.Column(db.String(100), nullable=False)
    provinsi = db.Column(db.String(100), nullable=False)

    def __init__(self, nama, kabupaten, provinsi):
        self.nama = nama
        self.kabupaten = kabupaten
        self.provinsi = provinsi
