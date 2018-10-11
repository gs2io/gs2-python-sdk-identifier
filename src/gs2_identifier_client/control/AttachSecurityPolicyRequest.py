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


class AttachSecurityPolicyRequest(Gs2BasicRequest):

    class Constant(Gs2Identifier):
        FUNCTION = "AttachSecurityPolicy"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(AttachSecurityPolicyRequest, self).__init__(params)
        if params is None:
            self.__user_name = None
        else:
            self.set_user_name(params['userName'] if 'userName' in params.keys() else None)
        if params is None:
            self.__security_policy_id = None
        else:
            self.set_security_policy_id(params['securityPolicyId'] if 'securityPolicyId' in params.keys() else None)

    def get_user_name(self):
        """
        ユーザの名前を指定します。を取得
        :return: ユーザの名前を指定します。
        :rtype: unicode
        """
        return self.__user_name

    def set_user_name(self, user_name):
        """
        ユーザの名前を指定します。を設定
        :param user_name: ユーザの名前を指定します。
        :type user_name: unicode
        """
        if user_name is not None and not (isinstance(user_name, str) or isinstance(user_name, unicode)):
            raise TypeError(type(user_name))
        self.__user_name = user_name

    def with_user_name(self, user_name):
        """
        ユーザの名前を指定します。を設定
        :param user_name: ユーザの名前を指定します。
        :type user_name: unicode
        :return: this
        :rtype: AttachSecurityPolicyRequest
        """
        self.set_user_name(user_name)
        return self

    def get_security_policy_id(self):
        """
        セキュリティポリシーのGRNを取得
        :return: セキュリティポリシーのGRN
        :rtype: unicode
        """
        return self.__security_policy_id

    def set_security_policy_id(self, security_policy_id):
        """
        セキュリティポリシーのGRNを設定
        :param security_policy_id: セキュリティポリシーのGRN
        :type security_policy_id: unicode
        """
        if security_policy_id is not None and not (isinstance(security_policy_id, str) or isinstance(security_policy_id, unicode)):
            raise TypeError(type(security_policy_id))
        self.__security_policy_id = security_policy_id

    def with_security_policy_id(self, security_policy_id):
        """
        セキュリティポリシーのGRNを設定
        :param security_policy_id: セキュリティポリシーのGRN
        :type security_policy_id: unicode
        :return: this
        :rtype: AttachSecurityPolicyRequest
        """
        self.set_security_policy_id(security_policy_id)
        return self
