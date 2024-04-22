import xlwt
from django.http import HttpResponse


class ExcelCoverter:
    @staticmethod
    def export_to_excel(header, students):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="students.xls"'
        work_book = xlwt.Workbook(encoding='utf-8')
        work_sheet = work_book.add_sheet('Students')
        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        for iteration in range(len(header)):
            work_sheet.write(0, iteration, header[iteration], font_style)

        font_style = xlwt.XFStyle()
        for iteration, student in enumerate(students):
            for nested_iteration in range(len(student)):
                work_sheet.write(iteration + 1, nested_iteration, str(student[nested_iteration]), font_style)

        work_book.save(response)
        return response
