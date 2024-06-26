from django.urls import path
from .views import *

app_name = 'institute'  # Namespace for this app

urlpatterns = [
    path('institute-create/', InstituteRegisterView.as_view(), name='add_institute'),
    path('institute-list/', InstituteList.as_view(), name='institute_list'),
    path('institute-update<int:pk>', InstituteUpdateView.as_view(), name="institute_update"),
    path('institute-delete<int:pk>', InstituteDeleteView.as_view(), name="institute_delete"),

#                              #List Of Masters urls starts

    # List of masters add forms
    path('add-signature', AddSignature.as_view(), name="add_signature"),
    path('add-caste', AddCaste.as_view(), name="add_caste"),
    path('add-category', AddCategory.as_view(), name="add_category"),
    path('add-house', AddHouse.as_view(), name="add_house"),
    path('add-medium', AddMedium.as_view(), name="add_medium"),
    path('add-religion', AddReligion.as_view(), name="add_religion"),
    path('add-standard', AddStandard.as_view(), name="add_standard"),
    path('add-reference', AddReference.as_view(), name="add_reference"),
    path('add-nationality', AddNationality.as_view(), name="add_nationality"),
    path('add-mother-tongue', AddMotherTongue.as_view(), name="add_mother_tongue"),
    path('add-family-relation', AddFamilyRelation.as_view(), name="add_family_relation"),
    path('add-enquiry-type', AddEnquiryType.as_view(), name="add_enquiry_type"),
    path('add-payment-mode', AddPaymentMode.as_view(), name="add_payment_mode"),
    path('add-class-groups', AddClassGroups.as_view(), name="add_class_groups"),
    path('add-standard', AddStandard.as_view(), name="add_standard"),
    path('add-subject', AddSubject.as_view(), name="add_subject"),
    path('add-documents', AddDocuments.as_view(), name="add_documents"),
    path('add-fee-heads', AddFeeHeads.as_view(), name="add_fee_heads"),
    path('add-fee-installments', AddFeeInstallments.as_view(), name="add_fee_installments"),
    path('add-leaving-reason', AddLeavingReason.as_view(), name="add_leaving_reason"),
    path('add-sainik-school', AddNameOfSainikSchool.as_view(), name="add_sainik_school"),
    path('add-name-of-bank', AddNameOfBank.as_view(), name="add_name_of_bank"),
    path('add-student-type', AddStudentType.as_view(), name="add_student_type"),
    path('add-child-status', AddChildStatus.as_view(), name="add_child_status"),

    #list of masters listview urls
    path('list-of-signature', ListofSignatures.as_view(), name="list_of_signatures"),
    path('list-of-caste', ListofCaste.as_view(), name="list_of_caste"),
    path('list-of-category', ListofCategory.as_view(), name="list_of_category"),
    path('list-of-house', ListofHouse.as_view(), name="list_of_house"),
    path('list-of-medium', ListofMedium.as_view(), name="list_of_medium"),
    path('list-of-religion', ListofReligion.as_view(), name="list_of_religion"),
    path('list-of-reference', ListofReference.as_view(), name="list_of_reference"),
    path('list-of-nationality', ListofNationality.as_view(), name="list_of_nationality"),
    path('list-of-mother-tongue', ListofMotherToungue.as_view(), name="list_of_mother_tongue"),
    path('list-of-family-relation', ListofFamilyRelation.as_view(), name="list_of_family_relation"),
    path('list-of-enquiry-type', ListofEnquiryType.as_view(), name="list_of_enquiry_type"),
    path('list-of-payment-mode', ListofPaymentMode.as_view(), name="list_of_payment_mode"),
    path('list-of-class-groups', ListofClassGroups.as_view(), name="list_of_class_groups"),
    path('list-of-standard', ListofStandard.as_view(), name="list_of_standard"),
    path('list-of-subjects', ListofSubjects.as_view(), name="list_of_subject"),
    path('list-of-documents', ListofDocuments.as_view(), name="list_of_documents"),
    path('list-of-fee-heads', ListofFeeHeads.as_view(), name="list_of_fee_heads"),
    path('list-of-fee-installments', ListofFeeInstallments.as_view(), name="list_of_fee_installments"),
    path('list-of-leaving-reason', ListofLeavingReasonTC.as_view(), name="list_of_leaving_reason"),
    path('list-of-sainik-school', ListofNameOfSainikSchool.as_view(), name="list_of_sainik_school"),
    path('list-of-name-of-banks', ListofNameOfTheBank.as_view(), name="list_of_name_of_bank"),
    path('list-of-student-types', ListofStudentType.as_view(), name="list_of_student_type"),
    path('list-of-child-status', ListofChildStatus.as_view(), name="list_of_child_status"),

    # deleting the entries
    path('delete/<int:pk>/', InstituteDeleteView.as_view(), name='institute_delete'),

]