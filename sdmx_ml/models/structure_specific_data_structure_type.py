from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.data_structure_type_abstract import (
    DataStructureTypeAbstract,
)
from sdmx_ml.models.obs_dimensions_code_type import ObsDimensionsCodeType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common"


@dataclass(frozen=True, kw_only=True)
class StructureSpecificDataStructureType(DataStructureTypeAbstract):
    """
    StructureSpecificDataStructureType defines the structural information
    for a structured data set.

    In addition to referencing the data structure or dataflow which defines
    the structure of the data, the namespace for the data structure
    specific schema as well as which dimension is used at the observation
    level must be provided. It is also necessary to state whether the
    format uses explicit measures, although this is technically only
    applicable is the dimension at the observation level is the measure
    dimension or the flat data format is used.
    """

    namespace: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    dimension_at_observation: str | ObsDimensionsCodeType = field(
        metadata={
            "name": "dimensionAtObservation",
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z][A-Za-z0-9_\-]*",
        }
    )
    explicit_measures: bool = field(
        default=False,
        metadata={
            "name": "explicitMeasures",
            "type": "Attribute",
        },
    )
