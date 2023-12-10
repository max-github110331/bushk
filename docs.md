# BusHK Docs

> What does BusHK do?
> - [Get data of the bus stop in Hong Kong](https://github.com/max-github110331/bushk/tree/main#get-data-of-the-bus-stop)
> - [Get data of route in Hong Kong](https://github.com/max-github110331/bushk/tree/main#get-data-of-the-route)
> - [Get ETA of bus in Hong Kong](https://github.com/max-github110331/bushk/tree/main#check-eta-of-bus)

> Remember to install BusHK
> ```shell
> pip install bushk
> ```

------------------------------
### [`@bushk.runner`](#bushkrunner)
This decorator can run the function which is asynchronous.
For example:
```py
import bushk


@bushk.runner
async def run():
    for stop in await bushk.Stops.all():
        print(f"{stop.name['tc']}({stop.id})")
```

------------------------------