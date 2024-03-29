# automatically generated by the FlatBuffers compiler, do not modify

# namespace: SmartCamera

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class GeneralPose(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = GeneralPose()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsGeneralPose(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # GeneralPose
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # GeneralPose
    def Score(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # GeneralPose
    def KeypointList(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from SmartCamera.KeyPoint import KeyPoint
            obj = KeyPoint()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # GeneralPose
    def KeypointListLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # GeneralPose
    def KeypointListIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

def GeneralPoseStart(builder):
    builder.StartObject(2)

def Start(builder):
    GeneralPoseStart(builder)

def GeneralPoseAddScore(builder, score):
    builder.PrependFloat32Slot(0, score, 0.0)

def AddScore(builder, score):
    GeneralPoseAddScore(builder, score)

def GeneralPoseAddKeypointList(builder, keypointList):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(keypointList), 0)

def AddKeypointList(builder, keypointList):
    GeneralPoseAddKeypointList(builder, keypointList)

def GeneralPoseStartKeypointListVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartKeypointListVector(builder, numElems: int) -> int:
    return GeneralPoseStartKeypointListVector(builder, numElems)

def GeneralPoseEnd(builder):
    return builder.EndObject()

def End(builder):
    return GeneralPoseEnd(builder)
