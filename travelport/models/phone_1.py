from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_taggable_phone_1 import TypeTaggablePhone1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class Phone1(TypeTaggablePhone1):
    """
    Profile Phone Number.

    Parameters
    ----------
    provisioned
        Indicator to show if this phone is used as the provisioned phone.
        Default is false.
    owner_id
        Id of the profile who owns the Traveler's proprietary data.Should be
        the immediate parent id of the traveler.
    """

    class Meta:
        name = "Phone"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

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
