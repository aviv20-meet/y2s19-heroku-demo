from model import Base, Idiot

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///idiots.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_idiot(first_name,last_name,gender,stupidness_level):

	idiot_object = Idiot(
			idiot_first_name = first_name,
			idiot_last_name = last_name,
			idiot_gender = gender,
			idiot_stupidness_level = stupidness_level)
	session.add(idiot_object)
	session.commit()
def query_all():
	return session.query(Idiot).all()
def delete_by_name(first_name,last_name):
	session.query(Idiot).filter_by(idiot_first_name=idiot_first_name).filter_by(idiot_last_name = last_name).delete()
	session.commit()
def delete_all():
	session.query(Idiot).delete()
	session.commit()
