from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class MedicalNeedEnumeration(Enum):
    ALLERGIC = "allergic"
    HEART_CONDITION = "heartCondition"
    OTHER_MEDICAL_NEED = "otherMedicalNeed"
