from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class MedicalNeedEnumeration(StrEnum):
    ALLERGIC = "allergic"
    HEART_CONDITION = "heartCondition"
    OTHER_MEDICAL_NEED = "otherMedicalNeed"
