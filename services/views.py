from django.shortcuts import render
from .models import Service
from blog.models import Post_blog
# Create your views here.
def services(request):
    civil_law = Service.objects.filter(category='civil law')[:1]
    criminal_law = Service.objects.filter(category='criminal law')[:1]
    family_law = Service.objects.filter(category='family law')[:1]
    writs = Service.objects.filter(category='writs')[:1]
    labour_laws = Service.objects.filter(category='labour laws')[:1]
    service_matters = Service.objects.filter(category='service matters')[:1]
    consumer_matters = Service.objects.filter(category='consumer matters')[:1]
    immigrations = Service.objects.filter(category='immigrations')[:1]
    consultants = Service.objects.filter(category='consultants')[:1]
    footer_blog_posts = Post_blog.objects.order_by('id')[:1]


    return render(request,'services.html',{"civil_law":civil_law,"criminal_law": criminal_law,"family_law":family_law,
        "writs":writs,"labour_laws":labour_laws,"service_matters":service_matters,"consumer_matters":consumer_matters,
        "immigrations":immigrations,"consultants":consultants,"footer_blog_posts":footer_blog_posts})
