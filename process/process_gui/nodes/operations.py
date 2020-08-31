from PyQt5.QtCore import *
from process.process_gui.process_conf import *
from process.process_gui.process_node_base import *
from node_editor.utils import dumpException


@register_node(OP_NODE_CLICK)
class ProcessNode_Click(ProcessNode):
    icon = ""
    op_code = OP_NODE_CLICK
    op_title = "Click"
    content_label = ""
    content_label_objname = "calc_node_bg"


@register_node(OP_NODE_WAIT)
class ProcessNode_Wait(ProcessNode):
    icon = ""
    op_code = OP_NODE_WAIT
    op_title = "Wait"
    content_label = ""
    content_label_objname = "calc_node_bg"


@register_node(OP_NODE_URL)
class ProcessNode_Url(ProcessNode):
    icon = ""
    op_code = OP_NODE_URL
    op_title = "Open Url"
    content_label = ""
    content_label_objname = "calc_node_url"


@register_node(OP_NODE_READ)
class ProcessNode_Read(ProcessNode):
    icon = ""
    op_code = OP_NODE_READ
    op_title = "Read"
    content_label = ""
    content_label_objname = "calc_node_read"


