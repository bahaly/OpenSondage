# -*- coding: utf-8 -*-
from django import forms


class DocumentForm(forms.Form):
    file = forms.FileField()