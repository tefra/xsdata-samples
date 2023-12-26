from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.account_info_2 import AccountInfo2
from travelport.models.accounting_reference_2 import AccountingReference2
from travelport.models.agency_group_info_2 import AgencyGroupInfo2
from travelport.models.agency_info_6 import AgencyInfo6
from travelport.models.agent_info_2 import AgentInfo2
from travelport.models.air_preference_2 import AirPreference2
from travelport.models.alternate_contact_2 import AlternateContact2
from travelport.models.branch_group_info_2 import BranchGroupInfo2
from travelport.models.branch_info_2 import BranchInfo2
from travelport.models.commission_8 import Commission8
from travelport.models.commission_reference_2 import CommissionReference2
from travelport.models.contract_2 import Contract2
from travelport.models.field_data_2 import FieldData2
from travelport.models.field_group_data_2 import FieldGroupData2
from travelport.models.form_of_payment_6 import FormOfPayment6
from travelport.models.hotel_preference_2 import HotelPreference2
from travelport.models.loyalty_program_enrollment_2 import (
    LoyaltyProgramEnrollment2,
)
from travelport.models.other_preference_2 import OtherPreference2
from travelport.models.policy_reference_2 import PolicyReference2
from travelport.models.rail_preference_2 import RailPreference2
from travelport.models.remark_6 import Remark6
from travelport.models.service_fee_2 import ServiceFee2
from travelport.models.travel_document_2 import TravelDocument2
from travelport.models.traveler_group_info_2 import TravelerGroupInfo2
from travelport.models.traveler_info_2 import TravelerInfo2
from travelport.models.vehicle_preference_2 import VehiclePreference2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class ProfileData2:
    """
    Agency-defined data.

    Parameters
    ----------
    agency_group_info
    agency_info
    branch_group_info
    branch_info
    account_info
    agent_info
    traveler_group_info
    traveler_info
    travel_document
    accounting_reference
    policy_reference
    commission_reference
    commission
    form_of_payment
    air_preference
    hotel_preference
    rail_preference
    other_preference
    contract
    service_fee
    alternate_contact
    loyalty_program_enrollment
    remark
    vehicle_preference
    field_data
        Data values associated to this entity. Each value is linked to a
        field that defines the structure and restrictions of the data.
    field_group_data
        Field groups and child fields and groups and their associated data
        values for this entity. Each field group is linked to an instance,
        which defines the attributes of the group specific to the asociated
        template or its parent field group.
    """

    class Meta:
        name = "ProfileData"
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
    account_info: None | AccountInfo2 = field(
        default=None,
        metadata={
            "name": "AccountInfo",
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
    commission_reference: list[CommissionReference2] = field(
        default_factory=list,
        metadata={
            "name": "CommissionReference",
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
    rail_preference: list[RailPreference2] = field(
        default_factory=list,
        metadata={
            "name": "RailPreference",
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
    loyalty_program_enrollment: list[LoyaltyProgramEnrollment2] = field(
        default_factory=list,
        metadata={
            "name": "LoyaltyProgramEnrollment",
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
    vehicle_preference: list[VehiclePreference2] = field(
        default_factory=list,
        metadata={
            "name": "VehiclePreference",
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
