Directory structure:
└── responses/
    ├── __init__.py
    ├── background.py
    ├── background_async.py
    ├── background_streaming.py
    ├── background_streaming_async.py
    ├── streaming.py
    ├── streaming_tools.py
    ├── structured_outputs.py
    └── structured_outputs_tools.py


Files Content:

================================================
FILE: examples/responses/__init__.py
================================================
[Empty file]


================================================
FILE: examples/responses/background.py
================================================
from typing import List

import rich
from pydantic import BaseModel

from openai import OpenAI


class Step(BaseModel):
    explanation: str
    output: str


class MathResponse(BaseModel):
    steps: List[Step]
    final_answer: str


client = OpenAI()
id = None

with client.responses.create(
    input="solve 8x + 31 = 2",
    model="gpt-4o-2024-08-06",
    background=True,
    stream=True,
) as stream:
    for event in stream:
        if event.type == "response.created":
            id = event.response.id
        if "output_text" in event.type:
            rich.print(event)
        if event.sequence_number == 10:
            break

print("Interrupted. Continuing...")

assert id is not None
with client.responses.retrieve(
    response_id=id,
    stream=True,
    starting_after=10,
) as stream:
    for event in stream:
        if "output_text" in event.type:
            rich.print(event)



================================================
FILE: examples/responses/background_async.py
================================================
import asyncio
from typing import List

import rich
from pydantic import BaseModel

from openai._client import AsyncOpenAI


class Step(BaseModel):
    explanation: str
    output: str


class MathResponse(BaseModel):
    steps: List[Step]
    final_answer: str


async def main() -> None:
    client = AsyncOpenAI()
    id = None

    async with await client.responses.create(
        input="solve 8x + 31 = 2",
        model="gpt-4o-2024-08-06",
        background=True,
        stream=True,
    ) as stream:
        async for event in stream:
            if event.type == "response.created":
                id = event.response.id
            if "output_text" in event.type:
                rich.print(event)
            if event.sequence_number == 10:
                break

    print("Interrupted. Continuing...")

    assert id is not None
    async with await client.responses.retrieve(
        response_id=id,
        stream=True,
        starting_after=10,
    ) as stream:
        async for event in stream:
            if "output_text" in event.type:
                rich.print(event)


if __name__ == "__main__":
    asyncio.run(main())



================================================
FILE: examples/responses/background_streaming.py
================================================
#!/usr/bin/env -S rye run python
from typing import List

import rich
from pydantic import BaseModel

from openai import OpenAI


class Step(BaseModel):
    explanation: str
    output: str


class MathResponse(BaseModel):
    steps: List[Step]
    final_answer: str


client = OpenAI()
id = None
with client.responses.stream(
    input="solve 8x + 31 = 2",
    model="gpt-4o-2024-08-06",
    text_format=MathResponse,
    background=True,
) as stream:
    for event in stream:
        if event.type == "response.created":
            id = event.response.id
        if "output_text" in event.type:
            rich.print(event)
        if event.sequence_number == 10:
            break

print("Interrupted. Continuing...")

assert id is not None
with client.responses.stream(
    response_id=id,
    starting_after=10,
    text_format=MathResponse,
) as stream:
    for event in stream:
        if "output_text" in event.type:
            rich.print(event)

    rich.print(stream.get_final_response())



================================================
FILE: examples/responses/background_streaming_async.py
================================================
import asyncio
from typing import List

import rich
from pydantic import BaseModel

from openai import AsyncOpenAI


class Step(BaseModel):
    explanation: str
    output: str


class MathResponse(BaseModel):
    steps: List[Step]
    final_answer: str


async def main() -> None:
    client = AsyncOpenAI()
    id = None
    async with client.responses.stream(
        input="solve 8x + 31 = 2",
        model="gpt-4o-2024-08-06",
        text_format=MathResponse,
        background=True,
    ) as stream:
        async for event in stream:
            if event.type == "response.created":
                id = event.response.id
            if "output_text" in event.type:
                rich.print(event)
            if event.sequence_number == 10:
                break

    print("Interrupted. Continuing...")

    assert id is not None
    async with client.responses.stream(
        response_id=id,
        starting_after=10,
        text_format=MathResponse,
    ) as stream:
        async for event in stream:
            if "output_text" in event.type:
                rich.print(event)

        rich.print(stream.get_final_response())


if __name__ == "__main__":
    asyncio.run(main())



================================================
FILE: examples/responses/streaming.py
================================================
from typing import List

