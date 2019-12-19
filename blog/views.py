from django.shortcuts import render,get_object_or_404
from django.conf import settings
from blog.models import Post_blog
from django.shortcuts import redirect
from django.utils import timezone

def blog(request):

    latests = Post_blog.objects.order_by('created_on')[:1]
    portfolio1 = Post_blog.objects.all()
    details = Post_blog.objects.all()
    civil_law = Post_blog.objects.filter(category='civil law')
    criminal_law = Post_blog.objects.filter(category='criminal law')
    family_law = Post_blog.objects.filter(category='family law')
    writs = Post_blog.objects.filter(category='writs')
    labour_laws = Post_blog.objects.filter(category='labour laws')
    service_matters = Post_blog.objects.filter(category='service matters')
    consumer_matters = Post_blog.objects.filter(category='consumer matters')
    immigrations = Post_blog.objects.filter(category='immigrations')
    consultants = Post_blog.objects.filter(category='consultants')
    popular_posts = Post_blog.objects.order_by('id')[:3]
    posts = Post_blog.objects.filter(slug='slug').order_by('category')
    footer_blog_posts = Post_blog.objects.order_by('id')[:1]

    return render(request,'blog.html',{"civil_law":civil_law,"criminal_law": criminal_law,"family_law":family_law,"details":details,
        "writs":writs,"labour_laws":labour_laws,"service_matters":service_matters,"consumer_matters":consumer_matters,
        "immigrations":immigrations,"consultants":consultants,"portfolio1":portfolio1,"latests":latests,"posts":posts,"popular_posts":popular_posts,"footer_blog_posts":footer_blog_posts})



def latest_blog_detail(request ,pk,slug):
    latests = Post_blog.objects.order_by('id')[:1]
    latest = get_object_or_404(Post_blog, pk=pk)
    return render(request,'latest_blog_detail.html', {'latest': latest,'latests':latests})
    

def detail_page(request ,pk,slug):
    details = Post_blog.objects.all()
    detail = get_object_or_404(Post_blog, pk=pk)
    return render(request,'detail_page.html', {'detail': detail,'details':details})


def popular_blog_detail(request ,pk,slug):
    popular_posts = Post_blog.objects.all()
    pop = get_object_or_404(Post_blog, pk=pk)
    return render(request,'popular_blog_detail.html', {'pop': pop,'popular_posts':popular_posts})
    

# def civil_law_detail(request ,pk,slug):
#     civil_law = Post_blog.objects.filter(category='civil law')
#     civil = get_object_or_404(Post_blog, pk=pk)
#     return render(request,'civil_law_detail.html', {'civil': civil,'civil_law':civil_law})


# def criminal_law_detail(request ,pk,slug):
#     criminal_law = Post_blog.objects.filter(category='criminal law')
#     criminal = get_object_or_404(Post_blog, pk=pk)
#     return render(request,'criminal_law_detail.html', {'criminal': criminal,'criminal_law':criminal_law})

# def family_law_detail(request ,pk,slug):
#     family_law = Post_blog.objects.filter(category='family law')
#     family = get_object_or_404(Post_blog, pk=pk)
#     return render(request,'family_law_detail.html', {'family': family,'family_law':family_law})


# def writs_detail(request ,pk,slug):
#     writs = Post_blog.objects.filter(category='writs')
#     writ = get_object_or_404(Post_blog, pk=pk)
#     return render(request,'writs_detail.html', {'writ': writ,'writs':writs})


# def labour_laws_detail(request ,pk,slug):
#     labour_laws = Post_blog.objects.filter(category='labour laws')
#     labour = get_object_or_404(Post_blog, pk=pk)
#     return render(request,'labour_laws_detail.html', {'labour': labour,'labour_laws':labour_laws})
    
# def service_matters_detail(request ,pk,slug):
#     service_matters = Post_blog.objects.filter(category='service matters')
#     service = get_object_or_404(Post_blog, pk=pk)
#     return render(request,'service_matters_detail.html', {'service': service,'service_matters':service_matters})

# def consumer_matters_detail(request ,pk,slug):
#     consumer_matters = Post_blog.objects.filter(category='consumer matters')
#     consumer = get_object_or_404(Post_blog, pk=pk)
#     return render(request,'consumer_matters_detail.html', {'consumer': consumer,'consumer_matters':consumer_matters})

# def immigrations_detail(request ,pk,slug):
#     immigrations = Post_blog.objects.filter(category='immigrations')
#     immigration = get_object_or_404(Post_blog, pk=pk)
#     return render(request,'immigrations_detail.html', {'immigration': immigration,'immigrations':immigrations})

# def consultants_detail(request ,pk,slug):
#     consultants = Post_blog.objects.filter(category='consultants')
#     consultant = get_object_or_404(Post_blog, pk=pk)
#     return render(request,'consultants_detail.html', {'consultant': consultant,'consultants':consultants})


