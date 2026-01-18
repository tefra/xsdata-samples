from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef

from sdmx_ml.models.empty_type import EmptyType
from sdmx_ml.models.wild_card_value_type import WildCardValueType
from sdmx_ml.models.wildcard_type import WildcardType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry"


@dataclass(frozen=True, kw_only=True)
class VersionableObjectEventType:
    """
    VersionableObjectEventType describes the structure of a reference to a
    versionable object's events.

    Either all instances of the object matching the inherited criteria, a
    specific instance, or specific instances of the object may be selected.
    """

    choice: tuple[
        EmptyType
        | VersionableObjectEventType.Urn
        | VersionableObjectEventType.Id
        | VersionableObjectEventType.Version,
        ...,
    ] = field(
        default_factory=tuple,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "All",
                    "type": EmptyType,
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                },
                {
                    "name": "URN",
                    "type": ForwardRef("VersionableObjectEventType.Urn"),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                },
                {
                    "name": "ID",
                    "type": ForwardRef("VersionableObjectEventType.Id"),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                },
                {
                    "name": "Version",
                    "type": ForwardRef("VersionableObjectEventType.Version"),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                },
            ),
            "max_occurs": 2,
        },
    )

    @dataclass(frozen=True, kw_only=True)
    class Urn:
        value: str = field(
            metadata={
                "required": True,
            }
        )

    @dataclass(frozen=True, kw_only=True)
    class Id:
        value: str | WildCardValueType = field(
            metadata={
                "required": True,
                "pattern": r"[A-Za-z0-9_@$\-]+",
            }
        )

    @dataclass(frozen=True, kw_only=True)
    class Version:
        value: str | WildcardType | WildCardValueType = field(
            metadata={
                "required": True,
                "pattern": r"(0|[1-9]\d*)(\.(0|[1-9]\d*))?",
            }
        )
