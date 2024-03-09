from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.traveler_identity_information_1 import (
    TravelerIdentityInformation1,
)
from travelport.models.type_account_info_history_1 import (
    TypeAccountInfoHistory1,
)
from travelport.models.type_accounting_reference_history_1 import (
    TypeAccountingReferenceHistory1,
)
from travelport.models.type_address_history_1 import TypeAddressHistory1
from travelport.models.type_advisory_history_1 import TypeAdvisoryHistory1
from travelport.models.type_agency_group_info_history_1 import (
    TypeAgencyGroupInfoHistory1,
)
from travelport.models.type_agency_info_history_1 import TypeAgencyInfoHistory1
from travelport.models.type_agent_info_history_1 import TypeAgentInfoHistory1
from travelport.models.type_air_preference_history_1 import (
    TypeAirPreferenceHistory1,
)
from travelport.models.type_alternate_contact_history_1 import (
    TypeAlternateContactHistory1,
)
from travelport.models.type_branch_group_info_history_1 import (
    TypeBranchGroupInfoHistory1,
)
from travelport.models.type_branch_info_history_1 import TypeBranchInfoHistory1
from travelport.models.type_commission_history_1 import TypeCommissionHistory1
from travelport.models.type_commission_reference_history_1 import (
    TypeCommissionReferenceHistory1,
)
from travelport.models.type_contract_history_1 import TypeContractHistory1
from travelport.models.type_electronic_address_history_1 import (
    TypeElectronicAddressHistory1,
)
from travelport.models.type_external_identifier_history_1 import (
    TypeExternalIdentifierHistory1,
)
from travelport.models.type_field_data_history_1 import TypeFieldDataHistory1
from travelport.models.type_field_group_data_history_1 import (
    TypeFieldGroupDataHistory1,
)
from travelport.models.type_form_of_payment_history_1 import (
    TypeFormOfPaymentHistory1,
)
from travelport.models.type_hotel_preference_history_1 import (
    TypeHotelPreferenceHistory1,
)
from travelport.models.type_loyalty_program_enrollment_history_1 import (
    TypeLoyaltyProgramEnrollmentHistory1,
)
from travelport.models.type_other_preference_history_1 import (
    TypeOtherPreferenceHistory1,
)
from travelport.models.type_phone_history_1 import TypePhoneHistory1
from travelport.models.type_policy_reference_history_1 import (
    TypePolicyReferenceHistory1,
)
from travelport.models.type_profile_link_history_1 import (
    TypeProfileLinkHistory1,
)
from travelport.models.type_profile_parent_history_1 import (
    TypeProfileParentHistory1,
)
from travelport.models.type_profile_status_history_1 import (
    TypeProfileStatusHistory1,
)
from travelport.models.type_proprietary_data_history_1 import (
    TypeProprietaryDataHistory1,
)
from travelport.models.type_provider_info_history_1 import (
    TypeProviderInfoHistory1,
)
from travelport.models.type_rail_preference_history_1 import (
    TypeRailPreferenceHistory1,
)
from travelport.models.type_remark_history_1 import TypeRemarkHistory1
from travelport.models.type_service_fee_history_1 import TypeServiceFeeHistory1
from travelport.models.type_travel_document_history_1 import (
    TypeTravelDocumentHistory1,
)
from travelport.models.type_traveler_group_info_history_1 import (
    TypeTravelerGroupInfoHistory1,
)
from travelport.models.type_traveler_info_history_1 import (
    TypeTravelerInfoHistory1,
)
from travelport.models.type_vehicle_preference_history_1 import (
    TypeVehiclePreferenceHistory1,
)

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class TypeHistorySubElement1:
    """
    A choice of all fields that have changed in the course of a add, modified, or
    deleted.
    """

    class Meta:
        name = "typeHistorySubElement"

    account_info: None | TypeAccountInfoHistory1 = field(
        default=None,
        metadata={
            "name": "AccountInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    traveler_info: None | TypeTravelerInfoHistory1 = field(
        default=None,
        metadata={
            "name": "TravelerInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    travel_document: None | TypeTravelDocumentHistory1 = field(
        default=None,
        metadata={
            "name": "TravelDocument",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    accounting_reference: None | TypeAccountingReferenceHistory1 = field(
        default=None,
        metadata={
            "name": "AccountingReference",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    policy_reference: None | TypePolicyReferenceHistory1 = field(
        default=None,
        metadata={
            "name": "PolicyReference",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    commission_reference: None | TypeCommissionReferenceHistory1 = field(
        default=None,
        metadata={
            "name": "CommissionReference",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    loyalty_program_enrollment: None | TypeLoyaltyProgramEnrollmentHistory1 = (
        field(
            default=None,
            metadata={
                "name": "LoyaltyProgramEnrollment",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
            },
        )
    )
    contract: None | TypeContractHistory1 = field(
        default=None,
        metadata={
            "name": "Contract",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    commission: None | TypeCommissionHistory1 = field(
        default=None,
        metadata={
            "name": "Commission",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    service_fee: None | TypeServiceFeeHistory1 = field(
        default=None,
        metadata={
            "name": "ServiceFee",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    alternate_contact: None | TypeAlternateContactHistory1 = field(
        default=None,
        metadata={
            "name": "AlternateContact",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    alternate_contact_address: (
        None | TypeHistorySubElement1.AlternateContactAddress
    ) = field(
        default=None,
        metadata={
            "name": "AlternateContactAddress",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    alternate_contact_phone: (
        None | TypeHistorySubElement1.AlternateContactPhone
    ) = field(
        default=None,
        metadata={
            "name": "AlternateContactPhone",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    alternate_contact_electronic_address: (
        None | TypeHistorySubElement1.AlternateContactElectronicAddress
    ) = field(
        default=None,
        metadata={
            "name": "AlternateContactElectronicAddress",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    form_of_payment: None | TypeFormOfPaymentHistory1 = field(
        default=None,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    remark: None | TypeRemarkHistory1 = field(
        default=None,
        metadata={
            "name": "Remark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    address: None | TypeAddressHistory1 = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    phone: None | TypePhoneHistory1 = field(
        default=None,
        metadata={
            "name": "Phone",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    electronic_address: None | TypeElectronicAddressHistory1 = field(
        default=None,
        metadata={
            "name": "ElectronicAddress",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    traveler_identity_information: None | TravelerIdentityInformation1 = field(
        default=None,
        metadata={
            "name": "TravelerIdentityInformation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    external_identifier: None | TypeExternalIdentifierHistory1 = field(
        default=None,
        metadata={
            "name": "ExternalIdentifier",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    air_preference: None | TypeAirPreferenceHistory1 = field(
        default=None,
        metadata={
            "name": "AirPreference",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    vehicle_preference: None | TypeVehiclePreferenceHistory1 = field(
        default=None,
        metadata={
            "name": "VehiclePreference",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    hotel_preference: None | TypeHotelPreferenceHistory1 = field(
        default=None,
        metadata={
            "name": "HotelPreference",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    rail_preference: None | TypeRailPreferenceHistory1 = field(
        default=None,
        metadata={
            "name": "RailPreference",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    profile_parent_history: None | TypeProfileParentHistory1 = field(
        default=None,
        metadata={
            "name": "ProfileParentHistory",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    field_data: None | TypeFieldDataHistory1 = field(
        default=None,
        metadata={
            "name": "FieldData",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    field_group_data: None | TypeFieldGroupDataHistory1 = field(
        default=None,
        metadata={
            "name": "FieldGroupData",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    advisory: None | TypeAdvisoryHistory1 = field(
        default=None,
        metadata={
            "name": "Advisory",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    agency_group_info: None | TypeAgencyGroupInfoHistory1 = field(
        default=None,
        metadata={
            "name": "AgencyGroupInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    agency_info: None | TypeAgencyInfoHistory1 = field(
        default=None,
        metadata={
            "name": "AgencyInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    branch_group_info: None | TypeBranchGroupInfoHistory1 = field(
        default=None,
        metadata={
            "name": "BranchGroupInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    branch_info: None | TypeBranchInfoHistory1 = field(
        default=None,
        metadata={
            "name": "BranchInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    agent_info: None | TypeAgentInfoHistory1 = field(
        default=None,
        metadata={
            "name": "AgentInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    traveler_group_info: None | TypeTravelerGroupInfoHistory1 = field(
        default=None,
        metadata={
            "name": "TravelerGroupInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    profile_status: None | TypeProfileStatusHistory1 = field(
        default=None,
        metadata={
            "name": "ProfileStatus",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    profile_link: None | TypeProfileLinkHistory1 = field(
        default=None,
        metadata={
            "name": "ProfileLink",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    provider_info: None | TypeProviderInfoHistory1 = field(
        default=None,
        metadata={
            "name": "ProviderInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    other_preference: None | TypeOtherPreferenceHistory1 = field(
        default=None,
        metadata={
            "name": "OtherPreference",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    proprietary_data: None | TypeProprietaryDataHistory1 = field(
        default=None,
        metadata={
            "name": "ProprietaryData",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )

    @dataclass
    class AlternateContactAddress(TypeAddressHistory1):
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
    class AlternateContactPhone(TypePhoneHistory1):
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
    class AlternateContactElectronicAddress(TypeElectronicAddressHistory1):
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
