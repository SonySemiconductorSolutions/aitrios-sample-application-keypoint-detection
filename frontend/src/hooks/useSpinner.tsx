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

import { createContext, useState, type ReactNode, useMemo, useContext } from 'react'

import { Spinner } from '@/components/elements/Spinner'

interface Props {
  children: ReactNode
}

interface ContextType {
  open: boolean
  openSpinner: () => void
  closeSpinner: () => void
}

const SpinnerContext = createContext<ContextType>({ open: false } as ContextType)

export function SpinnerProvider({ children }: Props) {
  const context: ContextType = useContext(SpinnerContext)
  const [open, setOpen] = useState<boolean>(context.open)

  const contextValue = useMemo(
    () => ({
      open,
      openSpinner: () => {
        setOpen(true)
      },
      closeSpinner: () => {
        setOpen(false)
      },
    }),
    [open, setOpen],
  )

  return (
    <SpinnerContext.Provider value={contextValue}>
      {children}
      <Spinner open={contextValue.open} />
    </SpinnerContext.Provider>
  )
}

export function useSpinner(): ContextType {
  return useContext(SpinnerContext)
}
