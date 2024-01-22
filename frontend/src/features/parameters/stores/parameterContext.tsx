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

import { createContext, useState, useEffect, useMemo, type ReactNode, useContext } from 'react'
import axios from '@/utils/axios'
import { useDeviceId } from '@/stores/deviceIdContext'
import { useAlert } from '@/hooks/useAlert'
import { useSpinner } from '@/hooks/useSpinner'

interface Props {
  children: ReactNode
}

interface ContextType {
  commandParam: string
  setCommandParam: (value: string) => void
  fileName: string
  setFileName: (value: string) => void
  models: string[]
  setModels: (value: string[]) => void
}

const ParameterContext = createContext<ContextType>({} as ContextType)

export function ParameterProvider({ children }: Props) {
  const { openSpinner, closeSpinner } = useSpinner()
  const { showAlert } = useAlert()
  const { deviceId } = useDeviceId()

  const [commandParam, setCommandParam] = useState<string>('')
  const [fileName, setFileName] = useState<string>('')
  const [models, setModels] = useState<string[]>([])

  const getData = () => {
    const data = {
      command_parameter: '',
      file_name: '',
      models: [],
    }
    return Promise.all([
      axios.get(`/devices/${deviceId}/command_parameter_file`),
      axios.get(`/devices/${deviceId}/models`),
    ])
      .then(([commandParamResponse, modelsResponse]) => {
        data.command_parameter = JSON.stringify(commandParamResponse.data.command_parameter, null, 2)
        data.file_name = commandParamResponse.data.file_name
        data.models = modelsResponse.data.models

        return Promise.resolve(data)
      })
      .catch((error) => {
        if (error.response) {
          showAlert(error.response.data.message, 'error')
        } else if (error.request) {
          showAlert(error.request, 'error')
        } else {
          showAlert(error.message, 'error')
        }
        return Promise.resolve(data)
      })
  }

  useEffect(() => {
    if (deviceId === '') {
      setCommandParam('')
      setFileName('')
      setModels([])
    } else {
      const asyncData = async () => {
        openSpinner()
        const data = await getData()
        setCommandParam(data.command_parameter)
        setFileName(data.file_name)
        if (Object.keys(data.models).length === 0) {
          showAlert('No model deployed on the device.', 'error')
        } else {
          setModels(data.models)
        }
        closeSpinner()
      }
      asyncData()
    }
  }, [deviceId])

  const paramContextValue = useMemo(
    () => ({ commandParam, fileName, models, setCommandParam, setFileName, setModels }),
    [commandParam, fileName, models, setCommandParam, setFileName, setModels],
  )

  return <ParameterContext.Provider value={paramContextValue}>{children}</ParameterContext.Provider>
}

export function useParameter(): ContextType {
  return useContext(ParameterContext)
}
