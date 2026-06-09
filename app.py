import os
import uuid
import traceback
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.responses import HTMLResponse
from dotenv import load_dotenv
from fastapi.staticfiles import StaticFiles


from fastapi import (
    FastAPI,
    UploadFile,
    File,
    Form
)

from layers.input_layer import (
    validate_uploaded_files
)
from layers.extraction_layer import (
    ExtractionLayer
)
from layers.validation_layer import (
    ValidationLayer
)
from layers.confidence_layer import (
    ConfidenceLayer
)

from layers.evidence_layer import (
    EvidenceLayer
)
from layers.observability_layer import (
    ObservabilityLayer
)
from layers.rag_layer import (
    RAGLayer
)
from services.vector_builder import (
    VectorBuilder
)
load_dotenv()
BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)
app = FastAPI(
    title="BHIV Multi-Input Intelligence Platform",
    version="1.0.0"
)
app.mount(
    "/static",
    StaticFiles(
        directory=os.path.join(
            BASE_DIR,
            "static"
        )
    ),
    name="static"
)


templates = Jinja2Templates(
    directory=os.path.join(
        BASE_DIR,
        "templates"
    )
)
ObservabilityLayer.setup_logging()

ObservabilityLayer.initialize_metrics()

UPLOAD_FOLDER = "uploads"

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.get("/verify-ui", response_class=HTMLResponse)
async def verify_ui(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="verify.html"
    )


@app.get("/rag-ui", response_class=HTMLResponse)
async def rag_ui(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="rag.html"
    )


@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="dashboard.html"
    )


@app.get("/health-ui", response_class=HTMLResponse)
async def health_ui(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="health.html"
    )

@app.get("/health")
def health():

    return {

        "status":
            "healthy",

        "services": {

            "ocr":
                "UP",

            "llm":
                "UP",

            "validation":
                "UP"
        }
    }


@app.get("/version")
def version():

    return {
        "version":
            "1.0.0"
    }


@app.post("/documents/verify")
async def verify_documents(

    name: str = Form(...),

    email: str = Form(...),

    dob: str = Form(None),

    phone: str = Form(None),

    aadhaar_number: str = Form(None),

    pan_number: str = Form(None),

    aadhaar_file: UploadFile = File(None),

    pan_file: UploadFile = File(None),

    passport_file: UploadFile = File(None)

):

    trace_id = (
    ObservabilityLayer
    .create_trace()
    )

    start_time = (
    ObservabilityLayer
    .start_timer()
    )

    try:

        validate_uploaded_files(
            aadhaar_file,
            pan_file,
            passport_file
        )

        if aadhaar_file:

            file_path = (
                f"uploads/"
                f"{aadhaar_file.filename}"
            )

            with open(
                file_path,
                "wb"
            ) as f:

                f.write(
                    await aadhaar_file.read()
                )

            extraction = (
                ExtractionLayer
                .extract_document(
                    file_path,
                    "aadhaar"
                )
            )

            identity = extraction["identity"]

            form_data = {

                "name":
                    name,

                "dob":
                    dob,

                "phone":
                    phone,

                "aadhaar_number":
                    aadhaar_number,

                "pan_number":
                    pan_number
            }

            validation = (
                ValidationLayer.validate(
                    form_data,
                    identity
                )
            )
            confidence = (
            ConfidenceLayer.calculate(
                validation,
                identity
            )
        )

            evidence = (
            EvidenceLayer.build(
                form_data,
                identity,
                validation
            )
        )
            latency = (
            ObservabilityLayer
            .stop_timer(
                start_time
            )
        )

        ObservabilityLayer.update_metrics(
            latency
        )

        ObservabilityLayer.log_success(
            trace_id,
            "Verification completed"
        )
        return {

            "trace_id":
                trace_id,

            "status":
                "success",

            "extraction":
                extraction,

            "validation":
                validation,

            "confidence":
                confidence,

            "evidence":
                evidence,

            "observability": {

                "trace_id":
                    trace_id,

                "latency_ms":
                    latency
            }
        }

    except Exception as e:

        latency = (
            ObservabilityLayer
            .stop_timer(
                start_time
            )
        )

        ObservabilityLayer.update_metrics(
            latency,
            error=True
        )

        ObservabilityLayer.log_error(
            trace_id,
            str(e)
        )

        return {

            "trace_id":
                trace_id,

            "status":
                "failed",

            "error":
                str(e),

            "observability": {

                "trace_id":
                    trace_id,

                "latency_ms":
                    latency
            }
        }

@app.post("/rag/upload")
async def upload_pdf(
    file: UploadFile = File(...)
):

    os.makedirs(
        "uploads",
        exist_ok=True
    )

    path = (
        f"uploads/{file.filename}"
    )

    with open(
        path,
        "wb"
    ) as f:

        f.write(
            await file.read()
        )

    chunks = (
        VectorBuilder.build(
            path
        )
    )

    return {

        "status":
            "success",

        "chunks_created":
            chunks
    }

@app.post("/rag/ask")
def ask_question(question: str):

    result = RAGLayer.ask(question)

    return result
    
@app.get("/metrics")
def metrics():

    return (
        ObservabilityLayer
        .get_metrics()
    )