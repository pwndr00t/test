# -*- coding: utf-8 -*-
from django.db import models
import sys

# fix for utf-8
reload(sys)
sys.setdefaultencoding('utf-8')

class Data(models.Model):
	data = models.TextField()

	def __unicode__(self):
		return self.data
