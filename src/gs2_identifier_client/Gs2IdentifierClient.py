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

import json

from gs2_core_client.Gs2Constant import Gs2Constant
from gs2_core_client.AbstractGs2Client import AbstractGs2Client


class Gs2IdentifierClient(AbstractGs2Client):

    ENDPOINT = "identifier"

    def __init__(self, credential, region):
        """
        コンストラクタ
        :param credential: 認証情報
        :type credential: IGs2Credential
        :param region: GS2リージョン
        :type region: str
        """
        super(Gs2IdentifierClient, self).__init__(credential, region)

    def attach_security_policy(self, request):
        """
        ユーザにセキュリティポリシーを割り当てます<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_identifier_client.control.AttachSecurityPolicyRequest.AttachSecurityPolicyRequest

        """
        body = { 
            "securityPolicyId": request.get_security_policy_id(),
        }

        headers = { 
        }
        from gs2_identifier_client.control.AttachSecurityPolicyRequest import AttachSecurityPolicyRequest

        self._do_put_request(
            url=Gs2Constant.ENDPOINT_HOST + "/user/" + str(("null" if request.get_user_name() is None else request.get_user_name())) + "/securityPolicy",
            service=self.ENDPOINT,
            module=AttachSecurityPolicyRequest.Constant.MODULE,
            function=AttachSecurityPolicyRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        )




    def create_identifier(self, request):
        """
        GSIを新規作成します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_identifier_client.control.CreateIdentifierRequest.CreateIdentifierRequest
        :return: 結果
        :rtype: gs2_identifier_client.control.CreateIdentifierResult.CreateIdentifierResult
        """
        body = { 
        }

        headers = { 
        }
        from gs2_identifier_client.control.CreateIdentifierRequest import CreateIdentifierRequest

        from gs2_identifier_client.control.CreateIdentifierResult import CreateIdentifierResult
        return CreateIdentifierResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/user/" + str(("null" if request.get_user_name() is None else request.get_user_name())) + "/identifier",
            service=self.ENDPOINT,
            module=CreateIdentifierRequest.Constant.MODULE,
            function=CreateIdentifierRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))




    def create_security_policy(self, request):
        """
        セキュリティポリシーを新規作成します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_identifier_client.control.CreateSecurityPolicyRequest.CreateSecurityPolicyRequest
        :return: 結果
        :rtype: gs2_identifier_client.control.CreateSecurityPolicyResult.CreateSecurityPolicyResult
        """
        body = { 
            "policy": request.get_policy(),
            "name": request.get_name(),
        }

        headers = { 
        }
        from gs2_identifier_client.control.CreateSecurityPolicyRequest import CreateSecurityPolicyRequest

        from gs2_identifier_client.control.CreateSecurityPolicyResult import CreateSecurityPolicyResult
        return CreateSecurityPolicyResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/securityPolicy",
            service=self.ENDPOINT,
            module=CreateSecurityPolicyRequest.Constant.MODULE,
            function=CreateSecurityPolicyRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))




    def create_user(self, request):
        """
        ユーザを新規作成します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_identifier_client.control.CreateUserRequest.CreateUserRequest
        :return: 結果
        :rtype: gs2_identifier_client.control.CreateUserResult.CreateUserResult
        """
        body = { 
            "name": request.get_name(),
        }

        headers = { 
        }
        from gs2_identifier_client.control.CreateUserRequest import CreateUserRequest

        from gs2_identifier_client.control.CreateUserResult import CreateUserResult
        return CreateUserResult(self._do_post_request(
            url=Gs2Constant.ENDPOINT_HOST + "/user",
            service=self.ENDPOINT,
            module=CreateUserRequest.Constant.MODULE,
            function=CreateUserRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))



    def delete_identifier(self, request):
        """
        GSIを削除します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_identifier_client.control.DeleteIdentifierRequest.DeleteIdentifierRequest

        """

        query_strings = {

        }
        headers = { 
        }
        from gs2_identifier_client.control.DeleteIdentifierRequest import DeleteIdentifierRequest

        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/user/" + str(("null" if request.get_user_name() is None else request.get_user_name())) + "/identifier/" + str(("null" if request.get_identifier_id() is None else request.get_identifier_id())) + "",
            service=self.ENDPOINT,
            module=DeleteIdentifierRequest.Constant.MODULE,
            function=DeleteIdentifierRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )



    def delete_security_policy(self, request):
        """
        セキュリティポリシーを削除します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_identifier_client.control.DeleteSecurityPolicyRequest.DeleteSecurityPolicyRequest

        """

        query_strings = {

        }
        headers = { 
        }
        from gs2_identifier_client.control.DeleteSecurityPolicyRequest import DeleteSecurityPolicyRequest

        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/securityPolicy/" + str(("null" if request.get_security_policy_name() is None else request.get_security_policy_name())) + "",
            service=self.ENDPOINT,
            module=DeleteSecurityPolicyRequest.Constant.MODULE,
            function=DeleteSecurityPolicyRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )



    def delete_user(self, request):
        """
        ユーザを削除します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_identifier_client.control.DeleteUserRequest.DeleteUserRequest

        """

        query_strings = {

        }
        headers = { 
        }
        from gs2_identifier_client.control.DeleteUserRequest import DeleteUserRequest

        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/user/" + str(("null" if request.get_user_name() is None else request.get_user_name())) + "",
            service=self.ENDPOINT,
            module=DeleteUserRequest.Constant.MODULE,
            function=DeleteUserRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )



    def describe_common_security_policy(self, request):
        """
        共用セキュリティポリシーの一覧を取得します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_identifier_client.control.DescribeCommonSecurityPolicyRequest.DescribeCommonSecurityPolicyRequest
        :return: 結果
        :rtype: gs2_identifier_client.control.DescribeCommonSecurityPolicyResult.DescribeCommonSecurityPolicyResult
        """

        query_strings = {

            'pageToken': request.get_page_token(),

            'limit': request.get_limit(),

        }
        headers = { 
        }
        from gs2_identifier_client.control.DescribeCommonSecurityPolicyRequest import DescribeCommonSecurityPolicyRequest

        from gs2_identifier_client.control.DescribeCommonSecurityPolicyResult import DescribeCommonSecurityPolicyResult
        return DescribeCommonSecurityPolicyResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/securityPolicy/common",
            service=self.ENDPOINT,
            module=DescribeCommonSecurityPolicyRequest.Constant.MODULE,
            function=DescribeCommonSecurityPolicyRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))



    def describe_identifier(self, request):
        """
        GSIの一覧を取得します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_identifier_client.control.DescribeIdentifierRequest.DescribeIdentifierRequest
        :return: 結果
        :rtype: gs2_identifier_client.control.DescribeIdentifierResult.DescribeIdentifierResult
        """

        query_strings = {

            'pageToken': request.get_page_token(),

            'limit': request.get_limit(),

        }
        headers = { 
        }
        from gs2_identifier_client.control.DescribeIdentifierRequest import DescribeIdentifierRequest

        from gs2_identifier_client.control.DescribeIdentifierResult import DescribeIdentifierResult
        return DescribeIdentifierResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/user/" + str(("null" if request.get_user_name() is None else request.get_user_name())) + "/identifier",
            service=self.ENDPOINT,
            module=DescribeIdentifierRequest.Constant.MODULE,
            function=DescribeIdentifierRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))



    def describe_security_policy(self, request):
        """
        セキュリティポリシーの一覧を取得します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_identifier_client.control.DescribeSecurityPolicyRequest.DescribeSecurityPolicyRequest
        :return: 結果
        :rtype: gs2_identifier_client.control.DescribeSecurityPolicyResult.DescribeSecurityPolicyResult
        """

        query_strings = {

            'pageToken': request.get_page_token(),

            'limit': request.get_limit(),

        }
        headers = { 
        }
        from gs2_identifier_client.control.DescribeSecurityPolicyRequest import DescribeSecurityPolicyRequest

        from gs2_identifier_client.control.DescribeSecurityPolicyResult import DescribeSecurityPolicyResult
        return DescribeSecurityPolicyResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/securityPolicy",
            service=self.ENDPOINT,
            module=DescribeSecurityPolicyRequest.Constant.MODULE,
            function=DescribeSecurityPolicyRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))



    def describe_user(self, request):
        """
        ユーザの一覧を取得します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_identifier_client.control.DescribeUserRequest.DescribeUserRequest
        :return: 結果
        :rtype: gs2_identifier_client.control.DescribeUserResult.DescribeUserResult
        """

        query_strings = {

            'pageToken': request.get_page_token(),

            'limit': request.get_limit(),

        }
        headers = { 
        }
        from gs2_identifier_client.control.DescribeUserRequest import DescribeUserRequest

        from gs2_identifier_client.control.DescribeUserResult import DescribeUserResult
        return DescribeUserResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/user",
            service=self.ENDPOINT,
            module=DescribeUserRequest.Constant.MODULE,
            function=DescribeUserRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))



    def detach_security_policy(self, request):
        """
        ユーザに割り当てられたセキュリティポリシーを解除します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_identifier_client.control.DetachSecurityPolicyRequest.DetachSecurityPolicyRequest

        """

        query_strings = {

        }
        headers = { 
        }
        from gs2_identifier_client.control.DetachSecurityPolicyRequest import DetachSecurityPolicyRequest

        self._do_delete_request(
            url=Gs2Constant.ENDPOINT_HOST + "/user/" + str(("null" if request.get_user_name() is None else request.get_user_name())) + "/securityPolicy/" + str(("null" if request.get_security_policy_id() is None else request.get_security_policy_id())) + "",
            service=self.ENDPOINT,
            module=DetachSecurityPolicyRequest.Constant.MODULE,
            function=DetachSecurityPolicyRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        )



    def get_identifier(self, request):
        """
        GSIを取得します。<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_identifier_client.control.GetIdentifierRequest.GetIdentifierRequest
        :return: 結果
        :rtype: gs2_identifier_client.control.GetIdentifierResult.GetIdentifierResult
        """

        query_strings = {

        }
        headers = { 
        }
        from gs2_identifier_client.control.GetIdentifierRequest import GetIdentifierRequest

        from gs2_identifier_client.control.GetIdentifierResult import GetIdentifierResult
        return GetIdentifierResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/user/" + str(("null" if request.get_user_name() is None else request.get_user_name())) + "/identifier/" + str(("null" if request.get_identifier_id() is None else request.get_identifier_id())) + "",
            service=self.ENDPOINT,
            module=GetIdentifierRequest.Constant.MODULE,
            function=GetIdentifierRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))



    def get_security_policy(self, request):
        """
        セキュリティポリシーを取得します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_identifier_client.control.GetSecurityPolicyRequest.GetSecurityPolicyRequest
        :return: 結果
        :rtype: gs2_identifier_client.control.GetSecurityPolicyResult.GetSecurityPolicyResult
        """

        query_strings = {

        }
        headers = { 
        }
        from gs2_identifier_client.control.GetSecurityPolicyRequest import GetSecurityPolicyRequest

        from gs2_identifier_client.control.GetSecurityPolicyResult import GetSecurityPolicyResult
        return GetSecurityPolicyResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/securityPolicy/" + str(("null" if request.get_security_policy_name() is None else request.get_security_policy_name())) + "",
            service=self.ENDPOINT,
            module=GetSecurityPolicyRequest.Constant.MODULE,
            function=GetSecurityPolicyRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))



    def get_user(self, request):
        """
        ユーザを取得します。<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_identifier_client.control.GetUserRequest.GetUserRequest
        :return: 結果
        :rtype: gs2_identifier_client.control.GetUserResult.GetUserResult
        """

        query_strings = {

        }
        headers = { 
        }
        from gs2_identifier_client.control.GetUserRequest import GetUserRequest

        from gs2_identifier_client.control.GetUserResult import GetUserResult
        return GetUserResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/user/" + str(("null" if request.get_user_name() is None else request.get_user_name())) + "",
            service=self.ENDPOINT,
            module=GetUserRequest.Constant.MODULE,
            function=GetUserRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))



    def has_security_policy(self, request):
        """
        ユーザが保持しているセキュリティポリシー一覧を取得します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_identifier_client.control.HasSecurityPolicyRequest.HasSecurityPolicyRequest
        :return: 結果
        :rtype: gs2_identifier_client.control.HasSecurityPolicyResult.HasSecurityPolicyResult
        """

        query_strings = {

        }
        headers = { 
        }
        from gs2_identifier_client.control.HasSecurityPolicyRequest import HasSecurityPolicyRequest

        from gs2_identifier_client.control.HasSecurityPolicyResult import HasSecurityPolicyResult
        return HasSecurityPolicyResult(self._do_get_request(
            url=Gs2Constant.ENDPOINT_HOST + "/user/" + str(("null" if request.get_user_name() is None else request.get_user_name())) + "/securityPolicy",
            service=self.ENDPOINT,
            module=HasSecurityPolicyRequest.Constant.MODULE,
            function=HasSecurityPolicyRequest.Constant.FUNCTION,
            query_strings=query_strings,
            headers=headers
        ))



    def update_security_policy(self, request):
        """
        セキュリティポリシーを更新します<br>
        <br>
        :param request: リクエストパラメータ
        :type request: gs2_identifier_client.control.UpdateSecurityPolicyRequest.UpdateSecurityPolicyRequest
        :return: 結果
        :rtype: gs2_identifier_client.control.UpdateSecurityPolicyResult.UpdateSecurityPolicyResult
        """
        body = { 
            "policy": request.get_policy(),
        }

        headers = { 
        }
        from gs2_identifier_client.control.UpdateSecurityPolicyRequest import UpdateSecurityPolicyRequest

        from gs2_identifier_client.control.UpdateSecurityPolicyResult import UpdateSecurityPolicyResult
        return UpdateSecurityPolicyResult(self._do_put_request(
            url=Gs2Constant.ENDPOINT_HOST + "/securityPolicy/" + str(("null" if request.get_security_policy_name() is None else request.get_security_policy_name())) + "",
            service=self.ENDPOINT,
            module=UpdateSecurityPolicyRequest.Constant.MODULE,
            function=UpdateSecurityPolicyRequest.Constant.FUNCTION,
            body=body,
            headers=headers
        ))


