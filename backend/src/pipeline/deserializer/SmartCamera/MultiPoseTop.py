# automatically generated by the FlatBuffers compiler, do not modify

# namespace: SmartCamera

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MultiPoseTop(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MultiPoseTop()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsMultiPoseTop(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # MultiPoseTop
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # MultiPoseTop
    def Perception(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from SmartCamera.MultiPoseData import MultiPoseData
            obj = MultiPoseData()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def MultiPoseTopStart(builder):
    builder.StartObject(1)

def Start(builder):
    MultiPoseTopStart(builder)

def MultiPoseTopAddPerception(builder, perception):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(perception), 0)

def AddPerception(builder, perception):
    MultiPoseTopAddPerception(builder, perception)

def MultiPoseTopEnd(builder):
    return builder.EndObject()

def End(builder):
    return MultiPoseTopEnd(builder)
