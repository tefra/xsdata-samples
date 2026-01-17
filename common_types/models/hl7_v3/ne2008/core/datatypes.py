from dataclasses import dataclass, field
from typing import Optional, Union

from .datatypes_base import (
    AnyType,
    Cd,
    Ce,
    EivlEvent,
    Int,
    IvlTs,
    Mo,
    Pq,
    Qty,
    Real,
    SxcmTs,
    Ts,
)
from .voc import (
    CalendarCycleOneLetter,
    CalendarCycleTwoLetterValue,
    ProbabilityDistributionType,
    SetOperator,
)

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class BxitCd(Cd):
    """
    :ivar qty: The quantity in which the bag item occurs in its
        containing bag.
    """

    class Meta:
        name = "BXIT_CD"

    qty: int = field(
        default=1,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class GlistPq(AnyType):
    """
    :ivar head: This is the start-value of the generated list.
    :ivar increment: The difference between one value and its previous
        different value. For example, to generate the sequence (1; 4; 7;
        10; 13; ...) the increment is 3; likewise to generate the
        sequence (1; 1; 4; 4; 7; 7; 10; 10; 13; 13; ...) the increment
        is also 3.
    :ivar period: If non-NULL, specifies that the sequence alternates,
        i.e., after this many increments, the sequence item values roll
        over to start from the initial sequence item value. For example,
        the sequence (1; 2; 3; 1; 2; 3; 1; 2; 3; ...) has period 3; also
        the sequence (1; 1; 2; 2; 3; 3; 1; 1; 2; 2; 3; 3; ...) has
        period 3 too.
    :ivar denominator: The integer by which the index for the sequence
        is divided, effectively the number of times the sequence
        generates the same sequence item value before incrementing to
        the next sequence item value. For example, to generate the
        sequence (1; 1; 1; 2; 2; 2; 3; 3; 3; ...)  the denominator is 3.
    """

    class Meta:
        name = "GLIST_PQ"

    head: Optional[Pq] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    increment: Optional[Pq] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    period: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    denominator: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class GlistTs(AnyType):
    """
    :ivar head: This is the start-value of the generated list.
    :ivar increment: The difference between one value and its previous
        different value. For example, to generate the sequence (1; 4; 7;
        10; 13; ...) the increment is 3; likewise to generate the
        sequence (1; 1; 4; 4; 7; 7; 10; 10; 13; 13; ...) the increment
        is also 3.
    :ivar period: If non-NULL, specifies that the sequence alternates,
        i.e., after this many increments, the sequence item values roll
        over to start from the initial sequence item value. For example,
        the sequence (1; 2; 3; 1; 2; 3; 1; 2; 3; ...) has period 3; also
        the sequence (1; 1; 2; 2; 3; 3; 1; 1; 2; 2; 3; 3; ...) has
        period 3 too.
    :ivar denominator: The integer by which the index for the sequence
        is divided, effectively the number of times the sequence
        generates the same sequence item value before incrementing to
        the next sequence item value. For example, to generate the
        sequence (1; 1; 1; 2; 2; 2; 3; 3; 3; ...)  the denominator is 3.
    """

    class Meta:
        name = "GLIST_TS"

    head: Optional[Ts] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    increment: Optional[Pq] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    period: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    denominator: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class HxitCe(Ce):
    """
    :ivar valid_time: The time interval during which the given
        information was, is, or is expected to be valid. The interval
        can be open or closed, as well as infinite or undefined on
        either side.
    """

    class Meta:
        name = "HXIT_CE"

    valid_time: Optional[IvlTs] = field(
        default=None,
        metadata={
            "name": "validTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )


@dataclass
class HxitPq(Pq):
    """
    :ivar valid_time: The time interval during which the given
        information was, is, or is expected to be valid. The interval
        can be open or closed, as well as infinite or undefined on
        either side.
    """

    class Meta:
        name = "HXIT_PQ"

    valid_time: Optional[IvlTs] = field(
        default=None,
        metadata={
            "name": "validTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )


@dataclass
class IvxbInt(Int):
    """
    :ivar inclusive: Specifies whether the limit is included in the
        interval (interval is closed) or excluded from the interval
        (interval is open).
    """

    class Meta:
        name = "IVXB_INT"

    inclusive: str = field(
        default="true",
        metadata={
            "type": "Attribute",
            "pattern": r"true|false",
        },
    )


@dataclass
class IvxbMo(Mo):
    """
    :ivar inclusive: Specifies whether the limit is included in the
        interval (interval is closed) or excluded from the interval
        (interval is open).
    """

    class Meta:
        name = "IVXB_MO"

    inclusive: str = field(
        default="true",
        metadata={
            "type": "Attribute",
            "pattern": r"true|false",
        },
    )


@dataclass
class IvxbPq(Pq):
    """
    :ivar inclusive: Specifies whether the limit is included in the
        interval (interval is closed) or excluded from the interval
        (interval is open).
    """

    class Meta:
        name = "IVXB_PQ"

    inclusive: str = field(
        default="true",
        metadata={
            "type": "Attribute",
            "pattern": r"true|false",
        },
    )


@dataclass
class IvxbReal(Real):
    """
    :ivar inclusive: Specifies whether the limit is included in the
        interval (interval is closed) or excluded from the interval
        (interval is open).
    """

    class Meta:
        name = "IVXB_REAL"

    inclusive: str = field(
        default="true",
        metadata={
            "type": "Attribute",
            "pattern": r"true|false",
        },
    )


@dataclass
class PivlTs(SxcmTs):
    """
    Note: because this type is defined as an extension of SXCM_T, all of
    the attributes and elements accepted for T are also accepted by this
    definition.

    However, they are NOT allowed by the normative description of this
    type. Unfortunately, we cannot write a general purpose schematron
    contraints to provide that extra validation, thus applications must be
    aware that instance (fragments) that pass validation with this might
    might still not be legal.

    :ivar phase: A prototype of the repeating interval specifying the
        duration of each occurrence and anchors the periodic interval
        sequence at a certain point in time.
    :ivar period: A time duration specifying a reciprocal measure of the
        frequency at which the periodic interval repeats.
    :ivar alignment: Specifies if and how the repetitions are aligned to
        the cycles of the underlying calendar (e.g., to distinguish
        every 30 days from "the 5th of every month".) A non-aligned
        periodic interval recurs independently from the calendar. An
        aligned periodic interval is synchronized with the calendar.
    :ivar institution_specified: Indicates whether the exact timing is
        up to the party executing the schedule (e.g., to distinguish
        "every 8 hours" from "3 times a day".)
    """

    class Meta:
        name = "PIVL_TS"

    phase: Optional[IvlTs] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    period: Optional[Pq] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    alignment: Optional[
        Union[CalendarCycleOneLetter, str, CalendarCycleTwoLetterValue]
    ] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[^\s]+",
        },
    )
    institution_specified: str = field(
        default="false",
        metadata={
            "name": "institutionSpecified",
            "type": "Attribute",
            "pattern": r"true|false",
        },
    )


@dataclass
class PpdPq(Pq):
    """
    :ivar standard_deviation: The primary measure of
        variance/uncertainty of the value (the square root of the sum of
        the squares of the differences between all data points and the
        mean). The standard deviation is used to normalize the data for
        computing the distribution function. Applications that cannot
        deal with probability distributions can still get an idea about
        the confidence level by looking at the standard deviation.
    :ivar distribution_type: A code specifying the type of probability
        distribution. Possible values are as shown in the attached
        table. The NULL value (unknown) for the type code indicates that
        the probability distribution type is unknown. In that case, the
        standard deviation has the meaning of an informal guess.
    """

    class Meta:
        name = "PPD_PQ"

    standard_deviation: Optional[Pq] = field(
        default=None,
        metadata={
            "name": "standardDeviation",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    distribution_type: Optional[ProbabilityDistributionType] = field(
        default=None,
        metadata={
            "name": "distributionType",
            "type": "Attribute",
        },
    )


@dataclass
class PpdTs(Ts):
    """
    :ivar standard_deviation: The primary measure of
        variance/uncertainty of the value (the square root of the sum of
        the squares of the differences between all data points and the
        mean). The standard deviation is used to normalize the data for
        computing the distribution function. Applications that cannot
        deal with probability distributions can still get an idea about
        the confidence level by looking at the standard deviation.
    :ivar distribution_type: A code specifying the type of probability
        distribution. Possible values are as shown in the attached
        table. The NULL value (unknown) for the type code indicates that
        the probability distribution type is unknown. In that case, the
        standard deviation has the meaning of an informal guess.
    """

    class Meta:
        name = "PPD_TS"

    standard_deviation: Optional[Pq] = field(
        default=None,
        metadata={
            "name": "standardDeviation",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    distribution_type: Optional[ProbabilityDistributionType] = field(
        default=None,
        metadata={
            "name": "distributionType",
            "type": "Attribute",
        },
    )


@dataclass
class RtoMoPq(Qty):
    """
    :ivar numerator: The quantity that is being divided in the ratio.
        The default is the integer number 1 (one).
    :ivar denominator: The quantity that devides the numerator in the
        ratio. The default is the integer number 1 (one). The
        denominator must not be zero.
    """

    class Meta:
        name = "RTO_MO_PQ"

    numerator: Optional[Mo] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    denominator: Optional[Pq] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )


@dataclass
class RtoPqPq(Qty):
    """
    :ivar numerator: The quantity that is being divided in the ratio.
        The default is the integer number 1 (one).
    :ivar denominator: The quantity that devides the numerator in the
        ratio. The default is the integer number 1 (one). The
        denominator must not be zero.
    """

    class Meta:
        name = "RTO_PQ_PQ"

    numerator: Optional[Pq] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    denominator: Optional[Pq] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )


@dataclass
class SlistPq(AnyType):
    """
    :ivar origin: The origin of the list item value scale, i.e., the
        physical quantity that a zero-digit in the sequence would
        represent.
    :ivar scale: A ratio-scale quantity that is factored out of the
        digit sequence.
    :ivar digits: A sequence of raw digits for the sample values. This
        is typically the raw output of an A/D converter.
    """

    class Meta:
        name = "SLIST_PQ"

    origin: Optional[Pq] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    scale: Optional[Pq] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    digits: list[int] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "tokens": True,
        },
    )


@dataclass
class SlistTs(AnyType):
    """
    :ivar origin: The origin of the list item value scale, i.e., the
        physical quantity that a zero-digit in the sequence would
        represent.
    :ivar scale: A ratio-scale quantity that is factored out of the
        digit sequence.
    :ivar digits: A sequence of raw digits for the sample values. This
        is typically the raw output of an A/D converter.
    """

    class Meta:
        name = "SLIST_TS"

    origin: Optional[Ts] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    scale: Optional[Pq] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    digits: list[int] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "tokens": True,
        },
    )


@dataclass
class SxcmCd(Cd):
    """
    :ivar operator: A code specifying whether the set component is
        included (union) or excluded (set-difference) from the set, or
        other set operations with the current set component and the set
        as constructed from the representation stream up to the current
        point.
    """

    class Meta:
        name = "SXCM_CD"

    operator: SetOperator = field(
        default=SetOperator.I,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class SxcmInt(Int):
    """
    :ivar operator: A code specifying whether the set component is
        included (union) or excluded (set-difference) from the set, or
        other set operations with the current set component and the set
        as constructed from the representation stream up to the current
        point.
    """

    class Meta:
        name = "SXCM_INT"

    operator: SetOperator = field(
        default=SetOperator.I,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class SxcmMo(Mo):
    """
    :ivar operator: A code specifying whether the set component is
        included (union) or excluded (set-difference) from the set, or
        other set operations with the current set component and the set
        as constructed from the representation stream up to the current
        point.
    """

    class Meta:
        name = "SXCM_MO"

    operator: SetOperator = field(
        default=SetOperator.I,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class SxcmPq(Pq):
    """
    :ivar operator: A code specifying whether the set component is
        included (union) or excluded (set-difference) from the set, or
        other set operations with the current set component and the set
        as constructed from the representation stream up to the current
        point.
    """

    class Meta:
        name = "SXCM_PQ"

    operator: SetOperator = field(
        default=SetOperator.I,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class SxcmReal(Real):
    """
    :ivar operator: A code specifying whether the set component is
        included (union) or excluded (set-difference) from the set, or
        other set operations with the current set component and the set
        as constructed from the representation stream up to the current
        point.
    """

    class Meta:
        name = "SXCM_REAL"

    operator: SetOperator = field(
        default=SetOperator.I,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class SxprTs(SxcmTs):
    class Meta:
        name = "SXPR_TS"

    comp: list[SxcmTs] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "min_occurs": 2,
        },
    )


@dataclass
class UvpTs(Ts):
    """
    :ivar probability: The probability assigned to the value, a decimal
        number between 0 (very uncertain) and 1 (certain).
    """

    class Meta:
        name = "UVP_TS"

    probability: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        },
    )


@dataclass
class IvlInt(SxcmInt):
    """
    :ivar low: The low limit of the interval.
    :ivar width: The difference between high and low boundary. The
        purpose of distinguishing a width property is to handle all
        cases of incomplete information symmetrically. In any interval
        representation only two of the three properties high, low, and
        width need to be stated and the third can be derived.
    :ivar high: The high limit of the interval.
    :ivar center: The arithmetic mean of the interval (low plus high
        divided by 2). The purpose of distinguishing the center as a
        semantic property is for conversions of intervals from and to
        point values.
    """

    class Meta:
        name = "IVL_INT"

    low: Optional[IvxbInt] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    width: list[Int] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "max_occurs": 3,
        },
    )
    high: list[IvxbInt] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "max_occurs": 3,
        },
    )
    center: Optional[Int] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )


