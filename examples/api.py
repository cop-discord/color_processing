from fastapi import FastAPI, Request
from fastapi.responses import Response, JSONResponse
from color_processing import ColorHolder, ColorInfoResponse
from pydantic import BaseModel
from typing import List, Tuple, Optional

app = FastAPI()
app.state.colors = ColorHolder.get_colors()
app.state.domain = "https://api.colors"

@app.get("/assets/{identifier}")
async def assets(request: Request, identifier: str):
    if not hasattr(app.state, "assets"):
        return JSONResponse(content = {"message": "No assets have been initialized"}, status_code = 404)
    if not (asset := app.state.assets.get(identifier.split('.')[0])):
        return JSONResponse(content = {"message": "Asset not found"}, status_code = 404)
    return Response(content = asset, media_type = 'image/png')

class WebSafe(BaseModel):
    hex: str
    rgb: Tuple[int]

class ColorInformationResponse(BaseModel):
    name: Optional[str] = None
    hex: str
    websafe: WebSafe
    rgb: Tuple[int]
    brightness: int
    shades: List[str]
    palette: str
    image: str

    @classmethod
    async def from_color(cls, information: ColorInfoResponse):
        palette_bytes = information.palette.read()
        image_bytes = information.image.read()
        palette_key = f'{information.hex.replace("#", "")}-Palette'
        image_key = f'{information.hex.replace("#", "")}-Image'
        if not hasattr(app.state, "assets"):
            app.state.assets = {}
        
        app.state.assets[palette_key] = palette_bytes
        app.state.assets[image_key] = image_bytes
        info = information.dict()
        info['palette'] = f"{app.state.domain}/assets/{palette_key}"
        info['image'] = f"{app.state.domain}/assets/{image_key}"
        return cls(**info)


@app.get("/color", response_model = ColorInformationResponse)
async def color_info(request: Request, query: str):
    info = await app.state.colors.color_info(query)
    return await ColorInformationResponse.from_color(info)
