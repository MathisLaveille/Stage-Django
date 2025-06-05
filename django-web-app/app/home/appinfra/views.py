from django.views.generic import TemplateView
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from django.core.mail import send_mail
from .forms import ContactUsForm, CustomUserCreationForm, CustomAuthenticationForm


def accueil(request):
    return render(request, 'autres/accueil.html')


class MyTemplateView(TemplateView):
    template_name = None
    class_form = None
    model = None
    class_table = None
    source = None
    action = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_object = None

        if self.action == "new":
            form = self.class_form(kwargs.get('POST'))
            context['form'] = form
            return context

        if 'id' in kwargs:
            if self.class_table and self.source and kwargs.get('id'):
                current_object = self.source.objects.filter(id=kwargs.get('id')).first()
                if current_object:
                    dataset_name = f'{self.model._meta.model_name}_set'
                    if hasattr(current_object, dataset_name):
                        object_list = getattr(current_object, dataset_name).all()
                    else:
                        object_list = super().get_queryset().filter(id__lt=0)
                else:
                    object_list = super().get_queryset().filter(id__lt=0)
                context['table'] = self.class_table(object_list)
            else:
                current_object = self.model.objects.filter(id=kwargs.get('id')).first()
                if kwargs.get('POST'):
                    form = self.class_form(kwargs.get('POST'), instance=current_object)
                else:
                    form = self.class_form(instance=current_object)
                context['current_object'] = current_object
                context['form'] = form
        else:
            if self.class_table:
                object_list = self.model.objects.all()
                context['table'] = self.class_table(object_list)

        return context

    def get(self, request, *args, **kwargs):
        if request.GET.get('delete'):
            return self.delete(request, *args, **kwargs)
        elif self.action == "new":
            return self.create(request, *args, **kwargs)
        else:
            return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if self.action == "new":
            return self.create(request, *args, **kwargs)

        kwargs = request.resolver_match.kwargs
        kwargs['POST'] = request.POST
        context = self.get_context_data(**kwargs)
        form = context.get('form')
        if form.is_valid():
            form.save()
        return super(TemplateView, self).render_to_response(context)

    def delete(self, request, *args, **kwargs):
        current_object = self.model.objects.filter(id=kwargs.get('id')).first()
        if current_object:
            current_object.delete()
        return redirect(f'{self.model._meta.model_name}_list')

    def create(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = self.class_form(request.POST)
            if form.is_valid():
                obj = form.save()
                return redirect(f'{self.model._meta.model_name}_update', obj.id)
        else:
            form = self.class_form()

        return render(request, f'{self.model._meta.model_name}/{self.model._meta.model_name}_create.html',
                      {'form': form})


def about(request):
    return render(request, 'autres/about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )
            return redirect('email_sent')
    else:
        form = ContactUsForm()

    return render(request, 'autres/contact.html', {'form': form})


def email_sent(request):
    return render(request, 'autres/email_sent.html')


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, _('Inscription réussie ! Vous êtes maintenant connecté.'))
            return redirect('accueil')
    else:
        form = CustomUserCreationForm()
    return render(request, 'authentication/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, _('Vous êtes maintenant connecté.'))
            return redirect('accueil')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'authentication/login.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, _('Vous avez été déconnecté.'))
    return redirect('accueil')


@method_decorator(login_required, name='dispatch')
class UserProfileView(TemplateView):
    template_name = 'authentication/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
