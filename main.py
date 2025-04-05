from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os

app = FastAPI()

# Allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class CodeInput(BaseModel):
    code: str
    style: str = "lstlisting"
    title: str = "Java Code Example"  # Optional title

@app.post("/convert")
async def convert_code(data: CodeInput):
    code = data.code
    title = data.title or "Java Code"

    if data.style == "minted":
        latex_code = (
            f"\\begin{{minted}}[frame=lines, linenos, fontsize=\\small, label={{{title}}}]{{java}}\n"
            f"{code}\n"
            f"\\end{{minted}}"
        )
    else:
        latex_code = latex_code = (
        f"\\begin{{lstlisting}}[language=Java, frame=single, numbers=left, caption={{{title}}}, "
        f"basicstyle=\\ttfamily\\small, breaklines=true, showstringspaces=false, xleftmargin=0.5cm, "
        f"xrightmargin=0.5cm, columns=fullflexible]\n"
        f"{code}\n"
        f"\\end{{lstlisting}}"
    )

    return {"latex": latex_code}

# ... rest of your existing code ... 