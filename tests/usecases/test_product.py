from typing import List
import pytest  # type: ignore
from uuid import UUID


from store.core.exceptions import NotFoundException
from store.schemas.product import ProductOut, ProductUpdateOut
from store.usecases.product import product_usecase


async def test_usecases_should_return_sucess(product_in):
    result = await product_usecase.create(body=product_in)

    assert isinstance(result, ProductOut)
    assert result.name == "Iphone 14 pro Max"


async def test_usecases_get_should_return_sucess(product_id):
    result = await product_usecase.get(id=product_id)

    assert isinstance(result, ProductOut)
    assert result.name == "Iphone 14 pro Max"


async def test_usecases_get_should_not_found():
    with pytest.raises(NotFoundException) as err:
        await product_usecase.get(id=UUID("1e4f214e-85f7-461a-89d0-a751a32e3bb9"))

    assert (
        err.value.message
        == "Product not found with filter: 1e4f214e-85f7-461a-89d0-a751a32e3bb9"
    )


async def test_usecases_query_should_return_sucess():
    result = await product_usecase.query()

    assert isinstance(result, List)


async def test_usecases_update_should_return_sucess(product_id, product_up):
    product_up.price = 7.500
    result = await product_usecase.update(id=product_id, body=product_up)

    assert isinstance(result, ProductUpdateOut)
