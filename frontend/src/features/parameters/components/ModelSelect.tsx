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

import { useEffect, useState } from 'react'
import { Selector } from '@/components/elements/Selector'
import { useParameter } from '@/features/parameters/stores/parameterContext'

export function ModelSelect() {
  const [model, setModel] = useState<string>('')
  const { commandParam, setCommandParam, models } = useParameter()

  useEffect(() => {
    if (commandParam === '') {
      setModel('')
    } else {
      try {
        const tempParam = JSON.parse(commandParam)
        const modelId = tempParam.commands[0].parameters.ModelId
        setModel(modelId)
      } catch (e) {
        // Go through if JSON.parse() cannot be done
      }
    }
  }, [commandParam])

  const handleInputChange = (modelId: string) => {
    try {
      const tempParam = JSON.parse(commandParam)
      tempParam.commands[0].parameters.ModelId = modelId

      setCommandParam(JSON.stringify(tempParam, null, 2))
      setModel(modelId)
    } catch (e) {
      // Go through if JSON.parse() cannot be done
    }
  }

  return (
    <Selector
      label="Models"
      items={models}
      value={model}
      size="small"
      onSelect={(modelId: string) => handleInputChange(modelId)}
    />
  )
}
