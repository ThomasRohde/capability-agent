import json
import logging
from io import StringIO

import httpx

from capability_agent.llm import LoggingTransport


def test_full_logging_emits_response_body():
    body = {"foo": "bar"}

    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json=body, request=request)

    transport = httpx.MockTransport(handler)

    log_stream = StringIO()
    logger = logging.getLogger("capability_agent.tests.logging")
    logger.setLevel(logging.INFO)
    logger.handlers = []
    stream_handler = logging.StreamHandler(log_stream)
    stream_handler.setFormatter(logging.Formatter("%(message)s"))
    logger.addHandler(stream_handler)
    logger.propagate = False

    logging_transport = LoggingTransport(
        transport=transport,
        logger=logger,
        log_level="full",
        log_body=True,
    )

    request = httpx.Request("POST", "https://example.com", json={"hello": "world"})
    response = logging_transport.handle_request(request)

    # Consume the response to trigger deferred logging.
    response.read()
    response.close()

    logs = [line for line in log_stream.getvalue().splitlines() if line.strip()]
    assert len(logs) >= 2  # request + response

    response_log = json.loads(logs[-1])
    assert response_log["type"] == "response"
    assert response_log.get("body") == body
