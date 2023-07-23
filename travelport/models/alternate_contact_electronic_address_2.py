from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_taggable_electronic_address_2 import TypeTaggableElectronicAddress2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class AlternateContactElectronicAddress2(TypeTaggableElectronicAddress2):
    """
    Alternate contact email.

    Parameters
    ----------
    alternate_contact_ref
        Key referencing to alternate contact.
    """
    class Meta:
        name = "AlternateContactElectronicAddress"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    alternate_contact_ref: None | str = field(
        default=None,
        metadata={
            "name": "AlternateContactRef",
            "type": "Attribute",
            "required": True,
        }
    )
