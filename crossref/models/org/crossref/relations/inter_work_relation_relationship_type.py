from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.crossref.org/relations.xsd"


class InterWorkRelationRelationshipType(Enum):
    IS_DERIVED_FROM = "isDerivedFrom"
    HAS_DERIVATION = "hasDerivation"
    IS_REVIEW_OF = "isReviewOf"
    HAS_REVIEW = "hasReview"
    IS_COMMENT_ON = "isCommentOn"
    HAS_COMMENT = "hasComment"
    IS_REPLY_TO = "isReplyTo"
    HAS_REPLY = "hasReply"
    BASED_ON_DATA = "basedOnData"
    IS_DATA_BASIS_FOR = "isDataBasisFor"
    HAS_RELATED_MATERIAL = "hasRelatedMaterial"
    IS_RELATED_MATERIAL = "isRelatedMaterial"
    IS_COMPILED_BY = "isCompiledBy"
    COMPILES = "compiles"
    IS_DOCUMENTED_BY = "isDocumentedBy"
    DOCUMENTS = "documents"
    IS_SUPPLEMENT_TO = "isSupplementTo"
    IS_SUPPLEMENTED_BY = "isSupplementedBy"
    IS_CONTINUED_BY = "isContinuedBy"
    CONTINUES = "continues"
    IS_PART_OF = "isPartOf"
    HAS_PART = "hasPart"
    REFERENCES = "references"
    IS_REFERENCED_BY = "isReferencedBy"
    IS_BASED_ON = "isBasedOn"
    IS_BASIS_FOR = "isBasisFor"
    REQUIRES = "requires"
    IS_REQUIRED_BY = "isRequiredBy"
    FINANCES = "finances"
    IS_FINANCED_BY = "isFinancedBy"
