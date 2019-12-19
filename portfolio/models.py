from django.db import models
from django.utils import timezone

CATEGORY = (
    ('civil law','CIVIL LAW'),
    ('criminal law', 'CRIMINAL LAW'),
    ('family law','FAMILY LAW'),
    ('writs','WRITS'),
    ('labour laws','LABOUR LAWS'),
    ('service matters','SERVICE MATTERS'),
    ('consumer matters','CONSUMER MATTERS'),
    ('immigrations','IMMIGRATIONS'),
    ('consultants','CONSULTANTS'),
)

class Portfolio(models.Model):
    img = models.ImageField(upload_to='pics/')
    title = models.CharField(max_length=150)
    descriptions = models.TextField()
    location = models.CharField(max_length=50,default="lahore,pakistan")
    created_on = models.DateTimeField('date published')
    category = models.CharField(max_length=30, choices=CATEGORY, default='civil law')

    def __str__(self):
        return self.title

