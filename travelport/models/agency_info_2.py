from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.address_1 import Address1
from travelport.models.advisory_1 import Advisory1
from travelport.models.agency_info_ursync_data_1 import AgencyInfoUrsyncData1
from travelport.models.electronic_address_1 import ElectronicAddress1
from travelport.models.external_identifier_1 import ExternalIdentifier1
from travelport.models.phone_1 import Phone1
from travelport.models.type_profile_info_1 import TypeProfileInfo1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class AgencyInfo2(TypeProfileInfo1):
    """
    Information relating to Agency.

    Parameters
    ----------
    advisory
        A set of documents or other advice for travel purposes that an
        agency recommends that a traveler have, based on a destination."
    address
        Agency Address
    phone
        Agency Phone Number
    electronic_address
        Agency Electronic Address
    external_identifier
        Agency External Identifier
    name
        Agency name. Modifying this value requires special authorization.
    iata_number
        An IATA number associated to the agency. Not used to transact with
        host systems. Specified in the profile only to support searching for
        the agency profile by IATA number.
    agency_code
        Zircon site ID. Modifying this value requires special authorization.
    uses_template
        If set to true, it denotes that the customer uses templates and
        during parent data inheritance, templates will be used. Value can be
        altered through modify service.Default is false.
    profile_sync_to
        Identify if profile sync to operation can be performed.Ignored in
        request message.
    profile_sync_from
        Identify if profile sync from operation can be performed.Ignored in
        request message.
    ursync_data
        If set to 'Masked' then Form Of Payment card number will be masked
        when Universal Record is sent to EventHandler.
    ursync_to
        Identify if Universal Record synch is activated at Agency Level.
    """

    class Meta:
        name = "AgencyInfo"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    advisory: list[Advisory1] = field(
        default_factory=list,
        metadata={
            "name": "Advisory",
            "type": "Element",
        },
    )
    address: list[Address1] = field(
        default_factory=list,
        metadata={
            "name": "Address",
            "type": "Element",
        },
    )
    phone: list[Phone1] = field(
        default_factory=list,
        metadata={
            "name": "Phone",
            "type": "Element",
        },
    )
    electronic_address: list[ElectronicAddress1] = field(
        default_factory=list,
        metadata={
            "name": "ElectronicAddress",
            "type": "Element",
        },
    )
    external_identifier: list[ExternalIdentifier1] = field(
        default_factory=list,
        metadata={
            "name": "ExternalIdentifier",
            "type": "Element",
        },
    )
    name: None | str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        },
    )
    iata_number: None | str = field(
        default=None,
        metadata={
            "name": "IataNumber",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 8,
        },
    )
    agency_code: None | str = field(
        default=None,
        metadata={
            "name": "AgencyCode",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 25,
        },
    )
    uses_template: bool = field(
        default=False,
        metadata={
            "name": "UsesTemplate",
            "type": "Attribute",
        },
    )
    profile_sync_to: None | bool = field(
        default=None,
        metadata={
            "name": "ProfileSyncTo",
            "type": "Attribute",
        },
    )
    profile_sync_from: None | bool = field(
        default=None,
        metadata={
            "name": "ProfileSyncFrom",
            "type": "Attribute",
        },
    )
    ursync_data: AgencyInfoUrsyncData1 = field(
        default=AgencyInfoUrsyncData1.MASKED,
        metadata={
            "name": "URSyncData",
            "type": "Attribute",
        },
    )
    ursync_to: bool = field(
        default=False,
        metadata={
            "name": "URSyncTo",
            "type": "Attribute",
        },
    )
