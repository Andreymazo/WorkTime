from django.contrib.auth.base_user import AbstractBaseUser
from django.core.validators import RegexValidator
from django.db import models

from worktime.managers import CustomUserManager

phone_validator = RegexValidator(r"^(\+?\d{0,4})?\s?-?\s?(\(?\d{3}\)?)\s?-?\s?(\(?\d{3}\)?)\s?-?\s?(\(?\d{4}\)?)?$",
                                 "The phone number provided is invalid")
NULLABLE = {'blank': True, 'null': True}


class CustomUser(AbstractBaseUser):  # , PermissionsMixin  # , PermissionsMixin):
    email = models.EmailField(max_length=100, unique=True)
    # VERIFICATION_TYPE = [
    #     ('sms', 'SMS'),
    # ]
    # phone_number = PhoneNumberField(unique = True)
    # verification_method = models.CharField(max_length=10,choices= VERIFICATION_TYPE)
    # phone_number = models.CharField(max_length=16, validators=[phone_validator], unique=True)
    full_name = models.CharField(max_length=30)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    # is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return f"{self.id}: {self.email}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        # permissions = [("workingtime.add_customuser", "Can add customuser"),
        #                ("workingtime.change_customuser", "Can change customuser"),
        #                ("workingtime.delete_customuser", "Can delete customuser"),
        #                ("workingtime.view_customuser", "Can view customuser")]

    @staticmethod
    def has_perm(perm, obj=None, **kwargs):
        return True

    @staticmethod
    def has_module_perms(app_label, **kwargs):
        return True


#
# class CustomUserTable(tables.Table):
#     class Meta:
#         model = CustomUser
#         empty_text = _(
#             "No hay ninguna asignatura que satisfaga los criterios de búsqueda."
#         )
#         template_name = "django_tables2/bootstrap3.html"
#         per_page = 20
#         # template_name = 'django_tables2/bootstrap.html'

class Employee(models.Model):
    customuser = models.OneToOneField('worktime.CustomUser', on_delete=models.CASCADE, related_name='employee')
    country = models.ForeignKey('worktime.Country', on_delete=models.CASCADE, related_name='employee')
    payment_type = models.ForeignKey('worktime.PaymentType', on_delete=models.CASCADE, related_name='employee')
    name = models.CharField(max_length=100, verbose_name='Имя')
    surname = models.CharField(max_length=100, verbose_name='Фамилия')

    @property
    def fullname(self):
        return f'{self.name} {self.surname}'

    def __str__(self):
        return f'{self.fullname}'


class EmployeeTimeStamp(models.Model):
    employee = models.ForeignKey('worktime.Employee', on_delete=models.CASCADE, related_name='timestamp')
    employee_sum = models.ForeignKey('working.EmployeeSum', on_delete=models.CASCADE, related_name='timestamp')
    date_start = models.DateField(auto_now=False, auto_now_add=False, verbose_name="Начало трудового дня")
    date_end = models.DateField(auto_now=False, auto_now_add=False, verbose_name="Конец трудового дня")


# 1 Nazvanie: EmployeeSum zamenit na DayData 2 Udobnee ne vstavlyat v EmployeeTimeStamp pole ucheta pererivov v rabote,
# a sdelat ego tut v DayData i libo auto_now=True libo perepisat metod save pod eto

class DayData(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False, verbose_name="День, за который идет зачет")
    break_time = models.DateField(auto_now=True, auto_now_add=False, verbose_name="Время начала и остановки работы")
    sum = models.IntegerField(verbose_name='Сумма заработка за день')


class CountryTypes(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')


class WorkDays(models.Model):
    employee = models.Model('worktime.Employee', on_delete=models.CASCADE, related_name='workdays')


class PaymentType(models.Model):
    DAY_PAYMENT = 'DAY PAYMENT'
    HOUR_PAYMENT = 'HOUR PAYMENT'
    STATUSES = (
        (DAY_PAYMENT, 'DAY PAYMENT'),
        (HOUR_PAYMENT, 'HOUR PAYMENT')
    )
    name = models.CharField(choices=STATUSES, verbose_name='Тип оплаты работы',
                            default=HOUR_PAYMENT)


class Salary(models.Model):
    ##Predlagau 1. nazvanie Salary 2. ForeignKey na Employee 3 sum peredelat na drugie nazvania amount naprimer
    date_start_salary = models.DateField(auto_now=False, auto_now_add=False,
                                         verbose_name="Начало начисления заработной платы")
    date_end_salary = models.DateField(auto_now=False, auto_now_add=False,
                                       verbose_name="Конец начисления заработной платы")
    currency = models.ForeignKey('worktime.Currency', on_delete=models.CASCADE)
    amount = models.CharField(max_length=10)
    payment_type = models.CharField()


class Currency(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=5)
    symbol = models.CharField(max_length=1)


# Pycharm podcherkivaet CountryTypes, predlagau prosto Country

class Country(models.Model):
    name = models.CharField(max_length=100)
