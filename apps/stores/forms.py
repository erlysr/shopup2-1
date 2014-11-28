# -*- coding: utf-8 -*-

from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Field, Submit
from crispy_forms.bootstrap import FormActions

from core.models import Town, PostalCode
from . models import Store, Contact


class Dropdown(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s" % obj.__unicode__()


def delegaciones_municipios(obj_list):

    lista = [
        ['', '-------- Select --------']
    ]
    for obj in obj_list:
        lista.append([obj.id, obj.__unicode__()])
    return tuple(lista)


class RegStoreStepOneForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('firstname', 'lastname', 'email', 'contact_phone')

    def __init__(self, *args, **kwargs):
        super(RegStoreStepOneForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = 'form-contact'
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-10'
        self.helper.layout = Layout(
            Fieldset(
                # list(self.fields)
                'Contacto', 'firstname', 'lastname', 'email', 'contact_phone'
            ),
            FormActions(Submit('save', 'save'))
        )


class RegStoreStepTwoForm(forms.ModelForm):

    # estado = forms.IntegerField()
    # ciudad = forms.IntegerField()
    delegacion_municipio = forms.IntegerField()
    codigo_postal = forms.IntegerField()

    class Meta:
        model = Store
        fields = (
            'contact', 'store_name', 'dimentions', 'activity', 'store_phone')

    def __init__(self, contact, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'register-store'
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-10'
        self.helper.layout = Layout(
            Fieldset(
                'Paso 2',
                # list(self.fields)
                Field('contact', type='hidden'),
                'store_name', 'dimentions', 'activity', 'store_phone',
                'delegacion_municipio', 'codigo_postal'
            ),
            FormActions(Submit('save', 'save'))
        )
        super(RegStoreStepTwoForm, self).__init__(*args, **kwargs)
        self.fields['contact'].initial = contact.id
        DELEGACIONES = delegaciones_municipios(Town.objects.all())
        self.fields['delegacion_municipio'] = forms.ChoiceField(
            choices=DELEGACIONES)
        self.fields['codigo_postal'] = Dropdown(PostalCode.objects.all())


class RegStoreStepThreeForm(forms.ModelForm):

    # estado = forms.IntegerField()
    # ciudad = forms.IntegerField()
    delegacion_municipio = forms.IntegerField()
    codigo_postal = forms.IntegerField()

    class Meta:
        model = Store
        fields = (
            'contact', 'store_name', 'dimentions', 'activity', 'store_phone')

    def __init__(self, contact, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'register-store'
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-10'
        self.helper.layout = Layout(
            Fieldset(
                'Paso 2',
                # list(self.fields)
                Field('contact', type='hidden'),
                'store_name', 'dimentions', 'activity', 'store_phone',
                'delegacion_municipio', 'codigo_postal'
            ),
            FormActions(Submit('save', 'save'))
        )
        super(RegStoreStepTwoForm, self).__init__(*args, **kwargs)
        self.fields['contact'].initial = contact.id
        DELEGACIONES = delegaciones_municipios(Town.objects.all())
        self.fields['delegacion_municipio'] = forms.ChoiceField(
            choices=DELEGACIONES)
        self.fields['codigo_postal'] = Dropdown(PostalCode.objects.all())