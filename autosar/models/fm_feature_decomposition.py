from __future__ import annotations

from dataclasses import dataclass, field

from .category_string import CategoryString
from .fm_feature_subtypes_enum import FmFeatureSubtypesEnum
from .positive_integer import PositiveInteger
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class FmFeatureDecomposition:
    """
    A FMFeatureDecomposition describes dependencies between a list of
    features and their parent feature (i.e., the FMFeature that aggregates
    the FMFeatureDecomposition).

    The kind of dependency is defined by the attribute category.

    :ivar category: The category of a FMFeatureDecomposition defines the
        type of dependency that is defined by the
        FMFeatureDecomposition. There are four different categories:
        MANDATORYFEATURE, OPTIONALFEATURE, ALTERNATIVEFEATURE, and
        MULTIPLEFEATURE.
    :ivar feature_refs: The features that are affected by the dependency
        defined by the FMFeatureDecomposition.
    :ivar max: For a dependency of category MULTIPLEFEATURE, this
        defines the maximum number of features allowed.
    :ivar min: For a dependency of category MULTIPLEFEATURE, this
        defines the minimum number of features allowed.
    :ivar s: Checksum calculated by the user's tool environment for an
        ArObject. May be used in an own tool environment to determine if
        an ArObject has changed. The checksum has no semantic meaning
        for an AUTOSAR model and there is no requirement for AUTOSAR
        tools to manage the checksum.
    :ivar t: Timestamp calculated by the user's tool environment for an
        ArObject. May be used in an own tool environment to determine
        the last change of an ArObject. The timestamp has no semantic
        meaning for an AUTOSAR model and there is no requirement for
        AUTOSAR tools to manage the timestamp.
    """

    class Meta:
        name = "FM-FEATURE-DECOMPOSITION"

    category: None | CategoryString = field(
        default=None,
        metadata={
            "name": "CATEGORY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    feature_refs: None | FmFeatureDecomposition.FeatureRefs = field(
        default=None,
        metadata={
            "name": "FEATURE-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    max: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "MAX",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    min: None | PositiveInteger = field(
        default=None,
        metadata={
            "name": "MIN",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: None | str = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: None | str = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )

    @dataclass
    class FeatureRefs:
        feature_ref: list[FmFeatureDecomposition.FeatureRefs.FeatureRef] = (
            field(
                default_factory=list,
                metadata={
                    "name": "FEATURE-REF",
                    "type": "Element",
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            )
        )

        @dataclass
        class FeatureRef(Ref):
            dest: None | FmFeatureSubtypesEnum = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                },
            )
