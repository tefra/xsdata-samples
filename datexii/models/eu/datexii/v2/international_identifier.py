from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.country_enum import CountryEnum
from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class InternationalIdentifier:
    """
    An identifier/name whose range is specific to the particular country.

    :ivar country: ISO 3166-1 two character country code.
    :ivar national_identifier: Identifier or name unique within the
        specified country.
    :ivar international_identifier_extension:
    """

    country: None | CountryEnum = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    national_identifier: None | str = field(
        default=None,
        metadata={
            "name": "nationalIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
            "max_length": 1024,
        },
    )
    international_identifier_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "internationalIdentifierExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
