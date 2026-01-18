from dataclasses import dataclass, field

from sdmx_ml.models.versionable_type import VersionableType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common"


@dataclass(frozen=True)
class MaintainableBaseType(VersionableType):
    """
    MaintainableBaseType is an abstract type that only serves the purpose
    of forming the base for the actual MaintainableType.

    The purpose of this type is to restrict the VersionableType to require
    the id attribute.
    """

    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z0-9_@$\-]+",
        },
    )