@dataclass
class IvlMo(SxcmMo):
    """
    :ivar low: The low limit of the interval.
    :ivar width: The difference between high and low boundary. The
        purpose of distinguishing a width property is to handle all
        cases of incomplete information symmetrically. In any interval
        representation only two of the three properties high, low, and
        width need to be stated and the third can be derived.
    :ivar high: The high limit of the interval.
    :ivar center: The arithmetic mean of the interval (low plus high
        divided by 2). The purpose of distinguishing the center as a
        semantic property is for conversions of intervals from and to
        point values.
    """

    class Meta:
        name = "IVL_MO"

    low: Optional[IvxbMo] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    width: list[Mo] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "max_occurs": 3,
        },
    )
    high: list[IvxbMo] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "max_occurs": 3,
        },
    )
    center: Optional[Mo] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )


@dataclass
class IvlPq(SxcmPq):
    """
    :ivar low: The low limit of the interval.
    :ivar width: The difference between high and low boundary. The
        purpose of distinguishing a width property is to handle all
        cases of incomplete information symmetrically. In any interval
        representation only two of the three properties high, low, and
        width need to be stated and the third can be derived.
    :ivar high: The high limit of the interval.
    :ivar center: The arithmetic mean of the interval (low plus high
        divided by 2). The purpose of distinguishing the center as a
        semantic property is for conversions of intervals from and to
        point values.
    """

    class Meta:
        name = "IVL_PQ"

    low: Optional[IvxbPq] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    width: list[Pq] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "max_occurs": 3,
        },
    )
    high: list[IvxbPq] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "max_occurs": 3,
        },
    )
    center: Optional[Pq] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )


