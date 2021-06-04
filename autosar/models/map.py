from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.area import Area

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class Map:
    """Image maps enable authors to specify regions of an image or object and
    assign a specific action to each region (e.g., retrieve a document, run a
    program, etc.) When the region is activated by the user, the action is
    executed.

    The class follows the html approach and is intended to support
    interactive documents.

    :ivar area: This element specifies a region in an image map. Image
        maps enable authors to specify regions in an object (e.g. a
        graphic) and to assign a specific activity to each region (e.g.
        load a document, launch a program etc.).
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
    :ivar class_value: This attribute assigns a class name or set of
        class names to an element. Any number of elements may be
        assigned the same class name or set of class names. Multiple
        class names shall be separated by white space characters. Class
        names are typically used to apply CSS formatting rules to an
        element.
    :ivar name: This attribute assigns a name to the image map in the
        MAP element. This name can be used to be referenced in an HTML
        image through the attribute USEMAP. Although this is not
        actually necessary in the MSR model, it was inserted in order to
        support the MAPs which were created for HTML.
    :ivar onclick: The ONCLICK-Event occurs, if the current element is
        clicked on. A script can be stored in this attribute to be
        performed in the Event.
    :ivar ondblclick: The ONDBLCLICK-Event occurs, if the current Event
        is "double" clicked-on.  A script can be stored in this
        attribute to be performed in the Event.
    :ivar onkeydown: The ONKEYDOWN-Event occurs, if a button on the
        current element is pressed down.   A script can be stored in
        this attribute to be performed in the event.
    :ivar onkeypress: The ONKEYPRESS-Event occurs, if a button on the
        current element is pressed down and released.   A script can be
        stored in this attribute to be performed in the Event.
    :ivar onkeyup: The ONKEYUP-Event occurs, if a button on the current
        element is released.   A script can be stored in this attribute
        to be performed in the Event.
    :ivar onmousedown: The ONMOUSEDOWN-Event occurs, if the mouse button
        used for clicking is held down on the current element.   A
        script can be stored in this attribute to be performed in the
        Event.
    :ivar onmousemove: The ONMOUSEMOVE-Event occurs, if the mouse
        pointer is moved on the current  element (i.e. it is located on
        the current element).   A script can be stored in this attribute
        to be performed in the Event.
    :ivar onmouseout: The ONMOUSEOUT-Event occurs, if the mouse pointer
        is moved from the current element.  A script can be stored in
        this attribute to be performed in the Event.
    :ivar onmouseover: The ONMOUSEOVER-Event occurs, if the mouse
        pointer is moved to the current element from another location
        outside it.   A script can be stored in this attribute to be
        performed in the Event.
    :ivar onmouseup: The ONMOUSEUP-Event occurs if the mouse button used
        for clicking is released on the current element.   A script can
        be stored in this attribute to be performed in the Event.
    :ivar style: This attribute specifies formatting style information
        for the current element. The content of this attribute is called
        inline CSS. The style attribute is deprecated (considered
        outdated), because it fuses together content and formatting.
    :ivar title: This attribute offers advisory information. Some Web
        browsers will display this information as tooltips. Authoring
        tools may make this information available to users as additional
        information about the element.
    """
    class Meta:
        name = "MAP"

    area: List[Area] = field(
        default_factory=list,
        metadata={
            "name": "AREA",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        }
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        }
    )
    class_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "CLASS",
            "type": "Attribute",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "NAME",
            "type": "Attribute",
        }
    )
    onclick: Optional[str] = field(
        default=None,
        metadata={
            "name": "ONCLICK",
            "type": "Attribute",
        }
    )
    ondblclick: Optional[str] = field(
        default=None,
        metadata={
            "name": "ONDBLCLICK",
            "type": "Attribute",
        }
    )
    onkeydown: Optional[str] = field(
        default=None,
        metadata={
            "name": "ONKEYDOWN",
            "type": "Attribute",
        }
    )
    onkeypress: Optional[str] = field(
        default=None,
        metadata={
            "name": "ONKEYPRESS",
            "type": "Attribute",
        }
    )
    onkeyup: Optional[str] = field(
        default=None,
        metadata={
            "name": "ONKEYUP",
            "type": "Attribute",
        }
    )
    onmousedown: Optional[str] = field(
        default=None,
        metadata={
            "name": "ONMOUSEDOWN",
            "type": "Attribute",
        }
    )
    onmousemove: Optional[str] = field(
        default=None,
        metadata={
            "name": "ONMOUSEMOVE",
            "type": "Attribute",
        }
    )
    onmouseout: Optional[str] = field(
        default=None,
        metadata={
            "name": "ONMOUSEOUT",
            "type": "Attribute",
        }
    )
    onmouseover: Optional[str] = field(
        default=None,
        metadata={
            "name": "ONMOUSEOVER",
            "type": "Attribute",
        }
    )
    onmouseup: Optional[str] = field(
        default=None,
        metadata={
            "name": "ONMOUSEUP",
            "type": "Attribute",
        }
    )
    style: Optional[str] = field(
        default=None,
        metadata={
            "name": "STYLE",
            "type": "Attribute",
        }
    )
    title: Optional[str] = field(
        default=None,
        metadata={
            "name": "TITLE",
            "type": "Attribute",
        }
    )
