from dataclasses import dataclass, field
from typing import Any

from sdmx_ml.models.component_list_type import ComponentListType
from sdmx_ml.models.measure import Measure

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class MeasureListType(ComponentListType):
    """
    MeasureListType describes the structure of the measure descriptor for a data
    structure definition.
    """

    choice_1: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    measure: tuple[Measure, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Measure",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "min_occurs": 1,
        },
    )
    id: str = field(
        init=False,
        default="MeasureDescriptor",
        metadata={
            "type": "Attribute",
            "pattern": r"[A-Za-z0-9_@$\-]+",
        },
    )
