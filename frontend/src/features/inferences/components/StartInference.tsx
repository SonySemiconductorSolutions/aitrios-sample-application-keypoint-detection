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

import { useState, useEffect } from 'react'
import axios from '@/utils/axios'
import { ContainedButton } from '@/components/elements/Button'
import { useDeviceId } from '@/stores/deviceIdContext'
import { useAlert } from '@/hooks/useAlert'
import { useSpinner } from '@/hooks/useSpinner'

export function StartInference() {
  const { openSpinner, closeSpinner } = useSpinner()
  const { showAlert } = useAlert()
  const { deviceId } = useDeviceId()
  const [isReceiving, setIsReceiving] = useState<boolean>(false)

  useEffect(() => {
    if (deviceId !== '') {
      axios
        .post(`/devices/${deviceId}/stop_processing`)
        .then(() => {
          setIsReceiving(false)
        })
    }
  }, [deviceId])

  const hundleClick = () => {
    openSpinner()
    if (!isReceiving) {
      axios
        .post(`/devices/${deviceId}/start_processing`)
        .then((response) => {
          if (response.status === 200) {
            showAlert(response.data.message, 'success')
          }
          setIsReceiving(true)
        })
        .catch((error) => {
          if (error.response) {
            showAlert(error.response.data.message, 'error')
          }
        })
        .finally(() => {
          closeSpinner()
        })
    } else {
      axios
        .post(`/devices/${deviceId}/stop_processing`)
        .then((response) => {
          if (response.status === 200) {
            showAlert(response.data.message, 'success')
          }
          setIsReceiving(false)
        })
        .catch((error) => {
          if (error.response) {
            showAlert(error.response.data.message, 'error')
          }
        })
        .finally(() => {
          closeSpinner()
        })
    }
  }

  return (
    <ContainedButton
      color={isReceiving ? 'success' : 'primary'}
      onClick={() => {
        hundleClick()
      }}
      disabled={false}
    >
      {isReceiving ? 'Stop Inference' : 'Start Inference'}
    </ContainedButton>
  )
}
