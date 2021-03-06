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


class SecurityPolicy(object):

    def __init__(self, params=None):
        if params is None:
            self.__security_policy_id = None
            self.__owner_id = None
            self.__name = None
            self.__policy = None
            self.__create_at = None
            self.__update_at = None
        else:
            self.set_security_policy_id(params['securityPolicyId'] if 'securityPolicyId' in params.keys() else None)
            self.set_owner_id(params['ownerId'] if 'ownerId' in params.keys() else None)
            self.set_name(params['name'] if 'name' in params.keys() else None)
            self.set_policy(params['policy'] if 'policy' in params.keys() else None)
            self.set_create_at(params['createAt'] if 'createAt' in params.keys() else None)
            self.set_update_at(params['updateAt'] if 'updateAt' in params.keys() else None)

    def get_security_policy_id(self):
        """
        セキュリティポリシーIDを取得
        :return: セキュリティポリシーID
        :rtype: unicode
        """
        return self.__security_policy_id

    def set_security_policy_id(self, security_policy_id):
        """
        セキュリティポリシーIDを設定
        :param security_policy_id: セキュリティポリシーID
        :type security_policy_id: unicode
        """
        self.__security_policy_id = security_policy_id

    def get_owner_id(self):
        """
        オーナーIDを取得
        :return: オーナーID
        :rtype: unicode
        """
        return self.__owner_id

    def set_owner_id(self, owner_id):
        """
        オーナーIDを設定
        :param owner_id: オーナーID
        :type owner_id: unicode
        """
        self.__owner_id = owner_id

    def get_name(self):
        """
        セキュリティポリシー名を取得
        :return: セキュリティポリシー名
        :rtype: unicode
        """
        return self.__name

    def set_name(self, name):
        """
        セキュリティポリシー名を設定
        :param name: セキュリティポリシー名
        :type name: unicode
        """
        self.__name = name

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
        self.__policy = policy

    def get_create_at(self):
        """
        作成日時(エポック秒)を取得
        :return: 作成日時(エポック秒)
        :rtype: int
        """
        return self.__create_at

    def set_create_at(self, create_at):
        """
        作成日時(エポック秒)を設定
        :param create_at: 作成日時(エポック秒)
        :type create_at: int
        """
        self.__create_at = create_at

    def get_update_at(self):
        """
        最終更新日時(エポック秒)を取得
        :return: 最終更新日時(エポック秒)
        :rtype: int
        """
        return self.__update_at

    def set_update_at(self, update_at):
        """
        最終更新日時(エポック秒)を設定
        :param update_at: 最終更新日時(エポック秒)
        :type update_at: int
        """
        self.__update_at = update_at

    def __getitem__(self, key):
        items = self.to_dict()
        if key in items.keys():
            return items[key]
        return super(SecurityPolicy, self).__getitem__(key)

    def to_dict(self):
        return {
            "securityPolicyId": self.__security_policy_id,
            "ownerId": self.__owner_id,
            "name": self.__name,
            "policy": self.__policy,
            "createAt": self.__create_at,
            "updateAt": self.__update_at,
        }
