# quiltz-testsupport

A package for test support

## Purpose

At QWAN we're building some applications in python. We collect usefull stuff in quiltz packages:

* **quiltz_domain**
  contains domain level modules like, entity id's, results, an email anonymizer, validators and parsers
* **quiltz_testsupport**
  contains test support modules, that supports mainly non unit tests, like integrating with smtp,  probing asynchronous results and asserting log statements
* **quilts_messaging**
  contains a messaging domain concept and an engine(s) to send the messages. Currently only smtp sending is supported.

## modules in this packag

### logging
With the logging module you can assert log statements in a test using the log_collector fixture:

#### in test:
```python
from quiltz.testsupport import log_collector
def test_logs_hello(log_collector):
    foo()
    log_collector.assert_info('hello info')
```

#### in production
```python
def foo():
    logger = logging.getLogger()
    logger.info('hello info')
```

### probing
With the probing module you can probe for async results:

```python
from hamcrest import assert_that, equal_to
from quiltz.testsupport import probe_that

def test_stub_server_collects_message_for_recepient(self):        
    message = aMessage(recipient='rob@mailinator.com', sender='no-reply@qwan.eu', subject='test', body='hello test')
    self.message_engine.send([message])
    
    probe_that(lambda: assert_that(self.server.messages, equal_to([
        stringified_message(message)
    ])))
```

### smtp
With the smtp module you can create a stub smtp server that collects smtp messages

```python
from hamcrest import assert_that, equal_to
from quiltz.testsupport import probe_that
def server()
    server = StubSmtpServer(hostname='localhost', port=9925)
    server.start()
    yield(server)
    server.stop()

def test_collects_message_for_recepient(self, server): 
    message_engine = SMTPClientForTest(host='localhost', port='9925')
    message = aMessage(recipient='rob@mailinator.com', sender='no-reply@qwan.eu', subject='test', body='hello test')
    message_engine.send([message])
    
    probe_that(lambda: assert_that(server.messages, equal_to([
        stringified_message(message)
    ])))
```

## installing 

```bash
pip install quiltz_testsupport
```

