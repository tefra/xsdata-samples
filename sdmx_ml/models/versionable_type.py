from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from sdmx_ml.models.nameable_type import NameableType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common"


@dataclass(frozen=True)
class VersionableType(NameableType):
    """
    VersionableType is an abstract base type for all versionable objects.

    :ivar version: This version attribute holds a version number (see
        common:VersionType definition for details). If not supplied,
        artefact is considered to be un-versioned.
    :ivar valid_from: The validFrom attribute provides the inclusive
        start date for providing supplemental validity information about
        the version.
    :ivar valid_to: The validTo attribute provides the inclusive end
        date for providing supplemental validity information about the
        version.
    """

    version: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"(0|[1-9]\d*)(\.(0|[1-9]\d*))?",
        },
    )
    valid_from: XmlDateTime | None = field(
        default=None,
        metadata={
            "name": "validFrom",
            "type": "Attribute",
        },
    )
    valid_to: XmlDateTime | None = field(
        default=None,
        metadata={
            "name": "validTo",
            "type": "Attribute",
        },
    )
