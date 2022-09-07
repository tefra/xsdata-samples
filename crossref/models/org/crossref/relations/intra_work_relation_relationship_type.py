from enum import Enum

__NAMESPACE__ = "http://www.crossref.org/relations.xsd"


class IntraWorkRelationRelationshipType(Enum):
    IS_TRANSLATION_OF = "isTranslationOf"
    HAS_TRANSLATION = "hasTranslation"
    IS_PREPRINT_OF = "isPreprintOf"
    HAS_PREPRINT = "hasPreprint"
    IS_MANUSCRIPT_OF = "isManuscriptOf"
    HAS_MANUSCRIPT = "hasManuscript"
    IS_EXPRESSION_OF = "isExpressionOf"
    HAS_EXPRESSION = "hasExpression"
    IS_MANIFESTATION_OF = "isManifestationOf"
    HAS_MANIFESTATION = "hasManifestation"
    IS_REPLACED_BY = "isReplacedBy"
    REPLACES = "replaces"
    IS_SAME_AS = "isSameAs"
    IS_IDENTICAL_TO = "isIdenticalTo"
    IS_VARIANT_FORM_OF = "isVariantFormOf"
    IS_ORIGINAL_FORM_OF = "isOriginalFormOf"
    IS_VERSION_OF = "isVersionOf"
    HAS_VERSION = "hasVersion"
    IS_FORMAT_OF = "isFormatOf"
    HAS_FORMAT = "hasFormat"
