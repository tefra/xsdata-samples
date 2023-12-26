from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_taggable_address_2 import TypeTaggableAddress2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class Address2(TypeTaggableAddress2):
    """
    Profile Address.

    Parameters
    ----------
    provisioned
        Indicator to show if this address is used as the provisioned
        address.  Default is false.
    owner_id
        Id of the profile who owns the Traveler's proprietary data.Should be
        the immediate parent id of the traveler.
    """

    class Meta:
        name = "Address"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    provisioned: bool = field(
        default=False,
        metadata={
            "name": "Provisioned",
            "type": "Attribute",
        },
    )
    owner_id: None | int = field(
        default=None,
        metadata={
            "name": "OwnerID",
            "type": "Attribute",
        },
    )