@dataclass
class IvlReal(SxcmReal):
    """
    :ivar low: The low limit of the interval.
    :ivar width: The difference between high and low boundary. The
        purpose of distinguishing a width property is to handle all
        cases of incomplete information symmetrically. In any interval
        representation only two of the three properties high, low, and
        width need to be stated and the third can be derived.
    :ivar high: The high limit of the interval.
    :ivar center: The arithmetic mean of the interval (low plus high
        divided by 2). The purpose of distinguishing the center as a
        semantic property is for conversions of intervals from and to
        point values.
    """

    class Meta:
        name = "IVL_REAL"

    low: Optional[IvxbReal] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    width: list[Real] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "max_occurs": 3,
        },
    )
    high: list[IvxbReal] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "max_occurs": 3,
        },
    )
    center: Optional[Real] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )


@dataclass
class IvxbPpdPq(PpdPq):
    """
    :ivar inclusive: Specifies whether the limit is included in the
        interval (interval is closed) or excluded from the interval
        (interval is open).
    """

    class Meta:
        name = "IVXB_PPD_PQ"

    inclusive: str = field(
        default="true",
        metadata={
            "type": "Attribute",
            "pattern": r"true|false",
        },
    )


@dataclass
class IvxbPpdTs(PpdTs):
    """
    :ivar inclusive: Specifies whether the limit is included in the
        interval (interval is closed) or excluded from the interval
        (interval is open).
    """

    class Meta:
        name = "IVXB_PPD_TS"

    inclusive: str = field(
        default="true",
        metadata={
            "type": "Attribute",
            "pattern": r"true|false",
        },
    )


