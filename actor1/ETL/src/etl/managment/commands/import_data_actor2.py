from django.core.management.base import BaseCommand
from etl.base_load_actor2 import *
from etl.misc import COLORS
import logging
import sys

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'main script'

    def run(self, cls):
        COLORS.ok('Starting..%s' % cls.__class__)
        try:
            cls.perform()
        except KeyboardInterrupt:
            COLORS.warning("Killing ETL Script...")
            sys.exit()
        except Exception as e:
            print('Exception..')
            logger.error(e)
        COLORS.ok('End..%s' % cls.__class__)
        del cls

    def handle(self, *args, **options):
        logger.info('START Renewbuy ETL')
        logger.info('Transaction Table Starts*******************************')
        transaction = Transaction()
        self.run(transaction)
        logger.info('Transaction Table Ends*********************************')
        logger.info('END Renewbuy ETL')
