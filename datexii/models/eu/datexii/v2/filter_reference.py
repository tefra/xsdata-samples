from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class FilterReference:
    """
    Details of a supplier's filter in a data exchange context.

    :ivar delete_filter: Indicates that a client defined filter has to
        be deleted.
    :ivar filter_operation_approved: Indicates that a client defined
        filter was either stored or deleted successfully.
    :ivar key_filter_reference: The unique key identifier of a supplier
        applied filter.
    :ivar filter_reference_extension:
    """

    delete_filter: Optional[bool] = field(
        default=None,
        metadata={
            "name": "deleteFilter",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    filter_operation_approved: Optional[bool] = field(
        default=None,
        metadata={
            "name": "filterOperationApproved",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    key_filter_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "keyFilterReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
            "max_length": 1024,
        },
    )
    filter_reference_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "filterReferenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
