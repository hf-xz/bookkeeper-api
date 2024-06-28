from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from apis.student.route import router as StudentRouter

app = FastAPI()

app.include_router(StudentRouter, tags=['Student'], prefix='/student')

@app.get('/', tags=['Root'], response_class=HTMLResponse)
def read_root():
    return '''
<html>
    <head>
        <title>Bookkeeper API</title>
    </head>
    <body>
        <h1>
        This is API for
            <a href="https://bookkeeper.hfxz.link/">Bookkeeper</a>
        </h1>
    </body>
</html>
'''


# 本地运行
if __name__ == '__main__':
    import uvicorn
    uvicorn.run('app:app', host='0.0.0.0', port=8000, reload=True)
