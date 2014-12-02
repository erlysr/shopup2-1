# -*- coding: utf-8 -*-

from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Field, Submit
from crispy_forms.bootstrap import FormActions

from stores.models import StatusType, Store

from . models import StoreRequest, RentType


class DropDown(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s" % obj.__unicode__()


class StoreRequestForm(forms.ModelForm):

    class Meta:
        model = StoreRequest
        fields = (
            'store',
            'user',
            'rent_type',
            'status_type',
            'start_date',
            'ending_date'
        )

    def __init__(self, user, *args, **kwargs):
        super(StoreRequestForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-10'
        self.helper.layout = Layout(
            Fieldset(
                'Nueva Petición de Tienda',
                'store',
                Field('user', type='hidden'),
                'rent_type',
                'status_type',
                'start_date',
                'ending_date'
            ),
            FormActions(Submit('Save', 'save'))
        )
        self.fields['store'] = DropDown(Store.objects.all())
        self.fields['user'].initial = user.id
        self.fields['rent_type'] = DropDown(RentType.objects.all())
        self.fields['status_type'] = DropDown(StatusType.objects.all())
