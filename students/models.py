from django.db import models


STATES = (
    ('AL', 'Alabama'),
    ('AK', 'Alaska'),
    ('AS', 'American Samoa'),
    ('AZ', 'Arizona'),
    ('AR', 'Arkansas'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DE', 'Delaware'),
    ('DC', 'District of Columbia'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('GU', 'Guam'),
    ('HI', 'Hawaii'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('IA', 'Iowa'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('ME', 'Maine'),
    ('MD', 'Maryland'),
    ('MA', 'Massachusetts'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MS', 'Mississippi'),
    ('MO', 'Missouri'),
    ('MT', 'Montana'),
    ('NE', 'Nebraska'),
    ('NV', 'Nevada'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NY', 'New York'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('MP', 'Northern Mariana Islands'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'),
    ('PR', 'Puerto Rico'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VT', 'Vermont'),
    ('VI', 'Virgin Islands'),
    ('VA', 'Virginia'),
    ('WA', 'Washington'),
    ('WV', 'West Virginia'),
    ('WI', 'Wisconsin'),
    ('WY', 'Wyoming')
)

DRIVER_LICENSE_CLASSES = (
    ('A', 'Class A'),
    ('B', 'Class B'),
    ('C', 'Class C'),
)


class Student(models.Model):
    first_name = models.CharField(max_length=75, null=True)
    last_name = models.CharField(max_length=75, null=True)
    email = models.EmailField(unique=True, null=True)
    phone_number = models.CharField(max_length=20, null=True)
    ssn = models.CharField(max_length=25, unique=True, null=True)
    driver_license_class = models.CharField(max_length=5, choices=DRIVER_LICENSE_CLASSES, null=True)
    driver_license_number = models.CharField(max_length=25, unique=True, null=True)
    state_issued = models.CharField(max_length=5, null=True, choices=STATES)
    date_of_birth = models.DateField(null=True)
    address = models.TextField(null=True)
    start_date = models.DateField(null=True)
    graduation_date = models.DateField(null=True, blank=True)
    transcript_file = models.FileField(upload_to='transcripts/', null=True, blank=True)
    id_file = models.FileField(upload_to='ids/', null=True, blank=True)
    application_file = models.FileField(upload_to='applications/', null=True, blank=True)
    driver_license_file = models.FileField(upload_to='driver_licenses/', null=True, blank=True)
    medical_card_file = models.FileField(upload_to='medical_cards/', null=True, blank=True)
    birth_certificate_file = models.FileField(upload_to='birth_certificates/', null=True, blank=True)
    drug_screening_file = models.FileField(upload_to='drug_screenings/', null=True, blank=True)
    miscellaneous_file = models.FileField(upload_to='miscellaneous/', null=True, blank=True)
