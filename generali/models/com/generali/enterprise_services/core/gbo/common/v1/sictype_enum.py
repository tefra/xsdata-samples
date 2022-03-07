from enum import Enum

__NAMESPACE__ = "http://generali.com/enterprise-services/core/gbo/common/v1"


class SictypeEnum(Enum):
    DIVISION = "Division"
    MAJOR_GROUP = "MajorGroup"
    INDUSTRY_GROUP = "IndustryGroup"
    INDUSTRY = "Industry"
    SUB_INDUSTRY = "Sub-Industry"
