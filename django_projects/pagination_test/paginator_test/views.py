from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def index(request):

    obj_list = ['page01','page02','page03','page04','page05','page06','page07','page08','page09','page10',
                'page11','page12','page13','page14','page15','page16','page17','page18','page19','page20',
                'page21','page22','page23','page24','page25','page26','page27','page28','page29','page30',]
    #create a paginator instance
    paginator = Paginator(obj_list,1)

    #Get the page_number of current page
    current_page_num = request.GET.get('page')

    try:
        current_page = paginator.page(current_page_num)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        current_page = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        current_page = paginator.page(paginator.num_pages)
    return render(request,'index.html',
                  {'current_page': current_page,
                   'paginator': paginator

                  })