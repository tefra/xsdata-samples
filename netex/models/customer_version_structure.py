from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from xsdata.models.datatype import XmlDate
from .alternative_texts_rel_structure import DataManagedObjectStructure
from .customer_accounts_rel_structure import CustomerAccountsRelStructure
from .customer_eligibilities_rel_structure import (
    CustomerEligibilitiesRelStructure,
)
from .fare_contracts_rel_structure import FareContractsRelStructure
from .gender_enumeration import GenderEnumeration
from .postal_address import PostalAddress
from .private_code_structure import PrivateCodeStructure
from .telephone_contact_structure import TelephoneContactStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CustomerVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "Customer_VersionStructure"

    surname: Optional[str] = field(
        default=None,
        metadata={
            "name": "Surname",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    first_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "FirstName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "name": "Title",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    date_of_birth: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DateOfBirth",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    gender: Optional[GenderEnumeration] = field(
        default=None,
        metadata={
            "name": "Gender",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    height: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    photo: Optional[str] = field(
        default=None,
        metadata={
            "name": "Photo",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    email: Optional[str] = field(
        default=None,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    phone: Optional[TelephoneContactStructure] = field(
        default=None,
        metadata={
            "name": "Phone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    postal_address: Optional[PostalAddress] = field(
        default=None,
        metadata={
            "name": "PostalAddress",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    identity_document_ref: Optional[PrivateCodeStructure] = field(
        default=None,
        metadata={
            "name": "IdentityDocumentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    customer_eligibilities: Optional[
        CustomerEligibilitiesRelStructure
    ] = field(
        default=None,
        metadata={
            "name": "customerEligibilities",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    customer_accounts: Optional[CustomerAccountsRelStructure] = field(
        default=None,
        metadata={
            "name": "customerAccounts",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_contracts: Optional[FareContractsRelStructure] = field(
        default=None,
        metadata={
            "name": "fareContracts",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
