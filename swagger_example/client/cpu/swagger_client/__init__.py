# coding: utf-8

"""
    cpuinfo

    A simple service to get cpuinfo as an example of using swagger-2.0 specification and codegen

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

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

from __future__ import absolute_import

# import models into sdk package
from .models.cpu import CPU

# import apis into sdk package
from .apis.default_api import DefaultApi

# import ApiClient
from .api_client import ApiClient

from .configuration import Configuration

configuration = Configuration()