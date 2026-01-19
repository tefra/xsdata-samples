from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.measure_base_type import MeasureBaseType
from sdmx_ml.models.usage_type import UsageType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"


@dataclass(frozen=True, kw_only=True)
class MeasureType(MeasureBaseType):
    """
    MeasureType defines the structure of a measure descriptor.

    In addition to the identifying concept and representation, a usage
    status and max occurs can be defined.

    :ivar concept_role: ConceptRole references concepts which define
        roles which this measure serves.
    :ivar usage: The usage attribute indicates whether a measure value
        must be available for any corresponding existing observation.
    """

    concept_role: tuple[str, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ConceptRole",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure",
            "pattern": r".+\.conceptscheme\.Concept=.+",
        },
    )
    usage: UsageType = field(
        default=UsageType.OPTIONAL,
        metadata={
            "type": "Attribute",
        },
    )
