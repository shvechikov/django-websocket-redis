from django.core.exceptions import PermissionDenied

def get_allowed_channels(request, channels):
    if request and request.user.is_authenticated():
        return set(channels).intersection(['subscribe-user'])
    raise PermissionDenied('Not allowed to subscribe nor to publish on the Websocket!')