@dataclass
class SxcmPpdPq(PpdPq):
    """
    :ivar operator: A code specifying whether the set component is
        included (union) or excluded (set-difference) from the set, or
        other set operations with the current set component and the set
        as constructed from the representation stream up to the current
        point.
    """

    class Meta:
        name = "SXCM_PPD_PQ"

    operator: SetOperator = field(
        default=SetOperator.I,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class SxcmPpdTs(PpdTs):
    """
    :ivar operator: A code specifying whether the set component is
        included (union) or excluded (set-difference) from the set, or
        other set operations with the current set component and the set
        as constructed from the representation stream up to the current
        point.
    """

    class Meta:
        name = "SXCM_PPD_TS"

    operator: SetOperator = field(
        default=SetOperator.I,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class BxitIvlPq(IvlPq):
    """
    :ivar qty: The quantity in which the bag item occurs in its
        containing bag.
    """

    class Meta:
        name = "BXIT_IVL_PQ"

    qty: int = field(
        default=1,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class EivlTs(SxcmTs):
    """
    Note: because this type is defined as an extension of SXCM_T, all of
    the attributes and elements accepted for T are also accepted by this
    definition.

    However, they are NOT allowed by the normative description of this
    type. Unfortunately, we cannot write a general purpose schematron
    contraints to provide that extra validation, thus applications must be
    aware that instance (fragments) that pass validation with this might
    might still not be legal.

    :ivar event: A code for a common (periodical) activity of daily
        living based on which the event related periodic interval is
        specified.
    :ivar offset: An interval of elapsed time (duration, not absolute
        point in time) that marks the offsets for the beginning, width
        and end of the event-related periodic interval measured from the
        time each such event actually occurred.
    """

    class Meta:
        name = "EIVL_TS"

    event: Optional[EivlEvent] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    offset: Optional[IvlPq] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )


@dataclass
class IvlPpdPq(SxcmPpdPq):
    """
    :ivar low: The low limit of the interval.
    :ivar width: The difference between high and low boundary. The
        purpose of distinguishing a width property is to handle all
        cases of incomplete information symmetrically. In any interval
        representation only two of the three properties high, low, and
        width need to be stated and the third can be derived.
    :ivar high: The high limit of the interval.
    :ivar center: The arithmetic mean of the interval (low plus high
        divided by 2). The purpose of distinguishing the center as a
        semantic property is for conversions of intervals from and to
        point values.
    """

    class Meta:
        name = "IVL_PPD_PQ"

    low: Optional[IvxbPpdPq] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    width: list[PpdPq] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "max_occurs": 3,
        },
    )
    high: list[IvxbPpdPq] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "max_occurs": 3,
        },
    )
    center: Optional[PpdPq] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )


