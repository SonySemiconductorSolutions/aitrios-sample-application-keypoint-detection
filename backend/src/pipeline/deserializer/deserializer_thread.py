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

from .deserialize_keypoint import deserialize_keypoint


class DeserializerThread(threading.Thread):
    def __init__(self, input_queue: deque, output_queue: deque):
        super().__init__()
        self.started = threading.Event()
        self.alive = True
        self.input_queue = input_queue
        self.output_queue = output_queue

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
            if len(self.input_queue) > 0:
                inference_data = self.input_queue.popleft()
                try:
                    deserialized_data = deserialize_keypoint(inference_data["inference_data"])
                    inference_data["inference_data"] = deserialized_data
                except Exception as e:
                    print(e)
                    inference_data["inference_data"] = []

                self.output_queue.append(inference_data)

    def kill(self):
        self.started.set()
        self.alive = False
        self.join()
