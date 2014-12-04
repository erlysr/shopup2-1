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
        self.helper = FormHelper()
        self.helper.form_id = 'form-contact'
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.form_class = 'form-vertical'
        self.helper.label_class = 'col-lg-4'
        self.helper.field_class = 'col-lg-12'
        self.helper.layout = Layout(
            Fieldset(
                'Contacto', 'firstname', 'lastname', 'email', 'contact_phone'
            ),
            FormActions(Submit('save', 'Siguiente'))
        )
        super(RegStoreStepOneForm, self).__init__(*args, **kwargs)


class RegStoreStepTwoForm(forms.ModelForm):

    # estado = forms.IntegerField()
    # ciudad = forms.IntegerField()
    delegacion_municipio = forms.IntegerField()
    codigo_postal = forms.IntegerField()

    class Meta:
        model = Store
        fields = (
            'user', 'contact', 'store_name', 'dimentions', 'activity',
            'store_phone'
        )

    def __init__(self, *args, **kwargs):
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
                Field('user', type='hidden'),
                Field('contact', type='hidden'),
                'store_name', 'dimentions', 'activity',
                'store_phone', 'delegacion_municipio', 'codigo_postal'
            ),
            FormActions(Submit('save', 'Siguiente'))
        )
        super(RegStoreStepTwoForm, self).__init__(*args, **kwargs)
        DELEGACIONES = delegaciones_municipios(Town.objects.all())
        self.fields['contact'].required = False
        self.fields['delegacion_municipio'] = forms.ChoiceField(
            choices=DELEGACIONES)
        self.fields['codigo_postal'] = Dropdown(PostalCode.objects.all())


class RegStoreStepThreeForm(forms.ModelForm):
    """
    Este paso no me parece importante
    """
    class Meta:
        model = Store
        fields = (
            'wireless', 'stands', 'repisas', 'boards',
            'lighting', 'electricity', 'water',
            'airconditioning', 'toilets', 'heating',
            'elevator', 'parkinglot', 'mostrador',
            'phoneline', 'storehouse', 'dressingroom'
        )

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_id = 'register-store'
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-10'
        self.helper.layout = Layout(
            Fieldset(
                'Paso 3',
                'wireless', 'stands', 'repisas', 'boards',
                'lighting', 'electricity', 'water',
                'airconditioning', 'toilets', 'heating',
                'elevator', 'parkinglot', 'mostrador',
                'phoneline', 'storehouse', 'dressingroom'
            ),
            FormActions(Submit('save', 'Siguiente'))
        )
        super(RegStoreStepThreeForm, self).__init__(*args, **kwargs)


class RegStoreStepFourForm(forms.ModelForm):
    """
    Este paso no me parece importante
    """
    class Meta:
        model = Store
        fields = (
            'website', 'facebook', 'twitter', 'youtube',
            'logo', 'image2', 'image3', 'image4', 'image5'

        )

    def __init__(self, *args, **kwargs):
        super(RegStoreStepFourForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'register-store'
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-10'
        self.helper.layout = Layout(
            Fieldset(
                'Paso 4',
                'website', 'facebook', 'twitter', 'youtube',
                'logo', 'image2', 'image3', 'image4', 'image5'
            ),
            FormActions(Submit('save', 'save'))
        )
