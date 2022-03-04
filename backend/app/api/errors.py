from fastapi import HTTPException
from fastapi import status


def fire_error_msg(field: str, values_set: set):
    raise HTTPException(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        detail=[
            {
                "loc": ["query", field],
                "msg": f"value must be in {values_set}",
                "type": "value_error",
            }
        ],
    )
