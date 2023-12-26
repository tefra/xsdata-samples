from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.fee_info import FeeInfo
from travelport.models.grouped_option_info import GroupedOptionInfo
from travelport.models.optional_service_1 import OptionalService1
from travelport.models.service_rule_type_1 import ServiceRuleType1
from travelport.models.tax_info import TaxInfo

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class OptionalServices:
    """
    A wrapper for all the information regarding each of the Optional services.

    Parameters
    ----------
    optional_services_total
        The total fares, fees and taxes associated with the Optional
        Services
    optional_service
    grouped_option_info
        Details about an unselected or "other" option when optional services
        are grouped together.
    optional_service_rules
        Holds the rules for selecting the optional service in the itinerary
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    optional_services_total: None | OptionalServices.OptionalServicesTotal = (
        field(
            default=None,
            metadata={
                "name": "OptionalServicesTotal",
                "type": "Element",
            },
        )
    )
    optional_service: list[OptionalService1] = field(
        default_factory=list,
        metadata={
            "name": "OptionalService",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
    grouped_option_info: list[GroupedOptionInfo] = field(
        default_factory=list,
        metadata={
            "name": "GroupedOptionInfo",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    optional_service_rules: list[ServiceRuleType1] = field(
        default_factory=list,
        metadata={
            "name": "OptionalServiceRules",
            "type": "Element",
            "max_occurs": 999,
        },
    )

    @dataclass
    class OptionalServicesTotal:
        """
        Parameters
        ----------
        tax_info
        fee_info
        total_price
            The total price for this entity including base price and all
            taxes.
        base_price
            Represents the base price for this entity. This does not include
            any taxes or surcharges.
        approximate_total_price
            The Converted total price in Default Currency for this entity
            including base price and all taxes.
        approximate_base_price
            The Converted base price in Default Currency for this entity.
            This does not include any taxes or surcharges.
        equivalent_base_price
            Represents the base price in the related currency for this
            entity. This does not include any taxes or surcharges.
        taxes
            The aggregated amount of all the taxes that are associated with
            this entity. See the associated TaxInfo array for a breakdown of
            the individual taxes.
        fees
            The aggregated amount of all the fees that are associated with
            this entity. See the associated FeeInfo array for a breakdown of
            the individual fees.
        services
            The total cost for all optional services.
        approximate_taxes
            The Converted tax amount in Default Currency.
        approximate_fees
            The Converted fee amount in Default Currency.
        """

        tax_info: list[TaxInfo] = field(
            default_factory=list,
            metadata={
                "name": "TaxInfo",
                "type": "Element",
                "max_occurs": 999,
            },
        )
        fee_info: list[FeeInfo] = field(
            default_factory=list,
            metadata={
                "name": "FeeInfo",
                "type": "Element",
                "max_occurs": 999,
            },
        )
        total_price: None | str = field(
            default=None,
            metadata={
                "name": "TotalPrice",
                "type": "Attribute",
            },
        )
        base_price: None | str = field(
            default=None,
            metadata={
                "name": "BasePrice",
                "type": "Attribute",
            },
        )
        approximate_total_price: None | str = field(
            default=None,
            metadata={
                "name": "ApproximateTotalPrice",
                "type": "Attribute",
            },
        )
        approximate_base_price: None | str = field(
            default=None,
            metadata={
                "name": "ApproximateBasePrice",
                "type": "Attribute",
            },
        )
        equivalent_base_price: None | str = field(
            default=None,
            metadata={
                "name": "EquivalentBasePrice",
                "type": "Attribute",
            },
        )
        taxes: None | str = field(
            default=None,
            metadata={
                "name": "Taxes",
                "type": "Attribute",
            },
        )
        fees: None | str = field(
            default=None,
            metadata={
                "name": "Fees",
                "type": "Attribute",
            },
        )
        services: None | str = field(
            default=None,
            metadata={
                "name": "Services",
                "type": "Attribute",
            },
        )
        approximate_taxes: None | str = field(
            default=None,
            metadata={
                "name": "ApproximateTaxes",
                "type": "Attribute",
            },
        )
        approximate_fees: None | str = field(
            default=None,
            metadata={
                "name": "ApproximateFees",
                "type": "Attribute",
            },
        )
