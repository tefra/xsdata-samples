from __future__ import annotations

from dataclasses import dataclass

from sdmx_ml.models.structure_specific_data_type import (
    StructureSpecificDataType,
)

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/message"


@dataclass(frozen=True, kw_only=True)
class StructureSpecificData(StructureSpecificDataType):
    """
    StructureSpecificData is used to convey data structure specific
    according to data structure definition.

    The payload of this message (i.e. the data sets) will be based on XML
    schemas which are specific to the data structure definition and the
    orientation (i.e. the observation dimension) of the data.
    """

    class Meta:
        namespace = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/message"
