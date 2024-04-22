from students.services.pdf_converter import PdfConverter
from django.shortcuts import reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from students.models import Student
from students.forms import StudentForm
from students.services.excel_converter import ExcelCoverter
from students.services.student_filter import StudentFilter
from students.services.pdf_converter import PdfConverter


class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    paginate_by = 10

    def get_queryset(self):
        return StudentFilter.filter_students(self.request.GET.get('search', ''),
                                             self.request.GET.get('start_date', None),
                                             self.request.GET.get('end_date', None))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Students'
        context['admin'] = True
        context['banner'] = 'studentBanner'
        return context


class StudentCreateView(LoginRequiredMixin, CreateView):
    template_name = 'students/student_form.html'
    form_class = StudentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'New Student'
        context['admin'] = True
        context['banner'] = 'studentBanner'
        return context

    def get_success_url(self):
        return reverse('students:list')


class StudentDetailView(LoginRequiredMixin, DetailView):
    model = Student
    context_object_name = 'student'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student Details'
        context['admin'] = True
        context['banner'] = 'studentBanner'
        return context


class StudentUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'students/student_form.html'
    model = Student
    form_class = StudentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Student'
        context['admin'] = True
        context['banner'] = 'studentBanner'
        return context

    def get_success_url(self):
        return reverse('students:list')


class StudentDeleteView(LoginRequiredMixin, DeleteView):
    model = Student
    http_method_names = 'post'

    def get_success_url(self):
        return reverse('students:list')


class StudentExportView(LoginRequiredMixin, View):
    def get(self, request):
        query = request.GET.get('export_search', '')
        headers = ['First name', 'Last name', 'Email', 'Phone number', 'SSN', 'Driver License Class',
                   'Driver License Number', 'State Issued', 'Date of Birth', 'Start Date', 'Graduation Date']
        student_qs = StudentFilter.filter_students(query, self.request.GET.get('start_date', None),
                                                   self.request.GET.get('end_date', None))

        if request.GET['type'] == 'excel':
            students = student_qs.values_list('first_name', 'last_name', 'email', 'phone_number', 'ssn',
                                              'driver_license_class', 'driver_license_number', 'state_issued',
                                              'date_of_birth', 'start_date', 'graduation_date')
            return ExcelCoverter.export_to_excel(headers, students)

        elif request.GET['type'] == 'pdf':
            return PdfConverter.export_to_pdf(student_qs)
