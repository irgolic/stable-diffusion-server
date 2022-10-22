import pydantic

from stable_diffusion_server.models.blob import BlobUrl
from stable_diffusion_server.models.params import ParamsUnion


class GeneratedImage(pydantic.BaseModel):
    blob_url: BlobUrl
    parameters_used: ParamsUnion
