from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.electronic_misc_document import ElectronicMiscDocument
from travelport.models.emdcommission import Emdcommission
from travelport.models.emdendorsement import Emdendorsement
from travelport.models.emdpricing_info import EmdpricingInfo
from travelport.models.emdtraveler_info import EmdtravelerInfo
from travelport.models.fare_calc import FareCalc
from travelport.models.form_of_payment_1 import FormOfPayment1
from travelport.models.payment_1 import Payment1
from travelport.models.supplier_locator_1 import SupplierLocator1
from travelport.models.type_element_status_1 import TypeElementStatus1

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class Emdinfo:
    """This is the parent container to display EMD information.

    Occurrence of multiple unique EMDs inside this container indicate
    that those EMDs are conjunctive to each other. Supported providers
    are 1G/1V/1P

    Parameters
    ----------
    emdtraveler_info
        Basic information of the traveler associated with this EMDInfo.
    supplier_locator
        List of Supplier Locator information that is associated with this
        document
    electronic_misc_document
        Electronic miscellaneous documents.As an EMDInfo container displays
        all the EMDs which are in conjunction, there can be maximum 4
        ElectronicMiscDocuments present in an EMDInfo
    payment
        Payment charged for EMD isuance
    form_of_payment
        FormOfPayment used for issuing these electronic miscellaneous
        documents
    emdpricing_info
        Fare related information for these electronic miscellaneous
        documents
    emdendorsement
    fare_calc
        Infomration about the fare calculation
    emdcommission
        Commission information applied during EMD issuance
    provider_code
    provider_locator_code
    supplier_code
        Represents Carrier Code for ACH PNR Retrieve.
    key
        System generated Key
    el_stat
        This attribute is used to show the action results of an element.
        Possible values are "A" (when elements have been added to the UR)
        and "M" (when existing elements have been modified). Response only.
    key_override
        If a duplicate key is found where we are adding elements in some
        cases like URAdd, then instead of erroring out set this attribute to
        true.
    """

    class Meta:
        name = "EMDInfo"
        namespace = "http://www.travelport.com/schema/air_v52_0"

    emdtraveler_info: None | EmdtravelerInfo = field(
        default=None,
        metadata={
            "name": "EMDTravelerInfo",
            "type": "Element",
            "required": True,
        },
    )
    supplier_locator: list[SupplierLocator1] = field(
        default_factory=list,
        metadata={
            "name": "SupplierLocator",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    electronic_misc_document: list[ElectronicMiscDocument] = field(
        default_factory=list,
        metadata={
            "name": "ElectronicMiscDocument",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
    payment: None | Payment1 = field(
        default=None,
        metadata={
            "name": "Payment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    form_of_payment: None | FormOfPayment1 = field(
        default=None,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    emdpricing_info: None | EmdpricingInfo = field(
        default=None,
        metadata={
            "name": "EMDPricingInfo",
            "type": "Element",
        },
    )
    emdendorsement: list[Emdendorsement] = field(
        default_factory=list,
        metadata={
            "name": "EMDEndorsement",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    fare_calc: None | FareCalc = field(
        default=None,
        metadata={
            "name": "FareCalc",
            "type": "Element",
        },
    )
    emdcommission: None | Emdcommission = field(
        default=None,
        metadata={
            "name": "EMDCommission",
            "type": "Element",
        },
    )
    provider_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "required": True,
            "min_length": 2,
            "max_length": 5,
        },
    )
    provider_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderLocatorCode",
            "type": "Attribute",
            "required": True,
            "max_length": 15,
        },
    )
    supplier_code: None | str = field(
        default=None,
        metadata={
            "name": "SupplierCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 5,
        },
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
    el_stat: None | TypeElementStatus1 = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        },
    )
    key_override: None | bool = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        },
    )
