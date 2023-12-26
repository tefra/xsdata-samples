from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.contact import Contact
from datexii.models.eu.datexii.v2.contact_details_versioned_reference import (
    ContactDetailsVersionedReference,
)
from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class ContactByReference(Contact):
    """
    Contact information that is addressed via a reference.

    :ivar contact_reference: Contact information provided by a
        reference.
    :ivar contact_by_reference_extension:
    """

    contact_reference: Optional[ContactDetailsVersionedReference] = field(
        default=None,
        metadata={
            "name": "contactReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    contact_by_reference_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "contactByReferenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
