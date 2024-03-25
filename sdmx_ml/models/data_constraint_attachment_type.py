from dataclasses import dataclass, field
from typing import Optional, Tuple, Type, Union

from sdmx_ml.models.queryable_data_source_type_1 import (
    QueryableDataSourceType1,
)

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class DataConstraintAttachmentType:
    """
    DataConstraintAttachmentType restricts the base ConstraintAttachmentType to
    only allow artefacts related to data.
    """

    data_provider_or_simple_data_source_or_data_structure: Tuple[
        Union[
            "DataConstraintAttachmentType.DataProvider",
            "DataConstraintAttachmentType.SimpleDataSource",
            "DataConstraintAttachmentType.DataStructure",
        ],
        ...,
    ] = field(
        default_factory=tuple,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DataProvider",
                    "type": Type["DataConstraintAttachmentType.DataProvider"],
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "SimpleDataSource",
                    "type": Type[
                        "DataConstraintAttachmentType.SimpleDataSource"
                    ],
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "DataStructure",
                    "type": Type["DataConstraintAttachmentType.DataStructure"],
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
            ),
        },
    )
    queryable_data_source_or_dataflow_or_provision_agreement: Tuple[
        Union[
            QueryableDataSourceType1,
            "DataConstraintAttachmentType.Dataflow",
            "DataConstraintAttachmentType.ProvisionAgreement",
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
                    "name": "Dataflow",
                    "type": Type["DataConstraintAttachmentType.Dataflow"],
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
                },
                {
                    "name": "ProvisionAgreement",
                    "type": Type[
                        "DataConstraintAttachmentType.ProvisionAgreement"
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
    class Dataflow:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
                "pattern": r".+\.datastructure\.Dataflow=.+",
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
