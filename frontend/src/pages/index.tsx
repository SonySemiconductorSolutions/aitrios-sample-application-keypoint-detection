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

import Head from 'next/head'
import { Box, Grid, Typography } from '@mui/material'
import { DeviceIdProvider } from '@/stores/deviceIdContext'
import { DeviceSelect } from '@/features/devices'
import { ResetState } from '@/features/reset'
import { ParameterProvider, ModelSelect, EditParameter, UpdateParameter } from '@/features/parameters'
import { StartInference } from '@/features/inferences'
import { KeypointDisplay } from '@/features/display'

export default function Home() {
  return (
    <>
      <Head>
        <title>Keypoint Detection</title>
        <meta name="description" content="Visualization tool by AITRIOS" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <DeviceIdProvider>
        <Box flexGrow={1} margin={3}>
          <Grid container spacing={1}>
            <Grid item xs>
              <DeviceSelect />
            </Grid>
            <Grid item justifyContent="flex-end">
              <ResetState />
            </Grid>
          </Grid>
        </Box>
        <Box flexGrow={1} margin={3}>
          <Grid container spacing={1}>
            <Grid item xs={12} md={4}>
              <Typography variant="overline">Command Parameter</Typography>
              <ParameterProvider>
                <Box>
                  <ModelSelect />
                </Box>
                <Box marginTop={1}>
                  <EditParameter />
                </Box>
                <Box marginTop={1}>
                  <UpdateParameter />
                </Box>
              </ParameterProvider>
              <Box marginTop={1}>
                <StartInference />
              </Box>
            </Grid>
            <Grid item xs={12} md={8}>
              <Typography variant="overline">Inference Result</Typography>
              <KeypointDisplay />
            </Grid>
          </Grid>
        </Box>
      </DeviceIdProvider>
    </>
  )
}
