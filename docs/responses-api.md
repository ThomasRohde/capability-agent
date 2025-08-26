========================
CODE SNIPPETS
========================
TITLE: OpenAI Python Responses API Methods
DESCRIPTION: Details the available methods for interacting with the OpenAI Responses API. These methods allow for creating new responses, retrieving existing ones by ID, deleting responses, and canceling ongoing response operations.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_69

LANGUAGE: APIDOC
CODE:
```
client.responses.create(**params) -> Response
  POST /responses
  Creates a new response.
  Parameters:
    params: Additional parameters for response creation.
```

LANGUAGE: APIDOC
CODE:
```
client.responses.retrieve(response_id, **params) -> Response
  GET /responses/{response_id}
  Retrieves a response by its unique identifier.
  Parameters:
    response_id: The unique identifier of the response.
    params: Additional parameters for retrieval.
```

LANGUAGE: APIDOC
CODE:
```
client.responses.delete(response_id) -> None
  DELETE /responses/{response_id}
  Deletes a response by its unique identifier.
```

LANGUAGE: APIDOC
CODE:
```
client.responses.cancel(response_id) -> Response
  POST /responses/{response_id}/cancel
  Cancels an ongoing response operation.
```

----------------------------------------

TITLE: Integrate Responses with Evals API in OpenAI
DESCRIPTION: Integrates responses with the Evals API, suggesting improvements in how evaluation results are handled or generated in conjunction with API responses.

SOURCE: https://github.com/openai/openai-python/blob/main/CHANGELOG.md#_snippet_13

LANGUAGE: APIDOC
CODE:
```
API Update:
  - Responses integrated with Evals API.
```

----------------------------------------

TITLE: OpenAI Python Responses Input Items API
DESCRIPTION: Provides methods for listing input items associated with a specific response. This allows retrieval of the history or components of a given response.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_70

LANGUAGE: APIDOC
CODE:
```
client.responses.input_items.list(response_id, **params) -> SyncCursorPage[ResponseItem]
  GET /responses/{response_id}/input_items
  Lists input items for a given response.
  Parameters:
    response_id: The unique identifier of the response.
    params: Additional parameters for listing input items.
```

----------------------------------------

TITLE: Creating OpenAI Responses in Python
DESCRIPTION: This method allows for the creation of a new response object using the OpenAI client. It accepts a dictionary of parameters (`params`) which define the characteristics of the response to be created, returning a `Response` object upon successful execution.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_131

LANGUAGE: python
CODE:
```
client.responses.create(**params) -> Response
```

----------------------------------------

TITLE: Retrieving OpenAI Responses in Python
DESCRIPTION: This method retrieves a specific response object by its unique `response_id`. Optional parameters (`params`) can be provided to refine the retrieval, and it returns the corresponding `Response` object if found.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_132

LANGUAGE: python
CODE:
```
client.responses.retrieve(response_id, **params) -> Response
```

----------------------------------------

TITLE: Streaming Responses with Synchronous Client
DESCRIPTION: Shows how to handle streaming responses from the OpenAI API using the synchronous client. It iterates over events as they are received.

SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_snippet_9

LANGUAGE: python
CODE:
```
from openai import OpenAI

client = OpenAI()

stream = client.responses.create(
    model="gpt-4o",
    input="Write a one-sentence bedtime story about a unicorn.",
    stream=True,
)

for event in stream:
    print(event)
```

----------------------------------------

TITLE: Add API Endpoint: Get Response Input Items
DESCRIPTION: Introduces a new API endpoint (`GET /responses/{response_id}/input_items`) to retrieve input items associated with a specific response ID. This enhances the ability to inspect the original data used for a given API response.

SOURCE: https://github.com/openai/openai-python/blob/main/CHANGELOG.md#_snippet_16

LANGUAGE: APIDOC
CODE:
```
GET /responses/{response_id}/input_items
```

----------------------------------------

TITLE: Streaming Response Data
DESCRIPTION: Illustrates how to stream response data using `.with_streaming_response`. This method requires a context manager and allows iterating over the response body chunk by chunk.

SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_snippet_31

LANGUAGE: python
CODE:
```
with client.chat.completions.with_streaming_response.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-4o",
) as response:
    print(response.headers.get("X-My-Header"))

    for line in response.iter_lines():
        print(line)
```

----------------------------------------

TITLE: Using Nested Parameters for Chat Responses
DESCRIPTION: Illustrates how to use nested parameters, specifically for the `chat.responses.create` method. It shows how to structure the `input` and `response_format` parameters.

SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_snippet_17

LANGUAGE: python
CODE:
```
from openai import OpenAI

client = OpenAI()

response = client.chat.responses.create(
    input=[
        {
            "role": "user",
            "content": "How much ?",
        }
    ],
    model="gpt-4o",
    response_format={"type": "json_object"},
)
```

----------------------------------------

TITLE: OpenAI Python Responses Types
DESCRIPTION: Provides a comprehensive list of type definitions for various response events, content parts, tool calls, and other data structures used within the OpenAI Responses API. These types are crucial for understanding and manipulating the data returned by the API.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_68

LANGUAGE: python
CODE:
```
from openai.types.responses import (
    ComputerTool,
    CustomTool,
    EasyInputMessage,
    FileSearchTool,
    FunctionTool,
    Response,
    ResponseAudioDeltaEvent,
    ResponseAudioDoneEvent,
    ResponseAudioTranscriptDeltaEvent,
    ResponseAudioTranscriptDoneEvent,
    ResponseCodeInterpreterCallCodeDeltaEvent,
    ResponseCodeInterpreterCallCodeDoneEvent,
    ResponseCodeInterpreterCallCompletedEvent,
    ResponseCodeInterpreterCallInProgressEvent,
    ResponseCodeInterpreterCallInterpretingEvent,
    ResponseCodeInterpreterToolCall,
    ResponseCompletedEvent,
    ResponseComputerToolCall,
    ResponseComputerToolCallOutputItem,
    ResponseComputerToolCallOutputScreenshot,
    ResponseContent,
    ResponseContentPartAddedEvent,
    ResponseContentPartDoneEvent,
    ResponseConversationParam,
    ResponseCreatedEvent,
    ResponseCustomToolCall,
    ResponseCustomToolCallInputDeltaEvent,
    ResponseCustomToolCallInputDoneEvent,
    ResponseCustomToolCallOutput,
    ResponseError,
    ResponseErrorEvent,
    ResponseFailedEvent,
    ResponseFileSearchCallCompletedEvent,
    ResponseFileSearchCallInProgressEvent,
    ResponseFileSearchCallSearchingEvent,
    ResponseFileSearchToolCall,
    ResponseFormatTextConfig,
    ResponseFormatTextJSONSchemaConfig,
    ResponseFunctionCallArgumentsDeltaEvent,
    ResponseFunctionCallArgumentsDoneEvent,
    ResponseFunctionToolCall,
    ResponseFunctionToolCallItem,
    ResponseFunctionToolCallOutputItem,
    ResponseFunctionWebSearch,
    ResponseImageGenCallCompletedEvent,
    ResponseImageGenCallGeneratingEvent,
    ResponseImageGenCallInProgressEvent,
    ResponseImageGenCallPartialImageEvent,
    ResponseInProgressEvent,
    ResponseIncludable,
    ResponseIncompleteEvent,
    ResponseInput,
    ResponseInputAudio,
    ResponseInputContent,
    ResponseInputFile,
    ResponseInputImage,
    ResponseInputItem,
    ResponseInputMessageContentList,
    ResponseInputMessageItem,
    ResponseInputText,
    ResponseItem,
    ResponseMcpCallArgumentsDeltaEvent,
    ResponseMcpCallArgumentsDoneEvent,
    ResponseMcpCallCompletedEvent,
    ResponseMcpCallFailedEvent,
    ResponseMcpCallInProgressEvent,
    ResponseMcpListToolsCompletedEvent,
    ResponseMcpListToolsFailedEvent,
    ResponseMcpListToolsInProgressEvent,
    ResponseOutputAudio,
    ResponseOutputItem,
    ResponseOutputItemAddedEvent,
    ResponseOutputItemDoneEvent,
    ResponseOutputMessage,
    ResponseOutputRefusal,
    ResponseOutputText,
    ResponseOutputTextAnnotationAddedEvent,
    ResponsePrompt,
    ResponseQueuedEvent,
    ResponseReasoningItem,
    ResponseReasoningSummaryPartAddedEvent,
    ResponseReasoningSummaryPartDoneEvent,
    ResponseReasoningSummaryTextDeltaEvent,
    ResponseReasoningSummaryTextDoneEvent,
    ResponseReasoningTextDeltaEvent,
    ResponseReasoningTextDoneEvent,
    ResponseRefusalDeltaEvent,
    ResponseRefusalDoneEvent,
    ResponseStatus,
    ResponseStreamEvent,
    ResponseTextConfig,
    ResponseTextDeltaEvent,
    ResponseTextDoneEvent,
    ResponseUsage,
    ResponseWebSearchCallCompletedEvent,
    ResponseWebSearchCallInProgressEvent,
    ResponseWebSearchCallSearchingEvent,
    Tool,
    ToolChoiceAllowed,
    ToolChoiceCustom,
    ToolChoiceFunction,
    ToolChoiceMcp,
    ToolChoiceOptions,
    ToolChoiceTypes,
    WebSearchTool,
)
```

----------------------------------------

TITLE: Generate Text with Responses API
DESCRIPTION: Generates text using the OpenAI Responses API with a specified model and instructions. It demonstrates setting the API key from an environment variable.

SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_snippet_1

LANGUAGE: python
CODE:
```
import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

response = client.responses.create(
    model="gpt-4o",
    instructions="You are a coding assistant that talks like a pirate.",
    input="How do I check if a Python object is an instance of a class?",
)

print(response.output_text)
```

----------------------------------------

TITLE: Streaming Responses with Asynchronous Client
DESCRIPTION: Demonstrates handling streaming responses using the asynchronous OpenAI client. It uses an async for loop to process events.

SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_snippet_10

LANGUAGE: python
CODE:
```
import asyncio
from openai import AsyncOpenAI

client = AsyncOpenAI()


async def main():
    stream = await client.responses.create(
        model="gpt-4o",
        input="Write a one-sentence bedtime story about a unicorn.",
        stream=True,
    )

    async for event in stream:
        print(event)


asyncio.run(main())
```

----------------------------------------

TITLE: Deleting OpenAI Responses in Python
DESCRIPTION: This method deletes a response object identified by its `response_id`. It performs a destructive operation and returns `None` upon successful deletion, indicating the resource has been removed.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_133

LANGUAGE: python
CODE:
```
client.responses.delete(response_id) -> None
```

----------------------------------------

TITLE: Fix Types: Improve Response Type Names
DESCRIPTION: Improves the naming conventions for response types, enhancing clarity and readability in the type definitions.

SOURCE: https://github.com/openai/openai-python/blob/main/CHANGELOG.md#_snippet_30

LANGUAGE: APIDOC
CODE:
```
Bug Fix: Response type names improved.
```

----------------------------------------

TITLE: Importing OpenAI Response Types in Python
DESCRIPTION: This snippet imports a comprehensive set of data types from the `openai.types.responses` module. These types represent various components and events related to API responses, including different tool types, content formats, and lifecycle events, enabling structured handling of response data.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_130

LANGUAGE: python
CODE:
```
from openai.types.responses import (
    ComputerTool,
    EasyInputMessage,
    FileSearchTool,
    FunctionTool,
    Response,
    ResponseAudioDeltaEvent,
    ResponseAudioDoneEvent,
    ResponseAudioTranscriptDeltaEvent,
    ResponseAudioTranscriptDoneEvent,
    ResponseCodeInterpreterCallCodeDeltaEvent,
    ResponseCodeInterpreterCallCodeDoneEvent,
    ResponseCodeInterpreterCallCompletedEvent,
    ResponseCodeInterpreterCallInProgressEvent,
    ResponseCodeInterpreterCallInterpretingEvent,
    ResponseCodeInterpreterToolCall,
    ResponseCompletedEvent,
    ResponseComputerToolCall,
    ResponseComputerToolCallOutputItem,
    ResponseComputerToolCallOutputScreenshot,
    ResponseContent,
    ResponseContentPartAddedEvent,
    ResponseContentPartDoneEvent,
    ResponseCreatedEvent,
    ResponseError,
    ResponseErrorEvent,
    ResponseFailedEvent,
    ResponseFileSearchCallCompletedEvent,
    ResponseFileSearchCallInProgressEvent,
    ResponseFileSearchCallSearchingEvent,
    ResponseFileSearchToolCall,
    ResponseFormatTextConfig,
    ResponseFormatTextJSONSchemaConfig,
    ResponseFunctionCallArgumentsDeltaEvent,
    ResponseFunctionCallArgumentsDoneEvent,
    ResponseFunctionToolCall,
    ResponseFunctionToolCallItem,
    ResponseFunctionToolCallOutputItem,
    ResponseFunctionWebSearch,
    ResponseImageGenCallCompletedEvent,
    ResponseImageGenCallGeneratingEvent,
    ResponseImageGenCallInProgressEvent,
    ResponseImageGenCallPartialImageEvent,
    ResponseInProgressEvent,
    ResponseIncludable,
    ResponseIncompleteEvent,
    ResponseInput,
    ResponseInputAudio,
    ResponseInputContent,
    ResponseInputFile,
    ResponseInputImage,
    ResponseInputItem,
    ResponseInputMessageContentList,
    ResponseInputMessageItem,
    ResponseInputText,
    ResponseItem,
    ResponseMcpCallArgumentsDeltaEvent,
    ResponseMcpCallArgumentsDoneEvent,
    ResponseMcpCallCompletedEvent,
    ResponseMcpCallFailedEvent,
    ResponseMcpCallInProgressEvent,
    ResponseMcpListToolsCompletedEvent,
    ResponseMcpListToolsFailedEvent,
    ResponseMcpListToolsInProgressEvent,
    ResponseOutputAudio,
    ResponseOutputItem,
    ResponseOutputItemAddedEvent,
    ResponseOutputItemDoneEvent,
    ResponseOutputMessage,
    ResponseOutputRefusal,
    ResponseOutputText,
    ResponseOutputTextAnnotationAddedEvent,
    ResponseQueuedEvent,
    ResponseReasoningDeltaEvent,
    ResponseReasoningDoneEvent,
    ResponseReasoningItem,
    ResponseReasoningSummaryDeltaEvent,
    ResponseReasoningSummaryDoneEvent,
    ResponseReasoningSummaryPartAddedEvent,
    ResponseReasoningSummaryPartDoneEvent,
    ResponseReasoningSummaryTextDeltaEvent,
    ResponseReasoningSummaryTextDoneEvent,
    ResponseRefusalDeltaEvent,
    ResponseRefusalDoneEvent,
    ResponseStatus,
    ResponseStreamEvent,
    ResponseTextConfig,
    ResponseTextDeltaEvent,
    ResponseTextDoneEvent,
    ResponseUsage,
    ResponseWebSearchCallCompletedEvent,
    ResponseWebSearchCallInProgressEvent,
    ResponseWebSearchCallSearchingEvent,
    Tool,
    ToolChoiceFunction,
    ToolChoiceOptions,
    ToolChoiceTypes,
    WebSearchTool,
)
```

----------------------------------------

TITLE: Listing OpenAI Response Input Items in Python
DESCRIPTION: This method retrieves a paginated list of input items associated with a specific `response_id`. It supports optional parameters (`params`) for filtering or pagination and returns a `SyncCursorPage` containing `ResponseItem` objects.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_136

LANGUAGE: python
CODE:
```
client.responses.input_items.list(response_id, **params) -> SyncCursorPage[ResponseItem]
```

----------------------------------------

TITLE: Auto-parsing Pydantic Models with Chat Completions
DESCRIPTION: Demonstrates how to use the `client.chat.completions.parse()` method to automatically parse API responses into Pydantic models. This simplifies data extraction by converting the model to a JSON schema, sending it to the API, and parsing the response back into the specified Pydantic object. It handles cases where the model might refuse to parse.

SOURCE: https://github.com/openai/openai-python/blob/main/helpers.md#_snippet_0

LANGUAGE: python
CODE:
```
from typing import List
from pydantic import BaseModel
from openai import OpenAI

class Step(BaseModel):
    explanation: str
    output: str

class MathResponse(BaseModel):
    steps: List[Step]
    final_answer: str

client = OpenAI()
completion = client.chat.completions.parse(
    model="gpt-4o-2024-08-06",
    messages=[
        {"role": "system", "content": "You are a helpful math tutor."},
        {"role": "user", "content": "solve 8x + 31 = 2"},
    ],
    response_format=MathResponse,
)

message = completion.choices[0].message
if message.parsed:
    print(message.parsed.steps)
    print("answer: ", message.parsed.final_answer)
else:
    print(message.refusal)
```

----------------------------------------

TITLE: Importing File Response Types for Containers in Python
DESCRIPTION: This snippet imports the necessary response types for file operations specifically within containers from the `openai.types.containers` module. These types define the structure of data returned when interacting with files associated with a container.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_157

LANGUAGE: python
CODE:
```
from openai.types.containers import FileCreateResponse, FileRetrieveResponse, FileListResponse
```

----------------------------------------

TITLE: Cancelling OpenAI Responses in Python
DESCRIPTION: This method cancels an in-progress response identified by its `response_id`. It attempts to stop the ongoing operation and returns the updated `Response` object, which typically reflects a cancelled status.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_134

LANGUAGE: python
CODE:
```
client.responses.cancel(response_id) -> Response
```

----------------------------------------

TITLE: OpenAI Chat Completions API - Structured Outputs
DESCRIPTION: Details the OpenAI API's capability to extract JSON from model responses using the `response_format` parameter. This section references a guide for more in-depth information on the API itself. It highlights the SDK's `parse()` method as a wrapper for `create()` that enhances Python integration.

SOURCE: https://github.com/openai/openai-python/blob/main/helpers.md#_snippet_2

