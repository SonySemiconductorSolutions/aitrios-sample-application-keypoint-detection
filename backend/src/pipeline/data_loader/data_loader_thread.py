"""
Copyright 2023 Sony Semiconductor Solutions Corp. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import threading
from collections import deque

from .console_data_loader import ConsoleDataLoader


class DataLoaderThread(threading.Thread):
    def __init__(self, output_queue: deque):
        super().__init__()
        self.started = threading.Event()
        self.alive = True
        self.output_queue = output_queue

        # initialize loader
        self.data_loader = ConsoleDataLoader()
        self.loader_param = None

        # Start run() method in a subthread
        self.start()

    def __del__(self):
        self.kill()

    def begin(self, param=None):
        if param is not None:
            self.loader_param = param
        self.started.set()

    def end(self):
        self.started.clear()

    def run(self):
        self.started.wait()
        while self.alive:
            self.started.wait()
            metadata = self.data_loader.get_metadata(self.loader_param)
            self.output_queue.append(metadata)

    def kill(self):
        self.started.set()
        self.alive = False
        self.join()
