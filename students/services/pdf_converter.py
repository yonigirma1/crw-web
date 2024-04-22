from weasyprint import HTML
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage


class PdfConverter:
    def export_to_pdf(students):
        html = HTML(string=render_to_string('students/export_students.html', {'object_list': students}))
        html.write_pdf(target='/tmp/student.pdf')
        file_system = FileSystemStorage('/tmp')

        with file_system.open('student.pdf') as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="student.pdf"'
            return response
