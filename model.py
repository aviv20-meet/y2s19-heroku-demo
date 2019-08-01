from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Idiot(Base):
	__tablename__ = 'idiots'
	idiot_id = Column(Integer,primary_key=True)
	idiot_first_name = Column(String)
	idiot_last_name = Column(String)
	idiot_gender = Column(String)
	idiot_stupidness_level = Column(String)

	def __repr__(self):
		return ("Idiot's First Name: {}\n"
				"idiot's Last Name: {}\n"
				"Idiot's gender: {}\n"
				"Idiot's stupidness level: {}\n"
				"ID: {}").format(
					self.idiot_first_name,
					self.idiot_last_name,
					self.idiot_gender,
					self.idiot_stupidness_level,
					self.idiot_id)