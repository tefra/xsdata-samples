from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.traveler_identity_information_2 import (
    TravelerIdentityInformation2,
)
from travelport.models.type_account_info_history_2 import (
    TypeAccountInfoHistory2,
)
from travelport.models.type_accounting_reference_history_2 import (
    TypeAccountingReferenceHistory2,
)
from travelport.models.type_address_history_2 import TypeAddressHistory2
from travelport.models.type_advisory_history_2 import TypeAdvisoryHistory2
from travelport.models.type_agency_group_info_history_2 import (
    TypeAgencyGroupInfoHistory2,
)
from travelport.models.type_agency_info_history_2 import TypeAgencyInfoHistory2
from travelport.models.type_agent_info_history_2 import TypeAgentInfoHistory2
from travelport.models.type_air_preference_history_2 import (
    TypeAirPreferenceHistory2,
)
from travelport.models.type_alternate_contact_history_2 import (
    TypeAlternateContactHistory2,
)
from travelport.models.type_branch_group_info_history_2 import (
    TypeBranchGroupInfoHistory2,
)
from travelport.models.type_branch_info_history_2 import TypeBranchInfoHistory2
from travelport.models.type_commission_history_2 import TypeCommissionHistory2
from travelport.models.type_commission_reference_history_2 import (
    TypeCommissionReferenceHistory2,
)
from travelport.models.type_contract_history_2 import TypeContractHistory2
from travelport.models.type_electronic_address_history_2 import (
    TypeElectronicAddressHistory2,
)
from travelport.models.type_external_identifier_history_2 import (
    TypeExternalIdentifierHistory2,
)
from travelport.models.type_field_data_history_2 import TypeFieldDataHistory2
from travelport.models.type_field_group_data_history_2 import (
    TypeFieldGroupDataHistory2,
)
from travelport.models.type_form_of_payment_history_2 import (
    TypeFormOfPaymentHistory2,
)
from travelport.models.type_hotel_preference_history_2 import (
    TypeHotelPreferenceHistory2,
)
from travelport.models.type_loyalty_program_enrollment_history_2 import (
    TypeLoyaltyProgramEnrollmentHistory2,
)
from travelport.models.type_other_preference_history_2 import (
    TypeOtherPreferenceHistory2,
)
from travelport.models.type_phone_history_2 import TypePhoneHistory2
from travelport.models.type_policy_reference_history_2 import (
    TypePolicyReferenceHistory2,
)
from travelport.models.type_profile_link_history_2 import (
    TypeProfileLinkHistory2,
)
from travelport.models.type_profile_parent_history_2 import (
    TypeProfileParentHistory2,
)
from travelport.models.type_profile_status_history_2 import (
    TypeProfileStatusHistory2,
)
from travelport.models.type_proprietary_data_history_2 import (
    TypeProprietaryDataHistory2,
)
from travelport.models.type_provider_info_history_2 import (
    TypeProviderInfoHistory2,
)
from travelport.models.type_rail_preference_history_2 import (
    TypeRailPreferenceHistory2,
)
from travelport.models.type_remark_history_2 import TypeRemarkHistory2
from travelport.models.type_service_fee_history_2 import TypeServiceFeeHistory2
from travelport.models.type_travel_document_history_2 import (
    TypeTravelDocumentHistory2,
)
from travelport.models.type_traveler_group_info_history_2 import (
    TypeTravelerGroupInfoHistory2,
)
from travelport.models.type_traveler_info_history_2 import (
    TypeTravelerInfoHistory2,
)
from travelport.models.type_vehicle_preference_history_2 import (
    TypeVehiclePreferenceHistory2,
)

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class TypeHistorySubElement2:
    """
    A choice of all fields that have changed in the course of a add, modified, or
    deleted.
    """

    class Meta:
        name = "typeHistorySubElement"

    account_info: None | TypeAccountInfoHistory2 = field(
        default=None,
        metadata={
            "name": "AccountInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    traveler_info: None | TypeTravelerInfoHistory2 = field(
        default=None,
        metadata={
            "name": "TravelerInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    travel_document: None | TypeTravelDocumentHistory2 = field(
        default=None,
        metadata={
            "name": "TravelDocument",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    accounting_reference: None | TypeAccountingReferenceHistory2 = field(
        default=None,
        metadata={
            "name": "AccountingReference",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    policy_reference: None | TypePolicyReferenceHistory2 = field(
        default=None,
        metadata={
            "name": "PolicyReference",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    commission_reference: None | TypeCommissionReferenceHistory2 = field(
        default=None,
        metadata={
            "name": "CommissionReference",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    loyalty_program_enrollment: None | TypeLoyaltyProgramEnrollmentHistory2 = (
        field(
            default=None,
            metadata={
                "name": "LoyaltyProgramEnrollment",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
            },
        )
    )
    contract: None | TypeContractHistory2 = field(
        default=None,
        metadata={
            "name": "Contract",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    commission: None | TypeCommissionHistory2 = field(
        default=None,
        metadata={
            "name": "Commission",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    service_fee: None | TypeServiceFeeHistory2 = field(
        default=None,
        metadata={
            "name": "ServiceFee",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    alternate_contact: None | TypeAlternateContactHistory2 = field(
        default=None,
        metadata={
            "name": "AlternateContact",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    alternate_contact_address: None | TypeHistorySubElement2.AlternateContactAddress = field(
        default=None,
        metadata={
            "name": "AlternateContactAddress",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    alternate_contact_phone: None | TypeHistorySubElement2.AlternateContactPhone = field(
        default=None,
        metadata={
            "name": "AlternateContactPhone",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    alternate_contact_electronic_address: None | TypeHistorySubElement2.AlternateContactElectronicAddress = field(
        default=None,
        metadata={
            "name": "AlternateContactElectronicAddress",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    form_of_payment: None | TypeFormOfPaymentHistory2 = field(
        default=None,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    remark: None | TypeRemarkHistory2 = field(
        default=None,
        metadata={
            "name": "Remark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    address: None | TypeAddressHistory2 = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    phone: None | TypePhoneHistory2 = field(
        default=None,
        metadata={
            "name": "Phone",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    electronic_address: None | TypeElectronicAddressHistory2 = field(
        default=None,
        metadata={
            "name": "ElectronicAddress",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    traveler_identity_information: None | TravelerIdentityInformation2 = field(
        default=None,
        metadata={
            "name": "TravelerIdentityInformation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    external_identifier: None | TypeExternalIdentifierHistory2 = field(
        default=None,
        metadata={
            "name": "ExternalIdentifier",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    air_preference: None | TypeAirPreferenceHistory2 = field(
        default=None,
        metadata={
            "name": "AirPreference",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    vehicle_preference: None | TypeVehiclePreferenceHistory2 = field(
        default=None,
        metadata={
            "name": "VehiclePreference",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    hotel_preference: None | TypeHotelPreferenceHistory2 = field(
        default=None,
        metadata={
            "name": "HotelPreference",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    rail_preference: None | TypeRailPreferenceHistory2 = field(
        default=None,
        metadata={
            "name": "RailPreference",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    profile_parent_history: None | TypeProfileParentHistory2 = field(
        default=None,
        metadata={
            "name": "ProfileParentHistory",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    field_data: None | TypeFieldDataHistory2 = field(
        default=None,
        metadata={
            "name": "FieldData",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    field_group_data: None | TypeFieldGroupDataHistory2 = field(
        default=None,
        metadata={
            "name": "FieldGroupData",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    advisory: None | TypeAdvisoryHistory2 = field(
        default=None,
        metadata={
            "name": "Advisory",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    agency_group_info: None | TypeAgencyGroupInfoHistory2 = field(
        default=None,
        metadata={
            "name": "AgencyGroupInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    agency_info: None | TypeAgencyInfoHistory2 = field(
        default=None,
        metadata={
            "name": "AgencyInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    branch_group_info: None | TypeBranchGroupInfoHistory2 = field(
        default=None,
        metadata={
            "name": "BranchGroupInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    branch_info: None | TypeBranchInfoHistory2 = field(
        default=None,
        metadata={
            "name": "BranchInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    agent_info: None | TypeAgentInfoHistory2 = field(
        default=None,
        metadata={
            "name": "AgentInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    traveler_group_info: None | TypeTravelerGroupInfoHistory2 = field(
        default=None,
        metadata={
            "name": "TravelerGroupInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    profile_status: None | TypeProfileStatusHistory2 = field(
        default=None,
        metadata={
            "name": "ProfileStatus",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    profile_link: None | TypeProfileLinkHistory2 = field(
        default=None,
        metadata={
            "name": "ProfileLink",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    provider_info: None | TypeProviderInfoHistory2 = field(
        default=None,
        metadata={
            "name": "ProviderInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    other_preference: None | TypeOtherPreferenceHistory2 = field(
        default=None,
        metadata={
            "name": "OtherPreference",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    proprietary_data: None | TypeProprietaryDataHistory2 = field(
        default=None,
        metadata={
            "name": "ProprietaryData",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )

    @dataclass
    class AlternateContactAddress(TypeAddressHistory2):
        """
        Parameters
        ----------
        alternate_contact_ref
            A reference to the Alternate Contact being that is the parent of
            this element.
        """

        alternate_contact_ref: None | str = field(
            default=None,
            metadata={
                "name": "AlternateContactRef",
                "type": "Attribute",
            },
        )

    @dataclass
    class AlternateContactPhone(TypePhoneHistory2):
        """
        Parameters
        ----------
        alternate_contact_ref
            A reference to the Alternate Contact being that is the parent of
            this element.
        """

        alternate_contact_ref: None | str = field(
            default=None,
            metadata={
                "name": "AlternateContactRef",
                "type": "Attribute",
            },
        )

    @dataclass
    class AlternateContactElectronicAddress(TypeElectronicAddressHistory2):
        """
        Parameters
        ----------
        alternate_contact_ref
            A reference to the Alternate Contact being that is the parent of
            this element.
        """

        alternate_contact_ref: None | str = field(
            default=None,
            metadata={
                "name": "AlternateContactRef",
                "type": "Attribute",
            },
        )
