#----------------------------------------------------------------------
def print_list_from_file(filename, prefix=None):
    """"""
    _ret = open(filename)
    if prefix:
        print prefix + ' = ['
    else:
        print '['
    for i in _ret:
        text = i.strip()
        print '    "{}",'.format(text)
    print ']'
    
    
#import os
#from utils import print_list_from_file

#base = 'data/svg_tag_attributes/'

#file_list = None
#for i in os.walk(base):
    #file_list = map(lambda x: base + x, i[2])

#for i in file_list:
    #_i = os.path.basename(i).replace('-', '_')
    #_i = _i.split('.txt')[0].upper()
    #print_list_from_file(i, _i)




