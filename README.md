# Quickstart

>　What does `bushk` do?
> - [Get ETA of bus in Hong Kong](#check-eta-of-bus)
> - [Get stops of bus data in Hong Kong](#)
> - [Get route of bus data in Hong Kong](#)

## Check ETA of Bus

> How can I can ETA of bus?
> 1. [Install `bushk`](#install-bushk)
> 2. [Copy or reference code](#example-code)
> 3. [Run your Python file](#check-eta-of-bus)

### Install `bushk`
```shell
pip install bushk
```

### Example Code
```py
import bushk


@bushk.runner
async def run():
	route=await bushk.Routes.get("NUMBER OF ROUTE WHICH YOU WANT TO CHECK THE ETA OF THE BUS")
	for eta in await bushk.ETA.get_route(route):
		print(f"{bushk.Stops.get(route.stops_id[eta.seq]).name['en']}: {eta.arrive_at}({eta.rmk})")
```