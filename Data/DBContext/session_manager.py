from threading import local
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from Data.Models.Track import Base

DATABASE_URI = 'sqlite:///Data/Source/UTDatabase.db'

db_engine = create_engine(DATABASE_URI)
Base.metadata.drop_all(db_engine, tables=[Base.metadata.tables['tracks']])
Base.metadata.create_all(db_engine)
SessionFactory = sessionmaker(bind=db_engine)

# Thread-local storage to ensure no conflict across threads
thread_storage = local()

def get_or_create_session():
    # Check for an existing session
    if getattr(thread_storage, 'session', None) is None:
        # No existing session, create a new one
        session = scoped_session(SessionFactory)
        thread_storage.session = session
    return thread_storage.session()

def close_session():
    session = getattr(thread_storage, 'session', None)
    if session:
        session.close()
        thread_storage.session = None
