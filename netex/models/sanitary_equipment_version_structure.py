from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field
from decimal import Decimal

from .accessibility_assessment import AccessibilityAssessment
from .gender_limitation_enumeration import GenderLimitationEnumeration
from .passenger_equipment_version_structure import (
    PassengerEquipmentVersionStructure,
)
from .payment_method_enumeration import PaymentMethodEnumeration
from .sanitary_facility_list import SanitaryFacilityList
from .staffing_enumeration import StaffingEnumeration
from .toilets_type_enumeration import ToiletsTypeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SanitaryEquipmentVersionStructure(PassengerEquipmentVersionStructure):
    class Meta:
        name = "SanitaryEquipment_VersionStructure"

    accessibility_assessment: None | AccessibilityAssessment = field(
        default=None,
        metadata={
            "name": "AccessibilityAssessment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    gender: None | GenderLimitationEnumeration = field(
        default=None,
        metadata={
            "name": "Gender",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    sanitary_facility_list: None | SanitaryFacilityList = field(
        default=None,
        metadata={
            "name": "SanitaryFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    number_of_toilets: None | int = field(
        default=None,
        metadata={
            "name": "NumberOfToilets",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    free_to_use: None | bool = field(
        default=None,
        metadata={
            "name": "FreeToUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    charge: None | Decimal = field(
        default=None,
        metadata={
            "name": "Charge",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    currency: None | str = field(
        default=None,
        metadata={
            "name": "Currency",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_length": 3,
            "max_length": 3,
            "pattern": r"[A-Z][A-Z][A-Z]",
        },
    )
    payment_methods: Sequence[PaymentMethodEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "PaymentMethods",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    change_available: None | bool = field(
        default=None,
        metadata={
            "name": "ChangeAvailable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    wheelchair_turning_circle: None | Decimal = field(
        default=None,
        metadata={
            "name": "WheelchairTurningCircle",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    support_bar_height: None | Decimal = field(
        default=None,
        metadata={
            "name": "SupportBarHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    call_button_available: None | bool = field(
        default=None,
        metadata={
            "name": "CallButtonAvailable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    sharps_disposal: None | bool = field(
        default=None,
        metadata={
            "name": "SharpsDisposal",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    staffing: None | StaffingEnumeration = field(
        default=None,
        metadata={
            "name": "Staffing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    locked_access: None | bool = field(
        default=None,
        metadata={
            "name": "LockedAccess",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    key_scheme: None | str = field(
        default=None,
        metadata={
            "name": "KeyScheme",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    hand_washing: None | bool = field(
        default=None,
        metadata={
            "name": "HandWashing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    drinking_water: None | bool = field(
        default=None,
        metadata={
            "name": "DrinkingWater",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    toilets_type: None | ToiletsTypeEnumeration = field(
        default=None,
        metadata={
            "name": "ToiletsType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
