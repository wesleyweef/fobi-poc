from .form import HTTPRepostForm, HTTPRepostFormWizard
from fobi.base import FormHandlerPlugin, form_handler_plugin_registry, \
    form_wizard_handler_plugin_registry, FormWizardHandlerPlugin
import requests
from django.core.mail import send_mail


class OnetRepostHandlerPlugin(FormHandlerPlugin):
    """HTTP repost handler plugin.

    Makes a HTTP repost to a given endpoint. Should be executed before
    ``db_store`` plugin.
    """

    uid = 'onet_repost'
    name = "Onet Repost"
    form = HTTPRepostForm

    def run(self, form_entry, request, form, form_element_entries=None):
        # csrfmiddlewaretoken
        data = request.POST.dict()
        data.pop("csrfmiddlewaretoken")

        print(self.data.endpoint_url)
        print(data)

        answer = ''
        for k, v in data.items():
            answer += v

        # print(answer)


form_handler_plugin_registry.register(OnetRepostHandlerPlugin)


class OnetRepostHandlerPluginWizard(FormWizardHandlerPlugin):
    """HTTP repost handler plugin.

    Makes a HTTP repost to a given endpoint. Should be executed before
    ``db_store`` plugin.
    """

    uid = 'onet_repost_wizard'
    name = "Onet Repost wizard"
    form = HTTPRepostFormWizard

    def run(self,
            form_wizard_entry,
            request,
            form_list,
            form_wizard,
            form_element_entries=None):

        url = self.data.endpoint_url

        headers = {
            'Authorization': self.data.key_auth,
            'Accept': 'application/json'
        }

        # import ipdb
        # # code
        # ipdb.set_trace()

        to = form_list.mapping['form-email'].cleaned_data['email']

        answers = ''

        for f in form_list:
            print(f.prefix)
            if f.prefix != 'form-email':

                data = f.cleaned_data

                for k, v in data.items():
                    answers += v

        print(answers)
        payload = {'answers': answers[:60]}
        # print(payload)
        # response = requests.get(url, headers=headers, params=payload)

        url_career = 'https://services.onetcenter.org/ws/mnm/interestprofiler/careers'

        # "?answers=553421321134342523523523254115342111351145453111231155343444&start=21&end=40"

        payload['job_zone'] = answers[60]

        response = requests.get(url_career, headers=headers, params=payload)

        print(response.status_code)
        print(response.text)
        r_json = response.json()

        resp = ""

        for i in r_json['career']:
            resp += f"{i['title']} - {i['fit']} \n"

        send_mail(
            "Resultado Form",
            resp,
            "wesley@weef.com.br",
            [to,],
            fail_silently=False,
        )


form_wizard_handler_plugin_registry.register(OnetRepostHandlerPluginWizard)
