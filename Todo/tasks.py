from __future__ import absolute_import, unicode_literals
from celery import task
from .models import *
from django.core.mail import EmailMessage
import datetime
@task()
def task_number_one():
	todos=ToDo.objects.all()
	for todo in todos:
		if todo.time==datetime.datetime.now():
			email_body = """\
		    <html>
		      <head></head>
		      <body>
		        <h2>%s</h2>
		        <p>%s</p>
		        <h5>%s</h5>
		      </body>
		    </html>
		    """ % (todo.task, todo.description,todo.time)
		    email = EmailMessage('A new mail!', email_body, to=['someEmail@gmail.com'])
			email.content_subtype = "html" # this is the crucial part 
			email.send()
