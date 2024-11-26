from typing import Type, List, Tuple
from crewai_tools import BaseTool
from pydantic import BaseModel, Field


class ProductReviewsToolInput(BaseModel):
    """ Input schema for the ProductReviewsTool"""
    product_id: str = Field(..., description="The ID of the product for which reviews need to be retrieved")


class ProductReviewsTool(BaseTool):
    name: str = "ProductReviewsTool"
    description: str = ("""Use this tool to retrieve reviews from buyers of a specific product.
                        You will be returned a list of tuples where the first element is the review score
                        out of 5 and the second element is the review text. If there are no reviews available,
                        you will be returned an empty list.""")

    args_schema: Type[BaseModel] = ProductReviewsToolInput
    
    def _run(self, product_id: str) -> List[Tuple[int, str]]:

        print(product_id)

        sample_reviews = [
            (5, "Great! No problems at all!"),
            (4, "Cool product! Expensive!"),
        ]

        return sample_reviews