from enum import Enum

__NAMESPACE__ = "http://www.crossref.org/AccessIndicators.xsd"


class LicenseRefAppliesTo(Enum):
    VOR = "vor"
    AM = "am"
    TDM = "tdm"
    STM_ASF = "stm-asf"
