from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class ReferentTypeEnum(Enum):
    """
    A set of types of known points along a linear object such as a road.

    :cvar BOUNDARY: A boundary between two jurisdictional or
        administrative areas. These may be legal boundaries such as
        between counties or countries, maintenance responsibility
        boundaries or control boundaries.
    :cvar INTERSECTION: A crossing of two or more roads where the
        precise point of intersection is defined according to specific
        business rules.
    :cvar REFERENCE_MARKER: A marker which is usually but not
        necessarily physical that is one of a sequence which are spaced
        out along the linear object (road)  to provide a location
        reference. The spacing of markers is not necessarily even.
    :cvar LANDMARK: A visible identifiable physical landmark either
        alongside or close to the linear object.
    :cvar ROAD_NODE: A topological node defined on a road network. Such
        nodes may delineate the segmentation of the road network
        according to defined business rules or may constitute a purely
        topological representation of a road network.
    """

    BOUNDARY = "boundary"
    INTERSECTION = "intersection"
    REFERENCE_MARKER = "referenceMarker"
    LANDMARK = "landmark"
    ROAD_NODE = "roadNode"