LANGUAGE: APIDOC
CODE:
```
OpenAI API:
  Chat Completions:
    response_format: object
      Allows extraction of JSON from the model response.
      See: https://platform.openai.com/docs/guides/structured-outputs

SDK Wrapper:
  client.chat.completions.parse()
    - Wrapper for client.chat.completions.create().
    - Provides richer integrations with Python types.
    - Returns a ParsedChatCompletion object (subclass of ChatCompletion).

Restrictions for .parse():
  - Raises LengthFinishReasonError or ContentFilterFinishReasonError if finish_reason is 'length' or 'content_filter'.
  - Only accepts strict function tools (e.g., {'type': 'function', 'function': {..., 'strict': True}}).
```

----------------------------------------

TITLE: Chat Completions Stream Helpers
DESCRIPTION: Provides helper methods for interacting with streaming Chat Completions. `.get_final_completion()` retrieves the complete response, while `.until_done()` waits for the stream to finish.

SOURCE: https://github.com/openai/openai-python/blob/main/helpers.md#_snippet_5

LANGUAGE: python
CODE:
```
async with client.chat.completions.stream(...) as stream:
    ...

completion = await stream.get_final_completion()
print(completion.choices[0].message)
```

LANGUAGE: python
CODE:
```
async with client.chat.completions.stream(...) as stream:
    await stream.until_done()
    # stream is now finished
```

----------------------------------------

TITLE: Vision - Image from URL
DESCRIPTION: Processes an image from a URL using the Responses API to answer a prompt. It includes the image URL directly in the input.

SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_snippet_3

LANGUAGE: python
CODE:
```
prompt = "What is in this image?"
img_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/2023_06_08_Raccoon1.jpg/1599px-2023_06_08_Raccoon1.jpg"

response = client.responses.create(
    model="gpt-4o-mini",
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": prompt},
                {"type": "input_image", "image_url": f"{img_url}"},
            ],
        }
    ],
)
```

----------------------------------------

TITLE: Accessing Raw Response Data
DESCRIPTION: Demonstrates how to access the raw HTTP response, including headers, using `.with_raw_response`. It also shows how to parse the response body into the expected object.

SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_snippet_30

LANGUAGE: python
CODE:
```
from openai import OpenAI

client = OpenAI()
response = client.chat.completions.with_raw_response.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-4o",
)
print(response.headers.get('X-My-Header'))

completion = response.parse()  # get the object that `chat.completions.create()` would have returned
print(completion)
```

----------------------------------------

TITLE: Importing Container Response Types in Python
DESCRIPTION: This snippet imports the necessary response types for container operations from the `openai.types` module. These types define the structure of data returned by the API when performing actions such as creating, retrieving, or listing containers.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_152

LANGUAGE: python
CODE:
```
from openai.types import ContainerCreateResponse, ContainerRetrieveResponse, ContainerListResponse
```

----------------------------------------

TITLE: Creating Assistant API Streams
DESCRIPTION: Details the different methods available for initiating streaming responses with the Assistant API. These include streaming an existing run, creating a thread and running it, and streaming tool outputs.

SOURCE: https://github.com/openai/openai-python/blob/main/helpers.md#_snippet_9

LANGUAGE: python
CODE:
```
client.beta.threads.runs.stream()
```

LANGUAGE: python
CODE:
```
client.beta.threads.create_and_run_stream()
```

LANGUAGE: python
CODE:
```
client.beta.threads.runs.submit_tool_outputs_stream()
```

----------------------------------------

TITLE: Importing OpenAI ResponseItemList Type in Python
DESCRIPTION: This snippet imports the `ResponseItemList` type from the `openai.types.responses` module. This type is used to represent a list of input items associated with a response, typically when paginating through them.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_135

LANGUAGE: python
CODE:
```
from openai.types.responses import ResponseItemList
```

----------------------------------------

TITLE: Using TypedDicts and Pydantic Models
DESCRIPTION: Explains the use of TypedDicts for request parameters and Pydantic models for responses in the OpenAI Python library. These provide type safety and helper methods.

SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_snippet_13

LANGUAGE: python
CODE:
```
from openai import OpenAI

client = OpenAI()

all_jobs = []

```

----------------------------------------

TITLE: OpenAI Embeddings Types
DESCRIPTION: Imports types related to embedding creation, including response and model types.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_7

LANGUAGE: python
CODE:
```
from openai.types import CreateEmbeddingResponse, Embedding, EmbeddingModel
```

----------------------------------------

TITLE: OpenAI Evals Types
DESCRIPTION: Defines the data structures for managing evaluations, including data source configurations and response types for various operations.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_76

LANGUAGE: python
CODE:
```
from openai.types import (
    EvalCustomDataSourceConfig,
    EvalStoredCompletionsDataSourceConfig,
    EvalCreateResponse,
    EvalRetrieveResponse,
    EvalUpdateResponse,
    EvalListResponse,
    EvalDeleteResponse,
)
```

----------------------------------------

TITLE: OpenAI Python SDK Types for Run Output Items
DESCRIPTION: Specifies the Python types for output items associated with runs, including response types for retrieving and listing output items.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_82

LANGUAGE: python
CODE:
```
from openai.types.evals.runs import OutputItemRetrieveResponse, OutputItemListResponse
```

----------------------------------------

TITLE: OpenAI Completions Types
DESCRIPTION: Imports specific types related to text completion requests and responses.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_1

LANGUAGE: python
CODE:
```
from openai.types import Completion, CompletionChoice, CompletionUsage
```

----------------------------------------

TITLE: OpenAI Python SDK Types for Containers
DESCRIPTION: Defines the Python types for container operations, covering response objects for creating, retrieving, and listing containers.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_83

LANGUAGE: python
CODE:
```
from openai.types import ContainerCreateResponse, ContainerRetrieveResponse, ContainerListResponse
```

----------------------------------------

TITLE: OpenAI Chat Completions Types
DESCRIPTION: Imports a comprehensive set of types for chat completion requests and responses, including message parameters, tool choices, and content parts.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_4

LANGUAGE: python
CODE:
```
from openai.types.chat import (
    ChatCompletion,
    ChatCompletionAllowedToolChoice,
    ChatCompletionAssistantMessageParam,
    ChatCompletionAudio,
    ChatCompletionAudioParam,
    ChatCompletionChunk,
    ChatCompletionContentPart,
    ChatCompletionContentPartImage,
    ChatCompletionContentPartInputAudio,
    ChatCompletionContentPartRefusal,
    ChatCompletionContentPartText,
    ChatCompletionCustomTool,
    ChatCompletionDeleted,
    ChatCompletionDeveloperMessageParam,
    ChatCompletionFunctionCallOption,
    ChatCompletionFunctionMessageParam,
    ChatCompletionFunctionTool,
    ChatCompletionMessage,
    ChatCompletionMessageCustomToolCall,
    ChatCompletionMessageFunctionToolCall,
    ChatCompletionMessageParam,
    ChatCompletionMessageToolCallUnion,
    ChatCompletionModality,
    ChatCompletionNamedToolChoice,
    ChatCompletionNamedToolChoiceCustom,
    ChatCompletionPredictionContent,
    ChatCompletionRole,
    ChatCompletionStoreMessage,
    ChatCompletionStreamOptions,
    ChatCompletionSystemMessageParam,
    ChatCompletionTokenLogprob,
    ChatCompletionToolUnion,
    ChatCompletionToolChoiceOption,
    ChatCompletionToolMessageParam,
    ChatCompletionUserMessageParam,
    ChatCompletionAllowedTools,
    ChatCompletionReasoningEffort,
)
```

----------------------------------------

TITLE: OpenAI Python SDK Types for Container Files
DESCRIPTION: Specifies the Python types for file management within containers, including response types for creating, retrieving, and listing files.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_84

LANGUAGE: python
CODE:
```
from openai.types.containers import FileCreateResponse, FileRetrieveResponse, FileListResponse
```

----------------------------------------

TITLE: Differentiating Null vs. Missing Fields
DESCRIPTION: Explains how to distinguish between a field explicitly set to `null` and a field that is missing entirely in an API response using the `.model_fields_set` attribute.

SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_snippet_29

LANGUAGE: python
CODE:
```
if response.my_field is None:
  if 'my_field' not in response.model_fields_set:
    print('Got json like {}, without a "my_field" key present at all.')
  else:
    print('Got json like {"my_field": null}.')
```

----------------------------------------

TITLE: Vision - Image as Base64 String
DESCRIPTION: Processes an image file encoded as a base64 string using the Responses API. The image is read from a local file path and embedded in the input.

SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_snippet_4

LANGUAGE: python
CODE:
```
import base64
from openai import OpenAI

client = OpenAI()

prompt = "What is in this image?"
with open("path/to/image.png", "rb") as image_file:
    b64_image = base64.b64encode(image_file.read()).decode("utf-8")

response = client.responses.create(
    model="gpt-4o-mini",
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": prompt},
                {"type": "input_image", "image_url": f"data:image/png;base64,{b64_image}"},
            ],
        }
    ],
)
```

----------------------------------------

TITLE: Assistant Streaming API - Event Handling
DESCRIPTION: Demonstrates how to create a custom event handler for streaming Assistant API responses. The `AssistantEventHandler` class allows overriding methods like `on_text_created`, `on_text_delta`, `on_tool_call_created`, and `on_tool_call_delta` to process different event types.

SOURCE: https://github.com/openai/openai-python/blob/main/helpers.md#_snippet_6

LANGUAGE: python
CODE:
```
from typing_extensions import override
from openai import AssistantEventHandler, OpenAI
from openai.types.beta.threads import Text, TextDelta
from openai.types.beta.threads.runs import ToolCall, ToolCallDelta

client = openai.OpenAI()

class EventHandler(AssistantEventHandler):
  @override
  def on_text_created(self, text: Text) -> None:
    print(f"\nassistant > ", end="", flush=True)

  @override
  def on_text_delta(self, delta: TextDelta, snapshot: Text):
    print(delta.value, end="", flush=True)

  @override
  def on_tool_call_created(self, tool_call: ToolCall):
    print(f"\nassistant > {tool_call.type}\n", flush=True)

  @override
  def on_tool_call_delta(self, delta: ToolCallDelta, snapshot: ToolCall):
    if delta.type == "code_interpreter" and delta.code_interpreter:
      if delta.code_interpreter.input:
        print(delta.code_interpreter.input, end="", flush=True)
      if delta.code_interpreter.outputs:
        print(f"\n\noutput >", flush=True)
        for output in delta.code_interpreter.outputs:
          if output.type == "logs":
            print(f"\n{output.logs}", flush=True)

with client.beta.threads.runs.stream(
  thread_id="thread_id",
  assistant_id="assistant_id",
  event_handler=EventHandler(),
) as stream:
  stream.until_done()
```

----------------------------------------

TITLE: Access Request IDs
DESCRIPTION: Shows how to retrieve the `_request_id` from an API response, which is useful for debugging and reporting issues to OpenAI. It demonstrates accessing this ID from both successful and failed requests.

SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_snippet_23

LANGUAGE: python
CODE:
```
response = await client.responses.create(
    model="gpt-4o-mini",
    input="Say 'this is a test'.",
)
print(response._request_id)  # req_123
```

LANGUAGE: python
CODE:
```
import openai

try:
    completion = await client.chat.completions.create(
        messages=[{"role": "user", "content": "Say this is a test"}], model="gpt-4"
    )
except openai.APIStatusError as exc:
    print(exc.request_id)  # req_123
    raise exc
```

----------------------------------------

TITLE: Realtime API Basic Text Example
DESCRIPTION: Provides a basic example of using the Realtime API for text-based conversations. It connects to the API, updates modalities, sends a message, and processes text responses.

SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_snippet_11

LANGUAGE: python
CODE:
```
import asyncio
from openai import AsyncOpenAI

async def main():
    client = AsyncOpenAI()

    async with client.beta.realtime.connect(model="gpt-4o-realtime-preview") as connection:
        await connection.session.update(session={'modalities': ['text']})

        await connection.conversation.item.create(
            item={
                "type": "message",
                "role": "user",
                "content": [{"type": "input_text", "text": "Say hello!"}],
            }
        )
        await connection.response.create()

        async for event in connection:
            if event.type == 'response.text.delta':
                print(event.delta, flush=True, end="")

            elif event.type == 'response.text.done':
                print()

            elif event.type == "response.done":
                break

asyncio.run(main())
```

----------------------------------------

TITLE: OpenAI Runs API
DESCRIPTION: Manages runs for evaluations, including creation, retrieval, listing, deletion, and cancellation. It utilizes specific request and response types for each operation.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_77

LANGUAGE: APIDOC
CODE:
```
POST /evals/{eval_id}/runs
  - Creates a new run for a given evaluation.
  - Parameters:
    - eval_id: The ID of the evaluation.
    - params: Additional parameters for run creation.
  - Returns: RunCreateResponse

GET /evals/{eval_id}/runs/{run_id}
  - Retrieves a specific run by its ID.
  - Parameters:
    - run_id: The ID of the run to retrieve.
    - eval_id: The ID of the evaluation the run belongs to.
  - Returns: RunRetrieveResponse

GET /evals/{eval_id}/runs
  - Lists all runs for a given evaluation.
  - Parameters:
    - eval_id: The ID of the evaluation.
    - params: Additional parameters for listing runs.
  - Returns: SyncCursorPage[RunListResponse]

DELETE /evals/{eval_id}/runs/{run_id}
  - Deletes a specific run.
  - Parameters:
    - run_id: The ID of the run to delete.
    - eval_id: The ID of the evaluation the run belongs to.
  - Returns: RunDeleteResponse

POST /evals/{eval_id}/runs/{run_id}
  - Cancels a specific run.
  - Parameters:
    - run_id: The ID of the run to cancel.
    - eval_id: The ID of the evaluation the run belongs to.
  - Returns: RunCancelResponse
```

----------------------------------------

TITLE: OpenAI Python SDK Types for Runs
DESCRIPTION: Defines the Python types used for various run-related operations in the OpenAI SDK, including data sources, errors, and response objects for create, retrieve, list, delete, and cancel actions.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_81

LANGUAGE: python
CODE:
```
from openai.types.evals import (
    CreateEvalCompletionsRunDataSource,
    CreateEvalJSONLRunDataSource,
    EvalAPIError,
    RunCreateResponse,
    RunRetrieveResponse,
    RunListResponse,
    RunDeleteResponse,
    RunCancelResponse,
)
```

----------------------------------------

TITLE: Making Undocumented POST Requests
DESCRIPTION: Shows how to make requests to undocumented API endpoints using `client.post`. It demonstrates specifying the response type and providing a request body.

SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_snippet_32

LANGUAGE: python
CODE:
```
import httpx

response = client.post(
    "/foo",
    cast_to=httpx.Response,
    body={"my_param": True},
)

print(response.headers.get("x-foo"))
```

----------------------------------------

TITLE: Retrieve Container File Content
DESCRIPTION: This method allows you to retrieve the content of a specific file within a container. It requires the file ID and the container ID as parameters and returns the file content as a binary response.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_85

LANGUAGE: Python
CODE:
```
client.containers.files.content.retrieve(file_id, container_id=container_id)
```

----------------------------------------

TITLE: Importing OpenAI Thread Types (Python)
DESCRIPTION: This Python snippet imports essential type definitions from the `openai.types.beta` module. These types, including `Thread` and `ThreadDeleted`, are crucial for defining and interacting with Thread objects and their associated properties like response formats and tool choices within the OpenAI API.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_90

LANGUAGE: Python
CODE:
```
from openai.types.beta import (
    AssistantResponseFormatOption,
    AssistantToolChoice,
    AssistantToolChoiceFunction,
    AssistantToolChoiceOption,
    Thread,
    ThreadDeleted,
)
```

----------------------------------------

TITLE: Importing Evals API Types in Python
DESCRIPTION: This snippet imports various data types used for interacting with the OpenAI Evals API. These types define the structure of configuration objects, request parameters, and response payloads for evaluation operations.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_137

LANGUAGE: Python
CODE:
```
from openai.types import (
    EvalCustomDataSourceConfig,
    EvalStoredCompletionsDataSourceConfig,
    EvalCreateResponse,
    EvalRetrieveResponse,
    EvalUpdateResponse,
    EvalListResponse,
    EvalDeleteResponse,
)
```

----------------------------------------

TITLE: Importing Evals Runs API Types in Python
DESCRIPTION: This snippet imports various data types specific to managing evaluation runs within the OpenAI Evals API. These types define the structure for creating run data sources, handling API errors, and managing run responses.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_143

LANGUAGE: Python
CODE:
```
from openai.types.evals import (
    CreateEvalCompletionsRunDataSource,
    CreateEvalJSONLRunDataSource,
    EvalAPIError,
    RunCreateResponse,
    RunRetrieveResponse,
    RunListResponse,
    RunDeleteResponse,
    RunCancelResponse,
)
```

----------------------------------------

TITLE: Listing Evals in OpenAI Python
DESCRIPTION: This method retrieves a paginated list of evaluations. It can accept parameters for filtering or pagination, returning a SyncCursorPage of EvalListResponse objects.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_141

LANGUAGE: Python
CODE:
```
client.evals.list(**params)
```

----------------------------------------

TITLE: Importing Batch Types for OpenAI Python API
DESCRIPTION: This snippet imports essential type definitions for managing batch operations in the OpenAI API. These types, `Batch`, `BatchError`, and `BatchRequestCounts`, are used to define the structure of batch objects, error responses, and request count summaries, facilitating the creation, retrieval, and cancellation of batch requests.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_119

LANGUAGE: python
CODE:
```
from openai.types import Batch, BatchError, BatchRequestCounts
```

----------------------------------------

TITLE: Submitting Tool Outputs for a Run (OpenAI Python)
DESCRIPTION: This method is used to provide the outputs of tool calls back to a run that is in a 'requires_action' state. It takes `run_id`, `thread_id`, and `params` containing the tool outputs, returning the updated `Run` object.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_104

