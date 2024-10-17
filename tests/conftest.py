from collections.abc import AsyncIterator

import pytest

from nats.aio.client import Client as NATS


@pytest.fixture(scope="function")
async def nats_client() -> AsyncIterator[NATS]:
    nc = NATS()
    await nc.connect()

    yield nc

    await nc.close()
