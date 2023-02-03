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
from aliyunsdkrds.endpoint import endpoint_data
import json

class ModifyMarketingStateRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Rds', '2014-08-15', 'ModifyMarketingState','rds')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_AliUid(self): # Long
		return self.get_query_params().get('AliUid')

	def set_AliUid(self, AliUid):  # Long
		self.add_query_param('AliUid', AliUid)
	def get_UpgradeCode(self): # String
		return self.get_query_params().get('UpgradeCode')

	def set_UpgradeCode(self, UpgradeCode):  # String
		self.add_query_param('UpgradeCode', UpgradeCode)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_InstanceNameList(self): # Array
		return self.get_query_params().get('InstanceNameList')

	def set_InstanceNameList(self, InstanceNameList):  # Array
		self.add_query_param("InstanceNameList", json.dumps(InstanceNameList))
	def get_StateValue(self): # Integer
		return self.get_query_params().get('StateValue')

	def set_StateValue(self, StateValue):  # Integer
		self.add_query_param('StateValue', StateValue)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_InstanceIds(self): # Array
		return self.get_query_params().get('InstanceIds')

	def set_InstanceIds(self, InstanceIds):  # Array
		self.add_query_param("InstanceIds", json.dumps(InstanceIds))
	def get_Bid(self): # String
		return self.get_query_params().get('Bid')

	def set_Bid(self, Bid):  # String
		self.add_query_param('Bid', Bid)