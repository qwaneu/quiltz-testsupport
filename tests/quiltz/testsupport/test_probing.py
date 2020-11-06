from testing import *
from quiltz.testsupport import probe_that, log_collector
from hamcrest import raises, calling
import time

class TestProbeThat_with_assert_that:
    def test_fails_on_assert_that_fails(self):
        assert_that(lambda: probe_that(lambda: assert_that(service_returning_true_eventually(), is_(False))), raises(AssertionError))

    def test_passes_on_assert_that_passes(self):
        probe_that(lambda: assert_that(service_returning_true_eventually(), is_(True)))

class TestProbeThat_without_assert_that_and_with_a_matcher:
    def test_fails_on_assert_that_fails(self):
        assert_that(calling(probe_that).with_args(service_returning_true_eventually, is_(False)), raises(AssertionError))

    def test_passes_on_assert_that_passes(self):
        probe_that(service_returning_true_eventually, is_(True))

    def test_fails_with_argument_error_when_matcher_is_not_really_a_matcher(self):
        assert_that(
            calling(probe_that).with_args(service_returning_true_eventually, 123), 
            raises(ValueError, "matcher is not a matcher"))


def service_returning_true_eventually(delay=0.02):
    time.sleep(delay)
    return True