# © [2024] Malith-Rukshan. All rights reserved.
# Repository: https://github.com/Malith-Rukshan/Suno-API

import os
from typing import List
from suno import suno
from suno.models import RequestParams, CreditsInfo, Clip
import fastapi
from fastapi.responses import RedirectResponse, JSONResponse
from suno import __version__

COOKIE = os.getenv("_cfuvid=OZL4yRvddQoctTjxMAClC02yn_AME178dQPTBdOHQYs-1717435922551-0.0.1.1-604800000; __client=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImNsaWVudF8yaE5ZTDFCYWpzYjd0cjdOZU5ldVY1VTlGTDEiLCJyb3RhdGluZ190b2tlbiI6IjFmMmw4OGFxMHNzcDA2eXY0cDB4NXZ0ZXFoNDl0bzBuOXBwbTdvdWsifQ.BCsFtC_3uSObK00fjQd0XH6kHpYZ6-e-_yqYlAjWeTU6GdSbvgpyC4bvQtzpnnpXH_oAf4x3OHHsXbEjd8Xt8CC1cufu32769CCBDqtBlmMI4LWp-rPV7bk7lN4lI_bXrqKmqXXJhyqo7TRvuhqdiPscXIqHjZRkPP7iuwntXAUMrlHywr0-FT128hvj-VLGx-CRjolczY1OXxT-ppIT2Jt4SjW-T7xuTpSRnx-PzSiCAfE7_N5yIYAal8ucv2nUKhxQQAcm6IVSyyZ7tV1FRp_CwRyCvdsBBqDIh7OOmUmRynoWy_40Yf8vzvsnlr-5kYHdSmuTUSe7VJYB3rScqw; __client_uat=1717435945; __cf_bm=P33ClypQlY8Q9OimZSjqPcENEQvmJAWdHPQ8oqkycbs-1717440609-1.0.1.1-kwTjBErlbjUnxmzL_Dx4byNW9BBTArx_OwJnzQrG00sLvIx.Oq6C8Y4mwZ6_YKngPwLeKGXbz6rqYpofC0DVAg; mp_26ced217328f4737497bd6ba6641ca1c_mixpanel=%7B%22distinct_id%22%3A%20%22902ef607-3d63-40d2-9038-5bac1f71b263%22%2C%22%24device_id%22%3A%20%2218fdf2875dc6fe-06a59a654f295d-26001c51-e1000-18fdf2875dc6fe%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22__mps%22%3A%20%7B%7D%2C%22__mpso%22%3A%20%7B%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D%2C%22__mpus%22%3A%20%7B%7D%2C%22__mpa%22%3A%20%7B%7D%2C%22__mpu%22%3A%20%7B%7D%2C%22__mpr%22%3A%20%5B%5D%2C%22__mpap%22%3A%20%5B%5D%2C%22%24user_id%22%3A%20%22902ef607-3d63-40d2-9038-5bac1f71b263%22%7D")

# Initilize Suno API Client
client = suno.Suno(cookie=COOKIE)

description = """
### Suno AI Unofficial API

<a href='https://pypi.org/project/SunoAI/'>
<img src='https://img.shields.io/badge/PyPi-Library-1cd760?logo=pypi&style=flat'>
</a>
<a href='https://github.com/Malith-Rukshan/Suno-API'>
<img src='https://img.shields.io/badge/Github-Suno--API-blue?logo=github&style=flat'> 
</a>
<a href='https://t.me/SingleDevelopers'>
<img src='https://img.shields.io/badge/Telegram-@SingleDevelopers-blue?logo=telegram&style=flat'> 
</a>

This is an **unofficial API for [Suno AI](https://www.suno.ai/)**, a platform that utilizes artificial intelligence to generate music.

### 🚀 Main Features
- **Generate Music:** Leverage Suno AI's capabilities to create music based on different styles and inputs.
- **Retrieve Music Data:** Access details about generated music tracks, including audio files, metadata, and more.
- **Get Credit Balance Info**
- **Documentation:** [📚 Redoc](/redoc) | [🏷 Usage](https://github.com/Malith-Rukshan/Suno-API?tab=readme-ov-file#-rest-api-usage)

### Repository
You can find the source code for this API at [GitHub](https://github.com/Malith-Rukshan/Suno-API).

### Disclaimer
This API is not officially associated with Suno AI. It was developed to facilitate easier access and manipulation of the music generation capabilities provided by Suno AI's official website.

### Usage
Please note that this API is intended for educational and development purposes. Ensure you respect Suno AI's terms of service when using their services.
"""

# FastAPI app
app = fastapi.FastAPI(
    title="Suno API",
    summary="An Unofficial Python Library for Suno AI API",
    description=description,
    version=__version__,
    contact={
        "name": "Malith Rukshan",
        "url": "https://MalithRukshan.t.me",
        "email": "singledeveloper.lk@gmail.com",
    }
)

# Redirect to Docs :)


@app.get("/", include_in_schema=False)
async def redirect_to_docs():
    return RedirectResponse(url='/docs')


@app.post(f"/generate", response_model=List[Clip])
def generate(params: RequestParams) -> JSONResponse:
    clips = client.generate(**params.model_dump())
    return JSONResponse(content=[clip.model_dump() for clip in clips])


@app.post(f"/songs", response_model=List[Clip])
def generate(song_ids: str | None = None) -> JSONResponse:
    clips = client.get_songs(song_ids)
    return JSONResponse(content=[clip.model_dump() for clip in clips])


@app.post(f"/get_song", response_model=Clip)
def generate(song_id: str) -> JSONResponse:
    clip = client.get_song(song_id)
    return JSONResponse(content=clip.model_dump())


@app.get(f"/credits", response_model=CreditsInfo)
def credits() -> JSONResponse:
    credits = client.get_credits()
    return JSONResponse(content=credits.model_dump())
