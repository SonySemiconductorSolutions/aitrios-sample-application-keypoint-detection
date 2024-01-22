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

import InputLabel from '@mui/material/InputLabel'
import MenuItem from '@mui/material/MenuItem'
import FormControl from '@mui/material/FormControl'
import Select, { type SelectChangeEvent } from '@mui/material/Select'

interface Props {
  label: string
  items: string[]
  value?: string
  size?: 'small' | 'medium'
  onSelect: (value: string) => void
}

export function Selector({ label, items, value, size, onSelect }: Props) {
  const handleOnChange = (valueName: string) => {
    onSelect(valueName)
  }

  return (
    <FormControl fullWidth size={size}>
      <InputLabel>{label}</InputLabel>
      <Select
        label={label}
        value={value}
        onChange={(event: SelectChangeEvent) => {
          handleOnChange(event.target.value)
        }}
      >
        {items.map((item) => (
          <MenuItem key={item} value={item}>
            {item}
          </MenuItem>
        ))}
      </Select>
    </FormControl>
  )
}
