from aiodynamo.client import Client
from aiodynamo.credentials import (
    ChainCredentials,
    ContainerMetadataCredentials,
    EnvironmentCredentials,
    InstanceMetadataCredentials,
)
from aiodynamo.http.aiohttp import AIOHTTP
from reminders.infrastructure import settings
from yarl import URL


def dynamo_client(aioclient):
    credentials_chain = ChainCredentials(
        candidates=[
            EnvironmentCredentials(),
            ContainerMetadataCredentials(),
            InstanceMetadataCredentials(),
        ]
    )
    dynamodb = Client(
        AIOHTTP(aioclient),
        credentials_chain,
        region=settings.region,
        endpoint=settings.dynamodb_url,
    )
    return dynamodb
