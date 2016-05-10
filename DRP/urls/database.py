'''A module containing urls for the database (reactions, compound guide) components of DRP'''

from django.conf.urls import url
import DRP.views
from DRP.models import NumRxnDescriptorValue, BoolRxnDescriptorValue, CatRxnDescriptorValue
from DRP.models import OrdRxnDescriptorValue
from DRP.forms import NumRxnDescValForm, OrdRxnDescValForm, BoolRxnDescValForm, CatRxnDescValForm  

urls = [
  url('^(?P<filetype>.csv|.html|.arff)?$', DRP.views.reaction.ListPerformedReactions.as_view(), name='reactionlist_typed'),
  url('^/$', DRP.views.reaction.ListPerformedReactions.as_view(), name='reactionlist'),
  url('^/add.html', DRP.views.reaction.createReaction, name='newReaction'),
  url('^/entry_(?P<rxn_id>\d+)/compoundquantities.html', DRP.views.reaction.addCompoundDetails, name="addCompoundDetails"),
  url('^/entry_(?P<rxn_id>\d+)/num_desc_vals.html', DRP.views.reaction.createGenDescVal,
                                                                        {'descValClass':NumRxnDescriptorValue, 
                                                                         'descValFormClass':NumRxnDescValForm,
                                                                         'infoHeader':'Numerical Descriptor Values'
                                                                        },
                                                                        name="createNumDescVals"),
  url('^/entry_(?P<rxn_id>\d+)/ord_desc_vals.html', DRP.views.reaction.createGenDescVal,
                                                                        {'descValClass':OrdRxnDescriptorValue, 
                                                                         'descValFormClass':OrdRxnDescValForm,
                                                                         'infoHeader':'Ordinal Descriptor Values'
                                                                        },
                                                                        name="createOrdDescVals"),
  url('^/entry_(?P<rxn_id>\d+)/cat_desc_vals.html', DRP.views.reaction.createGenDescVal,
                                                                        {'descValClass':CatRxnDescriptorValue, 
                                                                         'descValFormClass':CatRxnDescValForm,
                                                                         'infoHeader':'Categorical Descriptor Values'
                                                                        },
                                                                        name="createOrdDescVals"),
  url('^/entry_(?P<rxn_id>\d+)/bool_desc_vals.html', DRP.views.reaction.createGenDescVal,
                                                                        {'descValClass':BoolRxnDescriptorValue, 
                                                                         'descValFormClass':BoolRxnDescValForm,
                                                                         'infoHeader':'Boolean Descriptor Values'
                                                                        },
                                                                        name="createBoolDescVals"),
  url('^/entry_(?P<pk>\d+)/', DRP.views.reaction.editReaction, name='editReaction'),
  url('^/delete$', DRP.views.reaction.deleteReaction, name='deleteReaction'),
  url('^/invalidate$', DRP.views.reaction.invalidateReaction, name='invalidateReaction'),
  url('^/import/apiv1/(?P<component>[^//]*).xml', DRP.views.api1),
  url('^/select_viewing_group.html', DRP.views.selectGroup, name='selectGroup'),
  url('^/compoundguide(?P<filetype>.csv|.html|.arff|/)$', DRP.views.compound.ListCompound.as_view(), name='compoundguide'),
  url('^/compoundguide/search(?P<filetype>.html|.csv|.arff)$', DRP.views.compound.ListCompound.as_view(), name='compoundSearch'),
  url('^/compoundguide/advanced_search(?P<filetype>.html|.csv|.arff)$', DRP.views.compound.AdvancedCompoundSearchView.as_view(), name='advCompoundSearch'),
  url('^/compoundguide/add.html$', DRP.views.compound.CreateCompound.as_view(), name='newCompound'),
  url('^/compoundguide/delete$', DRP.views.compound.deleteCompound, name='deleteCompound'),
  url('^/compoundguide/edit_(?P<pk>\d+).html', DRP.views.compound.EditCompound.as_view(), name='editCompound'),
  url('^/compoundguide/upload.html', DRP.views.compound.uploadCompound, name='uploadcompoundcsv'),
  url('^/jsonapi/boolrxndescriptor.json', DRP.views.descriptors.BoolRxnDescriptor.as_view(), name='boolrxndescriptor'),
  url('^/jsonapi/catrxndescriptor.json', DRP.views.descriptors.CatRxnDescriptor.as_view(), name='catrxndescriptor'),
  url('^/jsonapi/numrxndescriptor.json', DRP.views.descriptors.NumRxnDescriptor.as_view(), name='numrxndescriptor'),
  url('^/jsonapi/ordrxndescriptor.json', DRP.views.descriptors.OrdRxnDescriptor.as_view(), name='ordrxndescriptor') 
]
