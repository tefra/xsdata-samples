from dataclasses import dataclass, field
from typing import Optional

from .same_class_of_use_enumeration import SameClassOfUseEnumeration
from .same_journey_enumeration import SameJourneyEnumeration
from .same_operator_enumeration import SameOperatorEnumeration
from .same_period_enumeration import SamePeriodEnumeration
from .same_route_enumeration import SameRouteEnumeration
from .same_stop_enumeration import SameStopEnumeration
from .same_type_of_product_category_enumeration import (
    SameTypeOfProductCategoryEnumeration,
)
from .same_type_of_travel_document_enumeration import (
    SameTypeOfTravelDocumentEnumeration,
)
from .same_user_enumeration import SameUserEnumeration
from .same_zone_enumeration import SameZoneEnumeration
from .user_profile_refs_rel_structure import UserProfileRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class EntitlementConstraintStructure:
    period_constraint: Optional[SamePeriodEnumeration] = field(
        default=None,
        metadata={
            "name": "PeriodConstraint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    origin_constraint: Optional[SameStopEnumeration] = field(
        default=None,
        metadata={
            "name": "OriginConstraint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    destination_constraint: Optional[SameStopEnumeration] = field(
        default=None,
        metadata={
            "name": "DestinationConstraint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    tariff_zone_constraint: Optional[SameZoneEnumeration] = field(
        default=None,
        metadata={
            "name": "TariffZoneConstraint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    route_constraint: Optional[SameRouteEnumeration] = field(
        default=None,
        metadata={
            "name": "RouteConstraint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    direction_constraint: Optional[SameRouteEnumeration] = field(
        default=None,
        metadata={
            "name": "DirectionConstraint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    operator_constraint: Optional[SameOperatorEnumeration] = field(
        default=None,
        metadata={
            "name": "OperatorConstraint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_product_category_constraint: Optional[
        SameTypeOfProductCategoryEnumeration
    ] = field(
        default=None,
        metadata={
            "name": "TypeOfProductCategoryConstraint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    class_of_use_constraint: Optional[SameClassOfUseEnumeration] = field(
        default=None,
        metadata={
            "name": "ClassOfUseConstraint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_travel_document_constraint: Optional[
        SameTypeOfTravelDocumentEnumeration
    ] = field(
        default=None,
        metadata={
            "name": "TypeOfTravelDocumentConstraint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    journey_constraint: Optional[SameJourneyEnumeration] = field(
        default=None,
        metadata={
            "name": "JourneyConstraint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    user_constraint: Optional[SameUserEnumeration] = field(
        default=None,
        metadata={
            "name": "UserConstraint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    specific_to_profiles: Optional[UserProfileRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "specificToProfiles",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
