from testing import *
from quiltz.testsupport import probe_that, log_collector
from hamcrest import raises
import time

class TestProbeThat_with_assert_that:
    def test_fails_on_assert_that_fails(self):
        assert_that(lambda: probe_that(lambda: assert_that(service_returning_true_eventually(), is_(False))), raises(AssertionError))

    def test_passes_on_assert_that_passes(self):
        probe_that(lambda: assert_that(service_returning_true_eventually(), is_(True)))

def service_returning_true_eventually(delay=0.02):
    time.sleep(delay)
    return True