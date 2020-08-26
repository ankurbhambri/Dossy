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


class FetchData(BaseCreate):

    def perform(self):
        """Main method"""

        # logger.info('%s starts...', )
