'''A utilities module for helping with molecular descriptor plugins'''
import DRP

class LazyDescDict(object):

  def __init__(self, descDict):
    self.internalDict = {}
    self.descDict = descDict
    self.initialised = False

  def initialise(self, descDict):
    if not self.initialised:
      for k,v in descDict.items():
        args = v.copy()
        del args['type']
        args['heading']=k
        if v['type'] == 'num':
          self.internalDict[k] = DRP.models.NumMolDescriptor.objects.get_or_create(**args)[0]
        elif v['type'] == 'bool':
          self.internalDict[k] = DRP.models.BoolMolDescriptor.objects.get_or_create(**args)[0]
        elif v['type'] == 'ord':
          self.internalDict[k] = DRP.models.OrdMolDescriptor.objects.get_or_create(**args)[0]
        elif v['type'] == 'cat':
          del args['permittedValues']
          self.internalDict[k] = DRP.models.CatMolDescriptor.objects.get_or_create(**args)[0]
          self.internalDict[k].save()
          for permittedValue in v['permittedValues']:
            perm = DRP.models.CatMolDescriptorPermitted.objects.get_or_create(value=permittedValue, descriptor=self.internalDict[k])[0]
            perm.save()
        else:
          raise RuntimeError("Invalid descriptor type provided")
        self.internalDict[k].save()
    self.initialised = True

  def __len__(self):
    return len(self.internalDict)

  def __iter__(self):
    self.initialise(self.descDict)
    return iter(self.internalDict)

  def __getitem__(self, key):
    self.initialise(self.descDict)
    return self.internalDict[key]

  def __contains__(self, item):
    return item in self.internalDict
   

def setup(descDict):
  return LazyDescDict(descDict)