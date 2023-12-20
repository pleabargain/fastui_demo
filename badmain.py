from typing import List
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse

from fastapi.responses import JSONResponse
from pydantic import BaseModel
from fastui import FastUI, AnyComponent, prebuilt_html, components as c
from fastui.components.display import DisplayMode, DisplayLookup

app = FastAPI()

class VerbInfo(BaseModel):
    topic: str
    category: str
    verb: str
    answer: List[str]
    synonyms: List[str]
    antonyms: List[str]
    questions: List[str]

# Example data, replace with actual data source
verb_data = [{
"topic": "persuasive verbs",
"category": "regular",
"verb": "convince",
"answer": [
"I/They/We/You convince | He/She/It convinces",
"I am | He/She/It is | They/We/You are convincing",
"I/You/They/We have | He/She/It has convinced",
"I/You/They/We have been convincing | He/She/It has been convincing",
"I/He/She/It/We/You/They convinced",
"I/He/She/It was convincing | They/We/You were convincing",
"I/He/She/It/We/You/They had convinced",
"I/He/She/It/We/You/They had been convincing",
"I/He/She/It/We/You/They will convince",
"I/He/She/It/We/You/They will be convincing",
"I/He/She/It/We/You/They will have convinced",
"I/He/She/It/We/You/They will have been convincing"
],
"synonyms": [
"persuade",
"induce",
"influence",
"coax",
"talk round",
"get",
"urge",
"win over",
"bring around",
"sway",
"coerce",
"prompt"
],
"antonyms": [
"dissuade",
"discourage",
"deterr"
],
"questions": [
"How can you convince your team to adopt this approach? (context: team management)",
"Who convinced you to take this job? (context: career)",
"Have you convinced your parents about your plan? (context: personal decision)",
"What argument convinced you to change your mind? (context: debate)",
"How do you plan to convince the board? (context: business proposal)"
],
},

{
    "topic": "daily activities",
    "category": "regular",
    "verb": "get dressed",
    "answer": [
        "I/They/We/You get dressed | He/She/It gets dressed",
        "I am | He/She/It is | They/We/You are getting dressed",
        "I/You/They/We have | He/She/It has got dressed",
        "I/You/They/We have been getting dressed | He/She/It has been getting dressed",
        "I/He/She/It/We/You/They got dressed",
        "I/He/She/It was getting dressed | They/We/You were getting dressed",
        "I/He/She/It/We/You/They had got dressed",
        "I/He/She/It/We/You/They had been getting dressed",
        "I/He/She/It/We/You/They will get dressed",
        "I/He/She/It/We/You/They will be getting dressed",
        "I/He/She/It/We/You/They will have got dressed",
        "I/He/She/It/We/You/They will have been getting dressed"
    ],
"synonyms":[ "dress up", "don clothes", "put on clothes", "attire oneself", "clothe oneself"],

"antonyms":[ "undress", "disrobe", "strip", "take off clothes"],

    "questions": [
        "Have you got dressed for the party?(context: social)",
        "Why is he getting dressed so early?(context: daily routine)",
        "Will they get dressed before breakfast?(context: daily routine)",
        "Who got dressed first?(context: competition)",
        "How quickly can you get dressed?(context: time management)"
    ]
},
]

def convert_to_json(verb_data):
    """
    Convert data to JSON format.
    """
    return json.dumps(verb_data)


@app.get("/api/verbs/", response_model=FastUI, response_model_exclude_none=True)
def list_verbs() -> list[AnyComponent]:
    """
    Show a table of verbs, `/api/verbs` is the endpoint the frontend will connect to
    when a user visits `/` to fetch components to render.
    """
    verb_objects = [VerbInfo(**verb) for verb in verb_data]
    return [
        c.Page(
            components=[
                c.Heading(text='Verb Conjugations', level=2),
                c.Table[VerbInfo](
                    data=verb_objects,
                    columns=[
                        c.DisplayLookup(field='topic', mode=c.DisplayMode.text),
                        c.DisplayLookup(field='verb', mode=c.DisplayMode.text),
                        # Add other fields as needed
                    ],
                ),
            ]
        ),
    ]

@app.get("/api/verb/{verb_topic}/", response_model=FastUI, response_model_exclude_none=True)
def verb_details(verb_topic: str) -> list[AnyComponent]:
    """
    Verb details page, the frontend will fetch this when the user visits `/verb/{topic}/`.
    """
    try:
        verb_info = next(verb for verb in verb_data if verb['topic'] == verb_topic)
    except StopIteration:
        raise HTTPException(status_code=404, detail="Verb topic not found")
    verb_object = VerbInfo(**verb_info)
    return [
        c.Page(
            components=[
                c.Heading(text=verb_object.topic, level=2),
                c.Link(components=[c.Text(text='Back')], on_click=c.BackEvent()),
                c.Details(data=verb_object),
            ]
        ),
    ]

@app.get('/{path:path}')
async def html_landing() -> HTMLResponse:
    """Simple HTML page which serves the React app, comes last as it matches all paths."""
    return HTMLResponse(prebuilt_html(title='Verb Conjugation App'))
