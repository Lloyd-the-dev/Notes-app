from discord_webhook import DiscordWebhook

logger = logging.getLogger('django')


class DiscordLogMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            message = f"CRUD Operation: {request.method} {request.path}"
            logger.info(message)
        return response


