from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.
# Verbose Names added to diplay Names in update form while using form as_p.

class Hospital(models.Model):

    cities = (
              ('Perth','Perth'),
              ('Hobart','Hobart'),
              ('Melbourne','Melbourne'),
              ('Darwin','Darwin'),
              ('Sydney','Sydney'),
              )

    hospital_name = models.CharField("Hospital Name",max_length=100,unique= True)
    city = models.CharField(max_length=15,choices=cities)
    created_date = models.DateTimeField(auto_now_add=True,auto_now= False)
    update_date = models.DateTimeField(auto_now_add=False,auto_now=True)

    def __str__(self):
        return self.hospital_name

class Doctor(models.Model):

    doctor_name = models.CharField("Doctor Name",max_length=100,unique= True)
    doctor_email = models.EmailField("Doctor Email")
    Hospital =  models.ForeignKey(Hospital, related_name = 'Doctor',on_delete=models.PROTECT)
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    def __str__(self):
        return self.doctor_name


class Patient(models.Model):
    gender_choice = (
                     ('M','Male'),
                     ('F','Female'),
                     ('U','Unknown')
                    )
    Diagnosis_chioce = (
                        ('Lupus Nephritis','Lupus Nephritis'),
                        ('Vasculitis','Vasculitis'),
                        ('Nephrotic Syndrome','Nephrotic Syndrome'),
                        ('MPGN','MPGN')
                       )

    Diagnosis_subtype = (
                         ('Lupus Nephritis',
                                (
                                 ('Class3','Class3'),
                                 ('Class4','Class4'),
                                 ('Class5','Class5'),
                                 ('Class3 and Class5','Class3 and Class5'),
                                 ('Class4 and Class5','Class4 and Class5'),
                                 )
                         ),
                         ('Vasculitis',
                                (
                                 ('ANCA MPO','ANCA MPO'),
                                 ('ANCA PR3','ANCA PR3'),
                                 ('ANCA -VE','ANCA -VE'),
                                 ('Other','Other'),
                                )
                         ),
                         ('Nephrotic Syndrome',
                               (
                                ('Minimal Change','Minimal Change'),
                                ('FSGS','FSGS'),
                                ('Membranous','Membranous'),
                                )
                         )
                        )
                        #-- MPGN disable
    Previoustrt_choices = (('Prednisolone','Prednisolone'),
                          ('Tacrolimus','Tacrolimus'),
                          ('Mycophenolate','Mycophenolate'),
                          ('Cyclosporin','Cyclosporin'),
                          ('Cyclophosphamide','Cyclophosphamide'),
                          ('Azathioprine','Azathioprine'),
                          ('Methotrexate','Methotrexate'),
                          ('Rituximab','Rituximab'),
                          ('Other','Other'))

    # in Form , Please check for multiple choce field.

    UMRN = models.CharField(max_length=10,unique=True)
    first_name = models.CharField("First Name",max_length=255,null= True ,blank= True)
    last_name = models.CharField("Last Name",max_length=255,null= True ,blank= True)
    gender = models.CharField("Gender",max_length=1,choices=gender_choice,null= True ,blank= True)
    DOB = models.DateField("Date of Birth",auto_now = False ,auto_now_add = False)
    date_of_diagnosis=models.DateField("Date of Diagnosis",auto_now = False ,auto_now_add = False)
    Diagnosis_type =models.CharField("Diagnsis Type",max_length=200 ,choices=Diagnosis_chioce,default='Nephrotic Syndrome',null= True ,blank= True )
    Diagnosis_subtype= models.CharField("Diagnsis Subtype",max_length=200,null= True ,blank= True,choices=Diagnosis_subtype) # addlist
    # Previous_treatment = models.CharField(max_length=2000)
    Previous_treatment = MultiSelectField("Previous Treatment",choices=Previoustrt_choices)
    prev_other_comment=models.CharField("Pre Other",max_length=50,null= True ,blank= True)
    pre_rtx_date=models.DateField("Pre RTX Date",auto_now = False ,auto_now_add = False,null= True,blank= True)
    pre_rtx_comment=models.CharField("Pre RTX Comment",max_length=50,null= True ,blank= True)
    doctor = models.ForeignKey(Doctor, related_name='Patient',null= True,blank = True,on_delete=models.PROTECT)
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


