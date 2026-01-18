from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_taggable_address_1 import TypeTaggableAddress1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass(kw_only=True)
class AlternateContactAddress1(TypeTaggableAddress1):
    """
    Alternate contact address.

    Parameters
    ----------
    alternate_contact_ref
        Key referencing to alternate contact.
    """

    class Meta:
        name = "AlternateContactAddress"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    alternate_contact_ref: str = field(
        metadata={
            "name": "AlternateContactRef",
            "type": "Attribute",
            "required": True,
        }
    )
