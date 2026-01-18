from dataclasses import dataclass, field
from typing import Optional

from sdmx_ml.models.component_map_type import ComponentMapType
from sdmx_ml.models.date_pattern_map_type import DatePatternMapType
from sdmx_ml.models.epoch_map_type import EpochMapType
from sdmx_ml.models.fixed_value_map_type import FixedValueMapType
from sdmx_ml.models.frequency_format_mapping_type import (
    FrequencyFormatMappingType,
)
from sdmx_ml.models.structure_map_base_type import StructureMapBaseType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class StructureMapType(StructureMapBaseType):
    """
    StructureMapType defines the structure for mapping components of one
    structure to components of another structure.

    A structure may be referenced directly meaning the map applies wherever
    the structure is used, or it may be a reference via a structure usage
    meaning the map only applies within the context of that usage. Using
    the related structures, one can make extrapolations between maps. For
    example, if key families, A, B, and C, are all grouped in a related
    structures container, then a map from data structure A to C and a map
    from data structure B to C could be used to infer a relation between
    data structure A to C.

    :ivar source: Source provides a reference to a structure (data or
        metadata) or a structure usage (dataflow or metadataflow) from
        which components defined by the actual structure are to mapped.
    :ivar target: Target provides a reference to a structure (data or
        metadata) or a structure usage (dataflow or metadataflow) to
        which components from the source are to mapped.
    :ivar epoch_map: Provides the ability to map source to target date
        formats. The source date is described as the number of epochs
        since a point in time, where the duration of each epoch is
        defined, e.g. number of milliseconds since 1970.
    :ivar date_pattern_map: Provides the ability to map source to target
        date formats. The source date is described as a pattern (for
        example MM-YYYY).
    :ivar frequency_format_mapping:
    :ivar component_map: ComponentMap defines the relationship between
        the components of the source and target structures, including
        information on how the value from the source component relates
        to values in the target component.
    :ivar fixed_value_map: FixedValueMap defines a fixed value for a
        source or target component in the mapping.
    """

    source: str | None = field(
        default=None,
        metadata={
            "name": "Source",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "required": True,
            "pattern": r".+\.datastructure\.DataStructure=.+|.+\.datastructure\.Dataflow=.+|.+\.metadatastructure\.MetadataStructure=.+|.+\.metadatastructure\.Metadataflow=.+",
        },
    )
    target: str | None = field(
        default=None,
        metadata={
            "name": "Target",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "required": True,
            "pattern": r".+\.datastructure\.DataStructure=.+|.+\.datastructure\.Dataflow=.+|.+\.metadatastructure\.MetadataStructure=.+|.+\.metadatastructure\.Metadataflow=.+",
        },
    )
    epoch_map: tuple[EpochMapType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "EpochMap",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    date_pattern_map: tuple[DatePatternMapType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "DatePatternMap",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    frequency_format_mapping: tuple[FrequencyFormatMappingType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "FrequencyFormatMapping",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    component_map: tuple[ComponentMapType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "ComponentMap",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    fixed_value_map: tuple[FixedValueMapType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "FixedValueMap",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
