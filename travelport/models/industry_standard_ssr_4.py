from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


@dataclass
class IndustryStandardSsr4:
    """
    Indicates Carrier Supports this industry standard.

    Parameters
    ----------
    code
        This code indicates which Standard of SSR's they support. Sucha as
        the 'AIRIMP' standard identified by 'IATA.org'
    """

    class Meta:
        name = "IndustryStandardSSR"
        namespace = "http://www.travelport.com/schema/common_v37_0"

    code: None | str = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
        },
    )
