import zope.interface
from Products.PortalTransforms.interfaces import ITransform

from pmr2.processor.legacy.transforms import cellml2html_mathml

class CellmlToHtmlMathml:
    """\
    CellmlToHtmlMathml - Processes MathML in CellML into HTML+MathML.
    """
    #wraps around cellml2html_mathml for PortalTransforms.

    zope.interface.implements(ITransform)

    __name__ = "pmr2_processor_legacy_cellml2html_mathml"
    output = "text/html"

    def __init__(self, name=None, inputs=('text/xml', 'application/cellml+xml', 'application/xml',)):
        self.config = { 'inputs' : inputs, }
        self.config_metadata = {
            'inputs' : ('list', 'Inputs', 'Input(s) MIME type. Change with care.'),
            }
        if name:
            self.__name__ = name

    def name(self):
        return self.__name__

    def __getattr__(self, attr):
        if attr == 'inputs':
            return self.config['inputs']
        if attr == 'output':
            return self.config['output']
        raise AttributeError(attr)

    def convert(self, orig, data, **kwargs):
        # we return html string, not the StringIO object
        data.setData('%s' % cellml2html_mathml(orig).getvalue())
        return data

def register():
    return CellmlToHtmlMathml()

