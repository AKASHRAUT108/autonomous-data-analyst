from pathlib import Path

from fastapi import APIRouter, File, HTTPException, UploadFile


router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)


PROJECT_ROOT = Path(__file__).resolve().parents[3]

UPLOAD_DIRECTORY = (
    PROJECT_ROOT
    / "data"
    / "raw"
)

ALLOWED_EXTENSIONS = {
    ".csv",
    ".xlsx",
    ".xls"
}


@router.post("/dataset")
async def upload_dataset(
    file: UploadFile = File(...)
):

    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="No file was provided."
        )

    extension = Path(file.filename).suffix.lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Only CSV and Excel files are supported."
        )

    UPLOAD_DIRECTORY.mkdir(
        parents=True,
        exist_ok=True
    )

    destination = UPLOAD_DIRECTORY / Path(file.filename).name

    contents = await file.read()

    with open(destination, "wb") as output_file:
        output_file.write(contents)

    return {
        "status": "success",
        "message": "Dataset uploaded successfully.",
        "filename": file.filename,
        "size_bytes": len(contents),
        "path": str(destination.relative_to(PROJECT_ROOT))
    }