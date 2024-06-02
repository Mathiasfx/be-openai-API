from jwt import decode, ExpiredSignatureError, InvalidTokenError, InvalidAlgorithmError, get_unverified_header

# Validation JWT in case expired [ UserModel or 401 ]
def auth_token(authorization):
    ACCESS_TOKEN_SECRET = "$2a$10$FAfiFosMXKTZajyRgFtijebf/BG33vJ3ZdyQsKfDkncD2rGICXIRq"

    # JWT expired return error 401
    if not authorization or not authorization.startswith('Bearer '):
        return {'message': 'Token has expired'}, 401

    hash_token = authorization.split(' ')[1]
    try:
        return decode(hash_token, ACCESS_TOKEN_SECRET, algorithms=['HS384'])
    except ExpiredSignatureError:
        return {'message': 'Token has expired'}, 401
    except InvalidAlgorithmError:
        return {'message': 'The specified algorithm is not allowed'}, 401
    except InvalidTokenError:
        return {'message': 'Invalid token'}, 401
