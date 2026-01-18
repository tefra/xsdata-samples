from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.activity import Activity
from datexii.models.eu.datexii.v2.authority_operation_type_enum import (
    AuthorityOperationTypeEnum,
)
from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class AuthorityOperation(Activity):
    """
    Authority initiated operation or activity that could disrupt traffic.

    :ivar authority_operation_type: Type of authority initiated
        operation or activity that could disrupt traffic.
    :ivar authority_operation_extension:
    """

    authority_operation_type: None | AuthorityOperationTypeEnum = field(
        default=None,
        metadata={
            "name": "authorityOperationType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    authority_operation_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "authorityOperationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
