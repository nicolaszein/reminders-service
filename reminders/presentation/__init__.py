from dependencies import Injector
from reminders.infrastructure.aiohttp import get_aiohttp_client
from reminders.infrastructure.aws.dynamodb import dynamo_client


async def get_application_container():
    async with get_aiohttp_client() as aioclient:
        yield Injector(
            dynamodb_client=dynamo_client(aioclient),
        )
