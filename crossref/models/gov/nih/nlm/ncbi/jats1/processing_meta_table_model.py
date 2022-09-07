from enum import Enum

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


class ProcessingMetaTableModel(Enum):
    BOTH = "both"
    NONE = "none"
    OASIS = "oasis"
    XHTML = "xhtml"
