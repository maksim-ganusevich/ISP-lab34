from sqlalchemy import PrimaryKeyConstraint
from app import db


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, index=True)
    is_admin = db.Column(db.Integer)
    username = db.Column(db.String(64))
    balance = db.Column(db.Float)
    business_id = db.Column(db.Integer, db.ForeignKey("business.id"))


class AchievementManager(db.Model):
    __tablename__ = 'achievement_manager'
    __table_args__ = (PrimaryKeyConstraint('medal_id', 'user_id'),)
    medal_id = db.Column(db.Integer, db.ForeignKey('medals.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), index=True)


class Medals(db.Model):
    __tablename__ = 'medals'
    id = db.Column(db.Integer, primary_key=True, index=True)
    medal_type = db.Column(db.String(32))


class Business(db.Model):
    __tablename__ = 'business'
    id = db.Column(db.Integer, primary_key=True, index=True)
    company_id = db.Column(db.Integer, db.ForeignKey("company.id"))
    fabric_id = db.Column(db.Integer, db.ForeignKey("fabric.id"))
    monopoly_id = db.Column(db.Integer, db.ForeignKey("monopoly.id"))
    stockexchange_id = db.Column(db.Integer, db.ForeignKey("stockexchange.id"))
    info = db.relationship("BusinessInfo", backref="business", lazy=True)


class BusinessInfo(db.Model):
   __tablename__ = 'business_info'
   id = db.Column(db.Integer, primary_key=True, index=True)
   business_id = db.Column(db.Integer, db.ForeignKey("business.id"))
   info = db.Column(db.String(64))


class Company(db.Model):
    __tablename__ = 'company'
    id = db.Column(db.Integer, primary_key=True, index=True)
    income = db.Column(db.Float)
    price = db.Column(db.Float)
    count = db.Column(db.Integer)


class Fabric(db.Model):
    __tablename__ = 'fabric'
    id = db.Column(db.Integer, primary_key=True, index=True)
    income = db.Column(db.Float)
    price = db.Column(db.Float)
    count = db.Column(db.Integer)


class Monopoly(db.Model):
    __tablename__ = 'monopoly'
    id = db.Column(db.Integer, primary_key=True, index=True)
    income = db.Column(db.Float)
    price = db.Column(db.Float)
    count = db.Column(db.Integer)


class StockExchange(db.Model):
    __tablename__ = 'stockexchange'
    id = db.Column(db.Integer, primary_key=True, index=True)
    income = db.Column(db.Float)
    price = db.Column(db.Float)
    count = db.Column(db.Integer)
