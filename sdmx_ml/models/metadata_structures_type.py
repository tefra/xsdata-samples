from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.metadata_structure_type import MetadataStructureType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class MetadataStructuresType:
    """
    MetadataStructuresType describes the structure of the metadata
    structure definitions container.

    It contains one or more metadata structure definition, which can be
    explicitly detailed or referenced from an external structure document
    or registry service.

    :ivar metadata_structure: MetadataStructure provides the details of
        a metadata structure definition, which is defined as a
        collection of metadata concepts, their structure and usage when
        used to collect or disseminate reference metadata. A metadata
        structure definition performs several functions: it groups sets
        of objects into "targets" against which reference metadata may
        be reported. Targets define the structure of the reference
        metadata "keys" which identify specific types of reported
        metadata, and describe the valid values for populating the keys.
        Also, metadata structure definitions provide a presentational
        organization of concepts for reporting purposes. The structure
        of reference metadata is derived from this presentational
        structure.
    """

    metadata_structure: tuple[MetadataStructureType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "MetadataStructure",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "min_occurs": 1,
        },
    )
