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

import { Selector } from '@/components/elements/Selector'
import { useDeviceId } from '@/stores/deviceIdContext'
import { useAlert } from '@/hooks/useAlert'
import { useSpinner } from '@/hooks/useSpinner'

export function DeviceSelect() {
  const { openSpinner, closeSpinner } = useSpinner()
  const { showAlert } = useAlert()
  const { setDeviceId } = useDeviceId()
  const [devices, setDevices] = useState<string[]>([])

  useEffect(() => {
    openSpinner()
    axios
      .get('/devices')
      .then((response) => {
        if (response.status === 200) {
          if (Object.keys(response.data.devices).length === 0) {
            showAlert('Device not found.', 'error')
          } else {
            setDevices(response.data.devices)
          }
        }
      })
      .catch((error) => {
        if (error.response) {
          showAlert(error.response.data.message, 'error')
        }
      })
      .finally(() => {
        closeSpinner()
      })
  }, [])

  return (
    <Selector
      label="Device ID"
      items={devices}
      size="small"
      onSelect={(device: string) => {
        setDeviceId(device)
      }}
    />
  )
}
