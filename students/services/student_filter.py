from students.models import Student
from django.db.models import Q


class StudentFilter:
    @staticmethod
    def filter_students(query, start_date, end_date):
        student_qs = Student.objects.filter(Q(id__contains=query) | Q(first_name__icontains=query) |
                                            Q(last_name__icontains=query) | Q(email__icontains=query) |
                                            Q(email__icontains=query) | Q(address__icontains=query) |
                                            Q(driver_license_number__icontains=query) | Q(start_date__icontains=query) |
                                            Q(graduation_date__icontains=query) | Q(phone_number__icontains=query))
        if start_date and end_date:
            student_qs = student_qs.filter(start_date__gte=start_date, start_date__lte=end_date)

        return student_qs
