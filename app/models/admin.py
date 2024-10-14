import datetime
from flask_jwt_extended import create_access_token, decode_token
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
from app import db, bcrypt
from app.models.user_base import UserBase
from flask_login import UserMixin


class Admin(db.Model, UserBase, UserMixin):
    __tablename__ = 'admin'
    password_hash = db.Column(db.String(120), nullable=False)
    confirmed = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return f'Admin(name={self.name}), email={self.email}'

    @property
    def password(self):
        raise AttributeError('Password is write-only')

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)


    def generate_confirmation_token(self, expiration=3600):
        """
        Generuje token JWT do potwierdzenia konta z czasem ważności (domyślnie 1 godzina).

        :param expiration: Czas ważności tokenu w sekundach (domyślnie 3600 sekund)
        :return: Zwraca zakodowany token jako string
        """
        expires_delta = datetime.timedelta(seconds=expiration)

        token = create_access_token(identity=self.id, expires_delta=expires_delta)


        return token

    def confirm_token(self, token):
        """
        Weryfikuje i dekoduje token JWT.

        :param token: Token JWT do zweryfikowania
        :return: True, jeśli token jest poprawny, False w przypadku błędu
        """
        try:
            payload = decode_token(token)  # Dekodowanie tokenu
        except ExpiredSignatureError:
            print("Token expired.")
            return False
        except InvalidTokenError:
            print("Invalid token.")
            return False
        except Exception:
            return False

        # Odczytanie identity z sub (domyślne miejsce, gdzie create_access_token umieszcza identity)
        if str(payload.get('sub')) != str(self.id):
            print("Token doesn't match user ID")
            return False

        self.confirmed = True
        db.session.add(self)
        return True