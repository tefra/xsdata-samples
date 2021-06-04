from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from netex.models.accessibility_assessment import AccessibilityAssessment
from netex.models.gender_limitation_enumeration import GenderLimitationEnumeration
from netex.models.passenger_equipment_version_structure import PassengerEquipmentVersionStructure
from netex.models.payment_method_enumeration import PaymentMethodEnumeration
from netex.models.sanitary_facility_enumeration import SanitaryFacilityEnumeration
from netex.models.staffing_enumeration import StaffingEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SanitaryEquipmentVersionStructure(PassengerEquipmentVersionStructure):
    class Meta:
        name = "SanitaryEquipment_VersionStructure"

    accessibility_assessment: Optional[AccessibilityAssessment] = field(
        default=None,
        metadata={
            "name": "AccessibilityAssessment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    gender: Optional[GenderLimitationEnumeration] = field(
        default=None,
        metadata={
            "name": "Gender",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sanitary_facility_list: List[SanitaryFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "SanitaryFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    number_of_toilets: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfToilets",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    free_to_use: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FreeToUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    charge: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Charge",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    currency: Optional[str] = field(
        default=None,
        metadata={
            "name": "Currency",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_length": 3,
            "max_length": 3,
            "pattern": r"[A-Z][A-Z][A-Z]",
        }
    )
    payment_methods: List[PaymentMethodEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "PaymentMethods",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    change_available: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ChangeAvailable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    wheelchair_turning_circle: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "WheelchairTurningCircle",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    support_bar_height: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SupportBarHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    call_button_available: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CallButtonAvailable",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sharps_disposal: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SharpsDisposal",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    staffing: Optional[StaffingEnumeration] = field(
        default=None,
        metadata={
            "name": "Staffing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    locked_access: Optional[bool] = field(
        default=None,
        metadata={
            "name": "LockedAccess",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    key_scheme: Optional[str] = field(
        default=None,
        metadata={
            "name": "KeyScheme",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
