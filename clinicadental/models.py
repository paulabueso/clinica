from django.core.validators import RegexValidator
from django.db import models
from django.db.models import permalink

# Create your models here.

class MakeAppointment(models.Model):
    name = models.CharField(max_length=30)
    phone = models.IntegerField(max_length=9, validators=[RegexValidator(regex='^\d{9}$', message='Debe tener 9 digitos', code='numero invalido')])
    email = models.EmailField(max_length=70)
    DR_CHOICES = (
                    ('Dra Ana Bejar', 'Dra. Ana Bejar'),
                    ('Dra Maria LLerandi', 'Dra. Maria LLerandi'),
                    ('no especificado', 'No lo se'),)
    dr = models.CharField(max_length=15, choices=DR_CHOICES)

    date = models.DateField(blank=False)
    TIME_CHOICES = (
                    ('9:00', '9:00'),
                    ('9.30', '9:30'),
                    ('10.00', '10:00'),
                    ('10:30', '10:30'),
                    ('11:00', '11:00'),
                    ('11:30', '11:30'),
                    ('12:00', '12:00'),
                    ('12:30', '12:30'),
                    ('13:00', '13:00'),
                    ('13:30', '13:30'),
                    ('14:00', '14:00'),
                    ('14:30', '14:30'),
                    ('15:00', '15:00'),
                    ('15:30', '15:30'),
                    ('16:00', '16:00'),
                    ('16:30', '16:30'),
                    ('17:00', '17:00'),
                    )
    time = models.CharField(max_length=6, choices=TIME_CHOICES)

# chat
class Messages(models.Model):
    message = models.TextField(max_length=300)
    # Should these actually be ForeignKeys?
    patient = models.TextField(max_length=20)
    secretary = models.TextField(max_length=20)

    def __unicode__(self):
        return u"{}".format(self.message)


# class Category(models.Model):
#     title = models.CharField(max_length=100, db_index=True)
#     slug = models.SlugField(max_length=100, db_index=True)
#
#     def __unicode__(self):
#         return '%s' % self.title
#
#     @permalink
#     def get_absolute_url(self):
#         return ('view_blog_category', None, { 'slug': self.slug })
#
# class Blog(models.Model):
#     title = models.CharField(max_length=100, unique=True)
#     slug = models.SlugField(max_length=100, unique=True)
#     body = models.TextField()
#     posted = models.DateField(db_index=True, auto_now_add=True)
#     category = models.ForeignKey(Category, related_name='blog')
#
#     def __unicode__(self):
#         return '%s' % self.title
#
#     @permalink
#     def get_absolute_url(self):
#         return ('view_blog_post', None, { 'slug': self.slug })

