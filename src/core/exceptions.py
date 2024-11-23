from fastapi import HTTPException, status


user_not_found_exception = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="User not found.",
)

user_alredy_exists_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="User with this email & full_name alredy exsists",
)

category_not_found_exception = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="Category not found.",
)

category_alredy_exists_exception = HTTPException(
    status_code=status.HTTP_400_BAD_REQUEST,
    detail="Category with this name alredy exsists",
)
