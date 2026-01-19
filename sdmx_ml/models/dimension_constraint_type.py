from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"


@dataclass(frozen=True, kw_only=True)
class DimensionConstraintType:
    """
    Specifies the fixed list of Dimensions (by ID) to which a Dataflow may
    be constrained.

    This is a required property if the DataStructure defines itself as an
    evolving structure, indicating that it can change dimensionality under
    a minor version change, and if the Dataflow references that
    DataStructure using a wildcarded minor version number. New minor DSD
    version can so still be used by this Dataflow even if that DSD version
    defines new additional dimensions. Dimensions not listed should not be
    used in Datasets for this Dataflow. The Time Dimension is not to be
    listed, as it is always to be used when defined in the DSD, and it
    cannot be added to a DSD without increasing its major version.
    """

    dimension: tuple[str, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Dimension",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure",
            "min_occurs": 1,
            "pattern": r"[A-Za-z0-9_@$\-]+",
        },
    )
