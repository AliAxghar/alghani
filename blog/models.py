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
class Post_blog(models.Model):
    img = models.ImageField(upload_to='pics/')
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.CharField(max_length=50)
    para1 = models.TextField()
    para2 = models.TextField()
    para3 = models.TextField()
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=20, choices=CATEGORY, default='civil law')

    class Meta:
        ordering = ['category']

    def __str__(self):
        return self.title
    
