# Quickstart

> What does `bushk` do?
> - [Get stops of bus data in Hong Kong](#get-stop-of-bus)
> - [Get route of bus data in Hong Kong](#)
> - [Get ETA of bus in Hong Kong](#check-eta-of-bus)

**Install `bushk`**
```shell
pip install bushk
```

## Get stop of bus

> How can I get stop of bus?
> 1. [Copy or reference code](#example-code)
> 2. [Run your Python file](#check-eta-of-bus)

### Example Code
```py
import bushk


@bushk.runner
async def run():
	stop=bushk.Stops.get("ID OF STOP")
```

## Check ETA of Bus

> How can I get ETA of bus?
> 1. [Copy or reference code](#example-code)
> 2. [Run your Python file](#check-eta-of-bus)

### Example Code
```py
import bushk


@bushk.runner
async def run():
	route=await bushk.Routes.get("NUMBER OF ROUTE WHICH YOU WANT TO CHECK THE ETA OF THE BUS")
	for eta in await bushk.ETA.get_route(route):
		print(f"{bushk.Stops.get(route.stops_id[eta.seq]).name['en']}: {eta.arrive_at}({eta.rmk})")
```