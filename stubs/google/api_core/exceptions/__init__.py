class GoogleAPIError(Exception):
    ...


class GoogleAPICallError(GoogleAPIError):
    ...


class ClientError(GoogleAPICallError):
    ...


class NotFound(ClientError):
    ...
