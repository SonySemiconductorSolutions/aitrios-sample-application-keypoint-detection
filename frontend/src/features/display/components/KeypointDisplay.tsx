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

import { useState, useEffect, type MouseEvent } from 'react'
import socketIOClient from 'socket.io-client'
import Box from '@mui/material/Box'
import Paper from '@mui/material/Paper'
import IconButton from '@mui/material/IconButton'
import DataObjectIcon from '@mui/icons-material/DataObject'
import Popover from '@mui/material/Popover'
import Typography from '@mui/material/Typography'

import baseURL from '@/config/backendConfig'
import { useDeviceId } from '@/stores/deviceIdContext'
import { type InferenceResult } from '../types'
import { resetCanvas, drawKeypoints, formatTimestampString } from '../utils'

export function KeypointDisplay() {
  const { deviceId } = useDeviceId()
  const [anchorElement, setAnchorElement] = useState<HTMLButtonElement | null>(null)
  const [timestamp, setTimestamp] = useState<string>('')
  const [inferenceResult, setInferenceResult] = useState<InferenceResult>({
    timestamp: '',
    inference_data: [],
  } as InferenceResult)

  useEffect(() => {
    resetCanvas()
    setTimestamp('')
  }, [deviceId])

  useEffect(() => {
    resetCanvas()
    drawKeypoints(inferenceResult.inference_data)
    setTimestamp(formatTimestampString(inferenceResult.timestamp))
  }, [inferenceResult])

  useEffect(() => {
    const socket = socketIOClient(baseURL)
    socket.on('processed_data', (message: InferenceResult) => {
      setInferenceResult(message)
    })

    return () => {
      socket.disconnect()
    }
  }, [])

  const handleIconClick = (event: MouseEvent<HTMLButtonElement>) => {
    setAnchorElement(event.currentTarget)
  }

  const handleIconClose = () => {
    setAnchorElement(null)
  }

  return (
    <Paper variant="outlined" sx={{ borderColor: 'grey.400', position: 'relative' }}>
      <Box margin={1} display="flex" justifyContent="center" alignItems="center">
        <canvas id="canvas" height="480" width="640" />
        <Box sx={{ top: 0, position: 'absolute', width: '100%', background: 'rgba(0,0,0,0.1)' }}>
          <IconButton
            onClick={(event) => {
              handleIconClick(event)
            }}
          >
            <DataObjectIcon />
          </IconButton>
          <Popover
            open={anchorElement !== null}
            anchorEl={anchorElement}
            onClose={handleIconClose}
            anchorOrigin={{
              vertical: 'center',
              horizontal: 'right',
            }}
          >
            <Box padding={2}>
              <pre>{JSON.stringify(inferenceResult.inference_data, null, 2)}</pre>
            </Box>
          </Popover>
          <Typography sx={{ display: 'inline', verticalAlign: 'middle' }}>{timestamp}</Typography>
        </Box>
      </Box>
    </Paper>
  )
}
