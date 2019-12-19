from django.shortcuts import render,get_object_or_404
from django.views.generic import View
from django.conf import settings
from blog.models import Post_blog
from .models import Portfolio
from django.shortcuts import redirect
from django.utils import timezone

def portfolio(request):
    portfolio1 = Portfolio.objects.all()
    # portfolio3 = Portfolio.objects.filter('category')
    civil_law = Portfolio.objects.filter(category='civil law')
    criminal_law = Portfolio.objects.filter(category='criminal law')
    family_law = Portfolio.objects.filter(category='family law')
    writs = Portfolio.objects.filter(category='writs')
    labour_laws = Portfolio.objects.filter(category='labour laws')
    service_matters = Portfolio.objects.filter(category='service matters')
    consumer_matters = Portfolio.objects.filter(category='consumer matters')
    immigrations = Portfolio.objects.filter(category='immigrations')
    consultants = Portfolio.objects.filter(category='consultants')
    footer_blog_posts = Post_blog.objects.order_by('id')[:1]

    # post3 = get_object_or_404(Portfolio, pk=pk)

    return render(request,'portfolio.html',{"civil_law":civil_law,"criminal_law": criminal_law,"family_law":family_law,
        "writs":writs,"labour_laws":labour_laws,"service_matters":service_matters,"consumer_matters":consumer_matters,
        "immigrations":immigrations,"consultants":consultants,"portfolio1":portfolio1,"footer_blog_posts":footer_blog_posts})


def portfolio_detail(request ,pk):
    portfolio2 = Portfolio.objects.order_by('created_on').filter()[:3]
    portfolio1 = Portfolio.objects.filter(category='civil law')
    post1 = get_object_or_404(Portfolio, pk=pk)
    return render(request,'portfolio_detail.html', {'post1': post1,'portfolio1':portfolio1,"portfolio2":portfolio2})
 