from enum import Enum

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


class OrganizationNameStyle(Enum):
    WESTERN = "western"
    EASTERN = "eastern"
    ISLENSK = "islensk"
    GIVEN_ONLY = "given-only"
