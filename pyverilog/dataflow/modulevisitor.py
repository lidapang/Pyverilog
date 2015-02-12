#-------------------------------------------------------------------------------
# modulevisitor.py
# 
# Module definition visitor
#
# Copyright (C) 2013, Shinya Takamaeda-Yamazaki
# License: Apache 2.0
#-------------------------------------------------------------------------------

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) )

import pyverilog.vparser.parser
from pyverilog.vparser.ast import *

if sys.version_info[0] >= 3:
    from pyverilog.dataflow.visit import *
else:
    from visit import *

class ModuleVisitor(NodeVisitor):
    def __init__(self):
        self.moduleinfotable = ModuleInfoTable()

    def visit_ModuleDef(self, node):
        self.moduleinfotable.addDefinition(node.name, node)
        self.generic_visit(node)

    def visit_Portlist(self, node):
        self.moduleinfotable.addPorts(node.ports)

    def visit_Input(self, node):
        self.moduleinfotable.addSignal(node.name, node)

    def visit_Output(self, node):
        self.moduleinfotable.addSignal(node.name, node)

    def visit_Inout(self, node):
        self.moduleinfotable.addSignal(node.name, node)

    def visit_Parameter(self, node):
        self.moduleinfotable.addConst(node.name, node)
        self.moduleinfotable.addParamName(node.name)

    def visit_Locaparam(self, node):
        self.moduleinfotable.addConst(node.name, node)

    # Skip Rule
    def visit_Function(self, node):
        pass

    def visit_Task(self, node):
        pass

    def visit_Always(self, node):
        pass

    def visit_Initial(self, node):
        pass

    def visit_InstanceList(self, node):
        pass

    def visit_Instance(self, node):
        pass

    def visit_Pragma(self, node):
        pass

    # get functions
    def get_modulenames(self):
        return self.moduleinfotable.get_names()

    def get_moduleinfotable(self):
        return self.moduleinfotable
