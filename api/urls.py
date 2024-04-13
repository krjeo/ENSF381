from django.urls import path
from .views import *

urlpatterns = [
    path('user', UserView.as_view()),
    path('admin', AdminView.as_view()),
    path('book', BookView.as_view()),
    path('bookAuthor', BookAuthorView.as_view()),
    path('BookRent', BookRentView.as_view()),
    path('Event', EventView.as_view()),
    path('EventHall', EventHallView.as_view()),
    path('EventApply', EventApplyView.as_view()),
    path('EventHeld', EventHeldView.as_view()),
    path('Facilities', FacilitiesView.as_view()),
    path('Floor', FloorView.as_view()),
    path('Lend', LendView.as_view()),
    path('Phone', PhoneView.as_view()),
    path('Seat', SeatView.as_view()),
    path('BookSeat', SeatBookView.as_view()),
    path('Shelf', ShelfView.as_view()),
    path('StudyRoom', StudyRoomView.as_view()),
    path('BookStudyRoom', StudyRoomBookView.as_view()),
    path('login/', LoginView.as_view(), name='login'),
    path('adminlogin/', AdminLoginView.as_view(), name='adminlogin'),
    path('signup', SignupView.as_view(), name='signup'),
    path('seat-data/', SeatDataView.as_view(), name='seat_data'),
    path('room-data/', RoomDataView.as_view(), name='room-data'),
    path('book-seat/', BookSeatView.as_view(), name='book_seat'),
    path('book-room/', BookRoomView.as_view(), name='book-room'),
    path('create-room/', CreateRoomView.as_view(), name='create-room'),
    path('create-seat/', CreateSeatView.as_view(), name='create-seat'),
    path('create-admin/', CreateAdmin.as_view(), name='create-admin'),
    path('edit-user/', EditUser.as_view(), name='edit-user'),
    path('account/', AccountView.as_view(), name='account'),
    path('browse-books/', BrowseBooksView.as_view()),
    path('claim-book/', ClaimBookView.as_view()),
    path('book-data/', BookDataView.as_view(), name="book-data"),
]
