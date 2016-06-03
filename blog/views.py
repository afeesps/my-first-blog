from django.shortcuts import render
from django.template.context_processors import request
from .models import Post
from django.utils import timezone
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.template.defaultfilters import slugify
from django.shortcuts import *
# Create your views here.
#def posts(request):
#    posts_list =  Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

#    paginator = Paginator(posts_list, 5)

 #   try:
  #      page = int(request.GET.get('page', '1'))
   # except:
    #    page = 1

    #try:
     #   posts = paginator.page(page)
   # except(EmptyPage, InvalidPage):
        
    #    posts = paginator.page(paginator.num_pages)

    #return render(request,'blog/posts.html',{ 'posts' : posts },context_instance=RequestContext(request))
    
def posts(request):
    
    posts = Post.objects.all().order_by('published_date')
    print posts
    return render(request,'blog/posts.html',{'posts':posts})
    

def index(request):
  # return render(request,'blog/post_list.html',{'posts':posts})
    return render(request,'blog/index.html',{})
  
 
