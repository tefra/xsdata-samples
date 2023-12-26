from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_search_address_2 import TypeSearchAddress2
from travelport.models.type_search_electronic_address_2 import (
    TypeSearchElectronicAddress2,
)
from travelport.models.type_search_external_identifier_2 import (
    TypeSearchExternalIdentifier2,
)
from travelport.models.type_search_phone_2 import TypeSearchPhone2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class TypeProfileSearchCriteria2:
    """
    Basic search criteria.

    Parameters
    ----------
    address
    phone
    electronic_address
    external_identifier
    additional_identifier
        Additional identifier managed by an external system.
    """

    class Meta:
        name = "typeProfileSearchCriteria"

    address: None | TypeSearchAddress2 = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    phone: None | TypeSearchPhone2 = field(
        default=None,
        metadata={
            "name": "Phone",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    electronic_address: None | TypeSearchElectronicAddress2 = field(
        default=None,
        metadata={
            "name": "ElectronicAddress",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    external_identifier: None | TypeSearchExternalIdentifier2 = field(
        default=None,
        metadata={
            "name": "ExternalIdentifier",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    additional_identifier: None | str = field(
        default=None,
        metadata={
            "name": "AdditionalIdentifier",
            "type": "Attribute",
        },
    )
