from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


def image_directory_path(instance, filename):
    return f'media/{instance}/{filename}'


class Word(models.Model):
    word = models.CharField(max_length=200)
    translate = models.CharField(max_length=200)
    transcription = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to=image_directory_path, blank=True)

    def __str__(self):
        return self.word


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    words = models.ManyToManyField(Word)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)

        words = Word.objects.all()[:10]
        student = Student.objects.get(user=instance)
        for word in words:
            student.words.add(word)
        student.save()


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.student.save()
