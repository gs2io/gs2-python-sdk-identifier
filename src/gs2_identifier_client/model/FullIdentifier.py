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

class FullIdentifier(object):

    def __init__(self, params=None):
        if params is None:
            self.__identifier_id = None
            self.__owner_id = None
            self.__user_id = None
            self.__client_id = None
            self.__client_secret = None
            self.__create_at = None
        else:
            self.set_identifier_id(params['identifierId'] if 'identifierId' in params.keys() else None)
            self.set_owner_id(params['ownerId'] if 'ownerId' in params.keys() else None)
            self.set_user_id(params['userId'] if 'userId' in params.keys() else None)
            self.set_client_id(params['clientId'] if 'clientId' in params.keys() else None)
            self.set_client_secret(params['clientSecret'] if 'clientSecret' in params.keys() else None)
            self.set_create_at(params['createAt'] if 'createAt' in params.keys() else None)


    def get_identifier_id(self):
        """
        ユーザGRNを取得
        :return: ユーザGRN
        :rtype: unicode
        """
        return self.__identifier_id

    def set_identifier_id(self, identifier_id):
        """
        ユーザGRNを設定
        :param identifier_id: ユーザGRN
        :type identifier_id: unicode
        """
        self.__identifier_id = identifier_id

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

    def get_user_id(self):
        """
        ユーザIDを取得
        :return: ユーザID
        :rtype: unicode
        """
        return self.__user_id

    def set_user_id(self, user_id):
        """
        ユーザIDを設定
        :param user_id: ユーザID
        :type user_id: unicode
        """
        self.__user_id = user_id

    def get_client_id(self):
        """
        クライアントIDを取得
        :return: クライアントID
        :rtype: unicode
        """
        return self.__client_id

    def set_client_id(self, client_id):
        """
        クライアントIDを設定
        :param client_id: クライアントID
        :type client_id: unicode
        """
        self.__client_id = client_id

    def get_client_secret(self):
        """
        クライアントシークレットを取得
        :return: クライアントシークレット
        :rtype: unicode
        """
        return self.__client_secret

    def set_client_secret(self, client_secret):
        """
        クライアントシークレットを設定
        :param client_secret: クライアントシークレット
        :type client_secret: unicode
        """
        self.__client_secret = client_secret

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

    def to_dict(self):
        return { 
            "identifierId": self.__identifier_id,
            "ownerId": self.__owner_id,
            "userId": self.__user_id,
            "clientId": self.__client_id,
            "clientSecret": self.__client_secret,
            "createAt": self.__create_at,
        }