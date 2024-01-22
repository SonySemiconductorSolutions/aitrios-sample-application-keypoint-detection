#!/usr/bin/env bash
# Copyright 2022 Sony Semiconductor Solutions Corp. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

set -ex

# Extract abs. path
DIR="$(cd "$(dirname "${BASH_SOURCE:-"${0}"}")" && pwd -P)"
BASE_DIR="$(cd ${DIR}/../ && pwd -P)"

# Setup frontend env
ENVFILE=".env.development"
pushd ${BASE_DIR}/frontend >/dev/null 2>&1
sed -i '2,3d' $ENVFILE
echo "NEXT_PUBLIC_CODESPACES=$CODESPACES" >> $ENVFILE
echo "NEXT_PUBLIC_CODESPACE_NAME=$CODESPACE_NAME" >> $ENVFILE
# Exclude .env.development file from git staging
git update-index --skip-worktree $ENVFILE
popd >/dev/null 2>&1

# Install dependencies required to run tutorials in Jupyter Notebook
pushd ${BASE_DIR}/tutorial >/dev/null 2>&1
pip install -r requirements.txt
popd >/dev/null 2>&1

exit 0