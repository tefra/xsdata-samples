from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from xsdata.models.datatype import XmlDate, XmlDateTime

from .customer_accounts_rel_structure import CustomerAccountsRelStructure
from .customer_eligibilities_rel_structure import (
    CustomerEligibilitiesRelStructure,
)
from .entity_in_version_structure import DataManagedObjectStructure
from .fare_contracts_rel_structure import FareContractsRelStructure
from .gender_enumeration import GenderEnumeration
from .postal_address import PostalAddress
from .private_code_structure import PrivateCodeStructure
from .telephone_contact_structure import TelephoneContactStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "Customer_VersionStructure"

    surname: None | str = field(
        default=None,
        metadata={
            "name": "Surname",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    first_name: None | str = field(
        default=None,
        metadata={
            "name": "FirstName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "name": "Title",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    date_of_birth: None | XmlDate = field(
        default=None,
        metadata={
            "name": "DateOfBirth",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    gender: None | GenderEnumeration = field(
        default=None,
        metadata={
            "name": "Gender",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    height: None | Decimal = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    photo: None | str = field(
        default=None,
        metadata={
            "name": "Photo",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    smoker: None | bool = field(
        default=None,
        metadata={
            "name": "Smoker",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    email: None | str = field(
        default=None,
        metadata={
            "name": "Email",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    email_verified: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "EmailVerified",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    phone: None | TelephoneContactStructure = field(
        default=None,
        metadata={
            "name": "Phone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    phone_verified: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "PhoneVerified",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    postal_address: None | PostalAddress = field(
        default=None,
        metadata={
            "name": "PostalAddress",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    identity_document_ref: None | PrivateCodeStructure = field(
        default=None,
        metadata={
            "name": "IdentityDocumentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    customer_eligibilities: None | CustomerEligibilitiesRelStructure = field(
        default=None,
        metadata={
            "name": "customerEligibilities",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    customer_accounts: None | CustomerAccountsRelStructure = field(
        default=None,
        metadata={
            "name": "customerAccounts",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_contracts: None | FareContractsRelStructure = field(
        default=None,
        metadata={
            "name": "fareContracts",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
