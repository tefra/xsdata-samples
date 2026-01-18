from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass(kw_only=True)
class TypeSearchExternalIdentifier2:
    """
    This is meant for external identification of a Profile.

    Parameters
    ----------
    ext_id
        The actual value of the External Id of the Profile.
    source
        The Source code for External ID. This depicts the origin/source of
        the External ID.
    """

    class Meta:
        name = "typeSearchExternalIdentifier"

    ext_id: str = field(
        metadata={
            "name": "ExtID",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 255,
        }
    )
    source: None | str = field(
        default=None,
        metadata={
            "name": "Source",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        },
    )
