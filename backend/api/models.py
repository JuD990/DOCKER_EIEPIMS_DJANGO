from django.db import models
from django.contrib.auth.hashers import make_password

class Students(models.Model):
    id = models.IntegerField(primary_key=True)
    student_id = models.CharField(max_length=20, unique=True)
    firstname = models.CharField(max_length=50)
    middlename = models.CharField(max_length=20, null=True, blank=True)
    lastname = models.CharField(max_length=50)
    password = models.CharField(max_length=128, null=True, blank=True)
    email = models.EmailField()
    year_level = models.CharField(max_length=20)
    program = models.CharField(max_length=20)
    role = models.CharField(max_length=20, default="Student")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith   ('pbkdf2_sha256$'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student_id} - {self.firstname} {self.lastname}"

class CollegePOCs(models.Model):
    id = models.IntegerField(primary_key=True)
    employee_id = models.CharField(max_length=20, unique=True)
    firstname = models.CharField(max_length=50)
    middlename = models.CharField(max_length=20, null=True, blank=True)
    lastname = models.CharField(max_length=50)
    password = models.CharField(max_length=128, null=True, blank=True)
    email = models.EmailField()
    role = models.CharField(max_length=20, default="College POC")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith   ('pbkdf2_sha256$'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.employee_id} - {self.firstname} {self.lastname}"

class LeadPOCs(models.Model):
    id = models.IntegerField(primary_key=True)
    employee_id = models.CharField(max_length=20, unique=True)
    firstname = models.CharField(max_length=50)
    middlename = models.CharField(max_length=20, null=True, blank=True)
    lastname = models.CharField(max_length=50)
    password = models.CharField(max_length=128, null=True, blank=True)
    email = models.EmailField()
    program = models.CharField(max_length=20)
    role = models.CharField(max_length=20, default="Lead POC")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith   ('pbkdf2_sha256$'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.employee_id} - {self.firstname} {self.lastname}"

class HeadPOCs(models.Model):
    id = models.IntegerField(primary_key=True)
    employee_id = models.CharField(max_length=20, unique=True)
    firstname = models.CharField(max_length=50)
    middlename = models.CharField(max_length=20, null=True, blank=True)
    lastname = models.CharField(max_length=50)
    password = models.CharField(max_length=128, null=True, blank=True)
    email = models.EmailField()
    role = models.CharField(max_length=20, default="EIE Head POC")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith   ('pbkdf2_sha256$'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.employee_id} - {self.firstname} {self.lastname}"

class EslPrime(models.Model):
    id = models.IntegerField(primary_key=True)
    employee_id = models.CharField(max_length=20, unique=True)
    firstname = models.CharField(max_length=50)
    middlename = models.CharField(max_length=20, null=True, blank=True)
    lastname = models.CharField(max_length=50)
    password = models.CharField(max_length=128, null=True, blank=True)
    email = models.EmailField()
    role = models.CharField(max_length=20, default="ESL Prime")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith   ('pbkdf2_sha256$'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.employee_id} - {self.firstname} {self.lastname}"

class EslChampion(models.Model):
    id = models.IntegerField(primary_key=True)
    employee_id = models.CharField(max_length=20, unique=True)
    firstname = models.CharField(max_length=50)
    middlename = models.CharField(max_length=20, null=True, blank=True)
    lastname = models.CharField(max_length=50)
    password = models.CharField(max_length=128, null=True, blank=True)
    email = models.EmailField()
    role = models.CharField(max_length=20, default="ESL Prime")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith   ('pbkdf2_sha256$'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.employee_id} - {self.firstname} {self.lastname}"