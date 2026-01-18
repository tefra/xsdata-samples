from __future__ import annotations

from dataclasses import dataclass, field

from .area_enum_nohref_simple import AreaEnumNohrefSimple
from .area_enum_shape_simple import AreaEnumShapeSimple

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class Area:
    """
    This element specifies a region in an image map.

    Image maps enable authors to specify regions in an object (e.g. a
    graphic) and to assign a specific activity to each region (e.g. load a
    document, launch a program etc.). For more details refer to the
    specification of HTML.

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
    :ivar accesskey: This attribute assigns an access key to an element.
        An access key is an individual character (e.g. "B") within the
        document character range. If an access key with an element
        assigned to it is pressed, the element comes into focus. The
        activity performed when an element comes into focus, is
        dependent on the element itself
    :ivar alt: This attribute specifies the text to be inserted as an
        alternative to illustrations, shapes or applets, where these
        cannot be displayed by user agents.
    :ivar class_value: Blank separated list of classes
    :ivar coords: This attribute specifies the position and shape on the
        screen. The number of values and their order depend on the
        geometrical figure defined.
    :ivar href: This attribute specifies the memory location of a web
        resource. It is therefore able to specify a link between the
        current element and the target element.
    :ivar nohref: If this attribute is set, the Area has no associated
        link.
    :ivar onblur: The ONBLUR-Event occurs, when focus is switched away
        from an element. A script can be stored in this attribute to be
        performed in the Event.
    :ivar onclick: The ONCLICK-Event occurs, if the current element is
        clicked-on. A script can be stored in this attribute to be
        performed in the Event.
    :ivar ondblclick: The ONCLICK-Event occurs, if the current element
        is "double" clicked-on. A script can be stored in this attribute
        to be performed in the Event.
    :ivar onfocus: The ONFOCUS-Event occurs, if an element comes into
        focus (e.g., through navigation using the tab button). A script
        can be stored in this attribute to be performed in the Event.
    :ivar onkeydown: The ONKEYDOWN-Event occurs, if a button on the
        current element is pressed down. A script can be stored in this
        attribute to be performed in the event.
    :ivar onkeypress: The ONKEYPRESS-Event occurs, if a button on the
        current element is pressed down and released. A script can be
        stored in this attribute to be performed in the Event.
    :ivar onkeyup: The ONKEYUP-Event occurs, if a button on the current
        element is released. A script can be stored in this attribute to
        be performed in the Event.
    :ivar onmousedown: The ONMOUSEDOWN-Event occurs, if the mouse button
        used for clicking is held down on the current element. A script
        can be stored in this attribute to be performed in the Event.
    :ivar onmousemove: The ONMOUSEMOVE-Event occurs, if the mouse
        pointer is moved on the current element (i.e. it is located on
        the current element). A script can be stored in this attribute
        to be performed in the Event.
    :ivar onmouseout: The ONMOUSEOUT-Event occurs, if the mouse pointer
        is moved from the current element. A script can be stored in
        this attribute to be performed in the Event.
    :ivar onmouseover: The ONMOUSEOVER-Event occurs, if the mouse
        pointer is moved to the current element from another location
        outside it. A script can be stored in this attribute to be
        performed in the Event.
    :ivar onmouseup: The ONMOUSEUP-Event occurs if the mouse button used
        for clicking is released on the current element. A script can be
        stored in this attribute to be performed in the Event.
    :ivar shape: The shape of the area. Note that in HTML this is
        defaulted to RECT.
    :ivar style: Information on the associated style
    :ivar tabindex: This attribute specifies the position of the current
        element in tabbing-order for the corresponding document. The
        value shall lie between 0 and 32767. The Tabbing Order defines
        the sequence in which elements are focused on, when the user
        navigates using the keyboard.
    :ivar title: Title information of the Area element
    """

    class Meta:
        name = "AREA"

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
    accesskey: None | str = field(
        default=None,
        metadata={
            "name": "ACCESSKEY",
            "type": "Attribute",
        },
    )
    alt: None | str = field(
        default=None,
        metadata={
            "name": "ALT",
            "type": "Attribute",
        },
    )
    class_value: None | str = field(
        default=None,
        metadata={
            "name": "CLASS",
            "type": "Attribute",
        },
    )
    coords: None | str = field(
        default=None,
        metadata={
            "name": "COORDS",
            "type": "Attribute",
        },
    )
    href: None | str = field(
        default=None,
        metadata={
            "name": "HREF",
            "type": "Attribute",
        },
    )
    nohref: None | AreaEnumNohrefSimple = field(
        default=None,
        metadata={
            "name": "NOHREF",
            "type": "Attribute",
        },
    )
    onblur: None | str = field(
        default=None,
        metadata={
            "name": "ONBLUR",
            "type": "Attribute",
        },
    )
    onclick: None | str = field(
        default=None,
        metadata={
            "name": "ONCLICK",
            "type": "Attribute",
        },
    )
    ondblclick: None | str = field(
        default=None,
        metadata={
            "name": "ONDBLCLICK",
            "type": "Attribute",
        },
    )
    onfocus: None | str = field(
        default=None,
        metadata={
            "name": "ONFOCUS",
            "type": "Attribute",
        },
    )
    onkeydown: None | str = field(
        default=None,
        metadata={
            "name": "ONKEYDOWN",
            "type": "Attribute",
        },
    )
    onkeypress: None | str = field(
        default=None,
        metadata={
            "name": "ONKEYPRESS",
            "type": "Attribute",
        },
    )
    onkeyup: None | str = field(
        default=None,
        metadata={
            "name": "ONKEYUP",
            "type": "Attribute",
        },
    )
    onmousedown: None | str = field(
        default=None,
        metadata={
            "name": "ONMOUSEDOWN",
            "type": "Attribute",
        },
    )
    onmousemove: None | str = field(
        default=None,
        metadata={
            "name": "ONMOUSEMOVE",
            "type": "Attribute",
        },
    )
    onmouseout: None | str = field(
        default=None,
        metadata={
            "name": "ONMOUSEOUT",
            "type": "Attribute",
        },
    )
    onmouseover: None | str = field(
        default=None,
        metadata={
            "name": "ONMOUSEOVER",
            "type": "Attribute",
        },
    )
    onmouseup: None | str = field(
        default=None,
        metadata={
            "name": "ONMOUSEUP",
            "type": "Attribute",
        },
    )
    shape: None | AreaEnumShapeSimple = field(
        default=None,
        metadata={
            "name": "SHAPE",
            "type": "Attribute",
        },
    )
    style: None | str = field(
        default=None,
        metadata={
            "name": "STYLE",
            "type": "Attribute",
        },
    )
    tabindex: None | str = field(
        default=None,
        metadata={
            "name": "TABINDEX",
            "type": "Attribute",
        },
    )
    title: None | str = field(
        default=None,
        metadata={
            "name": "TITLE",
            "type": "Attribute",
        },
    )
