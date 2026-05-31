from typing import Annotated

from fastapi import FastAPI, Form
from pydantic import BaseModel

#TODO: put these classes somewhere else
class WizardFormData(BaseModel):
    username: str
    password: str

class JobInfo(BaseModel):
    name: str
    url: str


app = FastAPI()

@app.post("/save-wizard")
def save_wizard(userData: Annotated[WizardFormData, Form()]):
    return {"message": "todo: save wizard"}

@app.get("/daily-mode-init")
def runJobSearch():
  return ("fake success, client hook should navigate upon success")

@app.get("/show-3-jobs")
def get_3_jobs():
    job = JobInfo(name="Example Job", url="https://example.com")
    return [job]

# is it better to send data in smalll chunks or send all the data at once? is this necessary?
@app.get("/daily-mode")
def applyToJob():
  return("user info to be parced and placed into chrome form")

@app.get("/start-application")
def startApplication(applicationFields):
  filled_applicationFields = applicationFields
  #also post job app started and time
  return filled_applicationFields

@app.post("/application-done")
def finishApplication():
  #post job app completed
  return ("yay")

@app.get("/linkedin-network")
def runNetworkSearch():
  #find people to reach out to
  #find emails on hunter.io
  #get sample message for each
  return ("yay")

