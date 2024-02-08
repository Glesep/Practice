# Extra Data Types
from datetime import datetime, time, timedelta
from typing import Annotated
from uuid import UUID
from fastapi import Body, FastAPI

app = FastAPI()

@app.put("/items/{item_id}")
async def read_items(
    item_id: UUID,
    start_datetime: Annotated[datetime | None, Body()] = None,                  # datetime: 날짜와 시간을 함께 다룸, 연도 ~ 마이크로초
    end_datetime: Annotated[datetime | None, Body()] = None,                    
    repeat_at: Annotated[time | None, Body()] = None,                           # time: 시간을 다룸, 시/분/초
    process_after: Annotated[timedelta | None, Body()] = None                   # timedelta: 두 날짜 또는 시간 사이의 차이 표현, 지나갈 날짜 시간 분 저장
):
    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "repeat_at": repeat_at,
        "process_after": process_after,
        "start_process": start_process,
        "duration": duration
    }