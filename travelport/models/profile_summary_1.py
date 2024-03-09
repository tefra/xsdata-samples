from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.account_info_1 import AccountInfo1
from travelport.models.accounting_reference_1 import AccountingReference1
from travelport.models.agency_group_info_1 import AgencyGroupInfo1
from travelport.models.agency_info_2 import AgencyInfo2
from travelport.models.agent_info_1 import AgentInfo1
from travelport.models.alternate_contact_1 import AlternateContact1
from travelport.models.branch_group_info_1 import BranchGroupInfo1
from travelport.models.branch_info_1 import BranchInfo1
from travelport.models.contract_1 import Contract1
from travelport.models.field_data_1 import FieldData1
from travelport.models.field_group_data_1 import FieldGroupData1
from travelport.models.form_of_payment_2 import FormOfPayment2
from travelport.models.loyalty_program_enrollment_1 import (
    LoyaltyProgramEnrollment1,
)
from travelport.models.policy_reference_1 import PolicyReference1
from travelport.models.travel_document_1 import TravelDocument1
from travelport.models.traveler_group_info_1 import TravelerGroupInfo1
from travelport.models.traveler_info_1 import TravelerInfo1
from travelport.models.type_profile_entity_status_1 import (
    TypeProfileEntityStatus1,
)
from travelport.models.type_profile_type_3 import TypeProfileType3

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class ProfileSummary1:
    """Profile summary information.

    The data returned is what was matched from the search request plus a
    subset of required identification info.

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
    immediate_parent_profile
    contract
        The contract number matched in the search.
    alternate_contact
        The contact matched in the search.
    travel_document
        The travel document number matched in the search.
    accounting_reference
        The accounting reference matched in the search.
    policy_reference
        The policy reference matched in the search.
    loyalty_program_enrollment
        The loyalty program matched in the search.
    form_of_payment
    field_data
        The custom fields matched in the search.
    field_group_data
        The custom fields groups matched in the search.
    profile_id
        The system-assigned, unique ID of the profile.
    profile_type
        The type of profile this profile is for (e.g., branch, account,
        traveler). The profile type identifies which default
        attributes/elements (minimum data set) the system will insert.
    status
        Profile status (Active, Inactive).
    version
        Version number of the profile.
    """

    class Meta:
        name = "ProfileSummary"
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
    agent_info: None | AgentInfo1 = field(
        default=None,
        metadata={
            "name": "AgentInfo",
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
    immediate_parent_profile: list[ProfileSummary1.ImmediateParentProfile] = (
        field(
            default_factory=list,
            metadata={
                "name": "ImmediateParentProfile",
                "type": "Element",
            },
        )
    )
    contract: list[Contract1] = field(
        default_factory=list,
        metadata={
            "name": "Contract",
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
    form_of_payment: list[FormOfPayment2] = field(
        default_factory=list,
        metadata={
            "name": "FormOfPayment",
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
    profile_id: None | int = field(
        default=None,
        metadata={
            "name": "ProfileID",
            "type": "Attribute",
            "required": True,
        },
    )
    profile_type: None | TypeProfileType3 = field(
        default=None,
        metadata={
            "name": "ProfileType",
            "type": "Attribute",
            "required": True,
        },
    )
    status: None | TypeProfileEntityStatus1 = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
            "required": True,
        },
    )
    version: None | int = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
        },
    )

    @dataclass
    class ImmediateParentProfile:
        """
        Parameters
        ----------
        immediate_parent_ref
            System-defined, unique identifier for ImmediateParent Reference
        control_branch
            If immediate parent is a control branch, it will be true other
            wise doesn't show this attribute.
        """

        immediate_parent_ref: None | str = field(
            default=None,
            metadata={
                "name": "ImmediateParentRef",
                "type": "Attribute",
            },
        )
        control_branch: None | bool = field(
            default=None,
            metadata={
                "name": "ControlBranch",
                "type": "Attribute",
            },
        )
