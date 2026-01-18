from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.activity import Activity
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.public_event_type_enum import (
    PublicEventTypeEnum,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class PublicEvent(Activity):
    """
    Organised public event which could disrupt traffic.

    :ivar public_event_type: Type of public event which could disrupt
        traffic.
    :ivar public_event_extension:
    """

    public_event_type: None | PublicEventTypeEnum = field(
        default=None,
        metadata={
            "name": "publicEventType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    public_event_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "publicEventExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
