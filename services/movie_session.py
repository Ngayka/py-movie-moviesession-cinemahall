from datetime import datetime

from django.db.models import QuerySet

from db.models import MovieSession, CinemaHall, Movie


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int) -> MovieSession:
    movie = Movie.objects.get(id=movie_id)
    cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
    movie_session = MovieSession.objects.create(
        movie=movie,
        cinema_hall=cinema_hall,
        show_time=movie_show_time)
    return movie_session


def get_movies_sessions(
        session_date: str = None
) -> QuerySet[MovieSession] | None:
    if session_date is None:
        return MovieSession.objects.all()
    session_date = datetime.strptime(session_date, "%Y-%m-%d").date()

    return MovieSession.objects.filter(show_time__date=session_date)


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None) -> MovieSession:
    session = MovieSession.objects.get(id=session_id)
    if show_time:
        if isinstance(show_time, str):
            show_time = datetime.fromisoformat(show_time)
        session.show_time = show_time
    if movie_id:
        movie = Movie.objects.get(id=movie_id)
        session.movie = movie
    if cinema_hall_id:
        cinema_hall = CinemaHall.objects.get(id=cinema_hall_id)
        session.cinema_hall = cinema_hall

    session.save()

    return session


def delete_movie_session_by_id(session_id: int) -> None:
    session = MovieSession.objects.get(id=session_id)
    session.delete()
