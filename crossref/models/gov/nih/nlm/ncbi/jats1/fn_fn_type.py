from enum import Enum

__NAMESPACE__ = "http://www.ncbi.nlm.nih.gov/JATS1"


class FnFnType(Enum):
    ABBR = "abbr"
    COI_STATEMENT = "coi-statement"
    COM = "com"
    CON = "con"
    CONFLICT = "conflict"
    CORRESP = "corresp"
    CURRENT_AFF = "current-aff"
    CUSTOM = "custom"
    DECEASED = "deceased"
    EDITED_BY = "edited-by"
    EQUAL = "equal"
    FINANCIAL_DISCLOSURE = "financial-disclosure"
    ON_LEAVE = "on-leave"
    OTHER = "other"
    PARTICIPATING_RESEARCHERS = "participating-researchers"
    PRESENT_ADDRESS = "present-address"
    PRESENTED_AT = "presented-at"
    PRESENTED_BY = "presented-by"
    PREVIOUSLY_AT = "previously-at"
    STUDY_GROUP_MEMBERS = "study-group-members"
    SUPPLEMENTARY_MATERIAL = "supplementary-material"
    SUPPORTED_BY = "supported-by"
