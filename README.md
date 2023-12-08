# Quickstart

## Check ETA of Bus

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
	
```