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

import axios from '@/utils/axios'
import { ContainedButton } from '@/components/elements/Button'
import { useAlert } from '@/hooks/useAlert'
import { useSpinner } from '@/hooks/useSpinner'
import { useParameter } from '@/features/parameters/stores/parameterContext'

export function UpdateParameter() {
  const { openSpinner, closeSpinner } = useSpinner()
  const { showAlert } = useAlert()

  const { commandParam, fileName } = useParameter()

  const hundleClick = () => {
    openSpinner()

    // JSON format validation
    try {
      JSON.parse(commandParam)
    } catch (e) {
      showAlert('Commnd Parameter must be written in correct JSON format.', 'error')
      closeSpinner()
      return
    }

    axios
      .put(`/command_parameter_file/${fileName}`, {
        command_param: commandParam,
      })
      .then((response) => {
        if (response.status === 200) {
          showAlert('Command Parameter binded successfully.', 'success')
        }
      })
      .catch((error) => {
        if (error.response) showAlert(error.response.data.message, 'error')
      })
      .finally(() => {
        closeSpinner()
      })
  }

  return <ContainedButton onClick={() => hundleClick()}>Bind Command Parameter</ContainedButton>
}