LANGUAGE: Python
CODE:
```
client.beta.threads.runs.submit_tool_outputs(run_id, *, thread_id, **params)
```

----------------------------------------

TITLE: Creating an Eval in OpenAI Python
DESCRIPTION: This method creates a new evaluation. It accepts various parameters to configure the evaluation, returning an EvalCreateResponse object upon success.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_138

LANGUAGE: Python
CODE:
```
client.evals.create(**params)
```

----------------------------------------

TITLE: OpenAI Assistant Convenience Methods
DESCRIPTION: Access additional context from within event handlers or retrieve accumulated data at the end of a stream. These methods provide access to the current state or final results of assistant operations.

SOURCE: https://github.com/openai/openai-python/blob/main/helpers.md#_snippet_11

LANGUAGE: python
CODE:
```
def current_event() -> AssistantStreamEvent | None
def current_run() -> Run | None
def current_message_snapshot() -> Message | None
def current_run_step_snapshot() -> RunStep | None

def get_final_run(self) -> Run
def get_final_run_steps(self) -> List[RunStep]
def get_final_messages(self) -> List[Message]
```

----------------------------------------

TITLE: Listing Eval Run Output Items in OpenAI Python
DESCRIPTION: This method retrieves a paginated list of output items for a specific evaluation run, identified by `run_id` and `eval_id`. It can accept parameters for filtering or pagination, returning a SyncCursorPage of OutputItemListResponse objects.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_151

LANGUAGE: Python
CODE:
```
client.evals.runs.output_items.list(run_id, *, eval_id, **params)
```

----------------------------------------

TITLE: OpenAI Python SDK - Submit Tool Outputs and Poll
DESCRIPTION: Demonstrates the `submit_tool_outputs_and_poll` method for submitting tool outputs and waiting for the run to complete.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_58

LANGUAGE: python
CODE:
```
from openai import OpenAI

client = OpenAI()

run = client.beta.threads.runs.submit_tool_outputs_and_poll(
    run_id="run_id",
    thread_id="thread_id",
    tool_outputs=[
        {
            "tool_call_id": "call_id",
            "output": "output",
        }
    ],
)
```

----------------------------------------

TITLE: OpenAI API Reference - Assistants Convenience Methods
DESCRIPTION: Convenience methods available on the assistant streaming object to access contextual information during event handling or to retrieve final results after stream completion.

SOURCE: https://github.com/openai/openai-python/blob/main/helpers.md#_snippet_14

LANGUAGE: APIDOC
CODE:
```
Assistant Streaming Object Methods:

- **Context Access**:
  - `current_event() -> AssistantStreamEvent | None`: Returns the current event being processed.
  - `current_run() -> Run | None`: Returns the current Run object.
  - `current_message_snapshot() -> Message | None`: Returns a snapshot of the current Message.
  - `current_run_step_snapshot() -> RunStep | None`: Returns a snapshot of the current RunStep.
  *Note: Context may be `None` if not applicable.*

- **Final Result Retrieval**:
  - `get_final_run() -> Run`: Consumes the stream to completion and returns the final Run object.
  - `get_final_run_steps() -> List[RunStep]`: Consumes the stream to completion and returns a list of all RunStep objects.
  - `get_final_messages() -> List[Message]`: Consumes the stream to completion and returns a list of all Message objects.
```

----------------------------------------

TITLE: Assistant Streaming API - Iterating Over Text Deltas
DESCRIPTION: Provides a convenient way to iterate specifically over text deltas received from the Assistant API stream, filtering out other event types.

SOURCE: https://github.com/openai/openai-python/blob/main/helpers.md#_snippet_8

LANGUAGE: python
CODE:
```
with client.beta.threads.runs.stream(
  thread_id=thread.id,
  assistant_id=assistant.id
) as stream:
    for text in stream.text_deltas:
        print(text)
```

----------------------------------------

TITLE: Listing Eval Runs in OpenAI Python
DESCRIPTION: This method retrieves a paginated list of runs for a given `eval_id`. It can accept parameters for filtering or pagination, returning a SyncCursorPage of RunListResponse objects.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_146

LANGUAGE: Python
CODE:
```
client.evals.runs.list(eval_id, **params)
```

----------------------------------------

TITLE: Submitting Tool Outputs and Polling Run (OpenAI Python)
DESCRIPTION: This method submits tool outputs to a run and then synchronously polls for its completion. It's a convenience for blocking operations after providing tool results, returning the final `Run` object.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_109



----------------------------------------

TITLE: Streaming Chat Completions with AsyncOpenAI
DESCRIPTION: Demonstrates how to use the `.chat.completions.stream()` method with `AsyncOpenAI` for asynchronous streaming of chat completions. It highlights the necessity of using a context manager for proper resource handling and iterating through events.

SOURCE: https://github.com/openai/openai-python/blob/main/helpers.md#_snippet_3

LANGUAGE: python
CODE:
```
from openai import AsyncOpenAI

client = AsyncOpenAI()

async with client.chat.completions.stream(
    model='gpt-4o-2024-08-06',
    messages=[...],
) as stream:
    async for event in stream:
        if event.type == 'content.delta':
            print(event.content, flush=True, end='')
```

----------------------------------------

TITLE: Assistant Streaming API - Iterating Over Events
DESCRIPTION: Shows how to iterate through all streamed events from the Assistant API. This allows for granular processing of each event as it arrives, such as printing text delta content.

SOURCE: https://github.com/openai/openai-python/blob/main/helpers.md#_snippet_7

LANGUAGE: python
CODE:
```
with client.beta.threads.runs.stream(
  thread_id=thread.id,
  assistant_id=assistant.id
) as stream:
    for event in stream:
        # Print the text from text delta events
        if event.event == "thread.message.delta" and event.data.delta.content:
            print(event.data.delta.content[0].text)
```

----------------------------------------

TITLE: Listing Containers with OpenAI Python Client
DESCRIPTION: This method allows for listing multiple containers, with optional filtering capabilities provided through `**params`. It returns a `SyncCursorPage` object, which facilitates pagination through a collection of `ContainerListResponse` objects.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_155

LANGUAGE: python
CODE:
```
client.containers.list(**params) -> SyncCursorPage[ContainerListResponse]
```

----------------------------------------

TITLE: OpenAI Python SDK - Submit Tool Outputs
DESCRIPTION: Illustrates how to submit tool outputs for a run that requires them, using the OpenAI Python SDK. This is crucial for functions or tools called by the assistant.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_53

LANGUAGE: python
CODE:
```
from openai import OpenAI

client = OpenAI()

run = client.beta.threads.runs.submit_tool_outputs(
    run_id="run_id",
    thread_id="thread_id",
    tool_outputs=[
        {
            "tool_call_id": "call_id",
            "output": "output",
        }
    ],
)
```

----------------------------------------

TITLE: Listing Messages in an OpenAI Thread (Python)
DESCRIPTION: This method retrieves a paginated list of messages from a specified thread. It requires `thread_id` and can accept additional parameters for filtering or pagination, returning a `SyncCursorPage[Message]` object.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_117

LANGUAGE: python
CODE:
```
client.beta.threads.messages.list(thread_id, **params) -> SyncCursorPage[Message]
```

----------------------------------------

TITLE: OpenAI Polling Helpers
DESCRIPTION: SDK helper functions for polling asynchronous API actions until they reach a terminal state. These methods simplify managing operations like creating runs or uploading files.

SOURCE: https://github.com/openai/openai-python/blob/main/helpers.md#_snippet_12

LANGUAGE: python
CODE:
```
client.beta.threads.create_and_run_poll(...)
client.beta.threads.runs.create_and_poll(...)
client.beta.threads.runs.submit_tool_outputs_and_poll(...)
client.beta.vector_stores.files.upload_and_poll(...)
client.beta.vector_stores.files.create_and_poll(...)
client.beta.vector_stores.file_batches.create_and_poll(...)
client.beta.vector_stores.file_batches.upload_and_poll(...)
```

----------------------------------------

TITLE: Retrieving an Eval in OpenAI Python
DESCRIPTION: This method retrieves a specific evaluation by its unique `eval_id`. It returns an EvalRetrieveResponse object containing the details of the requested evaluation.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_139

LANGUAGE: Python
CODE:
```
client.evals.retrieve(eval_id)
```

----------------------------------------

TITLE: OpenAI Python SDK - Submit Tool Outputs and Stream
DESCRIPTION: Shows how to use `submit_tool_outputs_stream` to submit tool outputs and receive a stream of events.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_59

LANGUAGE: python
CODE:
```
from openai import OpenAI
from openai.types.beta import AssistantStreamEventHandler

client = OpenAI()

stream = client.beta.threads.runs.submit_tool_outputs_stream(
    run_id="run_id",
    thread_id="thread_id",
    tool_outputs=[
        {
            "tool_call_id": "call_id",
            "output": "output",
        }
    ],
)

for event in stream:
    if isinstance(event, AssistantStreamEventHandler):
        print(event.data.content[0].text.value)

```

----------------------------------------

TITLE: Listing Assistants in Python
DESCRIPTION: This method retrieves a paginated list of assistants. It can accept parameters (`params`) for filtering or pagination and returns a `SyncCursorPage` containing `Assistant` objects.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_88

LANGUAGE: python
CODE:
```
client.beta.assistants.list(**params) -> SyncCursorPage[Assistant]
```

----------------------------------------

TITLE: Chat Completions API Events
DESCRIPTION: Provides a detailed reference for the various event types emitted by the Chat Completions streaming API. Each event type is described along with its associated properties, offering insights into the structure of streamed data.

SOURCE: https://github.com/openai/openai-python/blob/main/helpers.md#_snippet_4

LANGUAGE: APIDOC
CODE:
```
Chat Completions API Events:

These events allow you to track the progress of the chat completion generation, access partial results, and handle different aspects of the stream separately.

Below is a list of the different event types you may encounter:

ChunkEvent:
  Emitted for every chunk received from the API.
  - type: "chunk"
  - chunk: The raw ChatCompletionChunk object received from the API
  - snapshot: The current accumulated state of the chat completion

ContentDeltaEvent:
  Emitted for every chunk containing new content.
  - type: "content.delta"
  - delta: The new content string received in this chunk
  - snapshot: The accumulated content so far
  - parsed: The partially parsed content (if applicable)

ContentDoneEvent:
  Emitted when the content generation is complete. May be fired multiple times if there are multiple choices.
  - type: "content.done"
  - content: The full generated content
  - parsed: The fully parsed content (if applicable)

RefusalDeltaEvent:
  Emitted when a chunk contains part of a content refusal.
  - type: "refusal.delta"
  - delta: The new refusal content string received in this chunk
  - snapshot: The accumulated refusal content string so far

RefusalDoneEvent:
  Emitted when the refusal content is complete.
  - type: "refusal.done"
  - refusal: The full refusal content

FunctionToolCallArgumentsDeltaEvent:
  Emitted when a chunk contains part of a function tool call's arguments.
  - type: "tool_calls.function.arguments.delta"
  - name: The name of the function being called
  - index: The index of the tool call
  - arguments: The accumulated raw JSON string of arguments
  - parsed_arguments: The partially parsed arguments object
  - arguments_delta: The new JSON string fragment received in this chunk

FunctionToolCallArgumentsDoneEvent:
  Emitted when a function tool call's arguments are complete.
  - type: "tool_calls.function.arguments.done"
  - name: The name of the function being called
  - index: The index of the tool call
  - arguments: The full raw JSON string of arguments
  - parsed_arguments: The fully parsed arguments object. If you used openai.pydantic_function_tool() this will be an instance of the given model.

LogprobsContentDeltaEvent:
  Emitted when a chunk contains new content log probabilities.
  - type: "logprobs.content.delta"
  - content: A list of the new log probabilities received in this chunk
  - snapshot: A list of the accumulated log probabilities so far

LogprobsContentDoneEvent:
  Emitted when all content log probabilities have been received.
  - type: "logprobs.content.done"
  - content: The full list of token log probabilities for the content

LogprobsRefusalDeltaEvent:
  Emitted when a chunk contains new refusal log probabilities.
  - type: "logprobs.refusal.delta"
  - refusal: A list of the new log probabilities received in this chunk
  - snapshot: A list of the accumulated log probabilities so far

LogprobsRefusalDoneEvent:
  Emitted when all refusal log probabilities have been received.
  - type: "logprobs.refusal.done"
  - refusal: The full list of token log probabilities for the refusal
```

----------------------------------------

TITLE: OpenAI API Reference - Polling Helpers
DESCRIPTION: Helper functions provided by the SDK to poll asynchronous API actions until they reach a terminal state. These methods simplify the management of operations that take time to complete, such as starting runs or uploading files.

SOURCE: https://github.com/openai/openai-python/blob/main/helpers.md#_snippet_15

LANGUAGE: APIDOC
CODE:
```
Polling Helper Functions:

These functions poll the status of asynchronous operations until a terminal state is reached, returning the resulting object. They are indicated by methods ending in `_and_poll`.

- **Thread and Run Operations**:
  - `client.beta.threads.create_and_run_poll(...)`: Creates a thread and polls for run completion.
  - `client.beta.threads.runs.create_and_poll(...)`: Creates a run and polls for completion.
  - `client.beta.threads.runs.submit_tool_outputs_and_poll(...)`: Submits tool outputs for a run and polls for completion.

- **Vector Store Operations**:
  - `client.beta.vector_stores.files.upload_and_poll(...)`: Uploads a file to a vector store and polls for completion.
  - `client.beta.vector_stores.files.create_and_poll(...)`: Creates a file entry in a vector store and polls for completion.
  - `client.beta.vector_stores.file_batches.create_and_poll(...)`: Creates a file batch for a vector store and polls for completion.
  - `client.beta.vector_stores.file_batches.upload_and_poll(...)`: Uploads a file batch to a vector store and polls for completion.

*Polling Frequency*: The polling frequency can be controlled via the `poll_interval_ms` argument available in these methods.
```

----------------------------------------

TITLE: Updating an Eval in OpenAI Python
DESCRIPTION: This method updates an existing evaluation identified by `eval_id`. It allows modification of evaluation parameters, returning an EvalUpdateResponse object.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_140

LANGUAGE: Python
CODE:
```
client.evals.update(eval_id, **params)
```

----------------------------------------

TITLE: OpenAI API Reference - Assistants Streaming Events
DESCRIPTION: Provides detailed information on the types of events available for subscription within the OpenAI Assistant streaming API. Links to further documentation for specific event types and concepts.

SOURCE: https://github.com/openai/openai-python/blob/main/helpers.md#_snippet_13

LANGUAGE: APIDOC
CODE:
```
OpenAI Assistant Streaming Events:

- **General Events**:
  - `on_event(event: AssistantStreamEvent)`: Subscribe to all raw events.
  - `on_end()`: Triggered when the stream ends.
  - `on_timeout()`: Triggered if the request times out.
  - `on_exception(exception: Exception)`: Triggered if an exception occurs.

- **Run Step Events**:
  - `on_run_step_created(run_step: RunStep)`: Triggered when a RunStep is created.
  - `on_run_step_delta(delta: RunStepDelta, snapshot: RunStep)`: Triggered for RunStep updates.
  - `on_run_step_done(run_step: RunStep)`: Triggered when a RunStep completes.
  *See also: [Runs and RunSteps](https://platform.openai.com/docs/assistants/how-it-works/runs-and-run-steps)*

- **Message Events**:
  - `on_message_created(message: Message)`: Triggered when a Message is created.
  - `on_message_delta(delta: MessageDelta, snapshot: Message)`: Triggered for Message updates.
  - `on_message_done(message: Message)`: Triggered when a Message completes.
  *See also: [Message Object](https://platform.openai.com/docs/api-reference/messages/object)*

- **Text Content Events**:
  - `on_text_created(text: Text)`: Triggered when Text content is created.
  - `on_text_delta(delta: TextDelta, snapshot: Text)`: Triggered for Text content updates.
  - `on_text_done(text: Text)`: Triggered when Text content completes.

- **Image File Events**:
  - `on_image_file_done(image_file: ImageFile)`: Triggered when an ImageFile is available.

- **Tool Call Events**:
  - `on_tool_call_created(tool_call: ToolCall)`: Triggered when a ToolCall is created.
  - `on_tool_call_delta(delta: ToolCallDelta, snapshot: ToolCall)`: Triggered for ToolCall updates.
  - `on_tool_call_done(tool_call: ToolCall)`: Triggered when a ToolCall completes.
  *See also: [Tools](https://platform.openai.com/docs/assistants/tools)*

*For a comprehensive list of all possible raw events, refer to: [Events](https://platform.openai.com/docs/api-reference/assistants-streaming/events)*
```

----------------------------------------

TITLE: Listing Files within a Container in OpenAI Python Client
DESCRIPTION: This method lists files associated with a specified `container_id`, with optional filtering capabilities provided through `**params`. It returns a `SyncCursorPage` object, which facilitates pagination through a collection of `FileListResponse` objects.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_160

LANGUAGE: python
CODE:
```
client.containers.files.list(container_id, **params) -> SyncCursorPage[FileListResponse]
```

----------------------------------------

TITLE: Auto-parsing Function Tool Calls with Pydantic
DESCRIPTION: Illustrates how to automatically parse function tool calls using the `client.chat.completions.parse()` method in conjunction with `openai.pydantic_function_tool()`. This requires marking the tool schema with `"strict": True`. The example shows defining Pydantic models for table queries, conditions, and ordering, then using them to parse user requests into structured function calls.

SOURCE: https://github.com/openai/openai-python/blob/main/helpers.md#_snippet_1

LANGUAGE: python
CODE:
```
from enum import Enum
from typing import List, Union
from pydantic import BaseModel
import openai

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

client = openai.OpenAI()
completion = client.chat.completions.parse(
    model="gpt-4o-2024-08-06",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant. The current date is August 6, 2024. You help users query for the data they are looking for by calling the query function.",
        },
        {
            "role": "user",
            "content": "look up all my orders in may of last year that were fulfilled but not delivered on time",
        },
    ],
    tools=[
        openai.pydantic_function_tool(Query),
    ],
)

tool_call = (completion.choices[0].message.tool_calls or [])[0]
print(tool_call.function)
assert isinstance(tool_call.function.parsed_arguments, Query)
print(tool_call.function.parsed_arguments.table_name)
```

