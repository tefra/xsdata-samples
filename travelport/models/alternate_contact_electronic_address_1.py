from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_taggable_electronic_address_1 import (
    TypeTaggableElectronicAddress1,
)

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass(kw_only=True)
class AlternateContactElectronicAddress1(TypeTaggableElectronicAddress1):
    """
    Alternate contact email.

    Parameters
    ----------
    alternate_contact_ref
        Key referencing to alternate contact.
    """

    class Meta:
        name = "AlternateContactElectronicAddress"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    alternate_contact_ref: str = field(
        metadata={
            "name": "AlternateContactRef",
            "type": "Attribute",
            "required": True,
        }
    )
