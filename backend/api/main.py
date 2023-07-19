from fastapi import FastAPI, HTTPException

from .schemas import User, Report, Event


app = FastAPI()

test_user = User(id=1, name='test', email='test@gmail.com', icon_image='image/photo.img', introduction='Hi', oshimen='XXX')
test_event = Event(id=1, date='2023-7-12', venue='横浜スタジアム', target='乃木坂', type='ライブ')


reports = [
    Report(id=1, author=test_user, event=test_event, feedback='退屈だった', description='乃木坂の握手会', created_at='2023-7-17')
]

@app.get("/reports")
async def get_reports():
    return {'reports': reports}

@app.get("/reports/{id}")
async def get_report(id: str):
    for report in reports:
        if report.id == id:
            return report
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/reports")
async def create_report():
    pass 


@app.put("/reports")
async def update_report():
    pass 


@app.delete("/reports/{id}")
async def delete_report(id: str):
    pass