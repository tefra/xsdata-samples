from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.access_policies import AccessPolicies
from ipxact.models.bank_alignment_type import BankAlignmentType
from ipxact.models.banked_bank_type import BankedBankType
from ipxact.models.banked_block_type import BankedBlockType
from ipxact.models.banked_subspace_type import BankedSubspaceType
from ipxact.models.base_address import BaseAddress
from ipxact.models.description import Description
from ipxact.models.display_name import DisplayName
from ipxact.models.parameters import Parameters
from ipxact.models.short_description import ShortDescription
from ipxact.models.simple_access_handle import SimpleAccessHandle
from ipxact.models.usage_type import UsageType
from ipxact.models.vendor_extensions import VendorExtensions
from ipxact.models.volatile import Volatile

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(kw_only=True)
class AddressBankType:
    """
    Top level bank the specify an address.

    :ivar name: Unique name
    :ivar display_name:
    :ivar short_description:
    :ivar description:
    :ivar access_handles:
    :ivar base_address:
    :ivar bank_definition_ref:
    :ivar address_block: An address block within the bank.  No address
        information is supplied.
    :ivar bank: A nested bank of blocks within a bank.  No address
        information is supplied.
    :ivar subspace_map: A subspace map within the bank.  No address
        information is supplied.
    :ivar usage: Indicates the usage of this block.  Possible values are
        'memory', 'register' and 'reserved'.
    :ivar volatile:
    :ivar access_policies:
    :ivar parameters: Any additional parameters needed to describe this
        address block to the generators.
    :ivar vendor_extensions:
    :ivar bank_alignment: Describes whether this bank's blocks are
        aligned in 'parallel' or 'serial'.
    :ivar id:
    """

    class Meta:
        name = "addressBankType"

    name: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "required": True,
        }
    )
    display_name: None | DisplayName = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    short_description: None | ShortDescription = field(
        default=None,
        metadata={
            "name": "shortDescription",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    description: None | Description = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    access_handles: None | AddressBankType.AccessHandles = field(
        default=None,
        metadata={
            "name": "accessHandles",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    base_address: BaseAddress = field(
        metadata={
            "name": "baseAddress",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "required": True,
        }
    )
    bank_definition_ref: None | AddressBankType.BankDefinitionRef = field(
        default=None,
        metadata={
            "name": "bankDefinitionRef",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    address_block: list[BankedBlockType] = field(
        default_factory=list,
        metadata={
            "name": "addressBlock",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    bank: list[AddressBankType.Bank] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    subspace_map: list[BankedSubspaceType] = field(
        default_factory=list,
        metadata={
            "name": "subspaceMap",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    usage: None | UsageType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    volatile: None | Volatile = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    access_policies: None | AccessPolicies = field(
        default=None,
        metadata={
            "name": "accessPolicies",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    parameters: None | Parameters = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    vendor_extensions: None | VendorExtensions = field(
        default=None,
        metadata={
            "name": "vendorExtensions",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    bank_alignment: BankAlignmentType = field(
        metadata={
            "name": "bankAlignment",
            "type": "Attribute",
            "required": True,
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )

    @dataclass(kw_only=True)
    class AccessHandles:
        access_handle: list[SimpleAccessHandle] = field(
            default_factory=list,
            metadata={
                "name": "accessHandle",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
                "min_occurs": 1,
            },
        )

    @dataclass(kw_only=True)
    class BankDefinitionRef:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        type_definitions: str = field(
            metadata={
                "name": "typeDefinitions",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class Bank(BankedBankType):
        vendor_extensions: None | VendorExtensions = field(
            default=None,
            metadata={
                "name": "vendorExtensions",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            },
        )
