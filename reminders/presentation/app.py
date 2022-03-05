from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from reminders.infrastructure import settings
from reminders.infrastructure.aiohttp import get_aiohttp_client
from reminders.infrastructure.aws.dynamodb import dynamo_client

app = FastAPI()


@app.get("/health")
async def get_heath_check():
    try:
        async with get_aiohttp_client() as client:
            table_exist = await dynamo_client(client).table_exists(
                settings.service_data_table_name
            )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    if table_exist:
        return JSONResponse({"ok": True})
    raise HTTPException(status_code=500, detail="table not found")
