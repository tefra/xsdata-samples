from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.data_structure_type import DataStructureType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True, kw_only=True)
class DataStructuresType:
    """
    DataStructuresType describes the structure of the data structure
    definitions container.

    It contains one or more data structure definition, which can be
    explicitly detailed or referenced from an external structure document
    or registry service.

    :ivar data_structure: DataStructure provides the details of a data
        structure definition, which is defined as a collection of
        metadata concepts, their structure and usage when used to
        collect or disseminate data.
    """

    data_structure: tuple[DataStructureType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "DataStructure",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "min_occurs": 1,
        },
    )
