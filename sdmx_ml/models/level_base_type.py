from dataclasses import dataclass, field

from sdmx_ml.models.nameable_type import NameableType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class LevelBaseType(NameableType):
    """
    LevelBaseType is an abstract base type that makes up the basis for the
    LevelType.

    It requires a name and id.
    """

    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[A-Za-z0-9_@$\-]+",
        },
    )
