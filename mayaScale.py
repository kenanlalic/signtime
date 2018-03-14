import os
import maya.standalone
import maya.cmds as cmds


class mayaScale(object):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    maya_file_to_open = dir_path + "/views/simax.mb"
    scaledHeight = 0
    def __init__(self, y):
        maya.standalone.initialize("Python")
        cmds.file(self.maya_file_to_open, o=True)
        if cmds.objExists('myCube'):
            cmds.setAttr('myCube.scaleY', y)
        else:
            finalCube = cmds.polyCube(w = 1, h = 1, d = 1, n = 'myCube', ch = False)
        self.scaledHeight = cmds.getAttr('myCube.scaleY')
        cmds.file(force=True, save=True, type='mayaBinary')
        maya.standalone.uninitialize()

    def __del__(self):
        print("cleaning.....")
