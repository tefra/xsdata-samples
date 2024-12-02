from dataclasses import dataclass, field
from typing import ForwardRef, Optional, Union

from sdmx_ml.models.empty_type import EmptyType
from sdmx_ml.models.maintainable_event_type import MaintainableEventType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry"


@dataclass(frozen=True)
class DataRegistrationEventsType:
    """DataRegistrationEventsType details the data registration events for the
    subscription.

    It is possible to subscribe to all data registration events in the
    repository, or specific events for; single registrations, provision
    agreements, data providers, data flows, key families, and categories
    that categorize data flows or key families.

    :ivar choice:
    :ivar type_value: TYPE is a fixed attribute that is used to ensure
        only of each event selector may be provided, when it is
        referenced in a uniqueness constraint.
    """

    choice: tuple[
        Union[
            EmptyType,
            "DataRegistrationEventsType.RegistrationId",
            "DataRegistrationEventsType.ProvisionAgreement",
            "DataRegistrationEventsType.DataProvider",
            "DataRegistrationEventsType.DataflowReference",
            "DataRegistrationEventsType.KeyFamilyReference",
            "DataRegistrationEventsType.Category",
        ],
        ...,
    ] = field(
        default_factory=tuple,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AllEvents",
                    "type": EmptyType,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                },
                {
                    "name": "RegistrationID",
                    "type": ForwardRef(
                        "DataRegistrationEventsType.RegistrationId"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                },
                {
                    "name": "ProvisionAgreement",
                    "type": ForwardRef(
                        "DataRegistrationEventsType.ProvisionAgreement"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                },
                {
                    "name": "DataProvider",
                    "type": ForwardRef(
                        "DataRegistrationEventsType.DataProvider"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                },
                {
                    "name": "DataflowReference",
                    "type": ForwardRef(
                        "DataRegistrationEventsType.DataflowReference"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                },
                {
                    "name": "KeyFamilyReference",
                    "type": ForwardRef(
                        "DataRegistrationEventsType.KeyFamilyReference"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                },
                {
                    "name": "Category",
                    "type": ForwardRef("DataRegistrationEventsType.Category"),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                },
            ),
        },
    )
    type_value: str = field(
        init=False,
        default="DATA",
        metadata={
            "name": "TYPE",
            "type": "Attribute",
        },
    )

    @dataclass(frozen=True)
    class RegistrationId:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
                "pattern": r"[A-Za-z0-9_@$\-]+",
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
    class DataflowReference(MaintainableEventType):
        pass

    @dataclass(frozen=True)
    class KeyFamilyReference(MaintainableEventType):
        pass

    @dataclass(frozen=True)
    class Category:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
                "pattern": r".+\.categoryscheme\.Category=.+",
            },
        )
