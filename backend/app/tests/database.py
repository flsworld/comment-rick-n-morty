from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///./test.db", connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# def test_create_user():
#     response = client.post(
#         "/users/",
#         json={"email": "deadpool@example.com", "password": "chimichangas4life"},
#     )
#     assert response.status_code == 200, response.text
#     data = response.json()
#     assert data["email"] == "deadpool@example.com"
#     assert "id" in data
#     user_id = data["id"]
#
#     response = client.get(f"/users/{user_id}")
#     assert response.status_code == 200, response.text
#     data = response.json()
#     assert data["email"] == "deadpool@example.com"
#     assert data["id"] == user_id
