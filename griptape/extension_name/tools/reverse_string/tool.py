from __future__ import annotations
from griptape.artifacts import TextArtifact, ErrorArtifact
from griptape.tools import BaseTool
from griptape.utils.decorators import activity
from schema import Schema, Literal
from attrs import define


@define
class ReverseStringTool(BaseTool):
    @activity(
        config={
            "description": "Can be used to reverse a string",
            "schema": Schema(
                {Literal("input", description="The string to be reversed"): str}
            ),
        }
    )
    def reverse_string(self, params: dict) -> TextArtifact | ErrorArtifact:
        input_value = params["values"].get("input")

        return TextArtifact(input_value[::-1])

    @activity(
        config={
            "description": "Can be used to reverse words in a sentence",
            "schema": Schema(
                {Literal("input", description="The sentence to be reversed"): str}
            ),
        }
    )
    def reverse_sentence(self, params: dict) -> TextArtifact | ErrorArtifact:
        input_value = params["values"].get("input")
        return TextArtifact(" ".join(input_value.split()[::-1]))

    @activity(
        config={
            "description": "Can be used to reverse each word in a sentence without reversing the whole sentence.",
            "schema": Schema(
                {Literal("input", description="The sentence to be reversed"): str}
            ),
        }
    )
    def reverse_each_word(self, params: dict) -> TextArtifact | ErrorArtifact:
        input_value = params["values"].get("input")
        return TextArtifact(" ".join([word[::-1] for word in input_value.split()]))
