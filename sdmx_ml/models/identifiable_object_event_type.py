from dataclasses import dataclass, field
from typing import ForwardRef, Optional, Union

from sdmx_ml.models.empty_type import EmptyType
from sdmx_ml.models.wild_card_value_type import WildCardValueType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry"


@dataclass(frozen=True)
class IdentifiableObjectEventType:
    """
    IdentifiableObjectEventType describes the structure of a reference to
    an identifiable object's events.

    Either all instances of the object matching the inherited criteria, a
    specific instance, or specific instances of the object may be selected.
    """

    all_or_urn_or_id: Optional[
        Union[
            EmptyType,
            "IdentifiableObjectEventType.Urn",
            "IdentifiableObjectEventType.Id",
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
                    "name": "URN",
                    "type": ForwardRef("IdentifiableObjectEventType.Urn"),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                },
                {
                    "name": "ID",
                    "type": ForwardRef("IdentifiableObjectEventType.Id"),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/registry",
                },
            ),
        },
    )

    @dataclass(frozen=True)
    class Urn:
        value: Optional[str] = field(
            default=None,
            metadata={
                "required": True,
            },
        )

    @dataclass(frozen=True)
    class Id:
        value: Optional[Union[str, WildCardValueType]] = field(
            default=None,
            metadata={
                "required": True,
                "pattern": r"[A-Za-z0-9_@$\-]+",
            },
        )
