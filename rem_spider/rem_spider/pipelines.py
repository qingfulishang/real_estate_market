# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, Numeric
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()
class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String(40))
    birthdate = Column(String(20))
    bio = Column(String(1000))
    def __repr__(self):
        return "<Author(name='%s', birthdate='%s', bio='%s')>" % (
                            self.name, self.birthdate, self.bio)
class RemNewHouseInfo(Base):
    __tablename__ = 'rem_new_house_infos'
    rnhi_id = Column(Integer, primary_key=True)
    rnhi_city = Column(String(20))
    rnhi_district = Column(String(20))
    rnhi_block = Column(String(20))
    rnhi_neighbourhood = Column(String(20))
    rnhi_price = Column(Integer)
    rnhi_size = Column(Numeric(5,2))
    rnhi_type = Column(String(40))
    rnhi_floor = Column(String(40))
    rnhi_direction = Column(String(10))
    rnhi_metro = Column(String(100))
    rnhi_uri = Column(String(60))
    rnhi_time = Column(String(10))
    rnhi_create_time = Column(DateTime, index=True, default=datetime.utcnow)
    rnhi_update_time = Column(DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return "<RemNewHouseInfo(uri='%s')>" % (self.uri)

class RemOldHouseInfo(Base):
    __tablename__ = 'rem_old_house_infos'
    rohi_id = Column(Integer, primary_key=True)
    rohi_city = Column(String(20))
    rohi_district = Column(String(20))
    rohi_block = Column(String(20))
    rohi_neighbourhood = Column(String(20))
    rohi_price = Column(Integer)
    rohi_size = Column(Numeric(5,2))
    rohi_type = Column(String(40))
    rohi_floor = Column(String(40))
    rohi_direction = Column(String(10))
    rohi_metro = Column(String(100))
    rohi_uri = Column(String(60))
    rohi_time = Column(String(10))
    rohi_create_time = Column(DateTime, index=True, default=datetime.utcnow)
    rohi_update_time = Column(DateTime, index=True, default=datetime.utcnow)
 
    def __repr__(self):
        return "<RemOldHouseInfo(uri='%s')>" % (self.uri)

class RemRentHouseInfo(Base):
    __tablename__ = 'rem_rent_house_infos'
    rrhi_id = Column(Integer, primary_key=True)
    rrhi_city = Column(String(20))
    rrhi_district = Column(String(20))
    rrhi_block = Column(String(20))
    rrhi_neighbourhood = Column(String(20))
    rrhi_price = Column(Integer)
    rrhi_size = Column(Numeric(5,2))
    rrhi_type = Column(String(40))
    rrhi_floor = Column(String(40))
    rrhi_direction = Column(String(10))
    rrhi_metro = Column(String(100))
    rrhi_uri = Column(String(60))
    rrhi_time = Column(String(10))
    rrhi_create_time = Column(DateTime, index=True, default=datetime.utcnow)
    rrhi_update_time = Column(DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return "<RemRentHouseInfo(uri='%s')>" % (self.uri)

class MySQLPipeline(object):

    collection_name = 'scrapy_items'

    def __init__(self, mysql_uri="mysql://root:123456@localhost/quotes?charset=utf8"):
        self.mysql_uri = mysql_uri


    def open_spider(self, spider):
        engine = create_engine(self.mysql_uri, echo=True)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()        

    def close_spider(self, spider):
        pass

    def process_item(self, item, spider):
        author=Author(name=(item['name'].replace("\\",'')),birthdate=(item['birthdate'].replace("\\",'')),bio=(item['bio'].replace("\\",'')))
        self.session.add(author)
        self.session.commit()
        return item
