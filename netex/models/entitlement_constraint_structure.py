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
    period_constraint: SamePeriodEnumeration | None = field(
        default=None,
        metadata={
            "name": "PeriodConstraint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    origin_constraint: SameStopEnumeration | None = field(
        default=None,
        metadata={
            "name": "OriginConstraint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    destination_constraint: SameStopEnumeration | None = field(
        default=None,
        metadata={
            "name": "DestinationConstraint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    tariff_zone_constraint: SameZoneEnumeration | None = field(
        default=None,
        metadata={
            "name": "TariffZoneConstraint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    route_constraint: SameRouteEnumeration | None = field(
        default=None,
        metadata={
            "name": "RouteConstraint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    direction_constraint: SameRouteEnumeration | None = field(
        default=None,
        metadata={
            "name": "DirectionConstraint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    operator_constraint: SameOperatorEnumeration | None = field(
        default=None,
        metadata={
            "name": "OperatorConstraint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_product_category_constraint: SameTypeOfProductCategoryEnumeration | None = field(
        default=None,
        metadata={
            "name": "TypeOfProductCategoryConstraint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    class_of_use_constraint: SameClassOfUseEnumeration | None = field(
        default=None,
        metadata={
            "name": "ClassOfUseConstraint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_travel_document_constraint: SameTypeOfTravelDocumentEnumeration | None = field(
        default=None,
        metadata={
            "name": "TypeOfTravelDocumentConstraint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    journey_constraint: SameJourneyEnumeration | None = field(
        default=None,
        metadata={
            "name": "JourneyConstraint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    user_constraint: SameUserEnumeration | None = field(
        default=None,
        metadata={
            "name": "UserConstraint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    specific_to_profiles: UserProfileRefsRelStructure | None = field(
        default=None,
        metadata={
            "name": "specificToProfiles",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
