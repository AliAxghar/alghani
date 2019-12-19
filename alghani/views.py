from django.shortcuts import render
from django.shortcuts import render
from .models import Team, AdminTeam ,Testimonials
from django.conf import settings
from blog.models import Post_blog
from django.template.loader import render_to_string
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from django.core.mail import send_mail,BadHeaderError,mail_admins,mail_managers,send_mass_mail
from django.shortcuts import redirect
# Create your views here.


def index(request):
    alghani_Admin_teams = AdminTeam.objects.all()
    alghani_teams = Team.objects.all()
    testi = Testimonials.objects.order_by('id')[:]
    blog_posts = Post_blog.objects.order_by('id')[:3]
    footer_blog_posts = Post_blog.objects.order_by('id')[:1]

    if request.method =='POST':
        name = request.POST.get("name",'')
        email = request.POST.get("email",'')
        phone = request.POST.get("phone",'')
        organization = request.POST.get("organization")
        description = request.POST.get("description",'')
        how_can_we_help = request.POST.get("how_can_we_help")

        context = [how_can_we_help,name,phone,organization]
        if name and email and description:
            try:
                send_mail(context,"Project Description: "+description,'d.ali679asghar@gmail.com',[email],fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
                return HttpResponseRedirect('/contact/thanks/')
        else:
            return HttpResponse('Make sure all fields are entered and valid.')

    return render(request,'index.html', {"alghani_teams": alghani_teams,"alghani_Admin_teams":alghani_Admin_teams,
        "testi":testi,"blog_posts":blog_posts,"footer_blog_posts":footer_blog_posts})