@dataclass
class IvlPpdTs(SxcmPpdTs):
    """
    :ivar low: The low limit of the interval.
    :ivar width: The difference between high and low boundary. The
        purpose of distinguishing a width property is to handle all
        cases of incomplete information symmetrically. In any interval
        representation only two of the three properties high, low, and
        width need to be stated and the third can be derived.
    :ivar high: The high limit of the interval.
    :ivar center: The arithmetic mean of the interval (low plus high
        divided by 2). The purpose of distinguishing the center as a
        semantic property is for conversions of intervals from and to
        point values.
    """

    class Meta:
        name = "IVL_PPD_TS"

    low: Optional[IvxbPpdTs] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    width: list[PpdPq] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "max_occurs": 3,
        },
    )
    high: list[IvxbPpdTs] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "max_occurs": 3,
        },
    )
    center: Optional[PpdTs] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )


@dataclass
class EivlPpdTs(SxcmPpdTs):
    """
    Note: because this type is defined as an extension of SXCM_T, all of
    the attributes and elements accepted for T are also accepted by this
    definition.

    However, they are NOT allowed by the normative description of this
    type. Unfortunately, we cannot write a general purpose schematron
    contraints to provide that extra validation, thus applications must be
    aware that instance (fragments) that pass validation with this might
    might still not be legal.

    :ivar event: A code for a common (periodical) activity of daily
        living based on which the event related periodic interval is
        specified.
    :ivar offset: An interval of elapsed time (duration, not absolute
        point in time) that marks the offsets for the beginning, width
        and end of the event-related periodic interval measured from the
        time each such event actually occurred.
    """

    class Meta:
        name = "EIVL_PPD_TS"

    event: Optional[EivlEvent] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    offset: Optional[IvlPpdPq] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )


@dataclass
class PivlPpdTs(SxcmPpdTs):
    """
    Note: because this type is defined as an extension of SXCM_T, all of
    the attributes and elements accepted for T are also accepted by this
    definition.

    However, they are NOT allowed by the normative description of this
    type. Unfortunately, we cannot write a general purpose schematron
    contraints to provide that extra validation, thus applications must be
    aware that instance (fragments) that pass validation with this might
    might still not be legal.

    :ivar phase: A prototype of the repeating interval specifying the
        duration of each occurrence and anchors the periodic interval
        sequence at a certain point in time.
    :ivar period: A time duration specifying a reciprocal measure of the
        frequency at which the periodic interval repeats.
    :ivar alignment: Specifies if and how the repetitions are aligned to
        the cycles of the underlying calendar (e.g., to distinguish
        every 30 days from "the 5th of every month".) A non-aligned
        periodic interval recurs independently from the calendar. An
        aligned periodic interval is synchronized with the calendar.
    :ivar institution_specified: Indicates whether the exact timing is
        up to the party executing the schedule (e.g., to distinguish
        "every 8 hours" from "3 times a day".)
    """

    class Meta:
        name = "PIVL_PPD_TS"

    phase: Optional[IvlPpdTs] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    period: Optional[PpdPq] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    alignment: Optional[
        Union[CalendarCycleOneLetter, str, CalendarCycleTwoLetterValue]
    ] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[^\s]+",
        },
    )
    institution_specified: str = field(
        default="false",
        metadata={
            "name": "institutionSpecified",
            "type": "Attribute",
            "pattern": r"true|false",
        },
    )