# add foreign key to patient table

class rtx_infusion(models.Model):
    Previoustrt_choices = (('Prednisolone','Prednisolone'),
                          ('Tacrolimus','Tacrolimus'),
                          ('Mycophenolate','Mycophenolate'),
                          ('Cyclosporin','Cyclosporin'),
                          ('Cyclophosphamide','Cyclophosphamide'),
                          ('Azathioprine','Azathioprine'),
                          ('Methotrexate','Methotrexate'),
                          ('Rituximab','Rituximab'),
                          ('Other','Other'))

    date_of_infusion = models.DateField("Date of Infusion",null= True ,blank= True)
    no_of_infusion = models.IntegerField("Infusion No",unique= True)
    dose_in_mg = models.IntegerField("Dose in gms",null= True ,blank= True) # in Milli grams only number dose_in_mg
    concomitant_immunosuppression = MultiSelectField("Concomitant IS",choices=Previoustrt_choices)# same as prv treatment
    # schedule_followup_date = models.DateField(null= True ,blank= True)
    complication = models.CharField(max_length=200,null= True ,blank= True)
    patient = models.ForeignKey(Patient, related_name='infusion',null = True,on_delete=models.PROTECT)
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    def __str__(self):
       return "[{}] {}".format(self.id, self.patient)

class followup(models.Model):
    type_choice = (
                     ('PRE-RTX','PRE-RTX'),
                     ('RTX-1 Monthes','RTX-1M'),
                     ('RTX-3 Monthes','RTX-3M'),
                     ('RTX-6 Monthes','RTX-6M'),
                     ('RTX-9 Monthes','RTX-9M'),
                     ('RTX-12 Monthes','RTX-12M'),
                     ('RTX-1.5 Years','RTX-1.5Y'),
                     ('RTX-2 Years','RTX-2Y'),
                     ('RTX-3 Years','RTX-3Y'),
                     ('RTX-4 Years','RTX-4Y'),
                     ('RTX-5 Years','RTX-5Y'),
                     ('RTX-6 Years','RTX-6Y'),
                    )
    urinerbc_choice = (
                         ('< 10','< 10'),
                         ('10 - 100','10 - 100'),
                         ('> 100','> 100')
                        )
    type = models.CharField("Infusion Type",max_length=50,null= True,blank= True,choices=type_choice)
    test_date = models.DateField("Test Date",null= True ,blank= True)
    followup_date = models.DateField("Followup Date",null= True ,blank= True)
    cd19_abs_count = models.FloatField("CD19 abs Count",null= True ,blank= True)
    upcr = models.FloatField("UPCR",null= True ,blank= True)
    serum_albumin = models.FloatField("Serum Albumin",null= True ,blank= True)
    creatinine = models.FloatField("Creatinine",null= True ,blank= True)
    CRP = models.FloatField("CRP",null= True ,blank= True)
    ESR = models.FloatField("ESR",null= True ,blank= True)
    ANCA_titre = models.FloatField("ANCA Titre",null= True ,blank= True)
    PR3_titre = models.FloatField("PR3 Titre",null= True ,blank= True)
    MPO_titre = models.FloatField("MPO Titre",null= True ,blank= True)
    urine_rbc=models.CharField("Urine RBC",max_length=50,null= True,blank= True,choices=urinerbc_choice)
    infusion = models.ForeignKey(rtx_infusion,related_name='rtx_infusion',null = True,on_delete=models.PROTECT,verbose_name="Infusion No")
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    def __str__(self):
        return self.type
