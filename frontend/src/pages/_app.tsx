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

import type { AppProps } from 'next/app'

import { ThemeProvider } from '@mui/material/styles'
import { SpinnerProvider } from '@/hooks/useSpinner'
import { AlertProvider } from '@/hooks/useAlert'

import baseTheme from '@/styles/baseStyle'
import { Header, Footer } from '@/components/layouts'

export default function App({ Component, pageProps }: AppProps) {
  return (
    <ThemeProvider theme={baseTheme}>
      <SpinnerProvider>
        <AlertProvider>
          <Header mainTitle="Keypoint Detection" subTitle="Visualization App" />
          {/* eslint-disable-next-line react/jsx-props-no-spreading */}
          <Component {...pageProps} />
          <Footer />
        </AlertProvider>
      </SpinnerProvider>
    </ThemeProvider>
  )
}
