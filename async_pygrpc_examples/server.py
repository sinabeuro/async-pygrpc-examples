import asyncio
import logging
import random

from grpc.experimental import aio

from async_pygrpc_examples.proto import math_service_pb2
from async_pygrpc_examples.proto import math_service_pb2_grpc

class Math(math_service_pb2_grpc.MathServicer):
  async def GetSquare(self, request, context):
    print(f"got message : {request.input}")
    await asyncio.sleep(random.uniform(0.0,5.0))
    return math_service_pb2.GetSquareResponse(output=request.input)

async def _start_async_server():
  server = aio.server()
  server.add_insecure_port('[::]:50051')
  math_service_pb2_grpc.add_MathServicer_to_server(Math(), server)
  await server.start()
  await server.wait_for_termination()

def main():
  loop = asyncio.get_event_loop()
  loop.create_task(_start_async_server())
  loop.run_forever()

if __name__ == '__main__':
  logging.basicConfig()
  main()
