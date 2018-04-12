# encoding: utf-8
#
# Copyright 2016 Game Server Services, Inc. or its affiliates. All Rights
# Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.

from gs2_core_client.Gs2BasicRequest import Gs2BasicRequest
from gs2_identifier_client.Gs2Identifier import Gs2Identifier


class DeleteSecurityPolicyRequest(Gs2BasicRequest):

    class Constant(Gs2Identifier):
        FUNCTION = "DeleteSecurityPolicy"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(DeleteSecurityPolicyRequest, self).__init__(params)
        if params is None:
            self.__security_policy_name = None
        else:
            self.set_security_policy_name(params['securityPolicyName'] if 'securityPolicyName' in params.keys() else None)

    def get_security_policy_name(self):
        """
        セキュリティポリシーの名前を指定します。を取得
        :return: セキュリティポリシーの名前を指定します。
        :rtype: unicode
        """
        return self.__security_policy_name

    def set_security_policy_name(self, security_policy_name):
        """
        セキュリティポリシーの名前を指定します。を設定
        :param security_policy_name: セキュリティポリシーの名前を指定します。
        :type security_policy_name: unicode
        """
        if security_policy_name and not isinstance(security_policy_name, unicode):
            raise TypeError(type(security_policy_name))
        self.__security_policy_name = security_policy_name

    def with_security_policy_name(self, security_policy_name):
        """
        セキュリティポリシーの名前を指定します。を設定
        :param security_policy_name: セキュリティポリシーの名前を指定します。
        :type security_policy_name: unicode
        :return: this
        :rtype: DeleteSecurityPolicyRequest
        """
        self.set_security_policy_name(security_policy_name)
        return self
