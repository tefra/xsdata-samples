from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class GroupDiscountBasisEnumeration(Enum):
    NONE_VALUE = "none"
    FREE = "free"
    DISCOUNT_FOR_FIRST_PERSON_ONLY = "discountForFirstPersonOnly"
    DISCOUNT_FOR_SECOND_AND_SUBSEQUENT_PERSONS = "discountForSecondAndSubsequentPersons"
    STEP_DISCOUNT = "stepDiscount"
    OTHER = "other"
