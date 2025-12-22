


# REST = Representational State Transfer

===================================================

# charachteristic of REST:
import posixpath
- Statless: 
- client - server architecture
- standardization : (
    get
    post 
    patch = (particial update like : update name only)
    put = (compelete update- Hard reset if any value come null it will set it as null, doesn't matter if it is null or not)
    delete 
)
- easy to read : response come in : xml or json format


# ENDPOINT : 
    - web  : http://127.0.0.1:8000/students/
    - api : http://127.0.0.1:8000/api/students/


===================================================

# NOTES:

Serializer : it's help to convert the data into json or xml format.

