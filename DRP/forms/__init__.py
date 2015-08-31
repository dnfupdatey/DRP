'''The django forms and model forms used in the DRP
Classes.

'''
from LabGroup import LabGroupForm, LabGroupJoiningForm, LabGroupSelectionForm
from Contact import ContactForm
from compound import CompoundForm, CompoundAdminForm, CompoundEditForm, CompoundDeleteForm, CompoundUploadForm, CompoundFilterForm
from compound import CompoundFilterFormSet
from authentication import ConfirmationForm, LicenseAgreementForm, UserCreationForm
from FilterForm import FilterForm, FilterFormSet, filterFormSetFactory
