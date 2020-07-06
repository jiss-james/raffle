from django.db import models
from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from bootstrap_datepicker_plus import DatePickerInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your models here.


class Entry(models.Model):
    entry_id = models.AutoField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    no_of_tickets = models.IntegerField()
    amount_paid = models.DecimalField(max_digits=5, decimal_places=2)
    comp_id = models.ForeignKey('Competition', on_delete=models.CASCADE)


class Competition(models.Model):
    comp_id = models.AutoField(primary_key=True, unique=True)
    comp_name = models.CharField(max_length=50)
    description = models.TextField()
    entry_fee = models.DecimalField(max_digits=5, decimal_places=2)
    prize = models.DecimalField(max_digits=7, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()


class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ['first_name', 'last_name', 'email', 'address', 'no_of_tickets', 'amount_paid']


class CompForm(ModelForm):
    class Meta:
        model = Competition
        labels = {
            'comp_name': _('Competition Name'),
        }
        widgets = {
            'start_date': DatePickerInput(format='%Y-%m-%d'),
            'end_date': DatePickerInput(format='%Y-%m-%d'),  # specify date-frmat
        }
        fields = ['comp_name', 'description', 'prize', 'entry_fee', 'start_date', 'end_date']

class SignupForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    class Meta:
        model = User
        fields = ["first_name","last_name","username", "email", "password1", "password2"]