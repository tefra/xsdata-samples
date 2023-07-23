from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_element_status_5 import TypeElementStatus5

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


@dataclass
class Ssr4:
    """
    Special serivces like wheel chair, or pet carrier.

    Parameters
    ----------
    key
    segment_ref
        Reference to the air segment. May be required for some Types.
    passive_segment_ref
        Reference to the passive segment.
    provider_reservation_info_ref
        Provider reservation reference key.
    type_value
        Programmatic SSRs use codes recognized by the provider/supplier
        (example, VGML=vegetarian meal code). Manual SSRs do not have an
        associated programmatic code.
    status
    free_text
        Certain SSR types will require a free text message. For example MAAS
        (Meet and assist).
    carrier
    carrier_specific_text
        Carrier specific information which are not captured in the FreeText
        field(not present in IATA's standard SSR DOCO format). An example is
        VISA Expiration Date.
    description
    provider_defined_type
        Original Type as sent by the provider
    ssrrule_ref
        UniqueID to associate a rule to the SSR
    url
    el_stat
        This attribute is used to show the action results of an element.
        Possible values are "A" (when elements have been added to the UR)
        and "M" (when existing elements have been modified). Response only.
    key_override
        If a duplicate key is found where we are adding elements in some
        cases like URAdd, then instead of erroring out set this attribute to
        true.
    profile_id
        Key assigned for Secure Flight Document value from the specified
        profile
    profile_secure_flight_doc_key
        Unique ID of Booking Traveler's Profile that contains the Secure
        flight Detail
    """
    class Meta:
        name = "SSR"
        namespace = "http://www.travelport.com/schema/common_v37_0"

    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    segment_ref: None | str = field(
        default=None,
        metadata={
            "name": "SegmentRef",
            "type": "Attribute",
        }
    )
    passive_segment_ref: None | str = field(
        default=None,
        metadata={
            "name": "PassiveSegmentRef",
            "type": "Attribute",
        }
    )
    provider_reservation_info_ref: None | str = field(
        default=None,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Attribute",
        }
    )
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
            "min_length": 4,
            "max_length": 4,
        }
    )
    status: None | str = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
        }
    )
    free_text: None | str = field(
        default=None,
        metadata={
            "name": "FreeText",
            "type": "Attribute",
        }
    )
    carrier: None | str = field(
        default=None,
        metadata={
            "name": "Carrier",
            "type": "Attribute",
            "length": 2,
        }
    )
    carrier_specific_text: None | str = field(
        default=None,
        metadata={
            "name": "CarrierSpecificText",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 64,
        }
    )
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
        }
    )
    provider_defined_type: None | str = field(
        default=None,
        metadata={
            "name": "ProviderDefinedType",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 16,
        }
    )
    ssrrule_ref: None | str = field(
        default=None,
        metadata={
            "name": "SSRRuleRef",
            "type": "Attribute",
        }
    )
    url: None | str = field(
        default=None,
        metadata={
            "name": "URL",
            "type": "Attribute",
        }
    )
    el_stat: None | TypeElementStatus5 = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: None | bool = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )
    profile_id: None | str = field(
        default=None,
        metadata={
            "name": "ProfileID",
            "type": "Attribute",
        }
    )
    profile_secure_flight_doc_key: None | str = field(
        default=None,
        metadata={
            "name": "ProfileSecureFlightDocKey",
            "type": "Attribute",
        }
    )
