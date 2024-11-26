from typing import Type, List, Tuple
from crewai_tools import BaseTool
from pydantic import BaseModel, Field


class OrderLookupToolInput(BaseModel):
    """ Input schema for the OrderLookupTool"""
    order_id: str = Field(..., description="The ID of the Order that we want to retrieve.")
    customer_id: str = Field(..., description="The ID of the customer whose past orders we want to retrieve.")


class OrderLookupTool(BaseTool):
    name: str = "OrderLookupTool"
    description: str = ("""
                        Use this tool to look up past orders and their status. You need to either use the order_id or the customer_id. 
                        Both fields cannot be blank or empty strings. You will be returned a list of tuples representing a list of orders
                        where the first element is the Order ID and the second element is the Order Status. If there are no orders found
                        for the given order_id or customer_id, you will be returned an empty list.""")

    args_schema: Type[BaseModel] = OrderLookupToolInput
    
    def _run(self, order_id: str = "", customer_id: str = "") -> List[Tuple[str, str]]:

        print(order_id)
        print(customer_id)

        orders_and_status = [
            ("53cdb2fc8bc7dce0b6741e2150273451", "delivered"),
            ("15bed8e2fec7fdbadb186b57c46c92f2", "processing"),
        ]

        return orders_and_status