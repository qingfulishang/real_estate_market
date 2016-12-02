# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

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
