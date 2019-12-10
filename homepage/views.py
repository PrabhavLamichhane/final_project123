from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse,Http404
from addBook.models import Book
from .models import HomeSlide
from django.views.generic import ListView,DetailView

# Create your views here.

# def home(request):
#     book=Book.objects.all()
#     homeSlide=HomeSlide.objects.all()
#     return render(request,'home.html',{'book':book, 'homeSlide':homeSlide})

# # def bookButton(request):
# #     return HttpResponseRedirect('/')
    
class BookDetailSlugView(DetailView):
      queryset=Book.objects.all()
      template_name="detail.html"
      def get_object(self,*args,**kwargs):
        request=self.request
        slug=self.kwargs.get('slug')
       # instance=books.objects.get_by_id(slug) 
        #instance=books.objects.get(slug=slug)
        try:
            instance=Book.objects.get(slug=slug)
        except Book.DoesNotExist:
            raise Http404("Not found....")
        except Book.MultipleObjectsReturned:
            qs=Book.objects.filter(slug=slug,active=True)
            instance=qs.first()
        except:
            raise Http404("Ummmm")
        
        return instance


def book_list_view(request):
    instance=Book.objects.all()
    slide=HomeSlide.objects.all()
    context={
         'object':instance,
         'homeslide':slide
}  
    return render(request,"home.html",context)



def plustwo(request):
    book=Book.objects.filter(category='+2')
    title="Plus two books"
    return render(request,"category.html",{'title':title,'book':book}) 
    
def bachelor(request):
    book=Book.objects.filter(category='Bachelor')
    title="Bachelor books"
    return render(request,"category.html",{'title':title,'book':book})     

def diploma(request):
    book=Book.objects.filter(category='Diploma')
    title="Diploma Books"
    return render(request,"category.html",{'title':title,'book':book})     

def see(request):
    book=Book.objects.filter(category='SEE')
    title="SEE Books"
    return render(request,"category.html",{'title':title,'book':book})     

def school(request):
    book=Book.objects.filter(category='School')
    title="School Books"
    return render(request,"category.html",{'title':title,'book':book})     

def master(request):
    book=Book.objects.filter(category='Master')
    title="Master Books"
    return render(request,"category.html",{'title':title,'book':book})     

def extra(request):
    book=Book.objects.filter(category='Extra')
    title="Extra Books"
    return render(request,"category.html",{'title':title,'book':book})   