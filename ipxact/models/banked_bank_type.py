from dataclasses import dataclass, field
from typing import Optional

from ipxact.models.access_policies import AccessPolicies
from ipxact.models.bank_alignment_type import BankAlignmentType
from ipxact.models.banked_block_type import BankedBlockType
from ipxact.models.banked_subspace_type import BankedSubspaceType
from ipxact.models.description import Description
from ipxact.models.display_name import DisplayName
from ipxact.models.parameters import Parameters
from ipxact.models.short_description import ShortDescription
from ipxact.models.simple_access_handle import SimpleAccessHandle
from ipxact.models.usage_type import UsageType
from ipxact.models.vendor_extensions import VendorExtensions
from ipxact.models.volatile import Volatile

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class BankedBankType:
    """
    Banks nested inside a bank do not specify address.

    :ivar name: Unique name
    :ivar display_name:
    :ivar short_description:
    :ivar description:
    :ivar access_handles:
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
    :ivar bank_alignment:
    :ivar id:
    """

    class Meta:
        name = "bankedBankType"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            "required": True,
        },
    )
    display_name: Optional[DisplayName] = field(
        default=None,
        metadata={
            "name": "displayName",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    short_description: Optional[ShortDescription] = field(
        default=None,
        metadata={
            "name": "shortDescription",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    description: Optional[Description] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    access_handles: Optional["BankedBankType.AccessHandles"] = field(
        default=None,
        metadata={
            "name": "accessHandles",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    bank_definition_ref: Optional["BankedBankType.BankDefinitionRef"] = field(
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
    bank: list["BankedBankType.Bank"] = field(
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
    usage: Optional[UsageType] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    volatile: Optional[Volatile] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    access_policies: Optional[AccessPolicies] = field(
        default=None,
        metadata={
            "name": "accessPolicies",
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    parameters: Optional[Parameters] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
        },
    )
    bank_alignment: Optional[BankAlignmentType] = field(
        default=None,
        metadata={
            "name": "bankAlignment",
            "type": "Attribute",
            "required": True,
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        },
    )

    @dataclass
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

    @dataclass
    class BankDefinitionRef:
        value: str = field(
            default="",
            metadata={
                "required": True,
            },
        )
        type_definitions: Optional[str] = field(
            default=None,
            metadata={
                "name": "typeDefinitions",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class Bank:
        vendor_extensions: Optional[VendorExtensions] = field(
            default=None,
            metadata={
                "name": "vendorExtensions",
                "type": "Element",
                "namespace": "http://www.accellera.org/XMLSchema/IPXACT/1685-2022",
            },
        )
