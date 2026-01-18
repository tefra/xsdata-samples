from __future__ import annotations

from dataclasses import dataclass

from sdmx_ml.models.metadata_attribute_list_type import (
    MetadataAttributeListType,
)

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True, kw_only=True)
class MetadataAttributeList(MetadataAttributeListType):
    """
    MetadataAttributeList defines the set of metadata attributes that can
    be defined as a hierarchy, for reporting reference metadata about a
    target object.

    The identification of metadata attributes must be unique at any given
    level of the metadata structure. Although there are XML schema
    constraints to help enforce this, these only apply to explicitly
    assigned identifiers. Identifiers inherited from a concept from which a
    metadata attribute takes its identity cannot be validated against this
    constraint. Therefore, systems processing metadata structure
    definitions will have to perform this check outside of the XML
    validation.
    """

    class Meta:
        namespace = (
            "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"
        )
