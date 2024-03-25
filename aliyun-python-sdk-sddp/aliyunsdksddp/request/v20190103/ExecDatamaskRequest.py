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
from aliyunsdksddp.endpoint import endpoint_data

class ExecDatamaskRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sddp', '2019-01-03', 'ExecDatamask','sddp')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Data(self): # String
		return self.get_query_params().get('Data')

	def set_Data(self, Data):  # String
		self.add_query_param('Data', Data)
	def get_FeatureType(self): # Integer
		return self.get_query_params().get('FeatureType')

	def set_FeatureType(self, FeatureType):  # Integer
		self.add_query_param('FeatureType', FeatureType)
	def get_TemplateId(self): # Long
		return self.get_query_params().get('TemplateId')

	def set_TemplateId(self, TemplateId):  # Long
		self.add_query_param('TemplateId', TemplateId)
	def get_Lang(self): # String
		return self.get_query_params().get('Lang')

	def set_Lang(self, Lang):  # String
		self.add_query_param('Lang', Lang)
