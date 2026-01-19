from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.data_structure_base_type import DataStructureBaseType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"


@dataclass(frozen=True, kw_only=True)
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
        attribute relationship for a given metadata attribute.
    :ivar evolving_structure: An evolving data structure indicates that
        new Dimensions may be added under a minor version update e.g.
        1.0.0 to 1.1.0. Evolving Data Structures can only be used by
        Dataflows if they include a DimensionConstraint to fix the
        Dimensions to the subset required by the Dataflow.
    """

    metadata: None | str = field(
        default=None,
        metadata={
            "name": "Metadata",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure",
            "pattern": r".+\.metadatastructure\.MetadataStructure=.+",
        },
    )
    evolving_structure: bool = field(
        default=False,
        metadata={
            "name": "evolvingStructure",
            "type": "Attribute",
        },
    )
