from enum import Enum

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


class ProcessingMetaTagsetFamily(Enum):
    BITS = "bits"
    JATS = "jats"
    STS = "sts"
