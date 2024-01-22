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

import TextField from '@mui/material/TextField'
import FormControl from '@mui/material/FormControl'
import { useParameter } from '@/features/parameters/stores/parameterContext'

export function EditParameter() {
  const { commandParam, fileName, setCommandParam } = useParameter()

  const handleChange = (value: string) => {
    setCommandParam(value)
  }

  return (
    <FormControl fullWidth>
      <TextField
        label={fileName}
        inputProps={{ style: { fontSize: '12px', lineHeight: '1.2' } }}
        multiline
        rows={23.3}
        value={commandParam}
        onChange={(event: React.ChangeEvent<HTMLInputElement>) => {
          handleChange(event.target.value)
        }}
      />
    </FormControl>
  )
}
