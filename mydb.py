from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class CRM(Base):
    __tablename__ = 'CRM'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))

engine = create_engine('sqlite:///:memory:', echo=True)

Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

new_crm_entry = CRM(name='SMCRM')
session.add(new_crm_entry)
session.commit()

print("All Done!")
