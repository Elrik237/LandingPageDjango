from django.shortcuts import render, redirect
from .models import Arctiles
from .forms import ArctilesForm
from django.views.generic import DeleteView, UpdateView, DetailView


def news_home(request):
    news = Arctiles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})


class NewsDetailView(DetailView):
    model = Arctiles
    template_name = 'news/details_view.html'
    context_object_name = 'arctile'


class NewsUpdateView(UpdateView):
    model = Arctiles
    template_name = 'news/create.html'
    form_class = ArctilesForm


class NewsDeleteView(DeleteView):
    model = Arctiles
    success_url = '/news/'
    template_name = 'news/news_delete.html'




def create(request):
    error = ''
    if request.method == 'POST':
        form = ArctilesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news-home')
        else:
            error = 'Форма была невернй'

    form = ArctilesForm()

    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'news/create.html', data)
