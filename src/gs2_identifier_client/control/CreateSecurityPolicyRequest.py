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


class CreateSecurityPolicyRequest(Gs2BasicRequest):

    class Constant(Gs2Identifier):
        FUNCTION = "CreateSecurityPolicy"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(CreateSecurityPolicyRequest, self).__init__(params)
        if params is None:
            self.__name = None
        else:
            self.set_name(params['name'] if 'name' in params.keys() else None)
        if params is None:
            self.__policy = None
        else:
            self.set_policy(params['policy'] if 'policy' in params.keys() else None)

    def get_name(self):
        """
        名前を取得
        :return: 名前
        :rtype: unicode
        """
        return self.__name

    def set_name(self, name):
        """
        名前を設定
        :param name: 名前
        :type name: unicode
        """
        if name and not (isinstance(name, str) or isinstance(name, unicode)):
            raise TypeError(type(name))
        self.__name = name

    def with_name(self, name):
        """
        名前を設定
        :param name: 名前
        :type name: unicode
        :return: this
        :rtype: CreateSecurityPolicyRequest
        """
        self.set_name(name)
        return self

    def get_policy(self):
        """
        ポリシードキュメントを取得
        :return: ポリシードキュメント
        :rtype: unicode
        """
        return self.__policy

    def set_policy(self, policy):
        """
        ポリシードキュメントを設定
        :param policy: ポリシードキュメント
        :type policy: unicode
        """
        if policy and not (isinstance(policy, str) or isinstance(policy, unicode)):
            raise TypeError(type(policy))
        self.__policy = policy

    def with_policy(self, policy):
        """
        ポリシードキュメントを設定
        :param policy: ポリシードキュメント
        :type policy: unicode
        :return: this
        :rtype: CreateSecurityPolicyRequest
        """
        self.set_policy(policy)
        return self
