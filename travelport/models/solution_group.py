from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.account_code_1 import AccountCode1
from travelport.models.point_of_sale_1 import PointOfSale1
from travelport.models.type_diversity import TypeDiversity
from travelport.models.type_trip_type import TypeTripType

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class SolutionGroup:
    """
    Specifies the trip type and diversity of all or a subset of the result
    solutions.

    Parameters
    ----------
    permitted_account_codes
    preferred_account_codes
    prohibited_account_codes
    permitted_point_of_sales
    prohibited_point_of_sales
    count
        The number of solution to include in this group. If only one group
        specified, this can be left blank. If multiple groups specified, all
        counts must add up to the MaxResults of the request.
    trip_type
        Specifies the trip type for this group of results. Allows targeting
        a result set to a particular set of characterists.
    diversification
        Specifies the diversification of this group of results, if
        specified. Allows targeting a result set to ensure they contain more
        unique results.
    tag
        An arbitrary name for this group of solutions. Will be returned with
        the solution for idetification.
    primary
        Indicates that this is a primary SolutionGroup when using alternate
        pricing concepts
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    permitted_account_codes: None | SolutionGroup.PermittedAccountCodes = (
        field(
            default=None,
            metadata={
                "name": "PermittedAccountCodes",
                "type": "Element",
            },
        )
    )
    preferred_account_codes: None | SolutionGroup.PreferredAccountCodes = (
        field(
            default=None,
            metadata={
                "name": "PreferredAccountCodes",
                "type": "Element",
            },
        )
    )
    prohibited_account_codes: None | SolutionGroup.ProhibitedAccountCodes = (
        field(
            default=None,
            metadata={
                "name": "ProhibitedAccountCodes",
                "type": "Element",
            },
        )
    )
    permitted_point_of_sales: None | SolutionGroup.PermittedPointOfSales = (
        field(
            default=None,
            metadata={
                "name": "PermittedPointOfSales",
                "type": "Element",
            },
        )
    )
    prohibited_point_of_sales: None | SolutionGroup.ProhibitedPointOfSales = (
        field(
            default=None,
            metadata={
                "name": "ProhibitedPointOfSales",
                "type": "Element",
            },
        )
    )
    count: None | int = field(
        default=None,
        metadata={
            "name": "Count",
            "type": "Attribute",
        },
    )
    trip_type: None | TypeTripType = field(
        default=None,
        metadata={
            "name": "TripType",
            "type": "Attribute",
            "required": True,
        },
    )
    diversification: None | TypeDiversity = field(
        default=None,
        metadata={
            "name": "Diversification",
            "type": "Attribute",
        },
    )
    tag: None | str = field(
        default=None,
        metadata={
            "name": "Tag",
            "type": "Attribute",
            "max_length": 20,
        },
    )
    primary: bool = field(
        default=False,
        metadata={
            "name": "Primary",
            "type": "Attribute",
        },
    )

    @dataclass
    class PermittedAccountCodes:
        account_code: list[AccountCode1] = field(
            default_factory=list,
            metadata={
                "name": "AccountCode",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v52_0",
                "min_occurs": 1,
                "max_occurs": 999,
            },
        )

    @dataclass
    class PreferredAccountCodes:
        account_code: list[AccountCode1] = field(
            default_factory=list,
            metadata={
                "name": "AccountCode",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v52_0",
                "min_occurs": 1,
                "max_occurs": 999,
            },
        )

    @dataclass
    class ProhibitedAccountCodes:
        account_code: list[AccountCode1] = field(
            default_factory=list,
            metadata={
                "name": "AccountCode",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v52_0",
                "min_occurs": 1,
                "max_occurs": 999,
            },
        )

    @dataclass
    class PermittedPointOfSales:
        point_of_sale: list[PointOfSale1] = field(
            default_factory=list,
            metadata={
                "name": "PointOfSale",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v52_0",
                "min_occurs": 1,
                "max_occurs": 999,
            },
        )

    @dataclass
    class ProhibitedPointOfSales:
        point_of_sale: list[PointOfSale1] = field(
            default_factory=list,
            metadata={
                "name": "PointOfSale",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v52_0",
                "min_occurs": 1,
                "max_occurs": 999,
            },
        )
