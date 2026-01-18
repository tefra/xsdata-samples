from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.account_info_2 import AccountInfo2
from travelport.models.accounting_reference_2 import AccountingReference2
from travelport.models.address_2 import Address2
from travelport.models.advisory_2 import Advisory2
from travelport.models.agency_group_info_2 import AgencyGroupInfo2
from travelport.models.agency_info_6 import AgencyInfo6
from travelport.models.agent_info_2 import AgentInfo2
from travelport.models.air_preference_2 import AirPreference2
from travelport.models.alternate_contact_2 import AlternateContact2
from travelport.models.alternate_contact_address_2 import (
    AlternateContactAddress2,
)
from travelport.models.alternate_contact_electronic_address_2 import (
    AlternateContactElectronicAddress2,
)
from travelport.models.alternate_contact_phone_2 import AlternateContactPhone2
from travelport.models.branch_group_info_2 import BranchGroupInfo2
from travelport.models.branch_info_2 import BranchInfo2
from travelport.models.commission_8 import Commission8
from travelport.models.commission_reference_2 import CommissionReference2
from travelport.models.contract_2 import Contract2
from travelport.models.electronic_address_2 import ElectronicAddress2
from travelport.models.external_identifier_2 import ExternalIdentifier2
from travelport.models.field_data_2 import FieldData2
from travelport.models.field_group_data_2 import FieldGroupData2
from travelport.models.form_of_payment_6 import FormOfPayment6
from travelport.models.hotel_preference_2 import HotelPreference2
from travelport.models.loyalty_program_enrollment_2 import (
    LoyaltyProgramEnrollment2,
)
from travelport.models.other_preference_2 import OtherPreference2
from travelport.models.phone_2 import Phone2
from travelport.models.policy_reference_2 import PolicyReference2
from travelport.models.proprietary_data_2 import ProprietaryData2
from travelport.models.rail_preference_2 import RailPreference2
from travelport.models.remark_6 import Remark6
from travelport.models.service_fee_2 import ServiceFee2
from travelport.models.travel_document_2 import TravelDocument2
from travelport.models.traveler_group_info_2 import TravelerGroupInfo2
from travelport.models.traveler_identity_information_2 import (
    TravelerIdentityInformation2,
)
from travelport.models.traveler_info_2 import TravelerInfo2
from travelport.models.vehicle_preference_2 import VehiclePreference2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass(kw_only=True)
class ProfileDataUpdate2:
    """
    Update some basic information of the profile.

    Parameters
    ----------
    agency_group_info
    agency_info
    branch_group_info
    branch_info
    agent_info
    account_info
    traveler_group_info
    traveler_info
    address
        Address belonging to the profile (will be updated in the  "Info"
        elements)
    phone
        Phone Number belonging to the profile (will be updated in the
        "Info" elements)
    electronic_address
        Electronic Address belonging to the profile (will be updated in the
        "Info" elements)
    traveler_identity_information
        An additional means to identify or verify a travelers profile when
        then are duplicate traveler names.
    external_identifier
        Meant for external identification of a Profile. This will be updated
        in Info element of the Profile.
    travel_document
    accounting_reference
    policy_reference
    loyalty_program_enrollment
    commission
    contract
    service_fee
    alternate_contact
    alternate_contact_address
    alternate_contact_phone
    alternate_contact_electronic_address
    form_of_payment
    air_preference
    hotel_preference
    other_preference
    remark
    field_data
        Change the values of existing root-level or child-level custom
        fields. To add a new child field value, use FieldData within
        FieldGroupData. To delete an existing child field value, use
        ProfileDataDelete.
    field_group_data
        Add new child field values or modify existing child field values
        within an existing custom field group instance. To delete a field
        group instance and its child field values, use ProfileDataDelete.
    vehicle_preference
    advisory
    commission_reference
    rail_preference
    proprietary_data
    """

    class Meta:
        name = "ProfileDataUpdate"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    agency_group_info: None | AgencyGroupInfo2 = field(
        default=None,
        metadata={
            "name": "AgencyGroupInfo",
            "type": "Element",
        },
    )
    agency_info: None | AgencyInfo6 = field(
        default=None,
        metadata={
            "name": "AgencyInfo",
            "type": "Element",
        },
    )
    branch_group_info: None | BranchGroupInfo2 = field(
        default=None,
        metadata={
            "name": "BranchGroupInfo",
            "type": "Element",
        },
    )
    branch_info: None | BranchInfo2 = field(
        default=None,
        metadata={
            "name": "BranchInfo",
            "type": "Element",
        },
    )
    agent_info: None | AgentInfo2 = field(
        default=None,
        metadata={
            "name": "AgentInfo",
            "type": "Element",
        },
    )
    account_info: None | AccountInfo2 = field(
        default=None,
        metadata={
            "name": "AccountInfo",
            "type": "Element",
        },
    )
    traveler_group_info: None | TravelerGroupInfo2 = field(
        default=None,
        metadata={
            "name": "TravelerGroupInfo",
            "type": "Element",
        },
    )
    traveler_info: None | TravelerInfo2 = field(
        default=None,
        metadata={
            "name": "TravelerInfo",
            "type": "Element",
        },
    )
    address: list[Address2] = field(
        default_factory=list,
        metadata={
            "name": "Address",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    phone: list[Phone2] = field(
        default_factory=list,
        metadata={
            "name": "Phone",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    electronic_address: list[ElectronicAddress2] = field(
        default_factory=list,
        metadata={
            "name": "ElectronicAddress",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    traveler_identity_information: None | TravelerIdentityInformation2 = field(
        default=None,
        metadata={
            "name": "TravelerIdentityInformation",
            "type": "Element",
        },
    )
    external_identifier: list[ExternalIdentifier2] = field(
        default_factory=list,
        metadata={
            "name": "ExternalIdentifier",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    travel_document: list[TravelDocument2] = field(
        default_factory=list,
        metadata={
            "name": "TravelDocument",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    accounting_reference: list[AccountingReference2] = field(
        default_factory=list,
        metadata={
            "name": "AccountingReference",
            "type": "Element",
            "max_occurs": 20000,
        },
    )
    policy_reference: list[PolicyReference2] = field(
        default_factory=list,
        metadata={
            "name": "PolicyReference",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    loyalty_program_enrollment: list[LoyaltyProgramEnrollment2] = field(
        default_factory=list,
        metadata={
            "name": "LoyaltyProgramEnrollment",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    commission: list[Commission8] = field(
        default_factory=list,
        metadata={
            "name": "Commission",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    contract: list[Contract2] = field(
        default_factory=list,
        metadata={
            "name": "Contract",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    service_fee: list[ServiceFee2] = field(
        default_factory=list,
        metadata={
            "name": "ServiceFee",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    alternate_contact: list[AlternateContact2] = field(
        default_factory=list,
        metadata={
            "name": "AlternateContact",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    alternate_contact_address: list[AlternateContactAddress2] = field(
        default_factory=list,
        metadata={
            "name": "AlternateContactAddress",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    alternate_contact_phone: list[AlternateContactPhone2] = field(
        default_factory=list,
        metadata={
            "name": "AlternateContactPhone",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    alternate_contact_electronic_address: list[
        AlternateContactElectronicAddress2
    ] = field(
        default_factory=list,
        metadata={
            "name": "AlternateContactElectronicAddress",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    form_of_payment: list[FormOfPayment6] = field(
        default_factory=list,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    air_preference: list[AirPreference2] = field(
        default_factory=list,
        metadata={
            "name": "AirPreference",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    hotel_preference: list[HotelPreference2] = field(
        default_factory=list,
        metadata={
            "name": "HotelPreference",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    other_preference: list[OtherPreference2] = field(
        default_factory=list,
        metadata={
            "name": "OtherPreference",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    remark: list[Remark6] = field(
        default_factory=list,
        metadata={
            "name": "Remark",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    field_data: list[FieldData2] = field(
        default_factory=list,
        metadata={
            "name": "FieldData",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    field_group_data: list[FieldGroupData2] = field(
        default_factory=list,
        metadata={
            "name": "FieldGroupData",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    vehicle_preference: list[VehiclePreference2] = field(
        default_factory=list,
        metadata={
            "name": "VehiclePreference",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    advisory: list[Advisory2] = field(
        default_factory=list,
        metadata={
            "name": "Advisory",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    commission_reference: list[CommissionReference2] = field(
        default_factory=list,
        metadata={
            "name": "CommissionReference",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    rail_preference: list[RailPreference2] = field(
        default_factory=list,
        metadata={
            "name": "RailPreference",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    proprietary_data: list[ProprietaryData2] = field(
        default_factory=list,
        metadata={
            "name": "ProprietaryData",
            "type": "Element",
            "max_occurs": 999,
        },
    )