----------------------------------------

TITLE: OpenAI Conversation Item Management
DESCRIPTION: Enables management of items within conversations, including creation, retrieval, listing, and deletion. Requires conversation ID and item ID for specific operations.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_72

LANGUAGE: APIDOC
CODE:
```
POST /conversations/{conversation_id}/items
  Adds an item to a conversation.
  Parameters:
    conversation_id (str): The ID of the conversation.
    params (dict): Parameters for item creation.
  Returns: ConversationItemList - The list of conversation items.

GET /conversations/{conversation_id}/items/{item_id}
  Retrieves a specific item within a conversation.
  Parameters:
    item_id (str): The ID of the item to retrieve.
    conversation_id (str): The ID of the conversation.
    params (dict): Parameters for item retrieval.
  Returns: ConversationItem - The retrieved conversation item.

GET /conversations/{conversation_id}/items
  Lists items within a conversation.
  Parameters:
    conversation_id (str): The ID of the conversation.
    params (dict): Parameters for listing items.
  Returns: SyncConversationCursorPage[ConversationItem] - A page of conversation items.

DELETE /conversations/{conversation_id}/items/{item_id}
  Deletes an item from a conversation.
  Parameters:
    item_id (str): The ID of the item to delete.
    conversation_id (str): The ID of the conversation.
  Returns: Conversation - The conversation after item deletion.
```

----------------------------------------

TITLE: Retrieving an Eval Run Output Item in OpenAI Python
DESCRIPTION: This method retrieves a specific output item from an evaluation run using its `output_item_id`, `eval_id`, and `run_id`. It returns an OutputItemRetrieveResponse object.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_150

LANGUAGE: Python
CODE:
```
client.evals.runs.output_items.retrieve(output_item_id, *, eval_id, run_id)
```

----------------------------------------

TITLE: Add API Endpoint: Get Chat Completions
DESCRIPTION: Adds a new API endpoint (`GET /chat/completions`) for retrieving chat completions. This provides a direct method to access chat completion results via the API.

SOURCE: https://github.com/openai/openai-python/blob/main/CHANGELOG.md#_snippet_17

LANGUAGE: APIDOC
CODE:
```
GET /chat/completions
```

----------------------------------------

TITLE: Retrieving File Content from a Container in OpenAI Python Client
DESCRIPTION: This method retrieves the raw content of a specific file identified by `file_id` from within a given `container_id`. It returns an `HttpxBinaryResponseContent` object, providing direct access to the file's binary data.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_162

LANGUAGE: python
CODE:
```
client.containers.files.content.retrieve(file_id, *, container_id) -> HttpxBinaryResponseContent
```

----------------------------------------

TITLE: Retrieving an Eval Run in OpenAI Python
DESCRIPTION: This method retrieves a specific evaluation run by its `run_id` and associated `eval_id`. It returns a RunRetrieveResponse object containing the run's details.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_145

LANGUAGE: Python
CODE:
```
client.evals.runs.retrieve(run_id, *, eval_id)
```

----------------------------------------

TITLE: Fix Types: Handle More Discriminated Union Shapes
DESCRIPTION: Enhances the type system to correctly handle a wider variety of discriminated union shapes, improving type safety and compatibility.

SOURCE: https://github.com/openai/openai-python/blob/main/CHANGELOG.md#_snippet_35

LANGUAGE: APIDOC
CODE:
```
Bug Fix: Types handle more discriminated union shapes.
```

----------------------------------------

TITLE: Creating a Container with OpenAI Python Client
DESCRIPTION: This method creates a new container resource. It accepts parameters (`**params`) that define the container's properties and returns a `ContainerCreateResponse` object upon successful creation, detailing the newly created container.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_153

LANGUAGE: python
CODE:
```
client.containers.create(**params) -> ContainerCreateResponse
```

----------------------------------------

TITLE: Generate Text with Chat Completions API
DESCRIPTION: Generates text using the OpenAI Chat Completions API, providing messages with roles for the model and user. This is the standard method for text generation.

SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_snippet_2

LANGUAGE: python
CODE:
```
from openai import OpenAI

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "developer", "content": "Talk like a pirate."},
        {
            "role": "user",
            "content": "How do I check if a Python object is an instance of a class?",
        },
    ],
)

print(completion.choices[0].message.content)
```

----------------------------------------

TITLE: OpenAI Conversation Management
DESCRIPTION: Provides methods for creating, retrieving, updating, and deleting conversations. Requires conversation ID for specific operations and accepts parameters for creation and updates.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_71

LANGUAGE: APIDOC
CODE:
```
POST /conversations
  Creates a new conversation.
  Parameters: params (dict) - Parameters for conversation creation.
  Returns: Conversation - The created conversation object.

GET /conversations/{conversation_id}
  Retrieves a specific conversation.
  Parameters:
    conversation_id (str): The ID of the conversation to retrieve.
  Returns: Conversation - The retrieved conversation object.

POST /conversations/{conversation_id}
  Updates an existing conversation.
  Parameters:
    conversation_id (str): The ID of the conversation to update.
    params (dict): Parameters for conversation update.
  Returns: Conversation - The updated conversation object.

DELETE /conversations/{conversation_id}
  Deletes a conversation.
  Parameters:
    conversation_id (str): The ID of the conversation to delete.
  Returns: ConversationDeletedResource - The result of the delete operation.
```

----------------------------------------

TITLE: OpenAI Assistant Stream Events
DESCRIPTION: Subscribe to raw events from the OpenAI streaming API for assistants. This includes events for run steps, messages, text content, tool calls, and stream lifecycle events like end, timeout, and exceptions.

SOURCE: https://github.com/openai/openai-python/blob/main/helpers.md#_snippet_10

LANGUAGE: python
CODE:
```
def on_event(self, event: AssistantStreamEvent)

def on_run_step_created(self, run_step: RunStep)
def on_run_step_delta(self, delta: RunStepDelta, snapshot: RunStep)
def on_run_step_done(self, run_step: RunStep)

def on_message_created(self, message: Message)
def on_message_delta(self, delta: MessageDelta, snapshot: Message)
def on_message_done(self, message: Message)

def on_text_created(self, text: Text)
def on_text_delta(self, delta: TextDelta, snapshot: Text)
def on_text_done(self, text: Text)

def on_image_file_done(self, image_file: ImageFile)

def on_tool_call_created(self, tool_call: ToolCall)
def on_tool_call_delta(self, delta: ToolCallDelta, snapshot: ToolCall)
def on_tool_call_done(self, tool_call: ToolCall)

def on_end(self)

def on_timeout(self)

def on_exception(self, exception: Exception)
```

----------------------------------------

TITLE: Creating an Eval Run in OpenAI Python
DESCRIPTION: This method creates a new run for a specified evaluation. It requires the `eval_id` and accepts additional parameters for run configuration, returning a RunCreateResponse.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_144

LANGUAGE: Python
CODE:
```
client.evals.runs.create(eval_id, **params)
```

----------------------------------------

TITLE: Deleting an Eval in OpenAI Python
DESCRIPTION: This method deletes a specific evaluation identified by its `eval_id`. It returns an EvalDeleteResponse object upon successful deletion.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_142

LANGUAGE: Python
CODE:
```
client.evals.delete(eval_id)
```

----------------------------------------

TITLE: OpenAI Conversation Types
DESCRIPTION: Defines the various data structures used for representing conversation content and metadata in the OpenAI API.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_74

LANGUAGE: python
CODE:
```
from openai.types.conversations import (
    ComputerScreenshotContent,
    ContainerFileCitationBody,
    Conversation,
    ConversationDeleted,
    ConversationDeletedResource,
    FileCitationBody,
    InputFileContent,
    InputImageContent,
    InputTextContent,
    LobProb,
    Message,
    OutputTextContent,
    RefusalContent,
    SummaryTextContent,
    TextContent,
    TopLogProb,
    URLCitationBody,
)
```

----------------------------------------

TITLE: Retrieving a File from a Container by ID in OpenAI Python Client
DESCRIPTION: This method retrieves a specific file identified by `file_id` from within a given `container_id`. It returns a `FileRetrieveResponse` object, which contains the details and metadata of the requested file.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_159

LANGUAGE: python
CODE:
```
client.containers.files.retrieve(file_id, *, container_id) -> FileRetrieveResponse
```

----------------------------------------

TITLE: Retrieving a Container by ID in OpenAI Python Client
DESCRIPTION: This method retrieves a specific container using its unique identifier, `container_id`. It returns a `ContainerRetrieveResponse` object, which contains all the details and metadata of the requested container.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_154

LANGUAGE: python
CODE:
```
client.containers.retrieve(container_id) -> ContainerRetrieveResponse
```

----------------------------------------

TITLE: OpenAI Chat Completions Messages API
DESCRIPTION: Provides a method to list messages associated with a specific chat completion.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_6

LANGUAGE: APIDOC
CODE:
```
GET /chat/completions/{completion_id}/messages
client.chat.completions.messages.list(completion_id, **params) -> SyncCursorPage[ChatCompletionStoreMessage]

Description:
  Lists messages for a given chat completion.

Parameters:
  completion_id: The ID of the chat completion.
  **params: A dictionary containing parameters for listing messages.

Returns:
  SyncCursorPage[ChatCompletionStoreMessage]: A paginated list of messages.
```

----------------------------------------

TITLE: Listing Batch Requests in OpenAI Python
DESCRIPTION: This method retrieves a paginated list of batch requests. It can accept parameters for filtering or pagination and returns a `SyncCursorPage[Batch]`, allowing iteration over multiple batch operations.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_122

LANGUAGE: python
CODE:
```
client.batches.list(**params) -> SyncCursorPage[Batch]
```

----------------------------------------

TITLE: OpenAI Conversation Item Types
DESCRIPTION: Defines the data structures for conversation items, including the base types and list representations.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_75

LANGUAGE: python
CODE:
```
from openai.types.conversations import ConversationItem, ConversationItemList
```

----------------------------------------

TITLE: Chore: Update Supported Voice IDs for API
DESCRIPTION: Updates the list of supported Voice IDs for the API, expanding or refining the available options for voice-related features.

SOURCE: https://github.com/openai/openai-python/blob/main/CHANGELOG.md#_snippet_20

LANGUAGE: APIDOC
CODE:
```
Chore: API updates to supported Voice IDs.
```

----------------------------------------

TITLE: OpenAI Chat Completions API
DESCRIPTION: Provides methods for creating, retrieving, updating, listing, and deleting chat completions.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_5

LANGUAGE: APIDOC
CODE:
```
POST /chat/completions
client.chat.completions.create(**params) -> ChatCompletion

Description:
  Creates a chat completion request.

Parameters:
  **params: A dictionary containing the parameters for the chat completion request.

Returns:
  ChatCompletion: The chat completion object returned by the API.

---
```

LANGUAGE: APIDOC
CODE:
```
GET /chat/completions/{completion_id}
client.chat.completions.retrieve(completion_id) -> ChatCompletion

Description:
  Retrieves a specific chat completion by its ID.

Parameters:
  completion_id: The ID of the chat completion to retrieve.

Returns:
  ChatCompletion: The requested chat completion object.

---
```

LANGUAGE: APIDOC
CODE:
```
POST /chat/completions/{completion_id}
client.chat.completions.update(completion_id, **params) -> ChatCompletion

Description:
  Updates an existing chat completion.

Parameters:
  completion_id: The ID of the chat completion to update.
  **params: A dictionary containing the parameters for the update.

Returns:
  ChatCompletion: The updated chat completion object.

---
```

LANGUAGE: APIDOC
CODE:
```
GET /chat/completions
client.chat.completions.list(**params) -> SyncCursorPage[ChatCompletion]

Description:
  Lists chat completions, supporting pagination and filtering.

Parameters:
  **params: A dictionary containing parameters for listing completions (e.g., limit, order).

Returns:
  SyncCursorPage[ChatCompletion]: A paginated list of chat completion objects.
```

LANGUAGE: APIDOC
CODE:
```
DELETE /chat/completions/{completion_id}
client.chat.completions.delete(completion_id) -> ChatCompletionDeleted

Description:
  Deletes a chat completion by its ID.

Parameters:
  completion_id: The ID of the chat completion to delete.

Returns:
  ChatCompletionDeleted: An object indicating the result of the deletion.
```

----------------------------------------

TITLE: Add API Features: New TTS, STT Models and Realtime Audio
DESCRIPTION: Integrates new models for Text-to-Speech (TTS) and Speech-to-Text (STT), along with new audio features specifically designed for real-time applications via the API.

SOURCE: https://github.com/openai/openai-python/blob/main/CHANGELOG.md#_snippet_28

LANGUAGE: APIDOC
CODE:
```
Feature: New TTS, STT models and realtime audio features added to API.
```

----------------------------------------

TITLE: Deleting an Eval Run in OpenAI Python
DESCRIPTION: This method deletes a specific evaluation run identified by its `run_id` and `eval_id`. It returns a RunDeleteResponse object upon successful deletion.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_147

LANGUAGE: Python
CODE:
```
client.evals.runs.delete(run_id, *, eval_id)
```

----------------------------------------

TITLE: Iterating Through Fine-Tuning Jobs (Sync)
DESCRIPTION: Demonstrates how to synchronously iterate through all fine-tuning jobs, fetching additional pages as needed. This is useful for processing large numbers of jobs without manual pagination.

SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_snippet_15

LANGUAGE: python
CODE:
```
# Automatically fetches more pages as needed.
for job in client.fine_tuning.jobs.list(
    limit=20,
):
    # Do something with job here
    all_jobs.append(job)
print(all_jobs)
```

----------------------------------------

TITLE: Listing Runs for a Thread (OpenAI Python)
DESCRIPTION: This method retrieves a paginated list of all runs associated with a specific `thread_id`. It supports filtering and pagination `params`, returning a `SyncCursorPage` containing `Run` objects.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_102

LANGUAGE: Python
CODE:
```
client.beta.threads.runs.list(thread_id, **params)
```

----------------------------------------

TITLE: Creating a File within a Container in OpenAI Python Client
DESCRIPTION: This method creates a new file resource inside a specified `container_id`. It accepts file properties via `**params` and returns a `FileCreateResponse` object upon successful creation, detailing the newly uploaded file.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_158

LANGUAGE: python
CODE:
```
client.containers.files.create(container_id, **params) -> FileCreateResponse
```

----------------------------------------

TITLE: OpenAI Message Types
DESCRIPTION: Defines the data structures for messages and their content within the OpenAI API. Includes various content block types like text, image files, and file citations, as well as delta and deleted message types.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_65

LANGUAGE: Python
CODE:
```
from openai.types.beta.threads import (
    Annotation,
    AnnotationDelta,
    FileCitationAnnotation,
    FileCitationDeltaAnnotation,
    FilePathAnnotation,
    FilePathDeltaAnnotation,
    ImageFile,
    ImageFileContentBlock,
    ImageFileDelta,
    ImageFileDeltaBlock,
    ImageURL,
    ImageURLContentBlock,
    ImageURLDelta,
    ImageURLDeltaBlock,
    Message,
    MessageContent,
    MessageContentDelta,
    MessageContentPartParam,
    MessageDeleted,
    MessageDelta,
    MessageDeltaEvent,
    RefusalContentBlock,
    RefusalDeltaBlock,
    Text,
    TextContentBlock,
    TextContentBlockParam,
    TextDelta,
    TextDeltaBlock,
)
```

----------------------------------------

TITLE: Update Assistants and Evals API Schemas
DESCRIPTION: Updates the underlying schemas for the Assistants and Evals APIs. This ensures consistency and compatibility with the latest API definitions.

SOURCE: https://github.com/openai/openai-python/blob/main/CHANGELOG.md#_snippet_14

LANGUAGE: APIDOC
CODE:
```
API Schema Update:
  - Assistants API schema updated
  - Evals API schema updated
```

----------------------------------------

TITLE: Creating a Message in an OpenAI Thread (Python)
DESCRIPTION: This method adds a new message to a specified thread. It requires the `thread_id` and accepts various parameters to define the message content and properties, returning a `Message` object upon successful creation.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_114

LANGUAGE: python
CODE:
```
client.beta.threads.messages.create(thread_id, **params) -> Message
```

----------------------------------------

TITLE: Add Audio Helpers
DESCRIPTION: Introduces new audio helper utilities to simplify common audio-related tasks and operations within the library.

SOURCE: https://github.com/openai/openai-python/blob/main/CHANGELOG.md#_snippet_27

LANGUAGE: APIDOC
CODE:
```
Feature: New audio helper utilities added.
```

----------------------------------------

TITLE: Iterating Through Fine-Tuning Jobs (Async)
DESCRIPTION: Demonstrates how to asynchronously iterate through all fine-tuning jobs, fetching additional pages as needed. This is useful for processing large numbers of jobs without manual pagination.

SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_snippet_14

LANGUAGE: python
CODE:
```
import asyncio
from openai import AsyncOpenAI

client = AsyncOpenAI()


async def main() -> None:
    all_jobs = []
    # Iterate through items across all pages, issuing requests as needed.
    async for job in client.fine_tuning.jobs.list(
        limit=20,
    ):
        all_jobs.append(job)
    print(all_jobs)


asyncio.run(main())
```

----------------------------------------

TITLE: Importing Eval Run Output Item Types in Python
DESCRIPTION: This snippet imports data types specifically for retrieving and listing output items associated with evaluation runs within the OpenAI Evals API.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_149

LANGUAGE: Python
CODE:
```
from openai.types.evals.runs import OutputItemRetrieveResponse, OutputItemListResponse
```

----------------------------------------

TITLE: OpenAI Messages API
DESCRIPTION: Manages messages within threads in the OpenAI API. Supports creating, retrieving, updating, listing, and deleting messages. Requires thread ID and message ID for specific operations.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_62

