from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.note import NoteCreate, NoteUpdate, NoteResponse
from app.crud import note as note_crud

router = APIRouter(prefix="/notes", tags=["Notes"])

@router.post("/", response_model=NoteResponse, status_code=status.HTTP_201_CREATED)
def create(note: NoteCreate, db: Session = Depends(get_db)):
    return note_crud.create_note(db, note)

@router.get("/", response_model=List[NoteResponse])
def list_notes(db: Session = Depends(get_db)):
    return note_crud.get_notes(db)

@router.get("/{note_id}", response_model=NoteResponse)
def retrieve(note_id: int, db: Session = Depends(get_db)):
    db_note = note_crud.get_note(db, note_id)
    if not db_note:
        raise HTTPException(status_code=404, detail="Note not found")
    return db_note

@router.put("/{note_id}", response_model=NoteResponse)
def update(note_id: int, note: NoteUpdate, db: Session = Depends(get_db)):
    db_note = note_crud.update_note(db, note_id, note)
    if not db_note:
        raise HTTPException(status_code=404, detail="Note not found")
    return db_note

@router.delete("/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(note_id: int, db: Session = Depends(get_db)):
    db_note = note_crud.delete_note(db, note_id)
    if not db_note:
        raise HTTPException(status_code=404, detail="Note not found")
