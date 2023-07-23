from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_taggable_phone_1 import TypeTaggablePhone1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class AlternateContactPhone1(TypeTaggablePhone1):
    """
    Alternate contact phone.

    Parameters
    ----------
    alternate_contact_ref
        Key referencing to alternate contact.
    """
    class Meta:
        name = "AlternateContactPhone"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    alternate_contact_ref: None | str = field(
        default=None,
        metadata={
            "name": "AlternateContactRef",
            "type": "Attribute",
            "required": True,
        }
    )