LANGUAGE: APIDOC
CODE:
```
client.beta.threads.messages.create(thread_id, **params) -> Message
  POST /threads/{thread_id}/messages
  Creates a message within a thread.

client.beta.threads.messages.retrieve(message_id, *, thread_id) -> Message
  GET /threads/{thread_id}/messages/{message_id}
  Retrieves a specific message from a thread.

client.beta.threads.messages.update(message_id, *, thread_id, **params) -> Message
  POST /threads/{thread_id}/messages/{message_id}
  Updates a specific message in a thread.

client.beta.threads.messages.list(thread_id, **params) -> SyncCursorPage[Message]
  GET /threads/{thread_id}/messages
  Lists all messages in a thread, with support for pagination.

client.beta.threads.messages.delete(message_id, *, thread_id) -> MessageDeleted
  DELETE /threads/{thread_id}/messages/{message_id}
  Deletes a specific message from a thread.
```

----------------------------------------

TITLE: Fix Helpers/Audio: Remove Duplicative Module
DESCRIPTION: Removes a duplicative module within the `helpers/audio` section, streamlining the codebase and eliminating redundant implementations.

SOURCE: https://github.com/openai/openai-python/blob/main/CHANGELOG.md#_snippet_24

LANGUAGE: APIDOC
CODE:
```
Bug Fix: Duplicative module in helpers/audio removed.
```

----------------------------------------

TITLE: Importing Message Types for OpenAI Python API
DESCRIPTION: This snippet imports various type definitions related to messages within the OpenAI Assistants API. These types define the structure of message content, annotations, and delta updates, enabling the client to handle diverse message formats including text, image files, and URLs, as well as track changes.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_113

LANGUAGE: python
CODE:
```
from openai.types.beta.threads import (
    Annotation,
    AnnotationDelta,
    FileCitationAnnotation,
    FileCitationDeltaAnnotation,
    FilePathAnnotation,
    FilePathDeltaAnnotation,
    ImageFile,
    ImageFileContentBlock,
    ImageFileDelta,
    ImageFileDeltaBlock,
    ImageURL,
    ImageURLContentBlock,
    ImageURLDelta,
    ImageURLDeltaBlock,
    Message,
    MessageContent,
    MessageContentDelta,
    MessageContentPartParam,
    MessageDeleted,
    MessageDelta,
    MessageDeltaEvent,
    RefusalContentBlock,
    RefusalDeltaBlock,
    Text,
    TextContentBlock,
    TextContentBlockParam,
    TextDelta,
    TextDeltaBlock,
)
```

----------------------------------------

TITLE: OpenAI Realtime Beta Conversation Event Types
DESCRIPTION: Lists the various event types associated with real-time conversations in the OpenAI Beta API. These events cover the lifecycle of a conversation, including creation, item updates, and content changes.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_40

LANGUAGE: python
CODE:
```
from openai.types.beta.realtime import (
    ConversationCreatedEvent,
    ConversationItem,
    ConversationItemContent,
    ConversationItemCreateEvent,
    ConversationItemCreatedEvent,
    ConversationItemDeleteEvent,
    ConversationItemDeletedEvent,
    ConversationItemInputAudioTranscriptionCompletedEvent,
    ConversationItemInputAudioTranscriptionDeltaEvent,
    ConversationItemInputAudioTranscriptionFailedEvent,
    ConversationItemRetrieveEvent,
    ConversationItemTruncateEvent,
    ConversationItemTruncatedEvent,
    ConversationItemWithReference,
    ErrorEvent,
    InputAudioBufferAppendEvent,
    InputAudioBufferClearEvent,
    InputAudioBufferClearedEvent,
    InputAudioBufferCommitEvent,
    InputAudioBufferCommittedEvent,
    InputAudioBufferSpeechStartedEvent,
    InputAudioBufferSpeechStoppedEvent,
    RateLimitsUpdatedEvent,
    RealtimeClientEvent,
    RealtimeResponse,
    RealtimeResponseStatus,
    RealtimeResponseUsage,
    RealtimeServerEvent,
    ResponseAudioDeltaEvent,
    ResponseAudioDoneEvent,
    ResponseAudioTranscriptDeltaEvent,
    ResponseAudioTranscriptDoneEvent,
    ResponseCancelEvent,
    ResponseContentPartAddedEvent,
    ResponseContentPartDoneEvent,
    ResponseCreateEvent,
    ResponseCreatedEvent,
    ResponseDoneEvent,
    ResponseFunctionCallArgumentsDeltaEvent,
    ResponseFunctionCallArgumentsDoneEvent,
    ResponseOutputItemAddedEvent,
    ResponseOutputItemDoneEvent,
    ResponseTextDeltaEvent,
    ResponseTextDoneEvent,
    SessionCreatedEvent,
    SessionUpdateEvent,
    SessionUpdatedEvent,
    TranscriptionSessionUpdate,
    TranscriptionSessionUpdatedEvent,
)
```

----------------------------------------

TITLE: Retrieving a Specific Message in an OpenAI Thread (Python)
DESCRIPTION: This method fetches a specific message by its ID from a given thread. It requires both `message_id` and `thread_id` and returns a `Message` object containing the message's content and metadata.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_115

LANGUAGE: python
CODE:
```
client.beta.threads.messages.retrieve(message_id, *, thread_id) -> Message
```

----------------------------------------

TITLE: OpenAI Python SDK - List Runs
DESCRIPTION: Demonstrates how to list all runs associated with a specific thread using the OpenAI Python SDK. Supports pagination and filtering via parameters.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_51

LANGUAGE: python
CODE:
```
from openai import OpenAI

client = OpenAI()

runs = client.beta.threads.runs.list(
    thread_id="thread_id",
    # additional parameters can be passed here
)
```

----------------------------------------

TITLE: OpenAI Evals Management
DESCRIPTION: Facilitates the management of evaluation tasks, including creation, retrieval, updates, listing, and deletion of evals. Requires eval ID for specific operations.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_73

LANGUAGE: APIDOC
CODE:
```
POST /evals
  Creates a new evaluation.
  Parameters: params (dict) - Parameters for eval creation.
  Returns: EvalCreateResponse - The response after creating the eval.

GET /evals/{eval_id}
  Retrieves a specific evaluation.
  Parameters:
    eval_id (str): The ID of the eval to retrieve.
  Returns: EvalRetrieveResponse - The response after retrieving the eval.

POST /evals/{eval_id}
  Updates an existing evaluation.
  Parameters:
    eval_id (str): The ID of the eval to update.
    params (dict): Parameters for eval update.
  Returns: EvalUpdateResponse - The response after updating the eval.

GET /evals
  Lists all evaluations.
  Parameters: params (dict) - Parameters for listing evals.
  Returns: SyncCursorPage[EvalListResponse] - A page of eval list responses.

DELETE /evals/{eval_id}
  Deletes an evaluation.
  Parameters:
    eval_id (str): The ID of the eval to delete.
  Returns: EvalDeleteResponse - The response after deleting the eval.
```

----------------------------------------

TITLE: Execute Project Tests
DESCRIPTION: This command runs the project's test suite. For most tests, a mock server (set up with `prism`) must be running against the OpenAPI specification for proper execution and validation.

SOURCE: https://github.com/openai/openai-python/blob/main/CONTRIBUTING.md#_snippet_10

LANGUAGE: sh
CODE:
```
./scripts/test
```

----------------------------------------

TITLE: OpenAI Vector Store Files API
DESCRIPTION: Provides methods for managing files within OpenAI vector stores. Supports creating, retrieving, updating, listing, and deleting files, as well as retrieving file content. Includes methods for asynchronous operations like polling and uploading.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_34

LANGUAGE: APIDOC
CODE:
```
POST /vector_stores/{vector_store_id}/files
  - Creates a file and associates it with a vector store.
  - Parameters:
    - vector_store_id: The ID of the vector store.
    - params: Parameters for file creation (e.g., file_id, file_object).
  - Returns: VectorStoreFile object.

GET /vector_stores/{vector_store_id}/files/{file_id}
  - Retrieves a specific file associated with a vector store.
  - Parameters:
    - file_id: The ID of the file to retrieve.
    - vector_store_id: The ID of the vector store.
  - Returns: VectorStoreFile object.

POST /vector_stores/{vector_store_id}/files/{file_id}
  - Updates an existing file associated with a vector store.
  - Parameters:
    - file_id: The ID of the file to update.
    - vector_store_id: The ID of the vector store.
    - params: Parameters for file update.
  - Returns: VectorStoreFile object.

GET /vector_stores/{vector_store_id}/files
  - Lists all files associated with a vector store.
  - Parameters:
    - vector_store_id: The ID of the vector store.
    - params: Parameters for listing files (e.g., limit, order, after).
  - Returns: SyncCursorPage[VectorStoreFile].

DELETE /vector_stores/{vector_store_id}/files/{file_id}
  - Deletes a file from a vector store.
  - Parameters:
    - file_id: The ID of the file to delete.
    - vector_store_id: The ID of the vector store.
  - Returns: VectorStoreFileDeleted object.

GET /vector_stores/{vector_store_id}/files/{file_id}/content
  - Retrieves the content of a file associated with a vector store.
  - Parameters:
    - file_id: The ID of the file whose content to retrieve.
    - vector_store_id: The ID of the vector store.
  - Returns: SyncPage[FileContentResponse].

Additional Methods:
  - create_and_poll: Creates a file and polls for its completion.
  - poll: Polls for the status of a file operation.
  - upload: Uploads a file.
  - upload_and_poll: Uploads a file and polls for its completion.
```

----------------------------------------

TITLE: Webhook Verification and Payload Parsing
DESCRIPTION: Provides an example of how to verify webhook signatures and parse payloads using `client.webhooks.unwrap()`. It includes error handling for invalid signatures and demonstrates processing different event types.

SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_snippet_19

LANGUAGE: python
CODE:
```
from openai import OpenAI
from flask import Flask, request

app = Flask(__name__)
client = OpenAI()  # OPENAI_WEBHOOK_SECRET environment variable is used by default


@app.route("/webhook", methods=["POST"])
def webhook():
    request_body = request.get_data(as_text=True)

    try:
        event = client.webhooks.unwrap(request_body, request.headers)

        if event.type == "response.completed":
            print("Response completed:", event.data)
        elif event.type == "response.failed":
            print("Response failed:", event.data)
        else:
            print("Unhandled event type:", event.type)

        return "ok"
    except Exception as e:
        print("Invalid signature:", e)
        return "Invalid signature", 400


if __name__ == "__main__":
    app.run(port=8000)
```

----------------------------------------

TITLE: Handle OpenAI API Errors
DESCRIPTION: Illustrates how to handle various exceptions that can occur when interacting with the OpenAI API. It specifically catches `APIConnectionError` for connection issues and `APIStatusError` for non-success HTTP status codes, providing specific error messages and details.

SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_snippet_22

LANGUAGE: python
CODE:
```
import openai
from openai import OpenAI

client = OpenAI()

try:
    client.fine_tuning.jobs.create(
        model="gpt-4o",
        training_file="file-abc123",
    )
except openai.APIConnectionError as e:
    print("The server could not be reached")
    print(e.__cause__)  # an underlying Exception, likely raised within httpx.
except openai.RateLimitError as e:
    print("A 429 status code was received; we should back off a bit.")
except openai.APIStatusError as e:
    print("Another non-200-range status code was received")
    print(e.status_code)
    print(e.response)
```

----------------------------------------

TITLE: OpenAI Python Client - Vector Stores
DESCRIPTION: Python code for managing vector stores with the OpenAI client library. Includes examples for create, retrieve, update, list, delete, and search operations.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_33

LANGUAGE: Python
CODE:
```
from openai import OpenAI

client = OpenAI()

# Create vector store
vector_store = client.vector_stores.create(
    name="my-vector-store",
    # Add other params like file_ids or chunking_strategy as needed
)

# Retrieve vector store
retrieved_vector_store = client.vector_stores.retrieve(vector_store.id)

# Update vector store
updated_vector_store = client.vector_stores.update(
    vector_store.id,
    name="my-updated-vector-store",
)

# List vector stores
vector_stores_list = client.vector_stores.list()

# Delete vector store
client.vector_stores.delete(vector_store.id)

# Search vector store
search_response = client.vector_stores.search(
    vector_store.id,
    query="my search query",
)
```

----------------------------------------

TITLE: Install aiohttp for Async Client
DESCRIPTION: Installs the `aiohttp` library, which can be used as an alternative backend for the asynchronous OpenAI client for improved concurrency.

SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_snippet_6

LANGUAGE: sh
CODE:
```
pip install aiohttp
```

----------------------------------------

TITLE: Retrieving a Run for a Thread (OpenAI Python)
DESCRIPTION: This method fetches an existing run by its `run_id` within a given `thread_id`. It provides access to the run's current status, steps, and outputs, returning a `Run` object.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_100

LANGUAGE: Python
CODE:
```
client.beta.threads.runs.retrieve(run_id, *, thread_id)
```

----------------------------------------

TITLE: OpenAI Python SDK - Run Retrieval
DESCRIPTION: Shows how to retrieve a specific run by its ID and the thread ID it belongs to using the OpenAI Python SDK.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_49

LANGUAGE: python
CODE:
```
from openai import OpenAI

client = OpenAI()

run = client.beta.threads.runs.retrieve(
    run_id="run_id",
    thread_id="thread_id",
)
```

----------------------------------------

TITLE: Python Model Retrieval
DESCRIPTION: Example of how to retrieve a specific model using the OpenAI Python client.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_17

LANGUAGE: Python
CODE:
```
from openai import OpenAI

client = OpenAI()

model = client.models.retrieve("gpt-4")
```

----------------------------------------

TITLE: Streaming an Existing Run (OpenAI Python)
DESCRIPTION: This method streams real-time updates for an existing run identified by `run_id` within a `thread_id`. It provides an `AssistantStreamManager` for event-driven processing of the run's status and output.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_108

LANGUAGE: Python
CODE:
```
client.beta.threads.runs.stream(*args)
```

----------------------------------------

TITLE: OpenAI Runs Output Items API
DESCRIPTION: Manages output items associated with runs, allowing retrieval and listing of individual output items. It depends on run and evaluation IDs.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_78

LANGUAGE: APIDOC
CODE:
```
GET /evals/{eval_id}/runs/{run_id}/output_items/{output_item_id}
  - Retrieves a specific output item for a run.
  - Parameters:
    - output_item_id: The ID of the output item.
    - run_id: The ID of the run.
    - eval_id: The ID of the evaluation.
  - Returns: OutputItemRetrieveResponse

GET /evals/{eval_id}/runs/{run_id}/output_items
  - Lists all output items for a given run.
  - Parameters:
    - run_id: The ID of the run.
    - eval_id: The ID of the evaluation.
    - params: Additional parameters for listing output items.
  - Returns: SyncCursorPage[OutputItemListResponse]
```

----------------------------------------

TITLE: Cancelling an Eval Run in OpenAI Python
DESCRIPTION: This method cancels a specific evaluation run identified by its `run_id` and `eval_id`. It returns a RunCancelResponse object upon successful cancellation.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_148

LANGUAGE: Python
CODE:
```
client.evals.runs.cancel(run_id, *, eval_id)
```

----------------------------------------

TITLE: OpenAI Models API
DESCRIPTION: Provides methods to interact with OpenAI's model resources. Includes retrieving a specific model, listing all available models, and deleting a model.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_15

LANGUAGE: APIDOC
CODE:
```
GET /models/{model}
  Retrieves a specific model.
  Parameters:
    - model: The ID of the model to retrieve.
  Returns: A Model object.

GET /models
  Lists all available models.
  Returns: A SyncPage of Model objects.

DELETE /models/{model}
  Deletes a specific model.
  Parameters:
    - model: The ID of the model to delete.
  Returns: A ModelDeleted object.
```

----------------------------------------

TITLE: Listing Run Steps for a Run in OpenAI Python
DESCRIPTION: This method retrieves a paginated list of run steps associated with a specific run within a thread. It requires `run_id` and `thread_id` and returns a `SyncCursorPage[RunStep]`, allowing iteration over multiple run steps.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_112

LANGUAGE: python
CODE:
```
client.beta.threads.runs.steps.list(run_id, *, thread_id, **params) -> SyncCursorPage[RunStep]
```

----------------------------------------

TITLE: OpenAI Python Client: Vector Store Files Management
DESCRIPTION: Python code for interacting with OpenAI's vector store files API. Demonstrates creating, retrieving, updating, listing, and deleting files, as well as fetching file content. Includes examples for asynchronous operations.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_36

LANGUAGE: Python
CODE:
```
from openai import OpenAI

client = OpenAI()

# Create a file
vector_store_file = client.vector_stores.files.create(
    vector_store_id="vs_abc123",
    file_id="file-xyz789",
)
print(vector_store_file)

# Retrieve a file
retrieved_file = client.vector_stores.files.retrieve(
    file_id="file-xyz789",
    vector_store_id="vs_abc123",
)
print(retrieved_file)

# Update a file
updated_file = client.vector_stores.files.update(
    file_id="file-xyz789",
    vector_store_id="vs_abc123",
    # Add update parameters here if needed
)
print(updated_file)

# List files
files_page = client.vector_stores.files.list(vector_store_id="vs_abc123")
for file in files_page.data:
    print(file)

# Delete a file
deleted_file = client.vector_stores.files.delete(
    file_id="file-xyz789",
    vector_store_id="vs_abc123",
)
print(deleted_file)

# Get file content
content_page = client.vector_stores.files.content(
    file_id="file-xyz789",
    vector_store_id="vs_abc123",
)
for chunk in content_page.data:
    print(chunk)

# Asynchronous operations (example)
# file_for_poll = client.vector_stores.files.create_and_poll(...) 
# file_status = client.vector_stores.files.poll(...)
# uploaded_file = client.vector_stores.files.upload(...)
# uploaded_file_status = client.vector_stores.files.upload_and_poll(...)
```

