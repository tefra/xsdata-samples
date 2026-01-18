from __future__ import annotations

from dataclasses import dataclass

from sdmx_ml.models.structure_usage_type import StructureUsageType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class DataflowType(StructureUsageType):
    """
    DataflowType describes the structure of a data flow.

    A data flow is defined as the structure of data that will provided for
    different reference periods. If this type is not referenced externally,
    then a reference to a data structure must be provided.
    """
