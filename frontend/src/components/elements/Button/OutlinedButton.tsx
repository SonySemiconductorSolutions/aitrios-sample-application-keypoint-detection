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

import { ReactNode } from 'react'
import Button from '@mui/material/Button'
import ButtonGroup from '@mui/material/ButtonGroup'

interface Props {
  sx?: object
  color?: 'inherit' | 'primary' | 'secondary' | 'success' | 'error' | 'info' | 'warning'
  onClick: () => void
  children: ReactNode
}

export function OutlinedButton({ sx, color, onClick, children }: Props) {
  const hundleOnClick = () => {
    onClick()
  }

  return (
    <ButtonGroup fullWidth>
      <Button
        variant="outlined"
        sx={sx}
        color={color}
        onClick={() => {
          hundleOnClick()
        }}
      >
        {children}
      </Button>
    </ButtonGroup>
  )
}
