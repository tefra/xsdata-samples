from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.agency_scheme_type import AgencySchemeType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True, kw_only=True)
class AgencySchemesType:
    """
    AgencySchemesType describes the structure of the agency schemes
    container.

    It contains one or more agency scheme, which can be explicitly detailed
    or referenced from an external structure document or registry service.

    :ivar agency_scheme: AgencyScheme provides the details of an agency
        scheme, in which agencies are described.
    """

    agency_scheme: tuple[AgencySchemeType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "AgencyScheme",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "min_occurs": 1,
        },
    )
