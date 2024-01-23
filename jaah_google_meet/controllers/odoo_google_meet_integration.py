import datetime
import requests
from odoo import http, _
from odoo.exceptions import UserError
from odoo.http import request


class GoogleMeetAuth(http.Controller):
    """Controller for Google Meet authentication. """
    @http.route('/google_meet_authentication', type='http',
                auth="public", website=True)
    def get_auth_code(self, **kw):
        """ Get the authentication code for Google Meet"""
        company_id = http.request.env['res.users'].sudo().browse(
            request.uid).company_id
        if kw.get('code'):
            company_id.write(
                {'company_authorization_code': kw.get('code')})
            data = {
                'code': kw.get('code'),
                'client_id': company_id.client,
                'client_secret': company_id.client_secret,
                'redirect_uri': company_id.redirect_uri,
                'grant_type': 'authorization_code'
            }
            response = requests.post(
                'https://accounts.google.com/o/oauth2/token', data=data,
                headers={
                    'content-type': 'application/x-www-form-urlencoded'})
            if response.json() and response.json().get('access_token'):
                company_id.write({
                    'company_access_token':
                        response.json().get('access_token'),
                    'company_access_token_expiry':
                        datetime.datetime.now() + datetime.timedelta(
                            seconds=response.json().get('expires_in')),
                    'company_refresh_token':
                        response.json().get('access_token'),
                })
                return "Authentication Success. You Can Close this window"
            else:
                raise UserError(
                    _('Something went wrong during the token generation.'
                      'Maybe your Authorization Code is invalid'))
