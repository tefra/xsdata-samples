from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_profile_entity_status_2 import (
    TypeProfileEntityStatus2,
)

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass(kw_only=True)
class TypeProfileStatusHistory2:
    """
    History Element for ProfileStatus.

    Parameters
    ----------
    status
        The updated status.
    """

    class Meta:
        name = "typeProfileStatusHistory"

    status: None | TypeProfileEntityStatus2 = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
        },
    )
