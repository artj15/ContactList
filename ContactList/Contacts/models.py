from django.db import models
from django.forms import ModelForm

# Create your models here.
class ContactModel(models.Model):
    surname = models.CharField(max_length= 300)
    name = models.CharField(max_length=300)
    phone_number = models.IntegerField()
    def __str__(self):
        return  f'{self.surname} {self.name}'
    class Meta:
        ordering = ['surname', 'name']
        verbose_name='Contact'
class ContactForm(ModelForm):
    class Meta:
        model = ContactModel
        fields = '__all__'