import rich
from pydantic import BaseModel

from openai import OpenAI


class Step(BaseModel):
    explanation: str
    output: str


class MathResponse(BaseModel):
    steps: List[Step]
    final_answer: str


client = OpenAI()

with client.responses.stream(
    input="solve 8x + 31 = 2",
    model="gpt-4o-2024-08-06",
    text_format=MathResponse,
) as stream:
    for event in stream:
        if "output_text" in event.type:
            rich.print(event)

rich.print(stream.get_final_response())



================================================
FILE: examples/responses/streaming_tools.py
================================================
from enum import Enum
from typing import List, Union

import rich
from pydantic import BaseModel

import openai
from openai import OpenAI


class Table(str, Enum):
    orders = "orders"
    customers = "customers"
    products = "products"


class Column(str, Enum):
    id = "id"
    status = "status"
    expected_delivery_date = "expected_delivery_date"
    delivered_at = "delivered_at"
    shipped_at = "shipped_at"
    ordered_at = "ordered_at"
    canceled_at = "canceled_at"


class Operator(str, Enum):
    eq = "="
    gt = ">"
    lt = "<"
    le = "<="
    ge = ">="
    ne = "!="


class OrderBy(str, Enum):
    asc = "asc"
    desc = "desc"


class DynamicValue(BaseModel):
    column_name: str


class Condition(BaseModel):
    column: str
    operator: Operator
    value: Union[str, int, DynamicValue]


class Query(BaseModel):
    table_name: Table
    columns: List[Column]
    conditions: List[Condition]
    order_by: OrderBy


client = OpenAI()

with client.responses.stream(
    model="gpt-4o-2024-08-06",
    input="look up all my orders in november of last year that were fulfilled but not delivered on time",
    tools=[
        openai.pydantic_function_tool(Query),
    ],
) as stream:
    for event in stream:
        rich.print(event)



================================================
FILE: examples/responses/structured_outputs.py
================================================
from typing import List

import rich
from pydantic import BaseModel

from openai import OpenAI


class Step(BaseModel):
    explanation: str
    output: str


class MathResponse(BaseModel):
    steps: List[Step]
    final_answer: str


client = OpenAI()

rsp = client.responses.parse(
    input="solve 8x + 31 = 2",
    model="gpt-4o-2024-08-06",
    text_format=MathResponse,
)

for output in rsp.output:
    if output.type != "message":
        raise Exception("Unexpected non message")

    for item in output.content:
        if item.type != "output_text":
            raise Exception("unexpected output type")

        if not item.parsed:
            raise Exception("Could not parse response")

        rich.print(item.parsed)

        print("answer: ", item.parsed.final_answer)

# or

message = rsp.output[0]
assert message.type == "message"

text = message.content[0]
assert text.type == "output_text"

if not text.parsed:
    raise Exception("Could not parse response")

rich.print(text.parsed)

print("answer: ", text.parsed.final_answer)



================================================
FILE: examples/responses/structured_outputs_tools.py
================================================
from enum import Enum
from typing import List, Union

import rich
from pydantic import BaseModel

import openai
from openai import OpenAI


class Table(str, Enum):
    orders = "orders"
    customers = "customers"
    products = "products"


class Column(str, Enum):
    id = "id"
    status = "status"
    expected_delivery_date = "expected_delivery_date"
    delivered_at = "delivered_at"
    shipped_at = "shipped_at"
    ordered_at = "ordered_at"
    canceled_at = "canceled_at"


class Operator(str, Enum):
    eq = "="
    gt = ">"
    lt = "<"
    le = "<="
    ge = ">="
    ne = "!="


class OrderBy(str, Enum):
    asc = "asc"
    desc = "desc"


class DynamicValue(BaseModel):
    column_name: str


class Condition(BaseModel):
    column: str
    operator: Operator
    value: Union[str, int, DynamicValue]


class Query(BaseModel):
    table_name: Table
    columns: List[Column]
    conditions: List[Condition]
    order_by: OrderBy


client = OpenAI()

response = client.responses.parse(
    model="gpt-4o-2024-08-06",
    input="look up all my orders in november of last year that were fulfilled but not delivered on time",
    tools=[
        openai.pydantic_function_tool(Query),
    ],
)

rich.print(response)

function_call = response.output[0]
assert function_call.type == "function_call"
assert isinstance(function_call.parsed_arguments, Query)
print("table name:", function_call.parsed_arguments.table_name)


