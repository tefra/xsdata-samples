from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_profile_entity_status_1 import (
    TypeProfileEntityStatus1,
)

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class TypeProfileStatusHistory1:
    """
    History Element for ProfileStatus.

    Parameters
    ----------
    status
        The updated status.
    """

    class Meta:
        name = "typeProfileStatusHistory"

    status: None | TypeProfileEntityStatus1 = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
        },
    )
