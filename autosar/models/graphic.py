from __future__ import annotations

from dataclasses import dataclass, field

from .graphic_fit_enum_simple import GraphicFitEnumSimple
from .graphic_notation_enum_simple import GraphicNotationEnumSimple
from .nmtoken_string import NmtokenString
from .revision_label_string import RevisionLabelString

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class Graphic:
    """
    This class represents an artifact containing the image to be inserted
    in the document.

    :ivar short_label: This is the short name of the engineering object.
        Note that it is modeled as NameToken and not as Identifier since
        in ASAM-CC it is also a NameToken.
    :ivar category: This denotes the role of the engineering object in
        the development cycle. Categories are such as * SWSRC for source
        code * SWOBJ for object code * SWHDR for a C-header file Further
        roles need to be defined via Methodology.
    :ivar revision_labels:
    :ivar domain: This denotes the domain in which the engineering
        object is stored. This allows to indicate various segments in
        the repository keeping the engineering objects. The domain may
        segregate companies, as well as automotive domains. Details need
        to be defined by the Methodology. Attribute is optional to
        support a default domain.
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
    :ivar edit_height: Specifies the height of the graphic when it is
        displayed in an editor. The unit can be added to the number in
        the string. Possible units are: cm, mm, px, pt. The default unit
        is px.
    :ivar edit_width: Specifies the width of the graphic when it is
        displayed in an editor. The unit can be added to the number in
        the string. Possible units are: cm, mm, px, pt. The default unit
        is px.
    :ivar editfit: Specifies how the graphic shall be displayed in an
        editor. If the attribute is missing,
    :ivar editscale: Set the proportional scale when displayed in an
        editor.
    :ivar filename: Name of the file that should be displayed. This
        attribute is supported in ASAM FSX and kept in AUTOSAR in order
        to support cut and paste.
    :ivar fit: It determines the way in which the graphic should be
        inserted. Enter the attribute value "AS-IS" , to insert a
        graphic in its original dimensions. The graphic is adapted, if
        it is too big for the space for which it was intended. Default
        is "AS-IS"
    :ivar generator: This attribute specifies the generator which is
        used to generate the image. Use case is that when editing a
        documentation, a figure (to be delivered by the  modeling tool)
        is inserted by the authoring tool as reference (this is the role
        of graphic). But the real figure maybe injected during document
        processing. To  be able to recognize this situation, this
        attribute can be applied.
    :ivar height: Define the displayed height of the figure. The unit
        can be added to the number in the string. Possible units are:
        cm, mm, px, pt. The default unit is px.
    :ivar html_fit: How to fit the graphic in an online media. Default
        is AS-IS.
    :ivar html_height: Specifies the height of the graphic when it is
        displayed online. The unit can be added to the number in the
        string. Possible units are: cm, mm, px, pt. The default unit is
        px.
    :ivar html_scale: Set the proportional scale when displayed online.
    :ivar html_width: Specifies the width of the graphic when it is
        displayed online. The unit can be added to the number in the
        string. Possible units are: cm, mm, px, pt. The default unit is
        px.
    :ivar notation: This attribute captures the format used to represent
        the graphic.
    :ivar scale: In this element the dimensions of the graphic can be
        altered proportionally.
    :ivar width: Define the displayed width of the figure. The unit can
        be added to the number in the string. Possible units are: cm,
        mm, px, pt. The default unit is px.
    """

    class Meta:
        name = "GRAPHIC"

    short_label: None | NmtokenString = field(
        default=None,
        metadata={
            "name": "SHORT-LABEL",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    category: None | NmtokenString = field(
        default=None,
        metadata={
            "name": "CATEGORY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    revision_labels: None | Graphic.RevisionLabels = field(
        default=None,
        metadata={
            "name": "REVISION-LABELS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    domain: None | NmtokenString = field(
        default=None,
        metadata={
            "name": "DOMAIN",
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
    edit_height: None | str = field(
        default=None,
        metadata={
            "name": "EDIT-HEIGHT",
            "type": "Attribute",
        },
    )
    edit_width: None | str = field(
        default=None,
        metadata={
            "name": "EDIT-WIDTH",
            "type": "Attribute",
        },
    )
    editfit: None | GraphicFitEnumSimple = field(
        default=None,
        metadata={
            "name": "EDITFIT",
            "type": "Attribute",
        },
    )
    editscale: None | str = field(
        default=None,
        metadata={
            "name": "EDITSCALE",
            "type": "Attribute",
        },
    )
    filename: None | str = field(
        default=None,
        metadata={
            "name": "FILENAME",
            "type": "Attribute",
        },
    )
    fit: None | GraphicFitEnumSimple = field(
        default=None,
        metadata={
            "name": "FIT",
            "type": "Attribute",
        },
    )
    generator: None | str = field(
        default=None,
        metadata={
            "name": "GENERATOR",
            "type": "Attribute",
        },
    )
    height: None | str = field(
        default=None,
        metadata={
            "name": "HEIGHT",
            "type": "Attribute",
        },
    )
    html_fit: None | GraphicFitEnumSimple = field(
        default=None,
        metadata={
            "name": "HTML-FIT",
            "type": "Attribute",
        },
    )
    html_height: None | str = field(
        default=None,
        metadata={
            "name": "HTML-HEIGHT",
            "type": "Attribute",
        },
    )
    html_scale: None | str = field(
        default=None,
        metadata={
            "name": "HTML-SCALE",
            "type": "Attribute",
        },
    )
    html_width: None | str = field(
        default=None,
        metadata={
            "name": "HTML-WIDTH",
            "type": "Attribute",
        },
    )
    notation: None | GraphicNotationEnumSimple = field(
        default=None,
        metadata={
            "name": "NOTATION",
            "type": "Attribute",
        },
    )
    scale: None | str = field(
        default=None,
        metadata={
            "name": "SCALE",
            "type": "Attribute",
        },
    )
    width: None | str = field(
        default=None,
        metadata={
            "name": "WIDTH",
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class RevisionLabels:
        """
        :ivar revision_label: This is a revision label denoting a
            particular version of the engineering object.
        """

        revision_label: list[RevisionLabelString] = field(
            default_factory=list,
            metadata={
                "name": "REVISION-LABEL",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
