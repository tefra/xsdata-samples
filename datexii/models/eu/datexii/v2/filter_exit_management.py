from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class FilterExitManagement:
    """
    Filter indicators management information.

    :ivar filter_end: This attribute, set to true, indicates that the
        filter, for which a previous record version has been published,
        becomes inactive.
    :ivar filter_out_of_range: This attribute is set to true when a
        previous version of this record has been published and now, for
        this new record version, the record goes out of the filter
        range.
    :ivar filter_exit_management_extension:
    """

    filter_end: None | bool = field(
        default=None,
        metadata={
            "name": "filterEnd",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    filter_out_of_range: None | bool = field(
        default=None,
        metadata={
            "name": "filterOutOfRange",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    filter_exit_management_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "filterExitManagementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
