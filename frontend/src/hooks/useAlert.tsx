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

/* eslint react/destructuring-assignment: 0 */
/* eslint @typescript-eslint/no-unused-vars: 0 */

import { createContext, useState, type ReactNode, useMemo, useContext, useCallback } from 'react'
import { type AlertColor } from '@mui/material/Alert'

import { Alert } from '@/components/elements/Alert'

interface Props {
  children: ReactNode
}

interface ContextType {
  message: string
  severity: AlertColor
  showAlert: (message: string, severity: AlertColor) => void
}

export const AlertContext = createContext<ContextType>({
  message: '',
  severity: 'error',
  showAlert: (_message: string, _severity: AlertColor) => {},
} as ContextType)

export function AlertProvider({ children }: Props) {
  const context: ContextType = useContext(AlertContext)
  const [message, setMessage] = useState<string>(context.message)
  const [severity, setSeverity] = useState<AlertColor>(context.severity)

  const contextValue = useMemo(
    () => ({
      message,
      severity,
      showAlert: (_message: string, _severity: AlertColor) => {
        setMessage(_message)
        setSeverity(_severity)
      },
    }),
    [message, severity, setMessage, setSeverity],
  )

  const handleClose = useCallback(() => {
    setMessage('')
  }, [setMessage])

  return (
    <AlertContext.Provider value={contextValue}>
      {children}
      <Alert
        open={contextValue.message !== ''}
        message={contextValue.message}
        severity={contextValue.severity}
        onClose={handleClose}
      />
    </AlertContext.Provider>
  )
}

export function useAlert(): ContextType {
  return useContext(AlertContext)
}
