import os

from sqlalchemy import create_engine

URL = os.getenv('DB_URL')

engine = create_engine(URL)