----------------------------------------

TITLE: Fix Client: Remove Duplicate Types
DESCRIPTION: Fixes an issue in the client by removing duplicate type definitions, which helps in reducing redundancy and potential conflicts in the type system.

SOURCE: https://github.com/openai/openai-python/blob/main/CHANGELOG.md#_snippet_23

LANGUAGE: APIDOC
CODE:
```
Bug Fix: Client duplicate types removed.
```

----------------------------------------

TITLE: OpenAI Vector Stores API
DESCRIPTION: Manages vector stores, including creation, retrieval, update, listing, deletion, and searching. Supports various file chunking strategies.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_30

LANGUAGE: APIDOC
CODE:
```
POST /vector_stores
  - Creates a new vector store.
  - Parameters:
    - params: Parameters for creating the vector store, including chunking strategy.
  - Returns: VectorStore.

GET /vector_stores/{vector_store_id}
  - Retrieves a specific vector store.
  - Parameters:
    - vector_store_id: The ID of the vector store to retrieve.
  - Returns: VectorStore.

POST /vector_stores/{vector_store_id}
  - Updates an existing vector store.
  - Parameters:
    - vector_store_id: The ID of the vector store to update.
    - params: Parameters for updating the vector store.
  - Returns: VectorStore.

GET /vector_stores
  - Lists all vector stores.
  - Parameters:
    - params: Parameters for listing vector stores (e.g., limit, order).
  - Returns: SyncCursorPage[VectorStore].

DELETE /vector_stores/{vector_store_id}
  - Deletes a vector store.
  - Parameters:
    - vector_store_id: The ID of the vector store to delete.
  - Returns: VectorStoreDeleted.

POST /vector_stores/{vector_store_id}/search
  - Searches within a vector store.
  - Parameters:
    - vector_store_id: The ID of the vector store to search.
    - params: Parameters for the search query.
  - Returns: SyncPage[VectorStoreSearchResponse].
```

----------------------------------------

TITLE: Setting up Mock Server for Tests
DESCRIPTION: Instructions to set up a mock server using Prism for running tests against the OpenAPI specification.

SOURCE: https://github.com/openai/openai-python/blob/main/CONTRIBUTING.md#_snippet_6

LANGUAGE: sh
CODE:
```
# Requires npm installed
$ npx prism mock path/to/your/openapi.yml
```

----------------------------------------

TITLE: OpenAI Python SDK - Create and Poll Run
DESCRIPTION: Demonstrates the convenience method `create_and_poll` for creating a run and waiting for its completion, simplifying the workflow.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_54

LANGUAGE: python
CODE:
```
from openai import OpenAI

client = OpenAI()

run = client.beta.threads.runs.create_and_poll(
    thread_id="thread_id",
    # additional parameters can be passed here
)
```

----------------------------------------

TITLE: OpenAI Moderation API
DESCRIPTION: API endpoint for moderating content to detect potential policy violations. Supports text and image inputs.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_14

LANGUAGE: APIDOC
CODE:
```
POST /moderations
  Description: Moderates content.
  Parameters: **params (ModerationCreateParams)
  Returns: ModerationCreateResponse
```

----------------------------------------

TITLE: Realtime API Error Handling
DESCRIPTION: Illustrates how to handle errors within the Realtime API. Errors are delivered as 'error' events, and the connection remains open, requiring manual handling.

SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_snippet_12

LANGUAGE: python
CODE:
```
client = AsyncOpenAI()

async with client.beta.realtime.connect(model="gpt-4o-realtime-preview") as connection:
    ...
    async for event in connection:
        if event.type == 'error':
            print(event.error.type)
            print(event.error.code)
            print(event.error.event_id)
            print(event.error.message)
```

----------------------------------------

TITLE: Deleting an Assistant in Python
DESCRIPTION: This method deletes an assistant identified by its `assistant_id`. Upon successful deletion, it returns an `AssistantDeleted` object, confirming the operation.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_89

LANGUAGE: python
CODE:
```
client.beta.assistants.delete(assistant_id) -> AssistantDeleted
```

----------------------------------------

TITLE: Polling an Existing Run (OpenAI Python)
DESCRIPTION: This method polls an existing run identified by `run_id` within a `thread_id` until it reaches a terminal state. It's used to wait for the asynchronous execution of a run to finish, returning the final `Run` object.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_107

LANGUAGE: Python
CODE:
```
client.beta.threads.runs.poll(*args)
```

----------------------------------------

TITLE: Running Project Tests
DESCRIPTION: Command to execute the project's test suite.

SOURCE: https://github.com/openai/openai-python/blob/main/CONTRIBUTING.md#_snippet_7

LANGUAGE: sh
CODE:
```
$ ./scripts/test
```

----------------------------------------

TITLE: OpenAI Assistants API
DESCRIPTION: Manages Assistants within the OpenAI API. Supports creating, retrieving, updating, listing, and deleting assistants. Requires specific parameters for each operation.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_43

LANGUAGE: APIDOC
CODE:
```
client.beta.assistants.create(**params) -> Assistant
  POST /assistants
  Creates a new assistant.
  Parameters:
    params: Assistant creation parameters.
  Returns:
    The created Assistant object.
```

LANGUAGE: APIDOC
CODE:
```
client.beta.assistants.retrieve(assistant_id) -> Assistant
  GET /assistants/{assistant_id}
  Retrieves an assistant by its ID.
  Parameters:
    assistant_id: The ID of the assistant to retrieve.
  Returns:
    The Assistant object.
```

LANGUAGE: APIDOC
CODE:
```
client.beta.assistants.update(assistant_id, **params) -> Assistant
  POST /assistants/{assistant_id}
  Updates an existing assistant.
  Parameters:
    assistant_id: The ID of the assistant to update.
    params: Assistant update parameters.
  Returns:
    The updated Assistant object.
```

LANGUAGE: APIDOC
CODE:
```
client.beta.assistants.list(**params) -> SyncCursorPage[Assistant]
  GET /assistants
  Lists assistants with optional filtering parameters.
  Parameters:
    params: Assistant list parameters.
  Returns:
    A SyncCursorPage of Assistant objects.
```

LANGUAGE: APIDOC
CODE:
```
client.beta.assistants.delete(assistant_id) -> AssistantDeleted
  DELETE /assistants/{assistant_id}
  Deletes an assistant by its ID.
  Parameters:
    assistant_id: The ID of the assistant to delete.
  Returns:
    An AssistantDeleted object indicating the result of the deletion.
```

----------------------------------------

TITLE: Completing an Upload - OpenAI Python Client
DESCRIPTION: This method finalizes a multi-part file upload identified by `upload_id`. It requires additional parameters (`params`) to confirm the completion, such as a list of part IDs, returning the `Upload` object.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_127

LANGUAGE: python
CODE:
```
client.uploads.complete(upload_id, **params)
```

----------------------------------------

TITLE: Environment Setup with Rye
DESCRIPTION: Commands to bootstrap the project environment using Rye, including syncing dependencies and activating the virtual environment.

SOURCE: https://github.com/openai/openai-python/blob/main/CONTRIBUTING.md#_snippet_0

LANGUAGE: sh
CODE:
```
#!/usr/bin/env sh
$ ./scripts/bootstrap

# Or install Rye manually and run:
$ rye sync --all-features

# Activate the virtual environment
$ source .venv/bin/activate

# Run scripts
$ python script.py
```

----------------------------------------

TITLE: Updating an Assistant in Python
DESCRIPTION: This method updates an existing assistant identified by `assistant_id`. It allows modification of assistant properties using the provided `params` and returns the updated `Assistant` object.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_87

LANGUAGE: python
CODE:
```
client.beta.assistants.update(assistant_id, **params) -> Assistant
```

----------------------------------------

TITLE: OpenAI Vector Store File Batches API
DESCRIPTION: Manages batches of files for OpenAI vector stores. Supports creating, retrieving, cancelling batches, and listing files within a batch. Includes methods for asynchronous operations like polling and uploading.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_35

LANGUAGE: APIDOC
CODE:
```
POST /vector_stores/{vector_store_id}/file_batches
  - Creates a file batch for a vector store.
  - Parameters:
    - vector_store_id: The ID of the vector store.
    - params: Parameters for file batch creation (e.g., file_ids).
  - Returns: VectorStoreFileBatch object.

GET /vector_stores/{vector_store_id}/file_batches/{batch_id}
  - Retrieves a specific file batch.
  - Parameters:
    - batch_id: The ID of the file batch to retrieve.
    - vector_store_id: The ID of the vector store.
  - Returns: VectorStoreFileBatch object.

POST /vector_stores/{vector_store_id}/file_batches/{batch_id}/cancel
  - Cancels a file batch.
  - Parameters:
    - batch_id: The ID of the file batch to cancel.
    - vector_store_id: The ID of the vector store.
  - Returns: VectorStoreFileBatch object.

GET /vector_stores/{vector_store_id}/file_batches/{batch_id}/files
  - Lists files within a specific file batch.
  - Parameters:
    - batch_id: The ID of the file batch.
    - vector_store_id: The ID of the vector store.
    - params: Parameters for listing files (e.g., limit, order, after).
  - Returns: SyncCursorPage[VectorStoreFile].

Additional Methods:
  - create_and_poll: Creates a file batch and polls for its completion.
  - poll: Polls for the status of a file batch operation.
  - upload_and_poll: Uploads files and polls for batch completion.
```

----------------------------------------

TITLE: Uploading Files for Fine-Tuning
DESCRIPTION: Demonstrates how to upload files for fine-tuning using the OpenAI client. It shows how to pass file contents as bytes, a PathLike object, or a tuple.

SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_snippet_18

LANGUAGE: python
CODE:
```
from pathlib import Path
from openai import OpenAI

client = OpenAI()

client.files.create(
    file=Path("input.jsonl"),
    purpose="fine-tune",
)
```

----------------------------------------

TITLE: OpenAI Webhook Verification Methods
DESCRIPTION: Details the methods available for verifying webhook signatures using the OpenAI Python client. The `unwrap` method processes the payload, and `verify_signature` checks the integrity of incoming webhook requests against a provided secret.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_39

LANGUAGE: APIDOC
CODE:
```
client.webhooks.unwrap(payload, headers, *, secret) -> UnwrapWebhookEvent
  Processes the webhook payload and returns an UnwrapWebhookEvent object.

client.webhooks.verify_signature(payload, headers, *, secret, tolerance) -> None
  Verifies the signature of an incoming webhook request. Raises an exception if the signature is invalid.
```

----------------------------------------

TITLE: Fix Create Audio Transcription Endpoint
DESCRIPTION: Resolves an issue with the endpoint used for creating audio transcriptions. This ensures reliable and correct transcription service usage.

SOURCE: https://github.com/openai/openai-python/blob/main/CHANGELOG.md#_snippet_15

LANGUAGE: APIDOC
CODE:
```
API Endpoint Fix:
  - `create audio transcription` endpoint corrected.
```

----------------------------------------

TITLE: Refactor Package: Rename Audio Extra to Voice Helpers
DESCRIPTION: Refactors the package by renaming the 'audio extra' component to 'voice_helpers'. This change improves module naming consistency and clarity.

SOURCE: https://github.com/openai/openai-python/blob/main/CHANGELOG.md#_snippet_22

LANGUAGE: APIDOC
CODE:
```
Refactor: Package 'audio extra' renamed to 'voice_helpers'.
```

----------------------------------------

TITLE: Creating and Polling a Thread Run (OpenAI Python)
DESCRIPTION: This method creates a new run for a thread and then synchronously polls for its completion. It's a convenience for blocking operations, returning the final `Run` object once execution finishes.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_105

LANGUAGE: Python
CODE:
```
client.beta.threads.runs.create_and_poll(*args)
```

----------------------------------------

TITLE: Python Model Listing
DESCRIPTION: Example of how to list all available models using the OpenAI Python client.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_18

LANGUAGE: Python
CODE:
```
from openai import OpenAI

client = OpenAI()

models = client.models.list()
```

----------------------------------------

TITLE: Creating a Batch Request in OpenAI Python
DESCRIPTION: This method initiates a new batch request for processing multiple API calls asynchronously. It accepts various parameters to define the batch's operations and returns a `Batch` object, which can be used to track the batch's status.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_120

LANGUAGE: python
CODE:
```
client.batches.create(**params) -> Batch
```

----------------------------------------

TITLE: Deleting a Message from an OpenAI Thread (Python)
DESCRIPTION: This method removes a specific message from a thread. It requires `message_id` and `thread_id` and returns a `MessageDeleted` object indicating the success of the deletion.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_118

LANGUAGE: python
CODE:
```
client.beta.threads.messages.delete(message_id, *, thread_id) -> MessageDeleted
```

----------------------------------------

TITLE: OpenAI Webhook Event Types
DESCRIPTION: Provides a comprehensive list of Python types for various webhook events, including batch operations, evaluation runs, fine-tuning jobs, and response-related events. These types are essential for parsing and handling incoming webhook payloads.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_38

LANGUAGE: python
CODE:
```
from openai.types.webhooks import (
    BatchCancelledWebhookEvent,
    BatchCompletedWebhookEvent,
    BatchExpiredWebhookEvent,
    BatchFailedWebhookEvent,
    EvalRunCanceledWebhookEvent,
    EvalRunFailedWebhookEvent,
    EvalRunSucceededWebhookEvent,
    FineTuningJobCancelledWebhookEvent,
    FineTuningJobFailedWebhookEvent,
    FineTuningJobSucceededWebhookEvent,
    ResponseCancelledWebhookEvent,
    ResponseCompletedWebhookEvent,
    ResponseFailedWebhookEvent,
    ResponseIncompleteWebhookEvent,
    UnwrapWebhookEvent,
)
```

----------------------------------------

TITLE: OpenAI Completions API
DESCRIPTION: Provides the method for creating text completions using the OpenAI API.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_2

LANGUAGE: APIDOC
CODE:
```
POST /completions
client.completions.create(**params) -> Completion

Description:
  Creates a text completion request.

Parameters:
  **params: A dictionary containing the parameters for the completion request.

Returns:
  Completion: The completion object returned by the API.
```

----------------------------------------

TITLE: Retrieving a Thread (OpenAI Python)
DESCRIPTION: This method fetches an existing thread from the OpenAI API using its unique `thread_id`. It provides access to the thread's current state and content, returning a `Thread` object if found.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_92

LANGUAGE: Python
CODE:
```
client.beta.threads.retrieve(thread_id)
```

----------------------------------------

TITLE: OpenAI Audio Translation API
DESCRIPTION: API endpoint for translating audio files from various languages into English text. Supports customization and returns translated text.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_12

LANGUAGE: APIDOC
CODE:
```
POST /audio/translations
  Description: Translates audio into English text.
  Parameters: **params (TranslationCreateParams)
  Returns: TranslationCreateResponse
```

----------------------------------------

TITLE: Creating a Thread (OpenAI Python)
DESCRIPTION: This method creates a new conversational thread in the OpenAI API. It accepts `params` to configure the thread, such as initial messages or metadata, and returns a `Thread` object representing the newly created thread.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_91

LANGUAGE: Python
CODE:
```
client.beta.threads.create(**params)
```

----------------------------------------

TITLE: OpenAI Python Client: Vector Store File Batches Management
DESCRIPTION: Python code for managing file batches with OpenAI's vector stores. Demonstrates creating, retrieving, cancelling batches, and listing files within a batch. Includes examples for asynchronous operations.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_37

LANGUAGE: Python
CODE:
```
from openai import OpenAI

client = OpenAI()

# Create a file batch
file_batch = client.vector_stores.file_batches.create(
    vector_store_id="vs_abc123",
    file_ids=["file-xyz789", "file-abc456"],
)
print(file_batch)

# Retrieve a file batch
retrieved_batch = client.vector_stores.file_batches.retrieve(
    batch_id=file_batch.id,
    vector_store_id="vs_abc123",
)
print(retrieved_batch)

# Cancel a file batch
cancelled_batch = client.vector_stores.file_batches.cancel(
    batch_id=file_batch.id,
    vector_store_id="vs_abc123",
)
print(cancelled_batch)

# List files in a batch
files_in_batch_page = client.vector_stores.file_batches.list_files(
    batch_id=file_batch.id,
    vector_store_id="vs_abc123",
)
for file in files_in_batch_page.data:
    print(file)

# Asynchronous operations (example)
# batch_for_poll = client.vector_stores.file_batches.create_and_poll(...)
# batch_status = client.vector_stores.file_batches.poll(...)
# uploaded_batch_status = client.vector_stores.file_batches.upload_and_poll(...)
```

----------------------------------------

TITLE: OpenAI Containers API
DESCRIPTION: Provides functionality to manage containers, including creation, retrieval, listing, and deletion. It supports various container-related operations.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_79

LANGUAGE: APIDOC
CODE:
```
POST /containers
  - Creates a new container.
  - Parameters:
    - params: Additional parameters for container creation.
  - Returns: ContainerCreateResponse

GET /containers/{container_id}
  - Retrieves a specific container by its ID.
  - Parameters:
    - container_id: The ID of the container to retrieve.
  - Returns: ContainerRetrieveResponse

GET /containers
  - Lists all containers.
  - Parameters:
    - params: Additional parameters for listing containers.
  - Returns: SyncCursorPage[ContainerListResponse]

DELETE /containers/{container_id}
  - Deletes a specific container.
  - Parameters:
    - container_id: The ID of the container to delete.
  - Returns: None
```

----------------------------------------

TITLE: OpenAI File Management API
DESCRIPTION: API endpoints for managing files with OpenAI. Includes creating, retrieving, listing, deleting, and retrieving file content. Supports asynchronous operations and waiting for processing.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_9

