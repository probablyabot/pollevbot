endpoints = {
    'home': 'https://pollev.com/{host}',

    # MyUW Login
    'uw_login': 'https://idp.u.washington.edu/idp/profile/SAML2/'
                'Redirect/SSO;jsessionid={id}.idp03?execution=e1s1',
    'uw_saml': 'https://www.polleverywhere.com/auth/washington?'
               'redirect=https%3A%2F%2Fpollev.com%2F&token_required=false',
    'uw_callback': 'https://www.polleverywhere.com/auth/washington/callback',
    'uw_auth_token': 'https://pollev.com/proxy/api/participant_auth_token',

    # Stanford Login
    'stanford_login': 'https://login.stanford.edu/idp/profile/SAML2/Redirect/'
                      'SSO?execution=e1s{i}',
    'stanford_saml': 'https://www.polleverywhere.com/auth/saml/stanford',
    'stanford_duo_auth': 'https://api-531b0865.duosecurity.com/frame/v4/auth/'
                         'prompt/data?sid={id}',
    'stanford_duo_prompt': 'https://api-531b0865.duosecurity.com/frame/v4/prompt',
    'stanford_duo_status': 'https://api-531b0865.duosecurity.com/frame/v4/status',
    'stanford_duo_exit': 'https://api-531b0865.duosecurity.com/frame/v4/oidc/exit',
    'stanford_callback': 'https://id.polleverywhere.com/auth/saml/stanford/callback',

    # General Login
    'login': 'https://pollev.com/proxy/api/sessions',
    # CSRF authentication
    'csrf': 'https://pollev.com/proxy/api/csrf_token',

    # Respond to a poll
    'firehose_auth': 'https://pollev.com/proxy/api/users/{host}/registration_info',
    'firehose_with_token': 'https://firehose-production.polleverywhere.com/users/{host}/activity/'
                           'current.json?firehose_token={token}',
    'firehose_no_token': 'https://firehose-production.polleverywhere.com/users/{host}/activity/'
                         'current.json',
    'poll_data': 'https://pollev.com/proxy/api/participant/multiple_choice_polls/{uid}?include=collection',
    'respond_to_poll': 'https://pollev.com/proxy/api/participant/multiple_choice_polls/{uid}/results',
    'clear_responses': 'https://pollev.com/proxy/api/results/{id}',
    'check_responses': 'https://pollev.com/proxy/my/results?permalinks%5B%5D={uid}&'
                       'per_page=500&include_archived=false'
}
