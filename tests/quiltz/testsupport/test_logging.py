from testing import *
from quiltz.testsupport import log_collector
import logging

class TestLogCollector:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.logger = logging.getLogger(self.__class__.__name__)

    def test_collects_info_message(self, log_collector):
        self.logger.info('hello info')
        log_collector.assert_info('hello info')

    def test_collects_warning_message(self, log_collector):
        self.logger.warn('hello warning')
        log_collector.assert_warning('hello warning')