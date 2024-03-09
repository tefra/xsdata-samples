from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_key_element_1 import TypeKeyElement1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class ExternalIdentifier1(TypeKeyElement1):
    """
    This is meant for external identification of a Profile.

    Parameters
    ----------
    ext_id
        The actual value of the External Id of the Profile.
    source
        The Source code for External ID. This depicts the origin/source of
        the External ID. If the Source is a host provider i.e, 1G, 1V etc.,
        the ExtID and Source data may not be updated.
    """

    class Meta:
        name = "ExternalIdentifier"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    ext_id: None | str = field(
        default=None,
        metadata={
            "name": "ExtID",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 255,
        },
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
