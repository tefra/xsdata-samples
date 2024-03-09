from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_search_address_1 import TypeSearchAddress1
from travelport.models.type_search_electronic_address_1 import (
    TypeSearchElectronicAddress1,
)
from travelport.models.type_search_external_identifier_1 import (
    TypeSearchExternalIdentifier1,
)
from travelport.models.type_search_phone_1 import TypeSearchPhone1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class TypeProfileSearchCriteria1:
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

    address: None | TypeSearchAddress1 = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    phone: None | TypeSearchPhone1 = field(
        default=None,
        metadata={
            "name": "Phone",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    electronic_address: None | TypeSearchElectronicAddress1 = field(
        default=None,
        metadata={
            "name": "ElectronicAddress",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    external_identifier: None | TypeSearchExternalIdentifier1 = field(
        default=None,
        metadata={
            "name": "ExternalIdentifier",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    additional_identifier: None | str = field(
        default=None,
        metadata={
            "name": "AdditionalIdentifier",
            "type": "Attribute",
        },
    )
