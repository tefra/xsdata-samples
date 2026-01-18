from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TelephoneContactStructure:
    tel_national_number: str | None = field(
        default=None,
        metadata={
            "name": "TelNationalNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
            "pattern": r"[0-9 /-]{1,20}",
        },
    )
    tel_extension_number: str | None = field(
        default=None,
        metadata={
            "name": "TelExtensionNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "pattern": r"[0-9]{1,6}",
        },
    )
    tel_country_code: str | None = field(
        default=None,
        metadata={
            "name": "TelCountryCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "pattern": r"[0-9]{1,3}",
        },
    )
