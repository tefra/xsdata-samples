from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.account_info_1 import AccountInfo1
from travelport.models.accounting_reference_1 import AccountingReference1
from travelport.models.agency_group_info_1 import AgencyGroupInfo1
from travelport.models.agency_info_2 import AgencyInfo2
from travelport.models.agent_info_1 import AgentInfo1
from travelport.models.air_preference_1 import AirPreference1
from travelport.models.alternate_contact_1 import AlternateContact1
from travelport.models.branch_group_info_1 import BranchGroupInfo1
from travelport.models.branch_info_1 import BranchInfo1
from travelport.models.commission_4 import Commission4
from travelport.models.commission_reference_1 import CommissionReference1
from travelport.models.contract_1 import Contract1
from travelport.models.field_data_1 import FieldData1
from travelport.models.field_group_data_1 import FieldGroupData1
from travelport.models.form_of_payment_2 import FormOfPayment2
from travelport.models.hotel_preference_1 import HotelPreference1
from travelport.models.loyalty_program_enrollment_1 import (
    LoyaltyProgramEnrollment1,
)
from travelport.models.other_preference_1 import OtherPreference1
from travelport.models.policy_reference_1 import PolicyReference1
from travelport.models.rail_preference_1 import RailPreference1
from travelport.models.remark_2 import Remark2
from travelport.models.service_fee_1 import ServiceFee1
from travelport.models.travel_document_1 import TravelDocument1
from travelport.models.traveler_group_info_1 import TravelerGroupInfo1
from travelport.models.traveler_info_1 import TravelerInfo1
from travelport.models.vehicle_preference_1 import VehiclePreference1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class ProfileData1:
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
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    agency_group_info: None | AgencyGroupInfo1 = field(
        default=None,
        metadata={
            "name": "AgencyGroupInfo",
            "type": "Element",
        },
    )
    agency_info: None | AgencyInfo2 = field(
        default=None,
        metadata={
            "name": "AgencyInfo",
            "type": "Element",
        },
    )
    branch_group_info: None | BranchGroupInfo1 = field(
        default=None,
        metadata={
            "name": "BranchGroupInfo",
            "type": "Element",
        },
    )
    branch_info: None | BranchInfo1 = field(
        default=None,
        metadata={
            "name": "BranchInfo",
            "type": "Element",
        },
    )
    account_info: None | AccountInfo1 = field(
        default=None,
        metadata={
            "name": "AccountInfo",
            "type": "Element",
        },
    )
    agent_info: None | AgentInfo1 = field(
        default=None,
        metadata={
            "name": "AgentInfo",
            "type": "Element",
        },
    )
    traveler_group_info: None | TravelerGroupInfo1 = field(
        default=None,
        metadata={
            "name": "TravelerGroupInfo",
            "type": "Element",
        },
    )
    traveler_info: None | TravelerInfo1 = field(
        default=None,
        metadata={
            "name": "TravelerInfo",
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
    commission_reference: list[CommissionReference1] = field(
        default_factory=list,
        metadata={
            "name": "CommissionReference",
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
    rail_preference: list[RailPreference1] = field(
        default_factory=list,
        metadata={
            "name": "RailPreference",
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
    alternate_contact: list[AlternateContact1] = field(
        default_factory=list,
        metadata={
            "name": "AlternateContact",
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
    remark: list[Remark2] = field(
        default_factory=list,
        metadata={
            "name": "Remark",
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
    field_data: list[FieldData1] = field(
        default_factory=list,
        metadata={
            "name": "FieldData",
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
