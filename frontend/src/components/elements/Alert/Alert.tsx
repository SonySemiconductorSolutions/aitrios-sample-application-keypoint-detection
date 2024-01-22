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

import Snackbar from '@mui/material/Snackbar'
import AlertComponent, { type AlertColor } from '@mui/material/Alert'

interface Props {
  open: boolean
  message: string
  severity: AlertColor
  onClose: () => void
}

export function Alert({ open, message, severity, onClose }: Props) {
  return (
    <Snackbar
      open={open}
      autoHideDuration={6000}
      onClose={onClose}
      anchorOrigin={{ vertical: 'bottom', horizontal: 'center' }}
    >
      <AlertComponent variant="outlined" severity={severity} sx={{ bgcolor: 'background.paper' }}>
        {message}
      </AlertComponent>
    </Snackbar>
  )
}
