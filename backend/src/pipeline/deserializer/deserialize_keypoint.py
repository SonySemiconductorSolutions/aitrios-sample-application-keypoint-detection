"""
Copyright 2023 Sony Semiconductor Solutions Corp. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import sys
import os
import base64
from enum import Enum

sys.path.append(os.path.dirname(__file__))
from .SmartCamera import MultiPoseTop, Point2d


class KeyPointName(Enum):
    Nose = 0
    LeftEye = 1
    RightEye = 2
    LeftEar = 3
    RightEar = 4
    LeftShoulder = 5
    RightShoulder = 6
    LeftElbow = 7
    RightElbow = 8
    LeftWrist = 9
    RightWrist = 10
    LeftHip = 11
    RightHip = 12
    LeftKnee = 13
    RightKnee = 14
    LeftAnkle = 15
    RightAnkle = 16


def deserialize_keypoint(serialize_data):
    decoded_data = base64.b64decode(serialize_data)

    pose_list = []
    ppl_out = MultiPoseTop.MultiPoseTop.GetRootAsMultiPoseTop(decoded_data, 0)
    perception = ppl_out.Perception()
    for i in range(perception.PoseListLength()):
        keypoint_list = []
        general_pose = perception.PoseList(i)

        for j in range(general_pose.KeypointListLength()):
            pose = general_pose.KeypointList(j)
            point_2d = Point2d.Point2d()
            point_2d.Init(pose.Point().Bytes, pose.Point().Pos)

            keypoint_obj = {"point": {}}
            keypoint_obj["name"] = KeyPointName(pose.Name()).name
            keypoint_obj["point"].setdefault("x", point_2d.X())
            keypoint_obj["point"].setdefault("y", point_2d.Y())
            keypoint_list.append(keypoint_obj)

        person = {}
        person["score"] = general_pose.Score()
        person["keypoint_list"] = keypoint_list
        pose_list.append(person)

    return pose_list
