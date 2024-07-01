from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from apis.turnover.route import router as TurnoverRouter

app = FastAPI(
    title='Bookkeeper API',
    description='API for Bookkeeper',
    version='1.0',
)

app.include_router(TurnoverRouter, tags=['Turnover'], prefix='/turnover')

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
