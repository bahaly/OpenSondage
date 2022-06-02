from statistics import mode
from unicodedata import name
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.conf import settings
import json
from datetime import date

from .base import model_helper as base


class Document(base.BaseModel):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')


class Sondage(base.BaseModel):
    sondage = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True)
    theme = models.JSONField(default=dict)

    def __str__(self):
        return self.sondage


class Question(base.BaseModel):
    sondage = base.foreign('Sondage')
    question = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True)
    type = models.IntegerField(
        choices=((0, 'checkbox'), (1, 'multiple choice'), (2, 'text')), default=0)

    def __str__(self):
        return self.question


class QuestionLabel(base.BaseModel):
    question = base.foreign('Question')
    label = models.CharField(max_length=255)

    def __str__(self):
        return self.question


class Answer(base.BaseModel):
    question = base.foreign('Question')
    reponse = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, unique=True)
    type = models.CharField(max_length=255)


# PRODUCT SESSION
