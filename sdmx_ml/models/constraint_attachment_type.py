from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"


@dataclass(frozen=True, kw_only=True)
class ConstraintAttachmentType:
    """
    ConstraintAttachmentType describes a collection of references to
    constrainable artefacts.
    """

    choice: tuple[
        ConstraintAttachmentType.DataProvider
        | ConstraintAttachmentType.MetadataProvider
        | ConstraintAttachmentType.DataStructure
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
                    "name": "DataProvider",
                    "type": ForwardRef(
                        "ConstraintAttachmentType.DataProvider"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure",
                },
                {
                    "name": "MetadataProvider",
                    "type": ForwardRef(
                        "ConstraintAttachmentType.MetadataProvider"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure",
                },
                {
                    "name": "DataStructure",
                    "type": ForwardRef(
                        "ConstraintAttachmentType.DataStructure"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure",
                },
                {
                    "name": "MetadataStructure",
                    "type": ForwardRef(
                        "ConstraintAttachmentType.MetadataStructure"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure",
                },
                {
                    "name": "Dataflow",
                    "type": ForwardRef("ConstraintAttachmentType.Dataflow"),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure",
                },
                {
                    "name": "Metadataflow",
                    "type": ForwardRef(
                        "ConstraintAttachmentType.Metadataflow"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure",
                },
                {
                    "name": "ProvisionAgreement",
                    "type": ForwardRef(
                        "ConstraintAttachmentType.ProvisionAgreement"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure",
                },
                {
                    "name": "MetadataProvisionAgreement",
                    "type": ForwardRef(
                        "ConstraintAttachmentType.MetadataProvisionAgreement"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure",
                },
            ),
        },
    )

    @dataclass(frozen=True, kw_only=True)
    class DataProvider:
        value: str = field(
            default="",
            metadata={
                "required": True,
                "pattern": r".+\.base\.DataProvider=.+:DATA_PROVIDERS\(.+\).+",
            },
        )

    @dataclass(frozen=True, kw_only=True)
    class MetadataProvider:
        value: str = field(
            default="",
            metadata={
                "required": True,
                "pattern": r".+\.base\.MetadataProvider=.+:METADATA_PROVIDERS\(.+\).+",
            },
        )

    @dataclass(frozen=True, kw_only=True)
    class DataStructure:
        value: str = field(
            default="",
            metadata={
                "required": True,
                "pattern": r".+\.datastructure\.DataStructure=.+",
            },
        )

    @dataclass(frozen=True, kw_only=True)
    class MetadataStructure:
        value: str = field(
            default="",
            metadata={
                "required": True,
                "pattern": r".+\.metadatastructure\.MetadataStructure=.+",
            },
        )

    @dataclass(frozen=True, kw_only=True)
    class Dataflow:
        value: str = field(
            default="",
            metadata={
                "required": True,
                "pattern": r".+\.datastructure\.Dataflow=.+",
            },
        )

    @dataclass(frozen=True, kw_only=True)
    class Metadataflow:
        value: str = field(
            default="",
            metadata={
                "required": True,
                "pattern": r".+\.metadatastructure\.Metadataflow=.+",
            },
        )

    @dataclass(frozen=True, kw_only=True)
    class ProvisionAgreement:
        value: str = field(
            default="",
            metadata={
                "required": True,
                "pattern": r".+\.registry\.ProvisionAgreement=.+",
            },
        )

    @dataclass(frozen=True, kw_only=True)
    class MetadataProvisionAgreement:
        value: str = field(
            default="",
            metadata={
                "required": True,
                "pattern": r".+\.registry\.MetadataProvisionAgreement=.+",
            },
        )
