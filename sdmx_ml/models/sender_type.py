from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.party_type import PartyType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message"


@dataclass(frozen=True, kw_only=True)
class SenderType(PartyType):
    """
    SenderType extends the basic party structure to add an optional time
    zone declaration.

    :ivar timezone: Timezone specifies the time zone of the sender, and
        if specified can be applied to all un-time zoned time values in
        the message. In the absence of this, any dates without time zone
        are implied to be in an indeterminate "local time".
    """

    timezone: None | str = field(
        default=None,
        metadata={
            "name": "Timezone",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message",
            "pattern": r"Z|(\+|\-)(14:00|((0[0-9]|1[0-3]):[0-5][0-9]))",
        },
    )
