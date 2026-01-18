from dataclasses import dataclass, field
from typing import Optional

from sdmx_ml.models.attribute_base_type import AttributeBaseType
from sdmx_ml.models.attribute_relationship_type import (
    AttributeRelationshipType,
)
from sdmx_ml.models.measure_relationship_type import MeasureRelationshipType
from sdmx_ml.models.usage_type import UsageType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class AttributeType2(AttributeBaseType):
    """
    AttributeType describes the structure of a data attribute, which is
    defined as a characteristic of an object or entity.

    The attribute takes its semantic, and in some cases it representation,
    from its concept identity. An attribute can be coded by referencing a
    code list from its coded local representation. It can also specify its
    text format, which is used as the representation of the attribute if a
    coded representation is not defined. Neither the coded or uncoded
    representation are necessary, since the attribute may take these from
    the referenced concept. An attribute specifies its relationship with
    other data structure components and is given an assignment status.
    These two properties dictate where in a data message the attribute will
    be attached, and whether or not the attribute will be required to be
    given a value. A set of roles defined in concept scheme can be assigned
    to the attribute.

    :ivar concept_role: ConceptRole references concepts which define
        roles which this attribute serves.
    :ivar attribute_relationship: AttributeRelationship describes how
        the value of this attribute varies with the values of other
        components. These relationships will be used to determine the
        attachment level of the attribute in the various data formats.
    :ivar measure_relationship: MeasureRelationship identifies the
        measures that the attribute applies to. If this is not used, the
        attribute is assumed to apply to all measures.
    :ivar usage: The usage attribute indicates whether an attribute
        value must be available for any corresponding existing
        observation.
    """

    class Meta:
        name = "AttributeType"

    concept_role: tuple[str, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ConceptRole",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "pattern": r".+\.conceptscheme\.Concept=.+",
        },
    )
    attribute_relationship: AttributeRelationshipType | None = field(
        default=None,
        metadata={
            "name": "AttributeRelationship",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "required": True,
        },
    )
    measure_relationship: MeasureRelationshipType | None = field(
        default=None,
        metadata={
            "name": "MeasureRelationship",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    usage: UsageType = field(
        default=UsageType.OPTIONAL,
        metadata={
            "type": "Attribute",
        },
    )
