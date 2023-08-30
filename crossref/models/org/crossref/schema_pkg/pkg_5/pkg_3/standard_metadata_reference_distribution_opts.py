from enum import Enum

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


class StandardMetadataReferenceDistributionOpts(Enum):
    NONE = "none"
    QUERY = "query"
    ANY = "any"
