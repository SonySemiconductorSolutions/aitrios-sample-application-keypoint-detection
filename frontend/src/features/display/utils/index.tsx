/*
 * Copyright 2023 Sony Semiconductor Solutions Corp. All rights reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import { type PoseData } from '../types'

const getContext = () => {
  const canvasId = `canvas`
  const canvas = document.getElementById(canvasId) as HTMLCanvasElement
  const baseContext = canvas.getContext('2d')
  if (baseContext == null) return -1

  return baseContext
}

export const resetCanvas = () => {
  const baseContext = getContext()
  if (baseContext === -1) return

  baseContext.clearRect(0, 0, baseContext.canvas.clientWidth, baseContext.canvas.clientHeight)
  baseContext.strokeStyle = 'rgb(200, 200, 200)'
  baseContext.strokeRect(0, 0, 640, 480)
}

export const drawKeypoints = (results: PoseData[]) => {
  const baseContext = getContext()
  if (baseContext === -1) return

  results.forEach((result: PoseData) => {
    const { keypoint_list: keypointDict, score } = result
    baseContext.lineWidth = 2

    // Head
    const Nose = keypointDict.find((e) => e.name === 'Nose')?.point
    const LeftEye = keypointDict.find((e) => e.name === 'LeftEye')?.point
    const RightEye = keypointDict.find((e) => e.name === 'RightEye')?.point
    const LeftEar = keypointDict.find((e) => e.name === 'LeftEar')?.point
    const RightEar = keypointDict.find((e) => e.name === 'RightEar')?.point

    baseContext.fillStyle = 'green'
    baseContext.fillRect(LeftEye!.x - 2, LeftEye!.y - 2, 4, 4)
    baseContext.fillRect(RightEye!.x - 2, RightEye!.y - 2, 4, 4)
    baseContext.fillRect(Nose!.x - 2, Nose!.y - 2, 4, 4)
    baseContext.fillRect(LeftEar!.x - 2, LeftEar!.y - 2, 4, 4)
    baseContext.fillRect(RightEar!.x - 2, RightEar!.y - 2, 4, 4)

    // Draw posibility score
    baseContext.font = '15px Arial'
    baseContext.textBaseline = 'bottom'
    baseContext.textAlign = 'center'
    baseContext.fillText(`${score}`, Nose!.x, Nose!.y - 12)

    // Arm
    const LeftShoulder = keypointDict.find((e) => e.name === 'LeftShoulder')?.point
    const RightShoulder = keypointDict.find((e) => e.name === 'RightShoulder')?.point
    const LeftElbow = keypointDict.find((e) => e.name === 'LeftElbow')?.point
    const RightElbow = keypointDict.find((e) => e.name === 'RightElbow')?.point
    const LeftWrist = keypointDict.find((e) => e.name === 'LeftWrist')?.point
    const RightWrist = keypointDict.find((e) => e.name === 'RightWrist')?.point

    baseContext.fillStyle = 'dodgerblue'
    baseContext.fillRect(LeftWrist!.x - 2, LeftWrist!.y - 2, 4, 4)
    baseContext.fillRect(LeftElbow!.x - 2, LeftElbow!.y - 2, 4, 4)
    baseContext.fillRect(LeftShoulder!.x - 2, LeftShoulder!.y - 2, 4, 4)
    baseContext.fillRect(RightShoulder!.x - 2, RightShoulder!.y - 2, 4, 4)
    baseContext.fillRect(RightElbow!.x - 2, RightElbow!.y - 2, 4, 4)
    baseContext.fillRect(RightWrist!.x - 2, RightWrist!.y - 2, 4, 4)

    baseContext.beginPath()
    baseContext.strokeStyle = 'dodgerblue'
    baseContext.moveTo(LeftWrist!.x, LeftWrist!.y)
    baseContext.lineTo(LeftElbow!.x, LeftElbow!.y)
    baseContext.lineTo(LeftShoulder!.x, LeftShoulder!.y)
    baseContext.lineTo(RightShoulder!.x, RightShoulder!.y)
    baseContext.lineTo(RightElbow!.x, RightElbow!.y)
    baseContext.lineTo(RightWrist!.x, RightWrist!.y)
    baseContext.stroke()
    baseContext.closePath()

    // Leg
    const LeftHip = keypointDict.find((e) => e.name === 'LeftHip')?.point
    const RightHip = keypointDict.find((e) => e.name === 'RightHip')?.point
    const LeftKnee = keypointDict.find((e) => e.name === 'LeftKnee')?.point
    const RightKnee = keypointDict.find((e) => e.name === 'RightKnee')?.point
    const LeftAnkle = keypointDict.find((e) => e.name === 'LeftAnkle')?.point
    const RightAnkle = keypointDict.find((e) => e.name === 'RightAnkle')?.point

    baseContext.fillStyle = 'darkorange'
    baseContext.fillRect(LeftAnkle!.x - 2, LeftAnkle!.y - 2, 4, 4)
    baseContext.fillRect(LeftKnee!.x - 2, LeftKnee!.y - 2, 4, 4)
    baseContext.fillRect(LeftHip!.x - 2, LeftHip!.y - 2, 4, 4)
    baseContext.fillRect(RightHip!.x - 2, RightHip!.y - 2, 4, 4)
    baseContext.fillRect(RightKnee!.x - 2, RightKnee!.y - 2, 4, 4)
    baseContext.fillRect(RightAnkle!.x - 2, RightAnkle!.y - 2, 4, 4)

    baseContext.beginPath()
    baseContext.strokeStyle = 'darkorange'
    baseContext.moveTo(LeftAnkle!.x, LeftAnkle!.y)
    baseContext.lineTo(LeftKnee!.x, LeftKnee!.y)
    baseContext.lineTo(LeftHip!.x, LeftHip!.y)
    baseContext.moveTo(RightHip!.x, RightHip!.y)
    baseContext.lineTo(RightKnee!.x, RightKnee!.y)
    baseContext.lineTo(RightAnkle!.x, RightAnkle!.y)
    baseContext.stroke()
    baseContext.closePath()

    // Body
    baseContext.beginPath()
    baseContext.strokeStyle = 'darkviolet'
    baseContext.moveTo(LeftShoulder!.x, LeftShoulder!.y)
    baseContext.lineTo(LeftHip!.x, LeftHip!.y)
    baseContext.lineTo(RightHip!.x, RightHip!.y)
    baseContext.lineTo(RightShoulder!.x, RightShoulder!.y)
    baseContext.stroke()
    baseContext.closePath()
  })
}

export const formatTimestampString = (timestamp: string) => {
  if (timestamp === '') return ''

  // 20230801093912345 -> 2023/08/01 09:39:12.345
  const timestampString = timestamp.toString()
  const year = timestampString.slice(0, 4)
  const month = timestampString.slice(4, 6)
  const day = timestampString.slice(6, 8)
  const hour = timestampString.slice(8, 10)
  const min = timestampString.slice(10, 12)
  const sec = timestampString.slice(12, 14)
  const milisec = timestampString.slice(14, 17)
  const timestampText = `${year}/${month}/${day} ${hour}:${min}:${sec}.${milisec}`

  return timestampText
}
