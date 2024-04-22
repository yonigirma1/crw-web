from django.shortcuts import redirect, render
from django.views.generic import TemplateView, View
from pages.services.email_sender import EmailSender


class HomeView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        return context


class AboutView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'About'
        context['banner'] = 'aboutBanner'
        context['text'] = 'ABOUT US'
        return context


class AdmissionView(TemplateView):
    template_name = 'pages/admission.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Admission'
        context['banner'] = 'admissionBanner'
        context['text'] = 'APPLY ONLINE'
        return context


class ApplyOnlineView(View):
    def get(self, request):
        return render(request, 'pages/apply_online.html', context={'title': 'Apply Online'})

    def post(self, request):
        print(request.POST)
        sent = EmailSender.send_email(
            'email/apply_email.html',
            f"Online Application ({request.POST.get('first_name', '')} {request.POST.get('last_name', '')})",
            {
                'date': request.POST.get('date', ''),
                'first_name': request.POST.get('first_name', ''),
                'last_name': request.POST.get('last_name', ''),
                'email': request.POST.get('email', ''),
                'phone_number': request.POST.get('phone_number', ''),
                'date_of_birth': request.POST.get('date_of_birth', ''),
                'age': request.POST.get('age', ''),
                'email': request.POST.get('email', ''),
                'street_address': request.POST.get('street_address', ''),
                'address_1': request.POST.get('address_1', ''),
                'address_2': request.POST.get('address_2', ''),
                'city': request.POST.get('city', ''),
                'state': request.POST.get('state', ''),
                'postal_code': request.POST.get('postal_code', ''),
                'country': request.POST.get('country', ''),
                'ssn': request.POST.get('ssn', ''),
                'high_school_diploma': request.POST.get('high_school_diploma', ''),
                'license': request.POST.get('license', ''),
                'driver_license_class': request.POST.get('driver_license_class', ''),
                'driver_license_number': request.POST.get('driver_license_number', ''),
                'state_issued': request.POST.get('state_issued', ''),
                'tickets': request.POST.get('tickets', ''),
                'violation': request.POST.get('violation', ''),
                'dui_dwi': request.POST.get('dui_dwi', ''),
                'felony': request.POST.get('felony', ''),
                'drug': request.POST.get('drug', ''),
                'health': request.POST.get('health', ''),
                'driving': request.POST.get('driving', ''),
                'employed': request.POST.get('employed', '')
            })
        if sent:
            return redirect('pages:home')
        else:
            render(request, 'pages/apply_online.html', context={'title': 'Apply Online'})


class ContactView(View):
    def get(self, request):
        return render(request, 'pages/contact.html', context={'title': 'Contact'})

    def post(self, request):
        sent = EmailSender.send_email('email/contact_email.html', f"Contact ({request.POST.get('name', '')})", {
            'name': request.POST.get('name', ''),
            'email': request.POST.get('email', ''),
            'address': request.POST.get('address', '')
        })
        return redirect('pages:home') if sent else render(request, 'pages/contact.html', context={'title': 'Contact'})
