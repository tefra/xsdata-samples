from dataclasses import dataclass, field
from typing import Optional, Tuple, Type, Union

from sdmx_ml.models.queryable_data_source_type_1 import (
    QueryableDataSourceType1,
)

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class ConstraintAttachmentType:
    """
    ConstraintAttachmentType describes a collection of references to constrainable
    artefacts.
    """

    choice: Tuple[
        Union[
            "ConstraintAttachmentType.DataProvider",
            "ConstraintAttachmentType.MetadataProvider",
            "ConstraintAttachmentType.MetadataSet",
            "ConstraintAttachmentType.SimpleDataSource",
            "ConstraintAttachmentType.DataStructure",
        ],
        ...,
    ] = field(
        default_factory=tuple,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DataProvider",
                    "type": Type["ConstraintAttachmentType.DataProvider"],
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "MetadataProvider",
                    "type": Type["ConstraintAttachmentType.MetadataProvider"],
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "MetadataSet",
                    "type": Type["ConstraintAttachmentType.MetadataSet"],
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "SimpleDataSource",
                    "type": Type["ConstraintAttachmentType.SimpleDataSource"],
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "DataStructure",
                    "type": Type["ConstraintAttachmentType.DataStructure"],
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
            ),
        },
    )
    choice_1: Tuple[
        Union[
            QueryableDataSourceType1,
            "ConstraintAttachmentType.MetadataStructure",
            "ConstraintAttachmentType.Dataflow",
            "ConstraintAttachmentType.Metadataflow",
            "ConstraintAttachmentType.ProvisionAgreement",
            "ConstraintAttachmentType.MetadataProvisionAgreement",
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
                    "name": "MetadataStructure",
                    "type": Type["ConstraintAttachmentType.MetadataStructure"],
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "Dataflow",
                    "type": Type["ConstraintAttachmentType.Dataflow"],
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "Metadataflow",
                    "type": Type["ConstraintAttachmentType.Metadataflow"],
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "ProvisionAgreement",
                    "type": Type[
                        "ConstraintAttachmentType.ProvisionAgreement"
                    ],
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "MetadataProvisionAgreement",
                    "type": Type[
                        "ConstraintAttachmentType.MetadataProvisionAgreement"
                    ],
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
            ),
        },
    )

    @dataclass(frozen=True)
    class DataProvider:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
                "pattern": r".+\.base\.DataProvider=.+:DATA_PROVIDERS\(.+\).+",
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
    class DataStructure:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
                "pattern": r".+\.datastructure\.DataStructure=.+",
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
    class Dataflow:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
                "pattern": r".+\.datastructure\.Dataflow=.+",
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
    class ProvisionAgreement:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
                "pattern": r".+\.registry\.ProvisionAgreement=.+",
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