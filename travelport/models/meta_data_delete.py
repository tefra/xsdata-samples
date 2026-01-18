from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass(kw_only=True)
class MetaDataDelete:
    """
    Delete element of given type identified by its key.

    Parameters
    ----------
    key
        The identifier of the element that will be deleted from this
        profile.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    key: int = field(
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        }
    )
