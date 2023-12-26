from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.accounting_reference_1 import AccountingReference1
from travelport.models.address_1 import Address1
from travelport.models.advisory_1 import Advisory1
from travelport.models.air_preference_1 import AirPreference1
from travelport.models.alternate_contact_1 import AlternateContact1
from travelport.models.alternate_contact_address_1 import (
    AlternateContactAddress1,
)
from travelport.models.alternate_contact_electronic_address_1 import (
    AlternateContactElectronicAddress1,
)
from travelport.models.alternate_contact_phone_1 import AlternateContactPhone1
from travelport.models.commission_4 import Commission4
from travelport.models.commission_reference_1 import CommissionReference1
from travelport.models.contract_1 import Contract1
from travelport.models.electronic_address_1 import ElectronicAddress1
from travelport.models.external_identifier_1 import ExternalIdentifier1
from travelport.models.field_data_1 import FieldData1
from travelport.models.field_group_data_1 import FieldGroupData1
from travelport.models.form_of_payment_2 import FormOfPayment2
from travelport.models.hotel_preference_1 import HotelPreference1
from travelport.models.loyalty_program_enrollment_1 import (
    LoyaltyProgramEnrollment1,
)
from travelport.models.other_preference_1 import OtherPreference1
from travelport.models.phone_1 import Phone1
from travelport.models.policy_reference_1 import PolicyReference1
from travelport.models.proprietary_data_1 import ProprietaryData1
from travelport.models.provider_info_1 import ProviderInfo1
from travelport.models.rail_preference_1 import RailPreference1
from travelport.models.remark_2 import Remark2
from travelport.models.service_fee_1 import ServiceFee1
from travelport.models.travel_document_1 import TravelDocument1
from travelport.models.traveler_identity_information_1 import (
    TravelerIdentityInformation1,
)
from travelport.models.vehicle_preference_1 import VehiclePreference1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class ProfileDataAdd1:
    """
    Command to add profile data information.

    Parameters
    ----------
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
        Meant for external identification of a Profile. This will be added
        in Info element of the Profile.
    travel_document
    accounting_reference
    policy_reference
    loyalty_program_enrollment
    commission
    contract
    service_fee
    form_of_payment
    air_preference
    hotel_preference
    other_preference
    remark
    field_data
        Add new values for root-level custom fields. To add a new child
        field value, use ProfileDataUpdate and update the parent field
        group.
    alternate_contact
    alternate_contact_address
    alternate_contact_phone
    alternate_contact_electronic_address
    field_group_data
        Add new instances of a custom field group and child field values.
    vehicle_preference
    advisory
    commission_reference
    rail_preference
    provider_info
    proprietary_data
    """

    class Meta:
        name = "ProfileDataAdd"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

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
    traveler_identity_information: None | TravelerIdentityInformation1 = field(
        default=None,
        metadata={
            "name": "TravelerIdentityInformation",
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
    travel_document: list[TravelDocument1] = field(
        default_factory=list,
        metadata={
            "name": "TravelDocument",
            "type": "Element",
        },
    )
    accounting_reference: list[AccountingReference1] = field(
        default_factory=list,
        metadata={
            "name": "AccountingReference",
            "type": "Element",
        },
    )
    policy_reference: list[PolicyReference1] = field(
        default_factory=list,
        metadata={
            "name": "PolicyReference",
            "type": "Element",
        },
    )
    loyalty_program_enrollment: list[LoyaltyProgramEnrollment1] = field(
        default_factory=list,
        metadata={
            "name": "LoyaltyProgramEnrollment",
            "type": "Element",
        },
    )
    commission: list[Commission4] = field(
        default_factory=list,
        metadata={
            "name": "Commission",
            "type": "Element",
        },
    )
    contract: list[Contract1] = field(
        default_factory=list,
        metadata={
            "name": "Contract",
            "type": "Element",
        },
    )
    service_fee: list[ServiceFee1] = field(
        default_factory=list,
        metadata={
            "name": "ServiceFee",
            "type": "Element",
        },
    )
    form_of_payment: list[FormOfPayment2] = field(
        default_factory=list,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
        },
    )
    air_preference: list[AirPreference1] = field(
        default_factory=list,
        metadata={
            "name": "AirPreference",
            "type": "Element",
        },
    )
    hotel_preference: list[HotelPreference1] = field(
        default_factory=list,
        metadata={
            "name": "HotelPreference",
            "type": "Element",
        },
    )
    other_preference: list[OtherPreference1] = field(
        default_factory=list,
        metadata={
            "name": "OtherPreference",
            "type": "Element",
        },
    )
    remark: list[Remark2] = field(
        default_factory=list,
        metadata={
            "name": "Remark",
            "type": "Element",
        },
    )
    field_data: list[FieldData1] = field(
        default_factory=list,
        metadata={
            "name": "FieldData",
            "type": "Element",
        },
    )
    alternate_contact: list[AlternateContact1] = field(
        default_factory=list,
        metadata={
            "name": "AlternateContact",
            "type": "Element",
        },
    )
    alternate_contact_address: list[AlternateContactAddress1] = field(
        default_factory=list,
        metadata={
            "name": "AlternateContactAddress",
            "type": "Element",
        },
    )
    alternate_contact_phone: list[AlternateContactPhone1] = field(
        default_factory=list,
        metadata={
            "name": "AlternateContactPhone",
            "type": "Element",
        },
    )
    alternate_contact_electronic_address: list[
        AlternateContactElectronicAddress1
    ] = field(
        default_factory=list,
        metadata={
            "name": "AlternateContactElectronicAddress",
            "type": "Element",
        },
    )
    field_group_data: list[FieldGroupData1] = field(
        default_factory=list,
        metadata={
            "name": "FieldGroupData",
            "type": "Element",
        },
    )
    vehicle_preference: list[VehiclePreference1] = field(
        default_factory=list,
        metadata={
            "name": "VehiclePreference",
            "type": "Element",
        },
    )
    advisory: list[Advisory1] = field(
        default_factory=list,
        metadata={
            "name": "Advisory",
            "type": "Element",
        },
    )
    commission_reference: list[CommissionReference1] = field(
        default_factory=list,
        metadata={
            "name": "CommissionReference",
            "type": "Element",
        },
    )
    rail_preference: list[RailPreference1] = field(
        default_factory=list,
        metadata={
            "name": "RailPreference",
            "type": "Element",
        },
    )
    provider_info: list[ProviderInfo1] = field(
        default_factory=list,
        metadata={
            "name": "ProviderInfo",
            "type": "Element",
        },
    )
    proprietary_data: list[ProprietaryData1] = field(
        default_factory=list,
        metadata={
            "name": "ProprietaryData",
            "type": "Element",
        },
    )
