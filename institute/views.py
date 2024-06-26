from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import login
from .forms import *
from .models import *
from django.views.generic import UpdateView, CreateView, DeleteView, FormView, ListView

# Create your views here.

# def add_institute(request):
#     if request.method == 'POST':
#         form = InstituteForm(request.POST)
#         if form.is_valid():
#             form.save()  # Save the form data to the database
#             return redirect('institute_list')  # Redirect to a success page
#     else:
#         form = InstituteForm()
    
#     return render(request, 'create.html', {'form': form})


# def institute_list(request):
#     institutes = Institute.objects.all()
#     print(institutes)
#     return render(request, 'tables-datatable.html', {'institutes' : institutes})

class InstituteList(ListView):
    print("#####################")
    model = Institute
    context_object_name = 'institutes'
    template_name = 'list.html'


class InstituteUpdateView(UpdateView):
    model = Institute
    form_class = InstituteForm
    context_object_name = "form"
    template_name = 'update_form.html'
    success_url = reverse_lazy('institute:institute_list')

    def form_valid(self, form):
        messages.success(self.request, "Institute updated successfully!")
        return super().form_valid(form)
    

class InstituteRegisterView(CreateView):
    template_name = 'institute_register.html'
    form_class = CustomUserRegisterForm
    second_form_class = InstituteForm
    success_url = reverse_lazy('institute:institute_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'profile_form' not in context:
            context['profile_form'] = self.second_form_class()
        return context

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        profile_form = self.second_form_class(request.POST, request.FILES)

        if form.is_valid() and profile_form.is_valid():
            return self.form_valid(form, profile_form)
        else:
            return self.form_invalid(form, profile_form)

    def form_valid(self, form, profile_form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password1'])  # Handle password setting
        user.save()
        profile = profile_form.save(commit=False)
        profile.user = user
        profile.save()
        login(self.request, user)
        return redirect(self.success_url)

    def form_invalid(self, form, profile_form):
        return self.render_to_response(
            self.get_context_data(form=form, profile_form=profile_form)
        )
    

class InstituteDeleteView(DeleteView):
    model = Institute
    template_name = 'institute_delete.html'
    success_url = reverse_lazy('institute:institute_list')


#                                        signature CRUD Starts
class AddSignature(FormView):
    template_name = "lom_form.html"
    form_class = SignatureForm
    success_url = reverse_lazy('institute:list_of_signatures')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class ListofSignatures(ListView):
    model = LomSignature
    template_name = "list.html"
    context_object_name = 'signature_list'

class UpdateSignature(UpdateView):
    model = LomSignature
    form_class = SignatureForm
    context_object_name = "form"
    template_name = 'lom_form.html'
    success_url = reverse_lazy('institute:list_of_signature')

    def form_valid(self, form):
        messages.success(self.request, "Institute updated successfully!")
        return super().form_valid(form)

class InstituteDeleteView(DeleteView):
    model = Institute
    success_url = reverse_lazy('institute:institute_list')


class AddCaste(FormView):
    template_name = "lom_form.html"
    form_class = CasteForm
    success_url = reverse_lazy('institute:list_of_caste')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class ListofCaste(ListView):
    model = Caste
    template_name = "list.html"
    context_object_name = 'caste_list'

class UpdateCaste(UpdateView):
    model = Caste
    form_class = CasteForm
    context_object_name = "form"
    template_name = 'lom_form.html'
    success_url = reverse_lazy('institute:list_of_caste')

    def form_valid(self, form):
        messages.success(self.request, "Caste updated successfully!")
        return super().form_valid(form)

# class InstituteDeleteView(DeleteView):
#     model = LomSignature
#     template_name = 'institute_delete.html'
#     success_url = reverse_lazy('institute:institute_list')

    
class AddCategory(FormView):
    template_name = "lom_form.html"
    form_class = CategoryForm
    success_url = reverse_lazy('institute:list_of_category')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class ListofCategory(ListView):
    model = Category
    template_name = "category_list.html"
    context_object_name = 'category_list'
    
class AddHouse(FormView):
    template_name = "lom_form.html"
    form_class = HouseForm
    success_url = reverse_lazy('institute:institute_list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class AddMedium(FormView):
    template_name = "lom_form.html"
    form_class = MediumForm
    success_url = reverse_lazy('institute:institute_list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class AddReligion(FormView):
    template_name = "lom_form.html"
    form_class = ReligionForm
    success_url = reverse_lazy('institute:institute_list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class AddReference(FormView):
    template_name = "lom_form.html"
    form_class = ReferenceForm
    success_url = reverse_lazy('institute:institute_list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class AddNationality(FormView):
    template_name = "lom_form.html"
    form_class = NationalityForm
    success_url = reverse_lazy('institute:institute_list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class AddMotherTongue(FormView):
    template_name = "lom_form.html"
    form_class = MotherTongueForm
    success_url = reverse_lazy('institute:institute_list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class AddFamilyRelation(FormView):
    template_name = "lom_form.html"
    form_class = FamilyRelationForm
    success_url = reverse_lazy('institute:institute_list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class AddEnquiryType(FormView):
    template_name = "lom_form.html"
    form_class = EnquiryTypeForm
    success_url = reverse_lazy('institute:institute_list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class AddPaymentMode(FormView):
    template_name = "lom_form.html"
    form_class = PaymentModeForm
    success_url = reverse_lazy('institute:institute_list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class AddClassGroups(FormView):
    template_name = "lom_form.html"
    form_class = ClassGroupsForm
    success_url = reverse_lazy('institute:institute_list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class AddStandard(FormView):
    template_name = "lom_form.html"
    form_class = StandardForm
    success_url = reverse_lazy('institute:institute_list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class AddSubject(FormView):
    template_name = "lom_form.html"
    form_class = SubjectsForm
    success_url = reverse_lazy('institute:institute_list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class AddDocuments(FormView):
    template_name = "lom_form.html"
    form_class = DocumnetsForm
    success_url = reverse_lazy('institute:institute_list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class AddFeeHeads(FormView):
    template_name = "lom_form.html"
    form_class = FeeHeadsForm
    success_url = reverse_lazy('institute:institute_list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class AddFeeInstallments(FormView):
    template_name = "lom_form.html"
    form_class = FeeInstallmentForm
    success_url = reverse_lazy('institute:institute_list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class AddLeavingReason(FormView):
    template_name = "lom_form.html"
    form_class = LeavingReasonForm
    success_url = reverse_lazy('institute:institute_list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class AddNameOfSainikSchool(FormView):
    template_name = "lom_form.html"
    form_class = NameOfSainikSchoolForm
    success_url = reverse_lazy('institute:institute_list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class AddNameOfBank(FormView):
    template_name = "lom_form.html"
    form_class = NameOfBankForm
    success_url = reverse_lazy('institute:institute_list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class AddStudentType(FormView):
    template_name = "lom_form.html"
    form_class = StudentTypeForm
    success_url = reverse_lazy('institute:institute_list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
class AddChildStatus(FormView):
    template_name = "lom_form.html"
    form_class = ChildStatusForm
    success_url = reverse_lazy('institute:institute_list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    






class ListofHouse(ListView):
    model = House
    template_name = "list.html"
    context_object_name = 'house_list'


class ListofMedium(ListView):
    model = Medium
    template_name = "list.html"
    context_object_name = 'medium_list'


class ListofReligion(ListView):
    model = Religion
    template_name = "list.html"
    context_object_name = 'religion_list'


class ListofReference(ListView):
    model = Reference
    template_name = "list.html"
    context_object_name = 'reference_list'


class ListofNationality(ListView):
    model = Nationality
    template_name = "list.html"
    context_object_name = 'nationality_list'


class ListofMotherToungue(ListView):
    model = MotherToungue
    template_name = "list.html"
    context_object_name = 'mother_tongue_list'


class ListofFamilyRelation(ListView):
    model = FamiliRelation
    template_name = "list.html"
    context_object_name = 'family_relation_list'


class ListofEnquiryType(ListView):
    model = EnquiryType
    template_name = "list.html"
    context_object_name = 'enquiry_type_list'


class ListofPaymentMode(ListView):
    model = PaymentMode
    template_name = "list.html"
    context_object_name = 'payment_mode_list'


class ListofClassGroups(ListView):
    model = ClassGroups
    template_name = "list.html"
    context_object_name = 'class_group_list'


class ListofStandard(ListView):
    model = Standard
    template_name = "list.html"
    context_object_name = 'standard_list'


class ListofSubjects(ListView):
    model = Subjects
    template_name = "list.html"
    context_object_name = 'subjects_list'


class ListofDocuments(ListView):
    model = Documents
    template_name = "list.html"
    context_object_name = 'documents_list'


class ListofFeeHeads(ListView):
    model = FeeHeads
    template_name = "list.html"
    context_object_name = 'fee_heads_list'


class ListofFeeInstallments(ListView):
    model = FeeInstallments
    template_name = "list.html"
    context_object_name = 'fee_installments__list'


class ListofLeavingReasonTC(ListView):
    model = LeavingReasonTC
    template_name = "list.html"
    context_object_name = 'leaving_reason_list'


class ListofNameOfSainikSchool(ListView):
    model = NameOfSainikSchool
    template_name = "list.html"
    context_object_name = 'sainik_school_list'


class ListofNameOfTheBank(ListView):
    model = NameOfTheBank
    template_name = "list.html"
    context_object_name = 'name_of_bank_list'


class ListofStudentType(ListView):
    model = StudentType
    template_name = "list.html"
    context_object_name = 'student_type_list'


class ListofChildStatus(ListView):
    model = ChildStatus
    template_name = "list.html"
    context_object_name = 'child_status_list'
