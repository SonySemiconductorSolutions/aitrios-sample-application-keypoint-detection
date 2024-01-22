# automatically generated by the FlatBuffers compiler, do not modify

# namespace: SmartCamera

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MultiPoseData(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MultiPoseData()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsMultiPoseData(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # MultiPoseData
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # MultiPoseData
    def PoseList(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from SmartCamera.GeneralPose import GeneralPose
            obj = GeneralPose()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # MultiPoseData
    def PoseListLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # MultiPoseData
    def PoseListIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

def MultiPoseDataStart(builder):
    builder.StartObject(1)

def Start(builder):
    MultiPoseDataStart(builder)

def MultiPoseDataAddPoseList(builder, poseList):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(poseList), 0)

def AddPoseList(builder, poseList):
    MultiPoseDataAddPoseList(builder, poseList)

def MultiPoseDataStartPoseListVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartPoseListVector(builder, numElems: int) -> int:
    return MultiPoseDataStartPoseListVector(builder, numElems)

def MultiPoseDataEnd(builder):
    return builder.EndObject()

def End(builder):
    return MultiPoseDataEnd(builder)
