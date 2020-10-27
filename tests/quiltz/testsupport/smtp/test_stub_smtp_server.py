from testing import *
from smtplib import SMTP
import ssl
from email.message import EmailMessage
from quiltz.testsupport.smtp import StubSmtpServer
from quiltz.testsupport import probe_that, log_collector

class TestSMTPStubServer:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.server = StubSmtpServer(hostname='localhost', port=9925)
        self.message_engine = SMTPBasedMessageEngineForTest(host='localhost', port='9925')
        self.server.start()
        yield
        self.server.stop()

        def test_collects_message_for_recepient(self):        
            message = aMessage(recipient='rob@mailinator.com', sender='no-reply@qwan.eu', subject='test', body='hello test')
            self.message_engine.send([message])
            
            probe_that(lambda: assert_that(self.server.messages, equal_to([
                stringified_message(message)
            ])))

    def test_collects_multiple_messages_to_recipient(self):        
        messages = [
          aMessage(recipient='rob@mailinator.com', sender='no-reply@qwan.eu', subject='rob', body='hello rob'),
          aMessage(recipient='henk@mailinator.com', sender='no-reply@qwan.eu', subject='henk', body='hello henk'),
        ]
        self.message_engine.send(messages)
        probe_that(lambda: assert_that(self.server.messages, equal_to([
            stringified_message(message) for message in messages 
        ])))

def stringified_message(message):
    return '\r\n'.join(message.as_string().splitlines())

def aMessage(recipient, sender, subject, body):
    email_message = EmailMessage()
    email_message['To'] = recipient
    email_message['From'] = sender
    email_message['Subject'] = subject
    email_message.set_content(body)
    return email_message

class SMTPBasedMessageEngineForTest:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def create_ssl_context(self):
        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE
        return ssl_context

    def send(self, messages):
        with SMTP(self.host, self.port) as smtp:
            smtp.starttls(context=self.create_ssl_context())
            for message in messages:
                smtp.send_message(msg=message)
        


