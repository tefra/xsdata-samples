from dataclasses import dataclass, field
from typing import Union

from sdmx_ml.models.data_type import DataType
from sdmx_ml.models.representation_map_base_type import (
    RepresentationMapBaseType,
)
from sdmx_ml.models.value_mapping_type import ValueMappingType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class RepresentationMapType(RepresentationMapBaseType):
    source_codelist_or_source_data_type: tuple[str | DataType, ...] = (
        field(
            default_factory=tuple,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "SourceCodelist",
                        "type": str,
                        "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                        "pattern": r".+\.codelist\.Codelist=.+|.+\.codelist\.ValueList=.+",
                    },
                    {
                        "name": "SourceDataType",
                        "type": DataType,
                        "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                    },
                ),
            },
        )
    )
    target_codelist_or_target_data_type: tuple[str | DataType, ...] = (
        field(
            default_factory=tuple,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "TargetCodelist",
                        "type": str,
                        "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                        "pattern": r".+\.codelist\.Codelist=.+|.+\.codelist\.ValueList=.+",
                    },
                    {
                        "name": "TargetDataType",
                        "type": DataType,
                        "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                    },
                ),
            },
        )
    )
    representation_mapping: tuple[ValueMappingType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "RepresentationMapping",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
