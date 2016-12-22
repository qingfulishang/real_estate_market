# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, Numeric
from sqlalchemy.orm import sessionmaker
from datetime import date

table_name_prefix = "sz_"
table_name_suffix = str(date.today()).replace("-","_")
Base = declarative_base()
class RemNewHouseInfo(Base):
    __tablename__ = table_name_prefix + 'rem_new_house_infos' + table_name_suffix
    rnhi_id = Column(Integer, primary_key=True)
    rnhi_district = Column(String(20))
    rnhi_block = Column(String(20))
    rnhi_neighbourhood = Column(String(20))
    rnhi_price = Column(Integer)
    rnhi_size = Column(Numeric(5,2))
    rnhi_type = Column(String(40))
    rnhi_floor = Column(String(40))
    rnhi_direction = Column(String(10))
    rnhi_metro = Column(String(100))
    rnhi_uri = Column(String(60), index=True)
    rnhi_time = Column(String(10))

    def __repr__(self):
        return "<RemNewHouseInfo(uri='%s')>" % (self.uri)

class RemOldHouseInfo(Base):
    __tablename__ = table_name_prefix + 'rem_old_house_infos' + table_name_suffix
    rohi_id = Column(Integer, primary_key=True)
    rohi_district = Column(String(20))
    rohi_block = Column(String(20))
    rohi_neighbourhood = Column(String(20))
    rohi_price = Column(Integer)
    rohi_size = Column(Numeric(5,2))
    rohi_type = Column(String(40))
    rohi_floor = Column(String(40))
    rohi_direction = Column(String(10))
    rohi_metro = Column(String(100))
    rnhi_uri = Column(String(60), index=True)
    rohi_time = Column(String(10))

    def __repr__(self):
        return "<RemOldHouseInfo(uri='%s')>" % (self.uri)

class RemRentHouseInfo(Base):
    __tablename__ = table_name_prefix + 'rem_rent_house_infos' + table_name_suffix
    rrhi_id = Column(Integer, primary_key=True)
    rrhi_district = Column(String(20))
    rrhi_block = Column(String(20))
    rrhi_neighbourhood = Column(String(20))
    rrhi_price = Column(Integer)
    rrhi_size = Column(Numeric(5,2))
    rrhi_type = Column(String(40))
    rrhi_floor = Column(String(40))
    rrhi_direction = Column(String(10))
    rrhi_metro = Column(String(100))
    rnhi_uri = Column(String(60), index=True)
    rrhi_time = Column(String(10))

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
        rem_rent_house_info = RemRentHouseInfo(rrhi_district=item['district'],rrhi_block=item['block'],rrhi_neighbourhood=item['neighbourhood'],rrhi_price=item['price'],rrhi_size=item['size'],rrhi_type=item['type'],rrhi_floor=item['floor'],rrhi_direction=item['direction'],rrhi_metro=item['metro'],rrhi_uri=item['uri'],rrhi_time=item['time'])
        self.session.add(rem_rent_house_info)
        self.session.commit()
        return item
