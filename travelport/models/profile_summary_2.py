from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.account_info_2 import AccountInfo2
from travelport.models.accounting_reference_2 import AccountingReference2
from travelport.models.agency_group_info_2 import AgencyGroupInfo2
from travelport.models.agency_info_6 import AgencyInfo6
from travelport.models.agent_info_2 import AgentInfo2
from travelport.models.alternate_contact_2 import AlternateContact2
from travelport.models.branch_group_info_2 import BranchGroupInfo2
from travelport.models.branch_info_2 import BranchInfo2
from travelport.models.contract_2 import Contract2
from travelport.models.field_data_2 import FieldData2
from travelport.models.field_group_data_2 import FieldGroupData2
from travelport.models.form_of_payment_6 import FormOfPayment6
from travelport.models.loyalty_program_enrollment_2 import (
    LoyaltyProgramEnrollment2,
)
from travelport.models.policy_reference_2 import PolicyReference2
from travelport.models.travel_document_2 import TravelDocument2
from travelport.models.traveler_group_info_2 import TravelerGroupInfo2
from travelport.models.traveler_info_2 import TravelerInfo2
from travelport.models.type_profile_entity_status_2 import (
    TypeProfileEntityStatus2,
)
from travelport.models.type_profile_type_7 import TypeProfileType7

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class ProfileSummary2:
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
    hierarchy_level_id
        System-defined, unique identifier of the level in the profile's
        hierarchy to which this profile is associated.
    version
        Version number of the profile.
    """

    class Meta:
        name = "ProfileSummary"
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
    immediate_parent_profile: list[
        ProfileSummary2.ImmediateParentProfile
    ] = field(
        default_factory=list,
        metadata={
            "name": "ImmediateParentProfile",
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
    alternate_contact: list[AlternateContact2] = field(
        default_factory=list,
        metadata={
            "name": "AlternateContact",
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
    form_of_payment: list[FormOfPayment6] = field(
        default_factory=list,
        metadata={
            "name": "FormOfPayment",
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
    profile_id: None | int = field(
        default=None,
        metadata={
            "name": "ProfileID",
            "type": "Attribute",
            "required": True,
        },
    )
    profile_type: None | TypeProfileType7 = field(
        default=None,
        metadata={
            "name": "ProfileType",
            "type": "Attribute",
            "required": True,
        },
    )
    status: None | TypeProfileEntityStatus2 = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
            "required": True,
        },
    )
    hierarchy_level_id: None | str = field(
        default=None,
        metadata={
            "name": "HierarchyLevelID",
            "type": "Attribute",
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
