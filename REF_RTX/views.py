from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect

# Import class for delete/create/update view
from django.views.generic.edit import CreateView ,UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

# Import Models and Forms
from .models import Hospital,Doctor,Patient,rtx_infusion,followup
from .forms import HospitalForm,DoctorForm,PatientForm,RTXinfusionForm,FollowupFrom,PatientFilter

# To add Django Authentication
from django.contrib.auth.decorators import login_required

#Query Patients
from django.db.models import Q

# To Import/export data
import xlwt,csv

# To use django simple search for PatientForm
# from django.shortcuts import render
# from .forms import SearchForm

# To add custome message to Foreign Key protection Error
from django.db.models.deletion import ProtectedError

# Create your views here.
def index(request):
    return render(request,'index.html')

def success(request):
    return render(request,'success.html')

# Views for Hospital
@login_required()
def hospital(request):
    hospitals = Hospital.objects.all().order_by('-created_date')
    return render(request,'hospital.html',context= {'hospitals':hospitals})

@login_required()
def hospitalsearch(request,search_text):
    if request.method == 'POST':
        search_text = request.post['search_text']
    else:
        search_text = ''
        hospitals = Hospital.objects.filter(hospital_name=search_text)
    return render(request,'hospital.html',context= {'hospitals':hospitals})

@login_required()
def hospitaladd(request):
    if request.method == 'POST':
        form = HospitalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = HospitalForm()
    return render(request,'hospital_add.html',context= {'form':form})

@login_required()
def hospitaledit(request,pk = None):
    if request.method=='GET':
        hospital=get_object_or_404(Hospital,pk=pk)
        form = HospitalForm(instance=hospital)
    if request.method == 'POST':
        hospital=get_object_or_404(Hospital,pk=pk)
        form = HospitalForm(request.POST or None ,instance = hospital)
        if form.is_valid():
            hospital=form.save()
            return redirect('success')
    return render(request,'hospital_edit.html',context = {'hospital':hospital,'form':form})

class Hospitaldelete(DeleteView):
    model = Hospital
    template_name = "delete.html"
    # success_url = reverse_lazy('success')


    def get_context_data(self,**kwargs):
        context = super(Hospitaldelete,self).get_context_data(**kwargs)
        Hospitalname = Hospital.objects.get(pk=self.kwargs['pk']).hospital_name
        context["Delobject"] = Hospitalname
        return context

    def delete(self, request, *args, **kwargs):
        success_url = reverse_lazy('success')
        self.object = self.get_object()
        try:
            self.object.delete()
            return HttpResponseRedirect(success_url)
        except ProtectedError:
            # data = {'success':'violation_protected'}
            return HttpResponse("Hospital can't be deleted because of dependent record in Doctor form")


# Views for Doctor
@login_required()
def doctor(request):
    doctor = Doctor.objects.all().order_by('-created_date')[0:5]
    return render(request,'doctor.html',context= {'doctor':doctor})

