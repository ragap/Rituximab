from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.forms import ModelForm

import django_filters
from .models import Hospital,Doctor,Patient,rtx_infusion,followup

class Html5DateInput(forms.DateInput):
    input_type = "date"

class HospitalForm(ModelForm):
    class Meta:
        model = Hospital
        fields = ['hospital_name','city']
    def __init__(self,*args,**kwargs):
        super(HospitalForm,self).__init__(*args,**kwargs)

class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = ['doctor_name','doctor_email','Hospital']
    def __init__(self,*args,**kwargs):
        super(DoctorForm,self).__init__(*args,**kwargs)

class PatientForm(ModelForm):

    Previoustrt_choices = (
                              ('Prednisolone','Prednisolone'),
                              ('Tacrolimus','Tacrolimus'),
                              ('Mycophenolate','Mycophenolate'),
                              ('Cyclosporin','Cyclosporin'),
                              ('Cyclophosphamide','Cyclophosphamide'),
                              ('Azathioprine','Azathioprine'),
                              ('Methotrexate','Methotrexate'),
                              ('Other','Other')
                          )

    # Previous_treatment = forms.MultipleChoiceField(widget=forms.SelectMultiple,choices=Patient.Previoustrt_choices, required=True)
    class Meta:
        model = Patient
        fields = ['doctor','UMRN','first_name','last_name','gender','DOB','date_of_diagnosis','Diagnosis_type',
                  'Diagnosis_subtype','Previous_treatment','prev_other_comment','pre_rtx_date','pre_rtx_comment']


    def __init__(self,*args,**kwargs):
            super(PatientForm,self).__init__(*args,**kwargs)

class PatientFilter(django_filters.FilterSet):
    class Meta:
        model = Patient
        fields = ['first_name','last_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class RTXinfusionForm(ModelForm):
    Previoustrt_choices = (
                              ('Prednisolone','Prednisolone'),
                              ('Tacrolimus','Tacrolimus'),
                              ('Mycophenolate','Mycophenolate'),
                              ('Cyclosporin','Cyclosporin'),
                              ('Cyclophosphamide','Cyclophosphamide'),
                              ('Azathioprine','Azathioprine'),
                              ('Methotrexate','Methotrexate'),
                              ('Other','Other')
                          )


    class Meta:
        model = rtx_infusion
        fields =['patient','date_of_infusion','no_of_infusion','dose_in_mg',
                 'concomitant_immunosuppression','complication'
                 ]

    def __init__(self,*args,**kwargs):
      super(RTXinfusionForm,self).__init__(*args,**kwargs)

class FollowupFrom(ModelForm):

    class Meta:
        model = followup
        fields = ['type','test_date','followup_date','cd19_abs_count',
                  'upcr','serum_albumin','creatinine','CRP',
                  'ESR','ANCA_titre','PR3_titre','MPO_titre','urine_rbc','infusion']
    def __init__(self,*args,**kwargs):
        super(FollowupFrom,self).__init__(*args,**kwargs)
