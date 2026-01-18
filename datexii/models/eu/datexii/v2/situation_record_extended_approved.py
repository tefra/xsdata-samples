from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class SituationRecordExtendedApproved:
    """
    Extension class for SituationRecord.

    :ivar safety_related_message: Indicates, whether this
        SituationRecord specifies a safety related message according to
        Commission Delegated Regulation (EU) No 886/2013.
    """

    safety_related_message: bool | None = field(
        default=None,
        metadata={
            "name": "safetyRelatedMessage",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
