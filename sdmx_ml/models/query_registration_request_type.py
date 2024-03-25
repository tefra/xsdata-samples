from dataclasses import dataclass, field
from typing import Optional, Tuple, Type, Union

from sdmx_ml.models.cube_region_type import CubeRegionType
from sdmx_ml.models.data_key_set_type import DataKeySetType
from sdmx_ml.models.empty_type import EmptyType
from sdmx_ml.models.metadata_target_region_type import MetadataTargetRegionType
from sdmx_ml.models.query_type_type import QueryTypeType
from sdmx_ml.models.reference_period_type import ReferencePeriodType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry"


@dataclass(frozen=True)
class QueryRegistrationRequestType:
    """QueryRegistrationRequestType describes the structure of a registration query
    request.

    The type of query (data, reference metadata, or both) must be
    specified. It is possible to query for registrations for a
    particular provision agreement, data provider, or structure usage,
    or to query for all registrations in the registry. In addition the
    search can be refined by providing constraints in the form of
    explicit time periods, constraint regions, and key sets. When
    constraint regions and key sets are provided they will be
    effectively processed by first matching all data for the included
    keys and regions (all available data if there are none) and then
    removing any data matching the excluded keys or regions.

    :ivar query_type: QueryType defines the type of sets (data,
        metadata, or both) that are being queried for.
    :ivar choice:
    :ivar reference_period: ReferencePeriod provides an inclusive start
        and end date for the data or metadata being sought.
    :ivar data_key_set_or_cube_region_or_metadata_target_region:
    :ivar return_constraints: The returnConstraints attribute determines
        whether information about the constraints on the data or
        metadata sets returned should also be sent the results.
    """

    query_type: Optional[QueryTypeType] = field(
        default=None,
        metadata={
            "name": "QueryType",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
            "required": True,
        },
    )
    choice: Optional[
        Union[
            EmptyType,
            "QueryRegistrationRequestType.ProvisionAgreement",
            "QueryRegistrationRequestType.DataProvider",
            "QueryRegistrationRequestType.Dataflow",
            "QueryRegistrationRequestType.Metadataflow",
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "All",
                    "type": EmptyType,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                },
                {
                    "name": "ProvisionAgreement",
                    "type": Type[
                        "QueryRegistrationRequestType.ProvisionAgreement"
                    ],
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                },
                {
                    "name": "DataProvider",
                    "type": Type["QueryRegistrationRequestType.DataProvider"],
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                },
                {
                    "name": "Dataflow",
                    "type": Type["QueryRegistrationRequestType.Dataflow"],
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                },
                {
                    "name": "Metadataflow",
                    "type": Type["QueryRegistrationRequestType.Metadataflow"],
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                },
            ),
        },
    )
    reference_period: Optional[ReferencePeriodType] = field(
        default=None,
        metadata={
            "name": "ReferencePeriod",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
        },
    )
    data_key_set_or_cube_region_or_metadata_target_region: Tuple[
        Union[DataKeySetType, CubeRegionType, MetadataTargetRegionType], ...
    ] = field(
        default_factory=tuple,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DataKeySet",
                    "type": DataKeySetType,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                },
                {
                    "name": "CubeRegion",
                    "type": CubeRegionType,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                },
                {
                    "name": "MetadataTargetRegion",
                    "type": MetadataTargetRegionType,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                },
            ),
        },
    )
    return_constraints: bool = field(
        default=False,
        metadata={
            "name": "returnConstraints",
            "type": "Attribute",
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
    class DataProvider:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
                "pattern": r".+\.base\.DataProvider=.+:DATA_PROVIDERS\(.+\).+",
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
