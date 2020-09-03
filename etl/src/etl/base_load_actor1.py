import logging
import psycopg2
from .base import BaseCreate
from actor1_1.models import Customer

logger = logging.getLogger(__name__)


conn = psycopg2.connect(
    database="ppcazine",
    user="ppcazine",
    password="Hx17_KF9iab-EL7bizHv-mJzcfB5lSJc",
    host="postgres://ppcazine:Hx17_KF9iab-EL7bizHv-mJzcfB5lSJc@ruby.db.elephantsql.com:5432/ppcazine",
    port="5432"
)

cur = conn.cursor()
# One time run to create table scehma
cur.execute('''CREATE TABLE COMPANY
      (ID INT PRIMARY KEY     NOT NULL,
      NAME           TEXT    NOT NULL,
      CITY         REAL);''')

conn.commit()
conn.close()


class FetchData(BaseCreate):

    def perform(self):
        """Main method"""
        data = Customer.objects.all()
        for i in data:
            cur.execute(
                "INSERT INTO COMPANY (ID,NAME,CITY) VALUES (i.id, i.name, i.city)")

        # logger.info('%s starts...', )
