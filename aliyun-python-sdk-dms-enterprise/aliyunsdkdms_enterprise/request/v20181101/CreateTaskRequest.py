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
from aliyunsdkdms_enterprise.endpoint import endpoint_data

class CreateTaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dms-enterprise', '2018-11-01', 'CreateTask','dms-enterprise')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_TimeVariables(self): # String
		return self.get_query_params().get('TimeVariables')

	def set_TimeVariables(self, TimeVariables):  # String
		self.add_query_param('TimeVariables', TimeVariables)
	def get_NodeType(self): # String
		return self.get_query_params().get('NodeType')

	def set_NodeType(self, NodeType):  # String
		self.add_query_param('NodeType', NodeType)
	def get_DagId(self): # Long
		return self.get_query_params().get('DagId')

	def set_DagId(self, DagId):  # Long
		self.add_query_param('DagId', DagId)
	def get_Tid(self): # Long
		return self.get_query_params().get('Tid')

	def set_Tid(self, Tid):  # Long
		self.add_query_param('Tid', Tid)
	def get_NodeName(self): # String
		return self.get_query_params().get('NodeName')

	def set_NodeName(self, NodeName):  # String
		self.add_query_param('NodeName', NodeName)
	def get_NodeContent(self): # String
		return self.get_query_params().get('NodeContent')

	def set_NodeContent(self, NodeContent):  # String
		self.add_query_param('NodeContent', NodeContent)
	def get_NodeOutput(self): # String
		return self.get_query_params().get('NodeOutput')

	def set_NodeOutput(self, NodeOutput):  # String
		self.add_query_param('NodeOutput', NodeOutput)
	def get_GraphParam(self): # String
		return self.get_query_params().get('GraphParam')

	def set_GraphParam(self, GraphParam):  # String
		self.add_query_param('GraphParam', GraphParam)
