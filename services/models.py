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

class Service(models.Model):
    img = models.ImageField(upload_to='pics/')
    title = models.TextField(blank=True)
    list1 = models.TextField(blank=True)
    list2 = models.TextField(blank=True)
    list3 = models.TextField(blank=True)
    list4 = models.TextField(blank=True)
    list5 = models.TextField(blank=True)
    list6 = models.TextField(blank=True)
    list7 = models.TextField(blank=True)
    category = models.CharField(max_length=30, choices=CATEGORY, default='civil law')

    def __str__(self):
        return self.category
