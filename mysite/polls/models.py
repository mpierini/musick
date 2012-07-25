from django.db import models

import datetime 
from django.utils import timezone 
#Note the addition of import datetime and from django.utils import timezone,
#to reference Python's standard datetime module and Django's time-zone-related
#utilities in django.utils.timezone, respectively.

# Create your models here.
class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.question
        #It's important to add __unicode__() methods
        #to your models, not only for your own sanity
        #when dealing with the interactive prompt,
        #but also because objects' representations are used
        #throughout Django's automatically-generated admin.

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        #custom method

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField()

    def __unicode__(self):
        return self.choice_text
