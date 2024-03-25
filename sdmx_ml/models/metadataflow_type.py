from dataclasses import dataclass, field
from typing import Tuple

from sdmx_ml.models.metadataflow_base_type import MetadataflowBaseType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class MetadataflowType(MetadataflowBaseType):
    """MetadataflowType describes the structure of a metadata flow.

    A dataflow is defined as the structure of reference metadata that
    will be provided for different reference periods. If this type is
    not referenced externally, then a reference to a metadata structure
    definition must be provided

    :ivar target: References identifiable structures to which the
        refernece metadata described by the referenced metadata
        structure should be restricted to. These references may include
        wildcards for parts of the reference.
    """

    target: Tuple[str, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Target",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "min_occurs": 1,
            "pattern": r".+\)(\.[A-Za-z0-9_@$\-]+(\.[A-Za-z0-9_@$\-]+)*)?|.+\)(\.\*(\.\*)*)?",
        },
    )
