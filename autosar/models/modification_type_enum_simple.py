from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class ModificationTypeEnumSimple(Enum):
    """
    :cvar CONTENT_RELATED: The attribute contentRelated expresses, that
        a substantial change of the content was performed in the object.
        Usually this means e.g. that the derived artifacts need to be
        regenerated (e.g. code generation).
    :cvar DOC_RELATED: The attribute docRelated expresses, that a change
        was applied to the documentation or other informal aspects of
        the object. Usually this means e.g. that not all derived
        artifacts need to be regenerated (e.g. code generation).
    """
    CONTENT_RELATED = "CONTENT-RELATED"
    DOC_RELATED = "DOC-RELATED"
