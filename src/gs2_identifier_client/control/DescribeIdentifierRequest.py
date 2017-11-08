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


class DescribeIdentifierRequest(Gs2BasicRequest):

    class Constant(Gs2Identifier):
        FUNCTION = "DescribeIdentifier"

    def __init__(self, params=None):
        """
        コンストラクタ
        :param params: 辞書配列形式のパラメータ初期値リスト
        :type params: dict|None
        """
        super(DescribeIdentifierRequest, self).__init__(params)
        if params is None:
            self.__user_name = None
            self.__page_token = None
            self.__limit = None
        else:
            self.set_user_name(params['userName'] if 'userName' in params.keys() else None)
            self.set_page_token(params['pageToken'] if 'pageToken' in params.keys() else None)
            self.set_limit(params['limit'] if 'limit' in params.keys() else None)

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
        :rtype: DescribeIdentifierRequest
        """
        self.set_user_name(user_name)
        return self

    def get_page_token(self):
        """
        データの取得を開始する位置を指定するトークンを取得
        :return: データの取得を開始する位置を指定するトークン
        :rtype: unicode
        """
        return self.__page_token

    def set_page_token(self, page_token):
        """
        データの取得を開始する位置を指定するトークンを設定
        :param page_token: データの取得を開始する位置を指定するトークン
        :type page_token: unicode
        """
        self.__page_token = page_token

    def with_page_token(self, page_token):
        """
        データの取得を開始する位置を指定するトークンを設定
        :param page_token: データの取得を開始する位置を指定するトークン
        :type page_token: unicode
        :return: this
        :rtype: DescribeIdentifierRequest
        """
        self.set_page_token(page_token)
        return self

    def get_limit(self):
        """
        データの取得件数を取得
        :return: データの取得件数
        :rtype: int
        """
        return self.__limit

    def set_limit(self, limit):
        """
        データの取得件数を設定
        :param limit: データの取得件数
        :type limit: int
        """
        self.__limit = limit

    def with_limit(self, limit):
        """
        データの取得件数を設定
        :param limit: データの取得件数
        :type limit: int
        :return: this
        :rtype: DescribeIdentifierRequest
        """
        self.set_limit(limit)
        return self