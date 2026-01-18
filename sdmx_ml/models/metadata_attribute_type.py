from __future__ import annotations

from dataclasses import dataclass, field
from typing import Union

from sdmx_ml.models.metadata_attribute_base_type import (
    MetadataAttributeBaseType,
)
from sdmx_ml.models.unbounded_code_type import UnboundedCodeType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class MetadataAttributeType(MetadataAttributeBaseType):
    """
    MetadataAttributeType describes the structure of a metadata attribute.

    The metadata attribute takes its semantic, and in some cases it
    representation, from its concept identity. A metadata attribute may be
    coded (via the local representation), uncoded (via the text format), or
    take no value. In addition to this value, the metadata attribute may
    also specify subordinate metadata attributes. If a metadata attribute
    only serves the purpose of containing subordinate metadata attributes,
    then the isPresentational attribute should be used. Otherwise, it is
    assumed to also take a value. If the metadata attribute does take a
    value, and a representation is not defined, it will be inherited from
    the concept it takes its semantic from. The optional id on the metadata
    attribute uniquely identifies it within the metadata structured
    definition. If this id is not supplied, its value is assumed to be that
    of the concept referenced from the concept identity. Note that a
    metadata attribute (as identified by the id attribute) definition must
    be unique across the entire metadata structure definition.

    :ivar metadata_attribute:
    :ivar min_occurs: The minOccurs attribute indicates the minimum
        number of times this metadata attribute must occur within its
        parent object.
    :ivar max_occurs: The maxOccurs attribute indicates the maximum
        number of times this metadata attribute can occur within its
        parent object.
    :ivar is_presentational: The isPresentational attribute indicates
        whether the metadata attribute should allow for a value. A value
        of true, meaning the metadata attribute is presentational means
        that the attribute only contains child metadata attributes, and
        does not contain a value. If this attribute is not set to true,
        and a representation (coded or uncoded) is not defined, then the
        representation of the metadata attribute will be inherited from
        the concept from which it takes its identity.
    """

    metadata_attribute: tuple[MetadataAttribute, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "MetadataAttribute",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    min_occurs: int = field(
        default=1,
        metadata={
            "name": "minOccurs",
            "type": "Attribute",
        },
    )
    max_occurs: int | UnboundedCodeType = field(
        default=1,
        metadata={
            "name": "maxOccurs",
            "type": "Attribute",
            "min_inclusive": 1,
        },
    )
    is_presentational: bool = field(
        default=False,
        metadata={
            "name": "isPresentational",
            "type": "Attribute",
        },
    )


@dataclass(frozen=True)
class MetadataAttribute(MetadataAttributeType):
    """
    MetadataAttribute defines the a metadata attribute, which is the value
    of an attribute, such as the instance of a coded or uncoded attribute
    in a metadata structure definition.
    """

    class Meta:
        namespace = (
            "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"
        )