LANGUAGE: APIDOC
CODE:
```
POST /files
  Description: Creates a new file.
  Parameters: **params (FileCreateParams)
  Returns: FileObject

GET /files/{file_id}
  Description: Retrieves a specific file.
  Parameters: file_id (str)
  Returns: FileObject

GET /files
  Description: Lists files, with support for pagination.
  Parameters: **params (FileListParams)
  Returns: SyncCursorPage[FileObject]

DELETE /files/{file_id}
  Description: Deletes a specific file.
  Parameters: file_id (str)
  Returns: FileDeleted

GET /files/{file_id}/content
  Description: Retrieves the content of a specific file.
  Parameters: file_id (str)
  Returns: HttpxBinaryResponseContent

GET /files/{file_id}/content (retrieve_content)
  Description: Retrieves the content of a specific file as a string.
  Parameters: file_id (str)
  Returns: str

wait_for_processing(*args)
  Description: Waits for a file to be processed.
  Returns: FileObject
```

----------------------------------------

TITLE: Creating and Polling a Thread Run (OpenAI Python)
DESCRIPTION: This method creates a thread, starts a run, and then synchronously polls for the run's completion. It's a convenience for blocking operations, returning the final `Run` object once execution finishes.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_96

LANGUAGE: Python
CODE:
```
client.beta.threads.create_and_run_poll(*args)
```

----------------------------------------

TITLE: Fix Audio: Correct Transcription Stream Event Parsing
DESCRIPTION: Resolves a bug where transcription stream events were not being parsed correctly, improving the reliability and accuracy of audio transcription features.

SOURCE: https://github.com/openai/openai-python/blob/main/CHANGELOG.md#_snippet_18

LANGUAGE: APIDOC
CODE:
```
Bug Fix: Audio transcription stream event parsing corrected.
```

----------------------------------------

TITLE: Async Client Initialization with aiohttp
DESCRIPTION: Demonstrates how to initialize the asynchronous OpenAI client using the DefaultAioHttpClient for making API calls.

SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_snippet_8

LANGUAGE: python
CODE:
```
import asyncio
from openai import DefaultAioHttpClient
from openai import AsyncOpenAI


async def main() -> None:
    async with AsyncOpenAI(
        api_key="My API Key",
        http_client=DefaultAioHttpClient(),
    ) as client:
        chat_completion = await client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": "Say this is a test",
                }
            ],
            model="gpt-4o",
        )


asyncio.run(main())
```

----------------------------------------

TITLE: Python Fine-Tuning Job Resume
DESCRIPTION: Example of how to resume a paused fine-tuning job using the OpenAI Python client.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_26

LANGUAGE: Python
CODE:
```
from openai import OpenAI

client = OpenAI()

resumed_job = client.fine_tuning.jobs.resume("ftjob-abc123xyz")
```

----------------------------------------

TITLE: OpenAI Assistant and Thread Types
DESCRIPTION: Defines the data structures and types used for Assistants and Threads in the OpenAI API, including various tool types and event stream options.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_45

LANGUAGE: python
CODE:
```
from openai.types.beta import (
    Assistant,
    AssistantDeleted,
    AssistantStreamEvent,
    AssistantTool,
    CodeInterpreterTool,
    FileSearchTool,
    FunctionTool,
    MessageStreamEvent,
    RunStepStreamEvent,
    RunStreamEvent,
    ThreadStreamEvent,
    AssistantResponseFormatOption,
    AssistantToolChoice,
    AssistantToolChoiceFunction,
    AssistantToolChoiceOption,
    Thread,
    ThreadDeleted,
)
```

----------------------------------------

TITLE: Install OpenAI with aiohttp
DESCRIPTION: Installs the OpenAI Python library with support for aiohttp, enabling asynchronous HTTP requests.

SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_snippet_7

LANGUAGE: bash
CODE:
```
pip install openai[aiohttp]
```

----------------------------------------

TITLE: Chore: Add OpenAPI Spec Hash to .stats.yml
DESCRIPTION: Adds a hash of OpenAPI specification and configuration inputs to the `.stats.yml` file. This helps in tracking changes and ensuring consistency in API generation.

SOURCE: https://github.com/openai/openai-python/blob/main/CHANGELOG.md#_snippet_19

LANGUAGE: APIDOC
CODE:
```
Chore: Add hash of OpenAPI spec/config inputs to .stats.yml.
```

----------------------------------------

TITLE: Python Fine-Tuning Job Retrieval
DESCRIPTION: Example of how to retrieve a specific fine-tuning job using the OpenAI Python client.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_21

LANGUAGE: Python
CODE:
```
from openai import OpenAI

client = OpenAI()

job = client.fine_tuning.jobs.retrieve("ftjob-abc123xyz")
```

----------------------------------------

TITLE: Updating a Message in an OpenAI Thread (Python)
DESCRIPTION: This method modifies an existing message within a specified thread. It requires `message_id` and `thread_id`, along with parameters for the fields to be updated, and returns the updated `Message` object.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_116

LANGUAGE: python
CODE:
```
client.beta.threads.messages.update(message_id, *, thread_id, **params) -> Message
```

----------------------------------------

TITLE: OpenAI Python SDK - Poll Run Status
DESCRIPTION: Demonstrates how to use the `poll` method to check the status of a run without creating a new one.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_56

LANGUAGE: python
CODE:
```
from openai import OpenAI

client = OpenAI()

run = client.beta.threads.runs.poll(
    run_id="run_id",
    thread_id="thread_id",
)
```

----------------------------------------

TITLE: Verify Webhook Signature
DESCRIPTION: Demonstrates how to verify the signature of an incoming webhook request using the `client.webhooks.verify_signature()` method. It ensures the payload is authentic before processing. The raw request body and headers are used for verification. An exception is raised if the signature is invalid.

SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_snippet_21

LANGUAGE: python
CODE:
```
import json
from openai import OpenAI
from flask import Flask, request

app = Flask(__name__)
client = OpenAI()  # OPENAI_WEBHOOK_SECRET environment variable is used by default


@app.route("/webhook", methods=["POST"])
def webhook():
    request_body = request.get_data(as_text=True)

    try:
        client.webhooks.verify_signature(request_body, request.headers)

        # Parse the body after verification
        event = json.loads(request_body)
        print("Verified event:", event)

        return "ok"
    except Exception as e:
        print("Invalid signature:", e)
        return "Invalid signature", 400


if __name__ == "__main__":
    app.run(port=8000)
```

----------------------------------------

TITLE: Run Code Linting Checks
DESCRIPTION: This command executes the project's linting checks using configured tools like `ruff` and `black` to identify potential code quality, style, and best practice violations.

SOURCE: https://github.com/openai/openai-python/blob/main/CONTRIBUTING.md#_snippet_11

LANGUAGE: sh
CODE:
```
./scripts/lint
```

----------------------------------------

TITLE: OpenAI Python Client - Fine-Tuning Checkpoint Permissions
DESCRIPTION: Python code for interacting with the OpenAI fine-tuning checkpoint permissions API. Demonstrates creating, retrieving, and deleting permissions.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_31

LANGUAGE: Python
CODE:
```
from openai import OpenAI

client = OpenAI()

# Create permission
permission_create_response = client.fine_tuning.checkpoints.permissions.create(
    fine_tuned_model_checkpoint="your_checkpoint_id",
    # Add other params as needed
)

# Retrieve permissions
permission_retrieve_response = client.fine_tuning.checkpoints.permissions.retrieve(
    fine_tuned_model_checkpoint="your_checkpoint_id",
    # Add other params as needed
)

# Delete permission
permission_delete_response = client.fine_tuning.checkpoints.permissions.delete(
    permission_id="your_permission_id",
    fine_tuned_model_checkpoint="your_checkpoint_id",
)
```

----------------------------------------

TITLE: Configuring Timeouts
DESCRIPTION: Demonstrates how to configure client-level timeouts and override them on a per-request basis for OpenAI API calls. Includes default timeout values for different operations.

SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_snippet_27

LANGUAGE: python
CODE:
```
from openai import OpenAI
import httpx

# More granular control:
client = OpenAI(
    timeout=httpx.Timeout(60.0, read=5.0, write=10.0, connect=2.0),
)

# Override per-request:
client.with_options(timeout=5.0).chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "How can I list all files in a directory using Python?",
        }
    ],
    model="gpt-4o",
)
```

----------------------------------------

TITLE: OpenAI Python SDK - Retrieve Run Step
DESCRIPTION: Demonstrates how to retrieve a specific run step by its ID, along with the thread and run IDs.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_60

LANGUAGE: python
CODE:
```
from openai import OpenAI

client = OpenAI()

step = client.beta.threads.runs.steps.retrieve(
    step_id="step_id",
    thread_id="thread_id",
    run_id="run_id",
)
```

----------------------------------------

TITLE: Adding and Running Examples
DESCRIPTION: Steps to add a new Python example file and make it executable, allowing it to be run against the API.

SOURCE: https://github.com/openai/openai-python/blob/main/CONTRIBUTING.md#_snippet_2

LANGUAGE: python
CODE:
```
# add an example to examples/<your-example>.py

#!/usr/bin/env -S rye run python
…
```

----------------------------------------

TITLE: OpenAI Python SDK - Create and Stream Run
DESCRIPTION: Shows how to use `create_and_stream` to create a run and receive events as they happen, enabling real-time updates.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_55

LANGUAGE: python
CODE:
```
from openai import OpenAI
from openai.types.beta import AssistantStreamEventHandler

client = OpenAI()

stream = client.beta.threads.runs.create_and_stream(
    thread_id="thread_id",
    # additional parameters can be passed here
)

for event in stream:
    if isinstance(event, AssistantStreamEventHandler):
        print(event.data.content[0].text.value)

```

----------------------------------------

TITLE: Chore: CI Run Workflows on Next Branch
DESCRIPTION: Configures the Continuous Integration (CI) system to also run workflows on the 'next' branch, ensuring earlier detection of issues in development branches.

SOURCE: https://github.com/openai/openai-python/blob/main/CHANGELOG.md#_snippet_26

LANGUAGE: APIDOC
CODE:
```
Chore: CI workflows configured to run on 'next' branch.
```

----------------------------------------

TITLE: Manual Pagination Control for Fine-Tuning Jobs
DESCRIPTION: Shows how to manually control pagination when fetching fine-tuning jobs. It demonstrates checking for the next page, retrieving it, and accessing pagination details like the cursor.

SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_snippet_16

LANGUAGE: python
CODE:
```
# Remove `await` for non-async usage.
first_page = await client.fine_tuning.jobs.list(
    limit=20,
)
if first_page.has_next_page():
    print(f"will fetch next page using these details: {first_page.next_page_info()}")
    next_page = await first_page.get_next_page()
    print(f"number of items we just fetched: {len(next_page.data)}")

# Remove `await` for non-async usage.

first_page = await client.fine_tuning.jobs.list(
    limit=20,
)

print(f"next page cursor: {first_page.after}")  # => "next page cursor: ..."
for job in first_page.data:
    print(job.id)

# Remove `await` for non-async usage.
```

----------------------------------------

TITLE: Configure HTTP Client with Proxies and Transports
DESCRIPTION: Demonstrates how to override the httpx client to include custom configurations like proxies and transports for the OpenAI Python client. This allows for advanced network configurations.

SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_snippet_33

LANGUAGE: python
CODE:
```
import httpx
from openai import OpenAI, DefaultHttpxClient

client = OpenAI(
    # Or use the `OPENAI_BASE_URL` env var
    base_url="http://my.test.server.example.com:8083/v1",
    http_client=DefaultHttpxClient(
        proxy="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

----------------------------------------

TITLE: OpenAI Python SDK - List Run Steps
DESCRIPTION: Shows how to list all steps associated with a particular run within a thread using the OpenAI Python SDK.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_61

LANGUAGE: python
CODE:
```
from openai import OpenAI

client = OpenAI()

steps = client.beta.threads.runs.steps.list(
    run_id="run_id",
    thread_id="thread_id",
    # additional parameters can be passed here
)
```

----------------------------------------

TITLE: OpenAI Image Generation and Editing API
DESCRIPTION: API endpoints for generating and editing images using OpenAI. Supports creating image variations, editing existing images with masks, and generating new images from text prompts.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_10

LANGUAGE: APIDOC
CODE:
```
POST /images/variations
  Description: Creates variations of an image.
  Parameters: **params (ImageCreateVariationParams)
  Returns: ImagesResponse

POST /images/edits
  Description: Edits an image with a mask.
  Parameters: **params (ImageEditParams)
  Returns: ImagesResponse

POST /images/generations
  Description: Generates images from text prompts.
  Parameters: **params (ImageGenerateParams)
  Returns: ImagesResponse
```

----------------------------------------

TITLE: OpenAI API Reference
DESCRIPTION: This section outlines the core functionalities and methods available through the OpenAI API client, including fine-tuning jobs, chat completions, file uploads, and webhook handling.

SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_snippet_20

LANGUAGE: APIDOC
CODE:
```
OpenAIClient:
  __init__(api_key: str = None, organization: str = None, ...)
    Initializes the OpenAI client with optional API key and organization.

  fine_tuning.jobs:
    list(limit: int = 20, after: str = None, ...):
      Retrieves a list of fine-tuning jobs.
      Parameters:
        limit: Maximum number of jobs to return.
        after: A cursor for pagination, returning jobs after this job.
      Returns: A list of fine-tuning job objects.

    create(training_file: str, validation_file: str = None, ...):
      Creates a new fine-tuning job.
      Parameters:
        training_file: The ID of the training file.
        validation_file: The ID of the validation file.
      Returns: The created fine-tuning job object.

  chat.completions:
    create(model: str, messages: list, ...):
      Creates a completion for a chat conversation.
      Parameters:
        model: The ID of the model to use.
        messages: A list of messages comprising the conversation.
      Returns: A chat completion response object.

  files:
    create(file: bytes | PathLike | tuple, purpose: str, ...):
      Uploads a file to OpenAI.
      Parameters:
        file: The file to upload, as bytes, PathLike, or (filename, contents, media_type).
        purpose: The intended use of the file (e.g., "fine-tune").
      Returns: The file object.

  webhooks:
    unwrap(body: str, signature: str, ...):
      Parses and verifies a webhook payload.
      Parameters:
        body: The raw JSON string of the webhook request body.
        signature: The value of the 'OpenAI-Signature' header.
      Returns: The parsed event object.
      Raises: ValueError if the signature is invalid.
```

----------------------------------------

TITLE: Configure Retries
DESCRIPTION: Explains how to manage automatic retries for API requests. It shows how to set the default number of retries for all requests using `max_retries` during client initialization and how to override it for specific requests using `with_options()`.

SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_snippet_24

LANGUAGE: python
CODE:
```
from openai import OpenAI

# Configure the default for all requests:
client = OpenAI(
    # default is 2
    max_retries=0,
)

# Or, configure per-request:
client.with_options(max_retries=5).chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "How can I get the name of the current day in JavaScript?",
        }
    ],
    model="gpt-4o",
)
```

----------------------------------------

TITLE: OpenAI API Error Codes
DESCRIPTION: Provides a mapping of HTTP status codes to specific OpenAI API error types. This table is useful for understanding the nature of API errors and implementing appropriate error handling logic.

SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_snippet_26

LANGUAGE: APIDOC
CODE:
```
OpenAI API Error Codes:

| Status Code | Error Type                 |
| ----------- | -------------------------- |
| 400         | `BadRequestError`          |
| 401         | `AuthenticationError`      |
| 403         | `PermissionDeniedError`    |
| 404         | `NotFoundError`            |
| 422         | `UnprocessableEntityError` |
| 429         | `RateLimitError`           |
| >=500       | `InternalServerError`      |
| N/A         | `APIConnectionError`       |
```

----------------------------------------

TITLE: Importing OpenAI Run Types (Python)
DESCRIPTION: This Python snippet imports specific type definitions from `openai.types.beta.threads` module. These types, including `Run`, `RunStatus`, and `RequiredActionFunctionToolCall`, are essential for managing and understanding the state and interactions of Assistant runs within a thread.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_98

LANGUAGE: Python
CODE:
```
from openai.types.beta.threads import RequiredActionFunctionToolCall, Run, RunStatus
```

----------------------------------------

TITLE: Retrieving a Specific Batch Request in OpenAI Python
DESCRIPTION: This method fetches the details of a specific batch request by its ID. It requires the `batch_id` and returns a `Batch` object, providing information about the batch's current status, errors, and request counts.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_121

LANGUAGE: python
CODE:
```
client.batches.retrieve(batch_id) -> Batch
```

----------------------------------------

TITLE: Async Usage Example
DESCRIPTION: Demonstrates asynchronous usage of the OpenAI client by importing `AsyncOpenAI` and using `await` for API calls. It includes running an async function with `asyncio.run`.

SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_snippet_5

LANGUAGE: python
CODE:
```
import os
import asyncio
from openai import AsyncOpenAI

client = AsyncOpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)


async def main() -> None:
    response = await client.responses.create(
        model="gpt-4o", input="Explain disestablishmentarianism to a smart five year old."
    )
    print(response.output_text)

asyncio.run(main())
```

----------------------------------------

TITLE: Importing Run Step Types for OpenAI Python API
DESCRIPTION: This snippet imports various type definitions related to run steps within the OpenAI Assistants API. These types are used to define the structure of data returned by or sent to the API when managing or inspecting the execution steps of a run, including details about tool calls (Code Interpreter, File Search, Function) and message creation.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_110

LANGUAGE: python
CODE:
```
from openai.types.beta.threads.runs import (
    CodeInterpreterLogs,
    CodeInterpreterOutputImage,
    CodeInterpreterToolCall,
    CodeInterpreterToolCallDelta,
    FileSearchToolCall,
    FileSearchToolCallDelta,
    FunctionToolCall,
    FunctionToolCallDelta,
    MessageCreationStepDetails,
    RunStep,
    RunStepDelta,
    RunStepDeltaEvent,
    RunStepDeltaMessageDelta,
    RunStepInclude,
    ToolCall,
    ToolCallDelta,
    ToolCallDeltaObject,
    ToolCallsStepDetails,
)
```

----------------------------------------

TITLE: Running Examples
DESCRIPTION: Commands to make an example script executable and then run it.

SOURCE: https://github.com/openai/openai-python/blob/main/CONTRIBUTING.md#_snippet_3

LANGUAGE: sh
CODE:
```
$ chmod +x examples/<your-example>.py
$ ./examples/<your-example>.py
```

----------------------------------------

TITLE: Configure Timeouts
DESCRIPTION: Details how to set request timeouts for the OpenAI API. It demonstrates configuring a default timeout for all requests using the `timeout` parameter during client initialization, accepting either a float for seconds or an `httpx.Timeout` object.

SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_snippet_25

LANGUAGE: python
CODE:
```
from openai import OpenAI

