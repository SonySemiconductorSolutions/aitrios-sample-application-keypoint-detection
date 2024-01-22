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

from collections import deque

from .data_loader.data_loader_thread import DataLoaderThread
from .deserializer.deserializer_thread import DeserializerThread


class DataPipeline:
    def __init__(self, sender_queue_size):
        self.started = False

        # fixed length queue(initial queue, length)
        self.deserializer_queue = deque([])
        self.sender_queue = deque([], sender_queue_size)

        self.loader_thread = DataLoaderThread(self.deserializer_queue)
        self.deserializer_thread = DeserializerThread(self.deserializer_queue, self.sender_queue)

    def start_processing(self, loader_param=None):
        if self.loader_thread.alive:
            self.loader_thread.begin(loader_param)
            self.deserializer_thread.begin()

    def stop_processing(self):
        if self.loader_thread.alive:
            self.loader_thread.end()
            self.deserializer_thread.end()

    def get_sender_queue(self):
        return self.sender_queue

    def finalize(self):
        self.loader_thread.kill()
        self.deserializer_thread.kill()
