from dataclasses import dataclass, field
from typing import Optional

from sdmx_ml.models.data_structure_base_type import DataStructureBaseType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class DataStructureType(DataStructureBaseType):
    """
    DataStructureType defines the structure for a data structure
    definition.

    A data structure definition is defined as a collection of metadata
    concepts, their structure and usage when used to collect or disseminate
    data.

    :ivar metadata: A data structure definition may be related to a
        metadata structure definition in order to use its metadata
        attributes as part of the data. Note that the referenced
        metadata set cannot contain nested metadata attributes, as these
        are not supported in the data. By default all metadata
        attributes can be associated at any level of the data. However,
        a metadata attribute usage can be used to provide a specific
        attribute relationshp for a given metadata attribute.
    """

    metadata: str | None = field(
        default=None,
        metadata={
            "name": "Metadata",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "pattern": r".+\.metadatastructure\.MetadataStructure=.+",
        },
    )
