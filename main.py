from datetime import date

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastui import FastUI, AnyComponent, prebuilt_html, components as c
from fastui.components.display import DisplayMode, DisplayLookup
from fastui.events import GoToEvent, BackEvent
from pydantic import BaseModel, Field

app = FastAPI()

app = FastAPI()

class Property(BaseModel):
    id: int
    name: str
    country: str

# Define some properties
properties = [
    Property(id=1, name='Sunset Villa', country='USA'),
    Property(id=2, name='Mountain Retreat', country='Canada'),
    Property(id=3, name='Beachfront Bungalow', country='Australia'),
    Property(id=4, name='Urban Apartment', country='Japan'),
    Property(id=5, name='Countryside Cottage', country='France'),
    Property(id=6, name='Lakeside Cabin', country='Finland'),
    Property(id=7, name='City Loft', country='Germany'),
    Property(id=8, name='Island Getaway', country='Maldives'),
    Property(id=9, name='Desert Oasis', country='Morocco'),
    Property(id=10, name='Rainforest Hideaway', country='Brazil')
]

@app.get("/api/", response_model=FastUI, response_model_exclude_none=True)
def properties_table() -> list[AnyComponent]:
    """
    Show a table of properties, `/api` is the endpoint the frontend will connect to
    when a user visits `/` to fetch components to render.
    """
    return [
        c.Page(
            components=[
                c.Heading(text='Properties', level=2),
                c.Table[Property](
                    data=properties,
                    columns=[
                        DisplayLookup(field='name', on_click=GoToEvent(url='/property/{id}/')),
                        DisplayLookup(field='country'),
                    ],
                ),
            ]
        ),
    ]

@app.get("/api/property/{property_id}/", response_model=FastUI, response_model_exclude_none=True)
def property_profile(property_id: int) -> list[AnyComponent]:
    """
    Property profile page, the frontend will fetch this when the user visits `/property/{id}/`.
    """
    try:
        property = next(p for p in properties if p.id == property_id)
    except StopIteration:
        raise HTTPException(status_code=404, detail="Property not found")
    return [
        c.Page(
            components=[
                c.Heading(text=property.name, level=2),
                c.Link(components=[c.Text(text='Back')], on_click=BackEvent()),
                c.Details(data=property),
            ]
        ),
    ]

@app.get('/{path:path}')
async def html_landing() -> HTMLResponse:
    """Simple HTML page which serves the React app, comes last as it matches all paths."""
    return HTMLResponse(prebuilt_html(title='FastUI Demo'))

# Note: Remember to also import the necessary dependencies for the new components
