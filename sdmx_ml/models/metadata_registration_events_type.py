from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef, Optional, Union

from sdmx_ml.models.empty_type import EmptyType
from sdmx_ml.models.maintainable_event_type import MaintainableEventType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry"


@dataclass(frozen=True)
class MetadataRegistrationEventsType:
    """
    MetadataRegistrationEventsType details the metadata registration events
    for the subscription.

    It is possible to subscribe to all metadata registration events in the
    repository, or specific events for; single registrations, provision
    agreements, data providers, metadata flows, metadata structure
    definitions, and categories that categorize metadata flows or metadata
    structure definitions.

    :ivar choice:
    :ivar type_value: TYPE is a fixed attribute that is used to ensure
        only of each event selector may be provided, when it is
        referenced in a uniqueness constraint.
    """

    choice: tuple[
        EmptyType | MetadataRegistrationEventsType.RegistrationId | MetadataRegistrationEventsType.ProvisionAgreement | MetadataRegistrationEventsType.DataProvider | MetadataRegistrationEventsType.MetadataflowReference | MetadataRegistrationEventsType.MetadataStructureDefinitionReference | MetadataRegistrationEventsType.Category,
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
                        "MetadataRegistrationEventsType.RegistrationId"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                },
                {
                    "name": "ProvisionAgreement",
                    "type": ForwardRef(
                        "MetadataRegistrationEventsType.ProvisionAgreement"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                },
                {
                    "name": "DataProvider",
                    "type": ForwardRef(
                        "MetadataRegistrationEventsType.DataProvider"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                },
                {
                    "name": "MetadataflowReference",
                    "type": ForwardRef(
                        "MetadataRegistrationEventsType.MetadataflowReference"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                },
                {
                    "name": "MetadataStructureDefinitionReference",
                    "type": ForwardRef(
                        "MetadataRegistrationEventsType.MetadataStructureDefinitionReference"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                },
                {
                    "name": "Category",
                    "type": ForwardRef(
                        "MetadataRegistrationEventsType.Category"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                },
            ),
        },
    )
    type_value: str = field(
        init=False,
        default="METADATA",
        metadata={
            "name": "TYPE",
            "type": "Attribute",
        },
    )

    @dataclass(frozen=True)
    class RegistrationId:
        value: str | None = field(
            default=None,
            metadata={
                "required": True,
                "pattern": r"[A-Za-z0-9_@$\-]+",
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
    class DataProvider:
        value: str | None = field(
            default=None,
            metadata={
                "required": True,
                "pattern": r".+\.base\.DataProvider=.+:DATA_PROVIDERS\(.+\).+",
            },
        )

    @dataclass(frozen=True)
    class MetadataflowReference(MaintainableEventType):
        pass

    @dataclass(frozen=True)
    class MetadataStructureDefinitionReference(MaintainableEventType):
        pass

    @dataclass(frozen=True)
    class Category:
        value: str | None = field(
            default=None,
            metadata={
                "required": True,
                "pattern": r".+\.categoryscheme\.Category=.+",
            },
        )
