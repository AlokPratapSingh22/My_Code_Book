from django.http import HttpRequest, HttpResponseRedirect, HttpResponse

from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.messages.api import success
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CodeBlock, CodePage
from .forms import CodeBlockForm, CodePageForm, SignUpForm

app_name = 'day_code'


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                print("Succcess")
                return HttpResponseRedirect(reverse('day_code:block_list'))

            else:
                return HttpResponse("Account Not Active")

        else:
            print("Login failed")
            return HttpResponse("Invalid Login details supplied")

    return render(request, "registration/login.html")


@login_required
def user_logout(request: HttpRequest):
    logout(request)
    return HttpResponseRedirect(reverse('day_code:block_list'))


def signup(request):
    form = SignUpForm(request.POST)

    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('/')
    else:
        print("errr")
    context = {
        'form': form
    }
    return render(request, 'registration/register.html', context)


class CodeBlockListView(ListView):
    model = CodeBlock
    template_name = "day_code/block-list.html"

    def get_queryset(self):
        return CodeBlock.objects.order_by("-create_date")


class CodeBlockCreateView(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login/'
    model = CodeBlock
    form_class = CodeBlockForm
    template_name = "day_code/block-create.html"


class CodeBlockDeleteView(LoginRequiredMixin, DeleteView):
    model = CodeBlock
    template_name = "day_code/block-delete.html"
    success_url = reverse_lazy('day_code:block_list')


class CodeBlockDetailView(DetailView):
    model = CodeBlock
    template_name = "day_code/block-detail.html"


class CodeBlockUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login/'
    model = CodeBlock
    form_class = CodeBlockForm
    template_name = "day_code/block-create.html"


def index(request):
    return render(request, 'day_code/index.html')


@login_required
def add_page_to_block(request, pk):
    code_block = get_object_or_404(CodeBlock, pk=pk)

    if request.method == 'POST':
        form = CodePageForm(request.POST)
        if form.is_valid():
            page = form.save(commit=False)
            page.code_block = code_block
            page.save()
            return redirect('day_code:block_detail', pk=code_block.pk)
    else:
        form = CodePageForm()

    return render(request, 'day_code/page-create.html', {'form': form})


def page_detail(request, pk):
    page = get_object_or_404(CodePage, pk=pk)
    return render(request, template_name='day_code/page-detail.html', context={'page': page})


@login_required
def remove_page(request, pk):
    page = get_object_or_404(CodePage, pk=pk)
    block_pk = page.code_block.pk
    page.delete()
    return redirect('day_code:block_detail', pk=block_pk)
