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


class GetIdentifierRequest(Gs2BasicRequest):

    class Constant(Gs2Identifier):
        FUNCTION = "GetIdentifier"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(GetIdentifierRequest, self).__init__(params)
        if params is None:
            self.__user_name = None
            self.__identifier_id = None
        else:
            self.set_user_name(params['userName'] if 'userName' in params.keys() else None)
            self.set_identifier_id(params['identifierId'] if 'identifierId' in params.keys() else None)

    def get_user_name(self):
        """
        ユーザの名前を取得
        :return: ユーザの名前
        :rtype: unicode
        """
        return self.__user_name

    def set_user_name(self, user_name):
        """
        ユーザの名前を設定
        :param user_name: ユーザの名前
        :type user_name: unicode
        """
        self.__user_name = user_name

    def with_user_name(self, user_name):
        """
        ユーザの名前を設定
        :param user_name: ユーザの名前
        :type user_name: unicode
        :return: this
        :rtype: GetIdentifierRequest
        """
        self.set_user_name(user_name)
        return self

    def get_identifier_id(self):
        """
        GSIのGRNを取得
        :return: GSIのGRN
        :rtype: unicode
        """
        return self.__identifier_id

    def set_identifier_id(self, identifier_id):
        """
        GSIのGRNを設定
        :param identifier_id: GSIのGRN
        :type identifier_id: unicode
        """
        self.__identifier_id = identifier_id

    def with_identifier_id(self, identifier_id):
        """
        GSIのGRNを設定
        :param identifier_id: GSIのGRN
        :type identifier_id: unicode
        :return: this
        :rtype: GetIdentifierRequest
        """
        self.set_identifier_id(identifier_id)
        return self