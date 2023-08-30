from enum import Enum

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


class ComponentParentRelation(Enum):
    IS_PART_OF = "isPartOf"
    IS_REFERENCED_BY = "isReferencedBy"
    IS_REQUIRED_BY = "isRequiredBy"
    IS_TRANSLATION_OF = "isTranslationOf"
