from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
import threading


class EmailThread(threading.Thread):
  def __init__(self, email):
    self.email = email
    threading.Thread.__init__(self)

  def run(self):
    self.email.send()

def send_activation_email(recipient_email, activation_url):
  subject = 'Your account is ready to use'
  from_email = settings.DEFAULT_FROM_EMAIL

  # text_content = render_to_string('account/activation_email.txt', {'activation_url': activation_url})
  html_content = render_to_string('account/activation_email.html', {'activation_url': activation_url})
  text_content = strip_tags(html_content)

  msg = EmailMultiAlternatives(subject, text_content, from_email, [recipient_email])
  msg.attach_alternative(html_content, 'text/html')
  EmailThread(msg).start()

def send_password_reset_email(recipient_email, reset_url):
  subject = 'Password Reset'
  from_email = settings.DEFAULT_FROM_EMAIL

  # text_content = render_to_string('account/activation_email.txt', {'activation_url': activation_url})
  html_content = render_to_string('account/password_reset_email.html', {'reset_url': reset_url})
  text_content = strip_tags(html_content)

  msg = EmailMultiAlternatives(subject, text_content, from_email, [recipient_email])
  msg.attach_alternative(html_content, 'text/html')
  EmailThread(msg).start()