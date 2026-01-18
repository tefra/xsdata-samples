from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.data_set_type import DataSetType
from sdmx_ml.models.footer import Footer
from sdmx_ml.models.structure_specific_data_header_type import (
    StructureSpecificDataHeaderType,
)

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message"


@dataclass(frozen=True, kw_only=True)
class StructureSpecificDataType:
    """
    StructureSpecificDataType defines the structure of the structure
    specific data message.

    Note that the data set payload type is abstract, and therefore it will
    have to be assigned a type in an instance. This type must be derived
    from the base type referenced. This base type defines a general
    structure which can be followed to allow for generic processing of the
    data even if the exact details of the data structure specific format
    are not known.
    """

    header: StructureSpecificDataHeaderType = field(
        metadata={
            "name": "Header",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message",
            "required": True,
        }
    )
    data_set: tuple[DataSetType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "DataSet",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message",
        },
    )
    footer: None | Footer = field(
        default=None,
        metadata={
            "name": "Footer",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message/footer",
        },
    )