# Configure the default for all requests:
client = OpenAI(
    # 20 seconds (default is 10 minutes)
    timeout=20.0,
)
```

----------------------------------------

TITLE: Building and Installing from Source
DESCRIPTION: Commands to build the Python package distributable files (wheel) and then install it locally.

SOURCE: https://github.com/openai/openai-python/blob/main/CONTRIBUTING.md#_snippet_5

LANGUAGE: sh
CODE:
```
# Build the package
$ rye build
# or
$ python -m build

# Install the wheel file
$ pip install ./path-to-wheel-file.whl
```

----------------------------------------

TITLE: Manual Publishing to PyPI
DESCRIPTION: Instructions for manually publishing the package to PyPI using a provided script and environment variable.

SOURCE: https://github.com/openai/openai-python/blob/main/CONTRIBUTING.md#_snippet_9

LANGUAGE: sh
CODE:
```
# Ensure PYPI_TOKEN is set in the environment
$ bin/publish-pypi
```

----------------------------------------

TITLE: Creating an Upload - OpenAI Python Client
DESCRIPTION: This method initiates a new file upload to the OpenAI API. It accepts various parameters (`params`) to configure the upload, such as file content and purpose, returning an `Upload` object upon success.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_125

LANGUAGE: python
CODE:
```
client.uploads.create(**params)
```

----------------------------------------

TITLE: Fix Package: Make Sounddevice and Numpy Optional Dependencies
DESCRIPTION: Modifies the package configuration to make `sounddevice` and `numpy` optional dependencies. This reduces the default installation footprint for users who do not require these specific functionalities.

SOURCE: https://github.com/openai/openai-python/blob/main/CHANGELOG.md#_snippet_25

LANGUAGE: APIDOC
CODE:
```
Bug Fix: Sounddevice and numpy made optional dependencies.
```

----------------------------------------

TITLE: Linting and Formatting Code
DESCRIPTION: Commands to run linting checks and automatically format the code using Ruff and Black.

SOURCE: https://github.com/openai/openai-python/blob/main/CONTRIBUTING.md#_snippet_8

LANGUAGE: sh
CODE:
```
# To lint:
$ ./scripts/lint

# To format and fix issues:
$ ./scripts/format
```

----------------------------------------

TITLE: OpenAI Runs API
DESCRIPTION: Manages the lifecycle of runs within a thread. Supports creating, retrieving, updating, listing, canceling, and submitting tool outputs for runs. Includes methods for polling and streaming run events.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_46

LANGUAGE: APIDOC
CODE:
```
POST /threads/{thread_id}/runs
  - Creates a new run for a thread.
  - Parameters: thread_id, params (RunCreateParams)
  - Returns: Run

GET /threads/{thread_id}/runs/{run_id}
  - Retrieves a specific run.
  - Parameters: run_id, thread_id
  - Returns: Run

POST /threads/{thread_id}/runs/{run_id}
  - Updates a run.
  - Parameters: run_id, thread_id, params (RunUpdateParams)
  - Returns: Run

GET /threads/{thread_id}/runs
  - Lists runs for a thread.
  - Parameters: thread_id, params (RunListParams)
  - Returns: SyncCursorPage[Run]

POST /threads/{thread_id}/runs/{run_id}/cancel
  - Cancels a run.
  - Parameters: run_id, thread_id
  - Returns: Run

POST /threads/{thread_id}/runs/{run_id}/submit_tool_outputs
  - Submits tool outputs for a run.
  - Parameters: run_id, thread_id, params (RunSubmitToolOutputsParams)
  - Returns: Run

create_and_poll(*args) -> Run
  - Creates a run and polls for its completion.

create_and_stream(*args) -> AssistantStreamManager[AssistantEventHandler] | AssistantStreamManager[AssistantEventHandlerT]
  - Creates a run and streams its events.

poll(*args) -> Run
  - Polls for the status of a run.

stream(*args) -> AssistantStreamManager[AssistantEventHandler] | AssistantStreamManager[AssistantEventHandlerT]
  - Streams run events.

submit_tool_outputs_and_poll(*args) -> Run
  - Submits tool outputs and polls for completion.

submit_tool_outputs_stream(*args) -> AssistantStreamManager[AssistantEventHandler] | AssistantStreamManager[AssistantEventHandlerT]
  - Submits tool outputs and streams events.
```

----------------------------------------

TITLE: Creating a Run for a Thread (OpenAI Python)
DESCRIPTION: This method initiates a new execution run for a specified `thread_id`. It accepts `params` to configure the run, such as the Assistant to use, and returns a `Run` object representing the newly started execution.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_99

LANGUAGE: Python
CODE:
```
client.beta.threads.runs.create(thread_id, **params)
```

----------------------------------------

TITLE: OpenAI Client Configuration Options
DESCRIPTION: Lists the configuration options available for the `OpenAI` client, including base URL, and specific options for Azure OpenAI integration like `api_version` and `azure_endpoint`.

SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_snippet_38

LANGUAGE: apidoc
CODE:
```
OpenAI:
  __init__(base_url: str = None, http_client: DefaultHttpxClient = None, ...)
    base_url: The base URL for the OpenAI API. Defaults to the official OpenAI API endpoint.
    http_client: An optional httpx.Client instance for custom configurations.

AzureOpenAI:
  __init__(api_version: str, azure_endpoint: str, azure_deployment: str = None, azure_ad_token: str = None, azure_ad_token_provider: callable = None, ...)
    api_version: The version of the Azure OpenAI API to use (e.g., "2023-07-01-preview").
    azure_endpoint: The Azure OpenAI endpoint URL.
    azure_deployment: The name of the Azure OpenAI deployment.
    azure_ad_token: A token for Azure Active Directory authentication.
    azure_ad_token_provider: A callable that provides an Azure AD token.

Common Options:
  - `base_url` (or `OPENAI_BASE_URL` env var)
  - `http_client` (for `OpenAI`)
  - `azure_endpoint` (or `AZURE_OPENAI_ENDPOINT` env var) (for `AzureOpenAI`)
  - `azure_deployment` (for `AzureOpenAI`)
  - `api_version` (or `OPENAI_API_VERSION` env var) (for `AzureOpenAI`)
  - `azure_ad_token` (or `AZURE_OPENAI_AD_TOKEN` env var) (for `AzureOpenAI`)
  - `azure_ad_token_provider` (for `AzureOpenAI`)
```

----------------------------------------

TITLE: Chore: Internal - Codegen Related Update
DESCRIPTION: Performs an internal update related to code generation, potentially improving the efficiency or accuracy of generated code.

SOURCE: https://github.com/openai/openai-python/blob/main/CHANGELOG.md#_snippet_32

LANGUAGE: APIDOC
CODE:
```
Chore: Internal codegen related update.
```

----------------------------------------

TITLE: OpenAI Python SDK - Stream Run Events
DESCRIPTION: Shows how to use the `stream` method to get a real-time stream of events for an existing run.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_57

LANGUAGE: python
CODE:
```
from openai import OpenAI
from openai.types.beta import AssistantStreamEventHandler

client = OpenAI()

stream = client.beta.threads.runs.stream(
    run_id="run_id",
    thread_id="thread_id",
)

for event in stream:
    if isinstance(event, AssistantStreamEventHandler):
        print(event.data.content[0].text.value)

```

----------------------------------------

TITLE: OpenAI Audio Speech API
DESCRIPTION: API endpoint for converting text into spoken audio. Supports various models and voice options for speech synthesis.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_13

LANGUAGE: APIDOC
CODE:
```
POST /audio/speech
  Description: Converts text to speech.
  Parameters: **params (SpeechCreateParams)
  Returns: HttpxBinaryResponseContent
```

----------------------------------------

TITLE: Creating and Streaming a Thread Run (OpenAI Python)
DESCRIPTION: This method creates a thread, starts a run, and streams real-time updates as the run progresses. It returns an `AssistantStreamManager` which allows for event-driven processing of the run's lifecycle.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_97

LANGUAGE: Python
CODE:
```
client.beta.threads.create_and_run_stream(*args)
```

----------------------------------------

TITLE: Chore: Internal - Re-add Releases Workflow
DESCRIPTION: Re-adds the releases workflow internally, ensuring the automated process for creating and managing software releases is active.

SOURCE: https://github.com/openai/openai-python/blob/main/CHANGELOG.md#_snippet_31

LANGUAGE: APIDOC
CODE:
```
Chore: Internal releases workflow re-added.
```

----------------------------------------

TITLE: Creating and Streaming a Thread Run (OpenAI Python)
DESCRIPTION: This method creates a new run for a thread and streams real-time updates as the run progresses. It returns an `AssistantStreamManager` which allows for event-driven processing of the run's lifecycle.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_106

LANGUAGE: Python
CODE:
```
client.beta.threads.runs.create_and_stream(*args)
```

----------------------------------------

TITLE: Customize Client Per-Request
DESCRIPTION: Shows how to customize the HTTP client configuration on a per-request basis using the `with_options()` method.

SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_snippet_34

LANGUAGE: python
CODE:
```
client.with_options(http_client=DefaultHttpxClient(...))
```

----------------------------------------

TITLE: OpenAI Chat Types
DESCRIPTION: Imports the ChatModel type used for chat-based interactions.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_3

LANGUAGE: python
CODE:
```
from openai.types import ChatModel
```

----------------------------------------

TITLE: OpenAI Fine-Tuning Checkpoint Permissions API
DESCRIPTION: Manages permissions for fine-tuning checkpoints. Supports creating, retrieving, and deleting permissions.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_28

LANGUAGE: APIDOC
CODE:
```
POST /fine_tuning/checkpoints/{fine_tuned_model_checkpoint}/permissions
  - Creates a permission for a fine-tuning checkpoint.
  - Parameters:
    - fine_tuned_model_checkpoint: The ID of the fine-tuned model checkpoint.
    - params: Additional parameters for creating the permission.
  - Returns: A SyncPage of PermissionCreateResponse.

GET /fine_tuning/checkpoints/{fine_tuned_model_checkpoint}/permissions
  - Retrieves permissions for a fine-tuning checkpoint.
  - Parameters:
    - fine_tuned_model_checkpoint: The ID of the fine-tuned model checkpoint.
    - params: Additional parameters for retrieving permissions.
  - Returns: PermissionRetrieveResponse.

DELETE /fine_tuning/checkpoints/{fine_tuned_model_checkpoint}/permissions/{permission_id}
  - Deletes a specific permission for a fine-tuning checkpoint.
  - Parameters:
    - permission_id: The ID of the permission to delete.
    - fine_tuned_model_checkpoint: The ID of the fine-tuned model checkpoint.
  - Returns: PermissionDeleteResponse.
```

----------------------------------------

TITLE: Canceling an Upload - OpenAI Python Client
DESCRIPTION: This method cancels an in-progress file upload identified by its `upload_id`. It returns the `Upload` object with its status updated to canceled, preventing further processing.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_126

LANGUAGE: python
CODE:
```
client.uploads.cancel(upload_id)
```

----------------------------------------

TITLE: Add API Feature: O1-Pro Model Availability
DESCRIPTION: Enables the 'o1-pro' model to be accessible through the API, expanding the range of available models for users.

SOURCE: https://github.com/openai/openai-python/blob/main/CHANGELOG.md#_snippet_29

LANGUAGE: APIDOC
CODE:
```
Feature: 'o1-pro' model now available via API.
```

----------------------------------------

TITLE: OpenAI Threads API
DESCRIPTION: Manages Threads within the OpenAI API. Supports creating, retrieving, updating, deleting threads, and creating threads with associated runs. Includes streaming capabilities for runs.

SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_snippet_44

LANGUAGE: APIDOC
CODE:
```
client.beta.threads.create(**params) -> Thread
  POST /threads
  Creates a new thread.
  Parameters:
    params: Thread creation parameters.
  Returns:
    The created Thread object.
```

LANGUAGE: APIDOC
CODE:
```
client.beta.threads.retrieve(thread_id) -> Thread
  GET /threads/{thread_id}
  Retrieves a thread by its ID.
  Parameters:
    thread_id: The ID of the thread to retrieve.
  Returns:
    The Thread object.
```

LANGUAGE: APIDOC
CODE:
```
client.beta.threads.update(thread_id, **params) -> Thread
  POST /threads/{thread_id}
  Updates an existing thread.
  Parameters:
    thread_id: The ID of the thread to update.
    params: Thread update parameters.
  Returns:
    The updated Thread object.
```

LANGUAGE: APIDOC
CODE:
```
client.beta.threads.delete(thread_id) -> ThreadDeleted
  DELETE /threads/{thread_id}
  Deletes a thread by its ID.
  Parameters:
    thread_id: The ID of the thread to delete.
  Returns:
    A ThreadDeleted object indicating the result of the deletion.
```

LANGUAGE: APIDOC
CODE:
```
client.beta.threads.create_and_run(**params) -> Run
  POST /threads/runs
  Creates a thread and initiates a run.
  Parameters:
    params: Parameters for creating the thread and run.
  Returns:
    The created Run object.
```

LANGUAGE: APIDOC
CODE:
```
client.beta.threads.create_and_run_poll(*args) -> Run
  Polls for the completion of a thread run created with create_and_run.
  Parameters:
    *args: Arguments for polling.
  Returns:
    The Run object upon completion.
```

LANGUAGE: APIDOC
CODE:
```
client.beta.threads.create_and_run_stream(*args) -> AssistantStreamManager[AssistantEventHandler] | AssistantStreamManager[AssistantEventHandlerT]
  Streams the results of a thread run created with create_and_run.
  Parameters:
    *args: Arguments for streaming.
  Returns:
    An AssistantStreamManager for handling stream events.
```

========================
QUESTIONS AND ANSWERS
========================
TOPIC: OpenAI Python API Documentation
Q: What types are available for handling different response formats in the openai-python library?
A: The openai-python library supports various response formats, with types like `ResponseFormatJSONObject`, `ResponseFormatJSONSchema`, `ResponseFormatText`, `ResponseFormatTextGrammar`, and `ResponseFormatTextPython`.


SOURCE: https://github.com/openai/openai-python/blob/main/api.md#_qa_9

----------------------------------------

TOPIC: 
Q: What is the process for responsible disclosure of security issues found in the openai-python SDK?
A: Responsible disclosure involves reporting a suspected security vulnerability to the Stainless team and allowing them a reasonable amount of time to investigate and address the issue before making any information public.


SOURCE: https://github.com/openai/openai-python/blob/main/SECURITY.md#_qa_1

----------------------------------------

TOPIC: OpenAI Python API Library Documentation
Q: How can I generate text using the OpenAI Python library's Responses API?
A: You can generate text by creating an OpenAI client, specifying the model, and providing instructions and input. The response object will contain the generated output text.


SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_qa_5

----------------------------------------

TOPIC: OpenAI Python API Library Documentation
Q: What is the primary API for interacting with OpenAI models using the Python library?
A: The primary API for interacting with OpenAI models is the Responses API. This API allows you to generate text from models like GPT-4o.


SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_qa_4

----------------------------------------

TOPIC: OpenAI Python SDK: Structured Outputs and Streaming
Q: How does the OpenAI Python SDK assist in auto-parsing response content with Pydantic models?
A: You can pass a Pydantic model to the `.parse()` method. The SDK automatically converts this model into a JSON schema, sends it to the API, and then parses the API's response content back into the specified Pydantic model.


SOURCE: https://github.com/openai/openai-python/blob/main/helpers.md#_qa_1

----------------------------------------

TOPIC: OpenAI Python SDK: Structured Outputs and Streaming
Q: What is the `ParsedChatCompletion` object in the OpenAI Python SDK?
A: The `ParsedChatCompletion` object is returned by the `client.chat.completions.parse()` method. It is a subclass of the standard `ChatCompletion` class and provides richer integrations with Python-specific types for handling parsed responses.


SOURCE: https://github.com/openai/openai-python/blob/main/helpers.md#_qa_7

----------------------------------------

TOPIC: 
Q: Who should be contacted for questions or concerns about the security of OpenAI's services, unrelated to the SDK?
A: For questions or concerns regarding the security of OpenAI's services, unrelated to the SDK, please contact disclosure@openai.com.


SOURCE: https://github.com/openai/openai-python/blob/main/SECURITY.md#_qa_3

----------------------------------------

TOPIC: OpenAI Python API Library Documentation
Q: Can the OpenAI Python library handle image inputs?
A: Yes, the OpenAI Python library supports vision capabilities. You can provide image URLs or base64 encoded image strings as part of the input to the Responses API.


SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_qa_8

----------------------------------------

TOPIC: OpenAI Python SDK: Structured Outputs and Streaming
Q: What are the differences in restrictions between `chat.completions.parse()` and `chat.completions.create()` in the OpenAI Python SDK?
A: The `chat.completions.parse()` method raises `LengthFinishReasonError` or `ContentFilterFinishReasonError` if the completion finishes with a `length` or `content_filter` reason. Additionally, only strict function tools can be passed to `.parse()`.


SOURCE: https://github.com/openai/openai-python/blob/main/helpers.md#_qa_3

----------------------------------------

TOPIC: OpenAI Python API Library Documentation
Q: What is the OpenAI Python library?
A: The OpenAI Python library provides convenient access to the OpenAI REST API from any Python 3.8+ application. It includes type definitions for all request parameters and response fields, and offers both synchronous and asynchronous clients.


SOURCE: https://github.com/openai/openai-python/blob/main/README.md#_qa_0