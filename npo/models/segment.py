from __future__ import annotations

from dataclasses import dataclass

from npo.models.segment_type import SegmentType

__NAMESPACE__ = "urn:vpro:media:2009"


@dataclass
class Segment(SegmentType):
    """
    A program can contain a number of segments.

    A segment is an identifiable part of a program.
    """

    class Meta:
        name = "segment"
        namespace = "urn:vpro:media:2009"
