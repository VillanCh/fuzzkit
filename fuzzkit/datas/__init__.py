from .common_attrs import COMMON_ATTRS
from . import html_elements
from . import math_elements
from . import svg_elements
from .events import MOST_EVENT_ATTRIBUTES, AGNOSTIC_EVENT_ATTRIBUTES


_TAG_COLLECT = [html_elements, math_elements, svg_elements,]
_ELEMENT_LIST_ = 'ELEMENT_LIST'

#----------------------------------------------------------------------
def get_attrs_by_name(tag_name):
    """"""
    for i in _TAG_COLLECT:
        if tag_name in getattr(i, _ELEMENT_LIST_):
            
    
    