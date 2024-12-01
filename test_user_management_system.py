import pytest
from user_management import UserManagementSystem

@pytest.fixture
def setup_database():
    ums = UserManagementSystem()
    ums.delete_all_users()
    yield ums
    ums.close_connection()

def test_add_user(setup_database):
    ums = setup_database
    ums.add_user(1, "John", "Doe", "john.doe@example.com", 30)
    user = ums.display_user_by_id(1)
    assert user.first_name == "John"
    assert user.last_name == "Doe"

def test_remove_user(setup_database):
    ums = setup_database
    ums.add_user(2, "Jane", "Doe", "jane.doe@example.com", 25)
    ums.remove_user(2)
    user = ums.display_user_by_id(2)
    assert user is None

def test_update_first_name(setup_database):
    ums = setup_database
    ums.add_user(3, "Alice", "Smith", "alice.smith@example.com", 40)
    ums.update_first_name(3, "Alicia")
    user = ums.display_user_by_id(3)
    assert user.first_name == "Alicia"
