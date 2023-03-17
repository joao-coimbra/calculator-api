from sanic import Blueprint, response
from sanic.exceptions import SanicException
from functools import reduce
import math

api = Blueprint('api', url_prefix='/api')

@api.route("/add", methods=["POST"])
async def add(request):
    nums = request.json.get("nums")
    if nums is None or not isinstance(nums, list):
        raise SanicException("Missing required parameters")
    return response.json({"result": sum(nums)})


@api.route("/subtract", methods=["POST"])
async def subtract(request):
    nums = request.json.get("nums")
    if nums is None or not isinstance(nums, list):
        raise SanicException("Missing required parameters")
    return response.json({"result": reduce(lambda x, y: x - y, nums)})


@api.route("/multiply", methods=["POST"])
async def multiply(request):
    nums = request.json.get("nums")
    if nums is None or not isinstance(nums, list):
        raise SanicException("Missing required parameters")
    return response.json({"result": reduce(lambda x, y: x * y, nums)})


@api.route("/divide", methods=["POST"])
async def divide(request):
    num = request.json.get("num")
    divisor = request.json.get("divisor")
    if num is None or divisor is None:
        raise SanicException("Missing required parameters")
    if divisor == 0:
        raise SanicException("Impossible divide by zero")
    return response.json({"result": num / divisor})


@api.route("/sqrt", methods=["POST"])
async def sqrt(request):
    num = request.json.get("num")
    if num is None:
        raise SanicException("Missing required parameters")
    if num < 0:
        raise SanicException("Cannot take square root of negative number")
    return response.json({"result": math.sqrt(num)})


@api.route("/power", methods=["POST"])
async def power(request):
    base = request.json.get("base")
    exponent = request.json.get("exponent")
    if base is None or exponent is None:
        raise SanicException("Missing required parameters")
    return response.json({"result": base ** exponent})


@api.route("/mean", methods=["POST"])
async def mean(request):
    nums = request.json.get("nums")
    if nums is None or not isinstance(nums, list):
        raise SanicException("Missing or invalid input parameter")
    return response.json({"result": sum(nums) / len(nums)})


@api.route("/hmean", methods=["POST"])
async def hmean(request):
    nums = request.json.get("nums")
    if nums is None or not isinstance(nums, list):
        raise SanicException("Missing or invalid input parameter")

    return response.json({"result": len(nums) / sum(map(lambda x: x**-1, nums))})


@api.route("/moda", methods=["POST"])
async def moda(request):
    nums = request.json.get("nums")
    if nums is None or not isinstance(nums, list):
        raise SanicException("Missing or invalid input parameter")

    freq: dict = reduce(
        lambda x, y: {**x, y: x[y] + 1 if y in x else 1}, nums, {})

    return response.json(
        {"result": [x for x, y in freq.items() if y == max(freq.values())]}
    )

