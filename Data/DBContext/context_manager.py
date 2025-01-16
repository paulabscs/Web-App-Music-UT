from contextlib import contextmanager
from Data.DBContext.session_manager import get_or_create_session, close_session

@contextmanager
def session_scope():
    session = get_or_create_session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        close_session()
