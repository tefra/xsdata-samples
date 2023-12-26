from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_key_element_1 import TypeKeyElement1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class TypeExternalIdentifierHistory1(TypeKeyElement1):
    """
    This is meant for external identification of a Profile.

    Parameters
    ----------
    ext_id
        Value of the External Id of the Profile.
    source
        The Source code for External ID. This depicts the origin/source of
        the External ID.
    """

    class Meta:
        name = "typeExternalIdentifierHistory"

    ext_id: None | str = field(
        default=None,
        metadata={
            "name": "ExtID",
            "type": "Attribute",
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
