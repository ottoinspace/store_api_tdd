from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase  # type: ignore

from store.db.mongo import db_client
from store.schemas.product import ProductIn, ProductOut


class ProductUseCase:
    def __init__(self) -> None:
        self.client: AsyncIOMotorClient = db_client.get()
        self.database: AsyncIOMotorDatabase = self.client.get_database()
        self.collection = self.database.get_collection("products")

    async def create(self, body: ProductIn) -> ProductOut:
        await self.collection.insert_one(body.model_dump())


product_usecase = ProductUseCase()
