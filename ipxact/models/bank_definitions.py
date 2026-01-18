from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.access_policies import AccessPolicies
from ipxact.models.address_unit_bits import AddressUnitBits
from ipxact.models.banked_block_type import BankedBlockType
from ipxact.models.banked_definition_bank_type import BankedDefinitionBankType
from ipxact.models.description import Description
from ipxact.models.display_name import DisplayName
from ipxact.models.parameters import Parameters
from ipxact.models.short_description import ShortDescription
from ipxact.models.usage_type import UsageType
from ipxact.models.vendor_extensions import VendorExtensions
from ipxact.models.volatile import Volatile

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class BankDefinitions:
    class Meta:
        name = "bankDefinitions"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    bank_definition: list[BankDefinitions.BankDefinition] = field(
        default_factory=list,
        metadata={
            "name": "bankDefinition",
            "type": "Element",
            "min_occurs": 1,
        },
    )

    @dataclass
    class BankDefinition:
        """
        :ivar name: Unique name
        :ivar display_name:
        :ivar short_description:
        :ivar description:
        :ivar address_block: An address block within the bank.  No
            address information is supplied.
        :ivar bank: A nested bank of blocks within a bank.  No address
            information is supplied.
        :ivar usage: Indicates the usage of this block.  Possible values
            are 'memory', 'register' and 'reserved'.
        :ivar volatile:
        :ivar access_policies:
        :ivar parameters: Any additional parameters needed to describe
            this address block to the generators.
        :ivar address_unit_bits:
        :ivar vendor_extensions:
        :ivar id:
        """

        name: str | None = field(
            default=None,
            metadata={
                "type": "Element",
                "required": True,
            },
        )
        display_name: DisplayName | None = field(
            default=None,
            metadata={
                "name": "displayName",
                "type": "Element",
            },
        )
        short_description: ShortDescription | None = field(
            default=None,
            metadata={
                "name": "shortDescription",
                "type": "Element",
            },
        )
        description: Description | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        address_block: list[BankedBlockType] = field(
            default_factory=list,
            metadata={
                "name": "addressBlock",
                "type": "Element",
            },
        )
        bank: list[BankDefinitions.BankDefinition.Bank] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )
        usage: UsageType | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        volatile: Volatile | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        access_policies: AccessPolicies | None = field(
            default=None,
            metadata={
                "name": "accessPolicies",
                "type": "Element",
            },
        )
        parameters: Parameters | None = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        address_unit_bits: AddressUnitBits | None = field(
            default=None,
            metadata={
                "name": "addressUnitBits",
                "type": "Element",
            },
        )
        vendor_extensions: VendorExtensions | None = field(
            default=None,
            metadata={
                "name": "vendorExtensions",
                "type": "Element",
            },
        )
        id: str | None = field(
            default=None,
            metadata={
                "type": "Attribute",
                "namespace": "http://www.w3.org/XML/1998/namespace",
            },
        )

        @dataclass
        class Bank(BankedDefinitionBankType):
            vendor_extensions: VendorExtensions | None = field(
                default=None,
                metadata={
                    "name": "vendorExtensions",
                    "type": "Element",
                },
            )