@login_required()
def doctoradd(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = DoctorForm()
    return render (request,'doctor_add.html',{'form':form})

@login_required()
def doctoredit(request,pk = None):
    if request.method=='GET':
        doctor=get_object_or_404(Doctor,pk=pk)
        form = DoctorForm(instance=doctor)
    if request.method == 'POST':
        doctor=get_object_or_404(Doctor,pk=pk)
        form = DoctorForm(request.POST or None ,instance = doctor)
        if form.is_valid():
            doctor=form.save()
            return redirect('success')
    return render(request,'doctor_edit.html',context = {'doctor':doctor,'form':form})


class doctordelete(DeleteView):
    model = Doctor
    template_name = "delete.html"
    success_url = reverse_lazy('success')

    def get_context_data(self,**kwargs):
        context = super(doctordelete,self).get_context_data(**kwargs)
        doctorname = Doctor.objects.get(pk=self.kwargs['pk']).doctor_name
        context["Delobject"] = doctorname
        return context

    def delete(self, request, *args, **kwargs):
        success_url = reverse_lazy('success')
        self.object = self.get_object()
        try:
            self.object.delete()
            return HttpResponseRedirect(success_url)
        except ProtectedError:
            return HttpResponse("Doctor can't be deleted because of dependent Patient records")

# Views for Patient
@login_required()
def patient(request):
    patient = Patient.objects.all().order_by('-created_date')
    return render(request,'patient.html',context= {'patient':patient})

def patientsearch(request):
    pname = request.GET.get('q', None)
    name = Patient.objects.all()
    q = Q(first_name__icontains=pname) | Q(last_name__icontains=pname)
    patient = name.filter(q)

    return render(request, 'patient.html', {'patient': patient})


@login_required()
def patientadd(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = PatientForm()
    return render (request,'patient_add.html',{'form':form})

@login_required()
def patientedit(request,pk = None):
    if request.method=='GET':
        patient=get_object_or_404(Patient,pk=pk)
        # form = PatientForm(initial= {'Previous_treatment':patient.Previous_treatment},instance=patient)
        form = PatientForm(request.POST or None ,instance = patient)
    if request.method == 'POST':
        patient=get_object_or_404(Patient,pk=pk)
        form = PatientForm(request.POST or None ,instance = patient)
        if form.is_valid():
            patient=form.save()
            return redirect('success')
    return render(request,'patient_edit.html',context = {'patient':patient,'form':form,})

class patientdelete(DeleteView):
    model = Patient
    template_name = "delete.html"
    success_url = reverse_lazy('success')

    def get_context_data(self,**kwargs):
        context = super(patientdelete,self).get_context_data(**kwargs)
        patientname = Patient.objects.get(pk=self.kwargs['pk']).first_name
        context["Delobject"] = patientname
        return context

    def delete(self, request, *args, **kwargs):
        success_url = reverse_lazy('success')
        self.object = self.get_object()
        try:
            self.object.delete()
            return HttpResponseRedirect(success_url)
        except ProtectedError:
            return HttpResponse("Patient can't be deleted because of dependent Infusion records")

# Views for Infusion
@login_required()
def infusion(request,pk = None):

    patient=get_object_or_404(Patient,pk=pk)
    try:
        infusion =rtx_infusion.objects.filter(patient=pk)
        #infusion = get_object_or_404(rtx_infusion,pk=pk)
        return render(request,'infusion.html',context= {'infusion':infusion,'patient':patient})
    except rtx_infusion.DoesNotExist:
        infusion = rtx_infusion.objects.all()
        return render(request,'infusion.html',context= {'infusion':infusion,'patient':patient})

@login_required()
def infusionadd(request,pk=None):
    patient=get_object_or_404(Patient,pk=pk)
    if request.method == 'POST':
        form = RTXinfusionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = RTXinfusionForm(initial = {'patient' :patient} )
    return render(request,'infusion_add.html',context= {'form':form})

@login_required()
def infusionedit(request,pk = None):
    if request.method=='GET':
        infusion=get_object_or_404(rtx_infusion,pk=pk)
        form = RTXinfusionForm(instance=infusion)
    if request.method == 'POST':
        infusion=get_object_or_404(rtx_infusion,pk=pk)
        form = RTXinfusionForm(request.POST or None ,instance = infusion)
        if form.is_valid():
            hospital=form.save()
            return redirect('success')
    return render(request,'infusion_edit.html',context = {'infusion':infusion,'form':form})

class infusiondelete(DeleteView):
    model = rtx_infusion
    template_name = "delete.html"
    success_url = reverse_lazy('success')

    def get_context_data(self,**kwargs):
        context = super(infusiondelete,self).get_context_data(**kwargs)
        infusionname = rtx_infusion.objects.get(pk=self.kwargs['pk']).date_of_infusion
        context["Delobject"] = infusionname
        return context

    def delete(self, request, *args, **kwargs):
        success_url = reverse_lazy('success')
        self.object = self.get_object()
        try:
            self.object.delete()
            return HttpResponseRedirect(success_url)
        except ProtectedError:
            return HttpResponse("Infusion can't be deleted because of dependent Test Results records")

@login_required()
def results(request,pk = None):
        results =followup.objects.filter(infusion=pk)
        return render(request,'test_results.html',context= {'results':results,'infusion_id':pk})

@login_required()
def addresults(request,pk = None):
    infusion= get_object_or_404(rtx_infusion,pk=pk)
    if request.method == 'POST':
        form = FollowupFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = FollowupFrom(initial = {'infusion' :infusion})
    return render(request,'results_add.html',context= {'form':form})

@login_required()
def editresults(request,pk = None):
    if request.method=='GET':
        results=get_object_or_404(followup,pk=pk)
        form = FollowupFrom(instance=results)
    if request.method == 'POST':
        results=get_object_or_404(followup,pk=pk)
        form = FollowupFrom(request.POST or None ,instance = results)
        if form.is_valid():
            results=form.save()
            return redirect('success')
    return render(request,'results_edit.html',context = {'results':results,'form':form})


class resultsdelete(DeleteView):
    model = followup
    template_name = "delete.html"
    success_url = reverse_lazy('success')

    def get_context_data(self,**kwargs):
        context = super(resultsdelete,self).get_context_data(**kwargs)
        resultsname = followup.objects.get(pk=self.kwargs['pk']).type
        context["Delobject"] = resultsname
        return context

# Export  Data

def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename= "Patient.csv"'

    exp_patient = Patient.objects.all()

    writer = csv.writer(response)
    writer.writerow(['Doctor','UMRN','First name','Last name','DOB',
                    'Gender','Diagnosis date','Diagnosis type',
                    'Diagnosis subtype','Previous treatment','Prev other comment',
                    'Pre RTX date','Pre RTX comment','Infusion No','Infusion date',
                    'Infusion dose (mg)','Concomitant immunosuppression',
                    'Complication','RTX type','Followup Date','CD19 abs count','UPCR','Serum albumin','Creatinine',
                    'CRP','ESR','ANCA Titre','PR3 Titre','MPO Titre','Urine RBC'])

    for i in exp_patient:
        exp_infusion = rtx_infusion.objects.filter(patient=i.pk)
        for j in exp_infusion:
            exp_followup = followup.objects.filter(infusion=j.pk)
            for k in exp_followup:
                    writer.writerow([ i.doctor,
                                      i.UMRN,
                                      i.first_name,
                                      i.last_name,
                                      i.DOB,
                                      i.gender,
                                      i.date_of_diagnosis,
                                      i.Diagnosis_type,
                                      i.Diagnosis_subtype,
                                      i.Previous_treatment,
                                      i.prev_other_comment,
                                      i.pre_rtx_date,
                                      i.pre_rtx_comment,
                                      j.no_of_infusion,
                                      j.date_of_infusion,
                                      j.dose_in_mg,
                                      j.concomitant_immunosuppression,
                                      j.complication,
                                      k.type,
                                      k.followup_date,
                                      k.cd19_abs_count,
                                      k.upcr,
                                      k.serum_albumin,
                                      k.creatinine,
                                      k.CRP,
                                      k.ESR,
                                      k.ANCA_titre,
                                      k.PR3_titre,
                                      k.MPO_titre,
                                      k.urine_rbc,])
            if not exp_followup:
                 writer.writerow([i.doctor,
                                  i.UMRN,
                                  i.first_name,
                                  i.last_name,
                                  i.DOB,
                                  i.gender,
                                  i.date_of_diagnosis,
                                  i.Diagnosis_type,
                                  i.Diagnosis_subtype,
                                  i.Previous_treatment,
                                  i.prev_other_comment,
                                  i.pre_rtx_date,
                                  i.pre_rtx_comment,
                                  j.no_of_infusion,
                                  j.date_of_infusion,
                                  j.dose_in_mg,
                                  j.concomitant_immunosuppression,
                                  j.complication,
                                ])

        if not exp_infusion:
            writer.writerow([i.doctor,
                              i.UMRN,
                              i.first_name,
                              i.last_name,
                              i.DOB,
                              i.gender,
                              i.date_of_diagnosis,
                              i.Diagnosis_type,
                              i.Diagnosis_subtype,
                              i.Previous_treatment,
                              i.prev_other_comment,
                              i.pre_rtx_date,
                              i.pre_rtx_comment,
                            ])

    return response
