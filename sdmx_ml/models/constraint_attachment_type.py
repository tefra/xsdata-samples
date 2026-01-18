from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef

from sdmx_ml.models.queryable_data_source_type_1 import (
    QueryableDataSourceType1,
)

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class ConstraintAttachmentType:
    """
    ConstraintAttachmentType describes a collection of references to
    constrainable artefacts.
    """

    choice: tuple[
        ConstraintAttachmentType.DataProvider
        | ConstraintAttachmentType.MetadataProvider
        | ConstraintAttachmentType.MetadataSet
        | ConstraintAttachmentType.SimpleDataSource
        | ConstraintAttachmentType.DataStructure,
        ...,
    ] = field(
        default_factory=tuple,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DataProvider",
                    "type": ForwardRef(
                        "ConstraintAttachmentType.DataProvider"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "MetadataProvider",
                    "type": ForwardRef(
                        "ConstraintAttachmentType.MetadataProvider"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "MetadataSet",
                    "type": ForwardRef("ConstraintAttachmentType.MetadataSet"),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "SimpleDataSource",
                    "type": ForwardRef(
                        "ConstraintAttachmentType.SimpleDataSource"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "DataStructure",
                    "type": ForwardRef(
                        "ConstraintAttachmentType.DataStructure"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
            ),
        },
    )
    choice_1: tuple[
        QueryableDataSourceType1
        | ConstraintAttachmentType.MetadataStructure
        | ConstraintAttachmentType.Dataflow
        | ConstraintAttachmentType.Metadataflow
        | ConstraintAttachmentType.ProvisionAgreement
        | ConstraintAttachmentType.MetadataProvisionAgreement,
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
                    "type": ForwardRef(
                        "ConstraintAttachmentType.MetadataStructure"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "Dataflow",
                    "type": ForwardRef("ConstraintAttachmentType.Dataflow"),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "Metadataflow",
                    "type": ForwardRef(
                        "ConstraintAttachmentType.Metadataflow"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "ProvisionAgreement",
                    "type": ForwardRef(
                        "ConstraintAttachmentType.ProvisionAgreement"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "MetadataProvisionAgreement",
                    "type": ForwardRef(
                        "ConstraintAttachmentType.MetadataProvisionAgreement"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
            ),
        },
    )

    @dataclass(frozen=True)
    class DataProvider:
        value: str | None = field(
            default=None,
            metadata={
                "required": True,
                "pattern": r".+\.base\.DataProvider=.+:DATA_PROVIDERS\(.+\).+",
            },
        )

    @dataclass(frozen=True)
    class MetadataProvider:
        value: str | None = field(
            default=None,
            metadata={
                "required": True,
                "pattern": r".+\.base\.MetadataProvider=.+:METADATA_PROVIDERS\(.+\).+",
            },
        )

    @dataclass(frozen=True)
    class MetadataSet:
        value: str | None = field(
            default=None,
            metadata={
                "required": True,
                "pattern": r".+\.metadatastructure\.MetadataSet=.+",
            },
        )

    @dataclass(frozen=True)
    class SimpleDataSource:
        value: str | None = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass(frozen=True)
    class DataStructure:
        value: str | None = field(
            default=None,
            metadata={
                "required": True,
                "pattern": r".+\.datastructure\.DataStructure=.+",
            },
        )

    @dataclass(frozen=True)
    class MetadataStructure:
        value: str | None = field(
            default=None,
            metadata={
                "required": True,
                "pattern": r".+\.metadatastructure\.MetadataStructure=.+",
            },
        )

    @dataclass(frozen=True)
    class Dataflow:
        value: str | None = field(
            default=None,
            metadata={
                "required": True,
                "pattern": r".+\.datastructure\.Dataflow=.+",
            },
        )

    @dataclass(frozen=True)
    class Metadataflow:
        value: str | None = field(
            default=None,
            metadata={
                "required": True,
                "pattern": r".+\.metadatastructure\.Metadataflow=.+",
            },
        )

    @dataclass(frozen=True)
    class ProvisionAgreement:
        value: str | None = field(
            default=None,
            metadata={
                "required": True,
                "pattern": r".+\.registry\.ProvisionAgreement=.+",
            },
        )

    @dataclass(frozen=True)
    class MetadataProvisionAgreement:
        value: str | None = field(
            default=None,
            metadata={
                "required": True,
                "pattern": r".+\.registry\.MetadataProvisionAgreement=.+",
            },
        )
