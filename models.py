from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()           #SQLAlchemy를 사용해 데이터베이스 저장

class Fcuser(db.Model): 
    __tablename__ = 'fcuser'   #테이블 이름 : fcuser
    id = db.Column(db.Integer, primary_key = True)   #id를 프라이머리키로 설정
    username = db.Column(db.String(8))
    useremail = db.Column(db.String(32))       #이하 위와 동일
    password = db.Column(db.String(64))     #패스워드를 받아올 문자열길이 
    author = db.Column(db.String(8))
    genre = db.Column(db.String(64))
    way = db.Column(db.String(8))
    