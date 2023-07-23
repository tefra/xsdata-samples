from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_policy_codes_list_1 import TypePolicyCodesList1

__NAMESPACE__ = "http://www.travelport.com/schema/hotel_v52_0"


@dataclass
class RateInfo:
    """
    Parameters
    ----------
    policy_codes_list
        A list of codes that indicate why an item was determined to be ‘out
        of policy’.
    minimum_amount
        The low end of the nightly price range
    approximate_minimum_amount
        The low end of the nightly price range in another currency
    min_amount_rate_changed
        Indicates the low end price range changes over the requested stay
    maximum_amount
        The high end of the nightly price range
    approximate_maximum_amount
        The high end of the nightly price range in another currency
    max_amount_rate_changed
        Indicates the high end price range changes over the requested stay
    minimum_stay_amount
        The low end of the price range for the entire stay
    approximate_minimum_stay_amount
        The low end of the price range for the entire stay in another
        currency
    commission
        Commission information for this rate supplier
    rate_supplier
        Indicates the supplier of the rate.
    rate_supplier_logo
        Url of the supplier's logo
    min_in_policy
        This attribute will be used to indicate if the minimum fare or rate
        has been determined to be ‘in policy’ based on the associated policy
        settings.
    max_in_policy
        This attribute will be used to indicate if the maximum fare or rate
        has been determined to be ‘in policy’ based on the associated policy
        settings.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/hotel_v52_0"

    policy_codes_list: None | TypePolicyCodesList1 = field(
        default=None,
        metadata={
            "name": "PolicyCodesList",
            "type": "Element",
        }
    )
    minimum_amount: None | str = field(
        default=None,
        metadata={
            "name": "MinimumAmount",
            "type": "Attribute",
        }
    )
    approximate_minimum_amount: None | str = field(
        default=None,
        metadata={
            "name": "ApproximateMinimumAmount",
            "type": "Attribute",
        }
    )
    min_amount_rate_changed: None | bool = field(
        default=None,
        metadata={
            "name": "MinAmountRateChanged",
            "type": "Attribute",
        }
    )
    maximum_amount: None | str = field(
        default=None,
        metadata={
            "name": "MaximumAmount",
            "type": "Attribute",
        }
    )
    approximate_maximum_amount: None | str = field(
        default=None,
        metadata={
            "name": "ApproximateMaximumAmount",
            "type": "Attribute",
        }
    )
    max_amount_rate_changed: None | bool = field(
        default=None,
        metadata={
            "name": "MaxAmountRateChanged",
            "type": "Attribute",
        }
    )
    minimum_stay_amount: None | str = field(
        default=None,
        metadata={
            "name": "MinimumStayAmount",
            "type": "Attribute",
        }
    )
    approximate_minimum_stay_amount: None | str = field(
        default=None,
        metadata={
            "name": "ApproximateMinimumStayAmount",
            "type": "Attribute",
        }
    )
    commission: None | str = field(
        default=None,
        metadata={
            "name": "Commission",
            "type": "Attribute",
        }
    )
    rate_supplier: None | str = field(
        default=None,
        metadata={
            "name": "RateSupplier",
            "type": "Attribute",
            "max_length": 64,
        }
    )
    rate_supplier_logo: None | str = field(
        default=None,
        metadata={
            "name": "RateSupplierLogo",
            "type": "Attribute",
        }
    )
    min_in_policy: None | bool = field(
        default=None,
        metadata={
            "name": "MinInPolicy",
            "type": "Attribute",
        }
    )
    max_in_policy: None | bool = field(
        default=None,
        metadata={
            "name": "MaxInPolicy",
            "type": "Attribute",
        }
    )
