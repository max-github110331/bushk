# Quickstart

> What does `bushk` do?
> - [Get data of the bus stop in Hong Kong](#get-data-of-the-bus-stop)
> - [Get data of route in Hong Kong](#get-data-of-the-route)
> - [Get ETA of bus in Hong Kong](#check-eta-of-bus)

**Install `bushk`**
```shell
pip install bushk
```

## Get data of the bus stop

> How can I get data of the bus stop?
> 1. [Copy or reference code](#example-code)
> 2. [Run your Python file](#get-data-of-the-bus-stop)

### Example Code
```py
import bushk


@bushk.runner
async def _stop():
	stop=await bushk.Stops.get("ID OF STOP")
	print(f"{stop.id}: {stop.name['en']}")
```

## Get data of the route

> How can I get data of the bus stop?
> 1. [Copy or reference code](#example-code-1)
> 2. [Run your Python file](#get-stop-of-bus)

### Example Code
```py
import bushk


@bushk.runner
async def _route():
	route=await bushk.Routes.get("NUMBER OF THE ROUTE", "direction OF THE ROUTE(O, I, OUTBOUND, INBOUND, OB OR IB)(OPTIONAL)", "SERVICE TYPE OF THE ROUTE(1 OR 2)(OPTIONAL)")
	print(f"Route: {route.route}\nNormal: {route.normal}\nBound: {route.bound}")
```

## Check ETA of Bus

> How can I get ETA of bus?
> 1. [Copy or reference code](#example-code-2)
> 2. [Run your Python file](#check-eta-of-bus)

### Example Code
```py
import bushk


@bushk.runner
async def _eta():
	route=await bushk.Routes.get("NUMBER OF ROUTE WHICH YOU WANT TO CHECK THE ETA OF THE BUS")
	for eta in await bushk.ETA.get_route(route):
		print(f"{bushk.Stops.get(route.stops_id[eta.seq]).name['en']}: {eta.arrive_at}({eta.rmk})")
```