from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.db.models import Avg
from .models import T1

# Create your views here.
def books_short(request):
    ###  从models取数据传给template  ###
    shorts = T1.objects.all()

    # 评论数量
    counter = T1.objects.all().count()

    queryset = T1.objects.values('n_star')
    conditions = {'n_star': 4}
    four_star = queryset.filter(**conditions).count()

    queryset = T1.objects.values('n_star')
    conditions = {'n_star': 5}
    five_star = queryset.filter(**conditions).count()

    # 平均星级
    # star_value = T1.objects.values('n_star')
    star_avg = f" {T1.objects.aggregate(Avg('n_star'))['n_star__avg']:0.1f} "

    # 情感倾向
    sent_avg = f" {T1.objects.aggregate(Avg('sentiment'))['sentiment__avg']:0.2f} "

    high_start = four_star + five_star

    return render(request, 'week06.html', locals())


def search(request):

    q = request.GET.get('q')

    shorts = T1.objects.filter(short__contains=q)

    # 评论数量
    counter = T1.objects.filter(short__contains=q).count()

    queryset = T1.objects.filter(short__contains=q).values('n_star')
    conditions = {'n_star': 4}
    four_star = queryset.filter(**conditions).count()

    queryset = T1.objects.filter(short__contains=q).values('n_star')
    conditions = {'n_star': 5}
    five_star = queryset.filter(**conditions).count()

    high_start = four_star + five_star


    # 平均星级
    star_avg = f" {T1.objects.filter(short__contains=q).aggregate(Avg('n_star'))['n_star__avg']:0.1f} "

    # 情感倾向
    sent_avg = f" {T1.objects.filter(short__contains=q).aggregate(Avg('sentiment'))['sentiment__avg']:0.2f} "
    
    return render(request,'search_result.html',locals())
