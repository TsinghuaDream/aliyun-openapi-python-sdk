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

class GetAsyncErrorRequestStatByCodeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'DAS', '2020-01-16', 'GetAsyncErrorRequestStatByCode','das')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Role(self):
		return self.get_query_params().get('Role')

	def set_Role(self,Role):
		self.add_query_param('Role',Role)

	def get_Start(self):
		return self.get_query_params().get('Start')

	def set_Start(self,Start):
		self.add_query_param('Start',Start)

	def get_ConsoleContext(self):
		return self.get_query_params().get('ConsoleContext')

	def set_ConsoleContext(self,ConsoleContext):
		self.add_query_param('ConsoleContext',ConsoleContext)

	def get_InstanceId(self):
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self,InstanceId):
		self.add_query_param('InstanceId',InstanceId)

	def get_DbName(self):
		return self.get_query_params().get('DbName')

	def set_DbName(self,DbName):
		self.add_query_param('DbName',DbName)

	def get_End(self):
		return self.get_query_params().get('End')

	def set_End(self,End):
		self.add_query_param('End',End)

	def get_NodeId(self):
		return self.get_query_params().get('NodeId')

	def set_NodeId(self,NodeId):
		self.add_query_param('NodeId',NodeId)