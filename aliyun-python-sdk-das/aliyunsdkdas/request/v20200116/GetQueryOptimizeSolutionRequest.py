# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
from aliyunsdkdas.endpoint import endpoint_data

class GetQueryOptimizeSolutionRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'DAS', '2020-01-16', 'GetQueryOptimizeSolution','das')
		self.set_method('GET')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_SqlId(self):
		return self.get_query_params().get('SqlId')

	def set_SqlId(self,SqlId):
		self.add_query_param('SqlId',SqlId)

	def get_ConsoleContext(self):
		return self.get_query_params().get('ConsoleContext')

	def set_ConsoleContext(self,ConsoleContext):
		self.add_query_param('ConsoleContext',ConsoleContext)

	def get_RuleIds(self):
		return self.get_query_params().get('RuleIds')

	def set_RuleIds(self,RuleIds):
		self.add_query_param('RuleIds',RuleIds)

	def get_Engine(self):
		return self.get_query_params().get('Engine')

	def set_Engine(self,Engine):
		self.add_query_param('Engine',Engine)