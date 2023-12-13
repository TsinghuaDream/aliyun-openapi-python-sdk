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

class AddDataSourceLogRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'cloud-siem', '2022-06-16', 'AddDataSourceLog','cloud-siem')
		self.set_method('POST')

	def get_CloudCode(self): # String
		return self.get_body_params().get('CloudCode')

	def set_CloudCode(self, CloudCode):  # String
		self.add_body_params('CloudCode', CloudCode)
	def get_AccountId(self): # String
		return self.get_body_params().get('AccountId')

	def set_AccountId(self, AccountId):  # String
		self.add_body_params('AccountId', AccountId)
	def get_LogCode(self): # String
		return self.get_body_params().get('LogCode')

	def set_LogCode(self, LogCode):  # String
		self.add_body_params('LogCode', LogCode)
	def get_DataSourceInstanceLogs(self): # String
		return self.get_body_params().get('DataSourceInstanceLogs')

	def set_DataSourceInstanceLogs(self, DataSourceInstanceLogs):  # String
		self.add_body_params('DataSourceInstanceLogs', DataSourceInstanceLogs)
	def get_DataSourceInstanceId(self): # String
		return self.get_body_params().get('DataSourceInstanceId')

	def set_DataSourceInstanceId(self, DataSourceInstanceId):  # String
		self.add_body_params('DataSourceInstanceId', DataSourceInstanceId)
