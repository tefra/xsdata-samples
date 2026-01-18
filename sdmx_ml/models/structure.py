from __future__ import annotations

from dataclasses import dataclass

from sdmx_ml.models.structure_type import StructureType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message"


@dataclass(frozen=True)
class Structure(StructureType):
    """
    Structure is a message that contains structural metadata.

    It may contain any of the following; categorisations, category schemes,
    code lists, concepts (concept schemes), constraints (attachment and
    content) data flows, hierarchical code lists, metadata flows, metadata
    structure definitions, organisation schemes, processes, reporting
    taxonomies, and structure sets.
    """

    class Meta:
        namespace = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message"
