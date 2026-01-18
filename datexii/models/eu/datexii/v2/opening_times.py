from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.validity import Validity

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class OpeningTimes:
    """
    A specification of opening times (e.g. for a parking site, a service
    facility, an access or the availability for equipment).

    :ivar last_updated: The date/time at which this information was last
        updated.
    :ivar open_all_year: indicates whether the parking facility is
        available 365 days a year
    :ivar available24hours: Specifies if the availability is 24 hours a
        day. If omitted, this information is unknown or heterogeneous.
    :ivar url_link_address: A Uniform Resource Locator (URL) address
        pointing to a resource available on the Internet from where
        further relevant information may be obtained.
    :ivar opening_times_unknown: When true, the opening times are
        unknown.
    :ivar opening_times_not_specified: When true, the opening times are
        not specified.
    :ivar validity:
    :ivar opening_times_extension:
    """

    last_updated: XmlDateTime | None = field(
        default=None,
        metadata={
            "name": "lastUpdated",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    open_all_year: bool | None = field(
        default=None,
        metadata={
            "name": "openAllYear",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    available24hours: bool | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    url_link_address: str | None = field(
        default=None,
        metadata={
            "name": "urlLinkAddress",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    opening_times_unknown: bool | None = field(
        default=None,
        metadata={
            "name": "openingTimesUnknown",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    opening_times_not_specified: bool | None = field(
        default=None,
        metadata={
            "name": "openingTimesNotSpecified",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    validity: Validity | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    opening_times_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "openingTimesExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
