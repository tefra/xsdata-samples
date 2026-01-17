from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


class TypeRateCategory(Enum):
    """
    The category of the rate (Best, etc).
    """

    ASSOCIATION = "Association"
    BUSINESS = "Business"
    CORPORATE = "Corporate"
    GOVERNMENT = "Government"
    INDUSTRY = "Industry"
    PACKAGE = "Package"
    INCLUSIVE = "Inclusive"
    PROMOTIONAL = "Promotional"
    CREDENTIAL = "Credential"
    STANDARD = "Standard"
    CONSORTIUM = "Consortium"
    CONVENTION = "Convention"
    NEGOTIATED = "Negotiated"
    PREPAY = "Prepay"
