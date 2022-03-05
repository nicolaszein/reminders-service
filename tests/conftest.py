import pytest
from aiodynamo.models import KeySchema, KeySpec, KeyType, Throughput
from reminders.infrastructure import settings
from reminders.infrastructure.aiohttp import get_aiohttp_client
from reminders.infrastructure.aws.dynamodb import dynamo_client


@pytest.fixture
async def data_table():
    async with get_aiohttp_client() as aioclient:
        dynamodb = dynamo_client(aioclient)
        table = dynamodb.table(settings.service_data_table_name)
        if await table.exists():
            await table.delete(wait_for_disabled=True)

        await table.create(
            Throughput(read=10, write=10),
            KeySchema(
                hash_key=KeySpec("pk", KeyType.string),
                range_key=KeySpec("sk", KeyType.string),
            ),
            wait_for_active=True,
        )
        yield table

        await table.delete(wait_for_disabled=True)
