from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class ClientDataList:
    """A list of Name Value pairs that can be used to store data specific to a
    Client.

    Name must be unique within a ClientDataList. This element will only
    be added to ProfileCreate, ProfileModify and ProfileRetrieve (Search
    and Delete will not be supported). The ClientDataList will be
    deleted when the element is deleted or the profile is deleted.

    Parameters
    ----------
    name
        The Name that will be associated with the Value.
    value
        The Value that will be associated with the Name.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    name: None | str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 255,
        },
    )
    value: None | str = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 255,
        },
    )
