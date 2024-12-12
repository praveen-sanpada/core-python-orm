from sqlalchemy import Column, Integer, String
from db_connection import Base, engine, SessionLocal

# Define the User model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)

    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}', email='{self.email}')"

# Create the tables in the database
Base.metadata.create_all(bind=engine)

# CRUD Operations
def create_user(name: str, email: str):
    session = SessionLocal()
    try:
        new_user = User(name=name, email=email)
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
        print(f"User created: {new_user}")
    except Exception as e:
        session.rollback()
        print(f"Error: {e}")
    finally:
        session.close()

def get_users():
    session = SessionLocal()
    try:
        users = session.query(User).all()
        for user in users:
            print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")
    finally:
        session.close()

def update_user(user_id: int, new_name: str):
    session = SessionLocal()
    try:
        user = session.query(User).filter(User.id == user_id).first()
        if user:
            user.name = new_name
            session.commit()
            print(f"User updated: {user}")
        else:
            print("User not found.")
    finally:
        session.close()

def delete_user(user_id: int):
    session = SessionLocal()
    try:
        user = session.query(User).filter(User.id == user_id).first()
        if user:
            session.delete(user)
            session.commit()
            print(f"User deleted: {user}")
        else:
            print("User not found.")
    finally:
        session.close()

# Example Usage
if __name__ == "__main__":
    # Add your test cases here
    create_user("John Doe", "john1@example.com")
    # get_users()
    # update_user(1, "Jane Doe")
    # delete_user(1)
