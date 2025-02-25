from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel

# FastAPI instance
app = FastAPI(title="SCSU Student API", description="API for managing student records", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (use specific origins in production)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

# Database setup
DATABASE_URL = "sqlite:///./students.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Student Model for Database
class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    major = Column(String)
    gpa = Column(Float)

# Create tables
Base.metadata.create_all(bind=engine)

# Pydantic Schema for Request Body
class StudentCreate(BaseModel):
    name: str
    major: str
    gpa: float

class StudentResponse(StudentCreate):
    id: int
    class Config:
        orm_mode = True

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# API Endpoints
@app.post("/students", response_model=StudentResponse, tags=["Students"])
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    new_student = Student(**student.dict())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

@app.get("/students/{student_id}", response_model=StudentResponse, tags=["Students"])
def read_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@app.put("/students/{student_id}", response_model=StudentResponse, tags=["Students"])
def update_student(student_id: int, student_update: StudentCreate, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    
    student.name = student_update.name
    student.major = student_update.major
    student.gpa = student_update.gpa
    
    db.commit()
    db.refresh(student)
    return student

@app.delete("/students/{student_id}", tags=["Students"])
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    
    db.delete(student)
    db.commit()
    return {"message": "Student record deleted successfully"}

@app.get("/students", response_model=list[StudentResponse], tags=["Students"])
def get_students(db: Session = Depends(get_db)):
    students = db.query(Student).all()
    return students


# Run the API with uvicorn
# To run: uvicorn filename:app --reload
