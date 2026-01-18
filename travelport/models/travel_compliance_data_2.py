from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_element_status_3 import TypeElementStatus3
from travelport.models.type_profile_type_4 import TypeProfileType4

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass(kw_only=True)
class TravelComplianceData2:
    """
    Travel Compliance and Preferred Supplier information of the traveler
    specific to a segment.

    Parameters
    ----------
    policy_compliance
    contract_compliance
    preferred_supplier
    key
        System generated key, returned back in the response. This can be
        used to modify or delete a saved TravelComplianceData.
    air_segment_ref
        Refers to Air Segment. Applicable only for Air. Ignored for others.
    passive_segment_ref
        Refers to Passive Segment. Applicable only for Passive. Ignored for
        others.
    rail_segment_ref
        Refers to Rail Segment. Applicable only for Rail. Ignored for
        others.
    reservation_locator_ref
        This is returned in the response. Any input will be ignored for this
        attribute. This represents the association of Travel Compliance Data
        with the uAPI reservation locator code, mainly relevant to Hotel and
        Vehicle.
    el_stat
        This attribute is used to show the action results of an element.
        Possible values are "A" (when elements have been added to the UR)
        and "M" (when existing elements have been modified). Response only.
    key_override
        If a duplicate key is found where we are adding elements in some
        cases like URAdd, then instead of erroring out set this attribute to
        true.
    """

    class Meta:
        name = "TravelComplianceData"
        namespace = "http://www.travelport.com/schema/common_v32_0"

    policy_compliance: list[TravelComplianceData2.PolicyCompliance] = field(
        default_factory=list,
        metadata={
            "name": "PolicyCompliance",
            "type": "Element",
            "max_occurs": 2,
        },
    )
    contract_compliance: list[TravelComplianceData2.ContractCompliance] = (
        field(
            default_factory=list,
            metadata={
                "name": "ContractCompliance",
                "type": "Element",
                "max_occurs": 2,
            },
        )
    )
    preferred_supplier: list[TravelComplianceData2.PreferredSupplier] = field(
        default_factory=list,
        metadata={
            "name": "PreferredSupplier",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
    air_segment_ref: None | str = field(
        default=None,
        metadata={
            "name": "AirSegmentRef",
            "type": "Attribute",
        },
    )
    passive_segment_ref: None | str = field(
        default=None,
        metadata={
            "name": "PassiveSegmentRef",
            "type": "Attribute",
        },
    )
    rail_segment_ref: None | str = field(
        default=None,
        metadata={
            "name": "RailSegmentRef",
            "type": "Attribute",
        },
    )
    reservation_locator_ref: None | str = field(
        default=None,
        metadata={
            "name": "ReservationLocatorRef",
            "type": "Attribute",
            "min_length": 5,
            "max_length": 8,
        },
    )
    el_stat: None | TypeElementStatus3 = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        },
    )
    key_override: None | bool = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class PolicyCompliance:
        """
        Parameters
        ----------
        in_policy
            Policy Compliance Indicator. For In-Policy set to 'true', For
            Out-Of-Policy set to 'false''.
        policy_token
            Optional text message to set the rule or token for which it's In
            Policy or Out Of Policy.
        """

        in_policy: bool = field(
            metadata={
                "name": "InPolicy",
                "type": "Attribute",
                "required": True,
            }
        )
        policy_token: None | str = field(
            default=None,
            metadata={
                "name": "PolicyToken",
                "type": "Attribute",
                "min_length": 1,
                "max_length": 128,
            },
        )

    @dataclass(kw_only=True)
    class ContractCompliance:
        """
        Parameters
        ----------
        in_contract
            Contract Compliance Indicator. For In-Contract set to 'true',
            For Out-Of-Contract set to 'false'.
        contract_token
            Optional text message to set the rule or token for which it's In
            Contract or Out Of Contract.
        """

        in_contract: bool = field(
            metadata={
                "name": "InContract",
                "type": "Attribute",
                "required": True,
            }
        )
        contract_token: None | str = field(
            default=None,
            metadata={
                "name": "ContractToken",
                "type": "Attribute",
                "min_length": 1,
                "max_length": 128,
            },
        )

    @dataclass(kw_only=True)
    class PreferredSupplier:
        """
        Parameters
        ----------
        preferred
            Preferred Supplier - 'true', 'false'.
        profile_type
            Indicate profile type. e.g. if Agency Preferred then pass
            Agency, if Traveler Preferred then pass Traveler.
        """

        preferred: bool = field(
            metadata={
                "name": "Preferred",
                "type": "Attribute",
                "required": True,
            }
        )
        profile_type: TypeProfileType4 = field(
            metadata={
                "name": "ProfileType",
                "type": "Attribute",
                "required": True,
            }
        )
