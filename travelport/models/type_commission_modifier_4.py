from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


class TypeCommissionModifier4(Enum):
    """
    Optional commission modifier.

    Properties
    ----------
    FARE_PERCENT
        Commission percentage applied to the fare
    FARE_AMOUNT
        Commission amount applied to the fare
    COMMISSION_AMOUNT
        Specific commission amount to be applied
    LESS_STANDARD_COMMISSION
        Indicates commission percentage applied to the fare less the
        standard commission
    STANDARD_PLUS_SUPPLEMENTARY_PERCENT
        Indicates commission percentage includes standard and supplementary
        commission
    SUPPLEMENTARY_PERCENT
        Supplementary commission percent which is applied to the fare
    SUPPLEMENTARY_AMOUNT
        Supplementary commission amount which is applied to the fare
    """

    FARE_PERCENT = "FarePercent"
    FARE_AMOUNT = "FareAmount"
    COMMISSION_AMOUNT = "CommissionAmount"
    LESS_STANDARD_COMMISSION = "LessStandardCommission"
    STANDARD_PLUS_SUPPLEMENTARY_PERCENT = "StandardPlusSupplementaryPercent"
    SUPPLEMENTARY_PERCENT = "SupplementaryPercent"
    SUPPLEMENTARY_AMOUNT = "SupplementaryAmount"
