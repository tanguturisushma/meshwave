
import asyncio
import cloudpickle


# Python function that we want the server to execute
def add_numbers(a, b):
    return a + b


class ClientNode(asyncio.DatagramProtocol):

    def __init__(self, response_future):
        self.response_future = response_future

    def connection_made(self, transport):
        self.transport = transport

        # Prepare the function and arguments
        task = (add_numbers, (10, 20))

        # Serialize the task
        task_data = cloudpickle.dumps(task)

        print("Client Node started.")
        print("Sending remote task: add_numbers(10, 20)")
        print("Task sent to Server Node.")

        # Send the task to the server
        self.transport.sendto(
            task_data,
            ("127.0.0.1", 9999)
        )

    def datagram_received(self, data, addr):

        # Deserialize the server response
        status, result = cloudpickle.loads(data)

        if status == "success":
            print(f"\nRemote task result: {result}")
        else:
            print(f"\nRemote task failed: {result}")

        if not self.response_future.done():
            self.response_future.set_result(result)


async def main():

    loop = asyncio.get_running_loop()

    response_future = loop.create_future()

    transport, protocol = await loop.create_datagram_endpoint(
        lambda: ClientNode(response_future),
        local_addr=("127.0.0.1", 0)
    )

    try:
        await asyncio.wait_for(response_future, timeout=10)

    except asyncio.TimeoutError:
        print("Server did not respond.")

    finally:
        transport.close()


if __name__ == "__main__":
    asyncio.run(main())
