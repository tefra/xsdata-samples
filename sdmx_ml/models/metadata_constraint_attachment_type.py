from dataclasses import dataclass, field
from typing import ForwardRef, Optional, Union

from sdmx_ml.models.queryable_data_source_type_1 import (
    QueryableDataSourceType1,
)

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class MetadataConstraintAttachmentType:
    """
    MetadataConstraintAttachmentType restricts the base ConstraintAttachmentType to
    only allow artefacts related to metadata.
    """

    choice: tuple[
        Union[
            "MetadataConstraintAttachmentType.MetadataProvider",
            "MetadataConstraintAttachmentType.MetadataSet",
            "MetadataConstraintAttachmentType.SimpleDataSource",
            "MetadataConstraintAttachmentType.MetadataStructure",
        ],
        ...,
    ] = field(
        default_factory=tuple,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "MetadataProvider",
                    "type": ForwardRef(
                        "MetadataConstraintAttachmentType.MetadataProvider"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "MetadataSet",
                    "type": ForwardRef(
                        "MetadataConstraintAttachmentType.MetadataSet"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "SimpleDataSource",
                    "type": ForwardRef(
                        "MetadataConstraintAttachmentType.SimpleDataSource"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "MetadataStructure",
                    "type": ForwardRef(
                        "MetadataConstraintAttachmentType.MetadataStructure"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
            ),
        },
    )
    queryable_data_source_or_metadataflow_or_metadata_provision_agreement: tuple[
        Union[
            QueryableDataSourceType1,
            "MetadataConstraintAttachmentType.Metadataflow",
            "MetadataConstraintAttachmentType.MetadataProvisionAgreement",
        ],
        ...,
    ] = field(
        default_factory=tuple,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "QueryableDataSource",
                    "type": QueryableDataSourceType1,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "Metadataflow",
                    "type": ForwardRef(
                        "MetadataConstraintAttachmentType.Metadataflow"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "MetadataProvisionAgreement",
                    "type": ForwardRef(
                        "MetadataConstraintAttachmentType.MetadataProvisionAgreement"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
            ),
        },
    )

    @dataclass(frozen=True)
    class MetadataProvider:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
                "pattern": r".+\.base\.MetadataProvider=.+:METADATA_PROVIDERS\(.+\).+",
            },
        )

    @dataclass(frozen=True)
    class MetadataSet:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
                "pattern": r".+\.metadatastructure\.MetadataSet=.+",
            },
        )

    @dataclass(frozen=True)
    class SimpleDataSource:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass(frozen=True)
    class MetadataStructure:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
                "pattern": r".+\.metadatastructure\.MetadataStructure=.+",
            },
        )

    @dataclass(frozen=True)
    class Metadataflow:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
                "pattern": r".+\.metadatastructure\.Metadataflow=.+",
            },
        )

    @dataclass(frozen=True)
    class MetadataProvisionAgreement:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
                "pattern": r".+\.registry\.MetadataProvisionAgreement=.+",
            },
        )
