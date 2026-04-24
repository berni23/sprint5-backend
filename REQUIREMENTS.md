
Major requirements

* you should use python 3.13 or higher
* use uv for package management and development
* use classes
* use files to simulate a database. It can be json/csv/txt. Whatever you prefer
* use flask, fastapi or no framework at all.


The app should have:



* do operation endpoint. It should accept : two numbers and an operation
* get list of all operations done and the result

Minimum set of operations

* sum
* substract
* multiply
* divide

-> you HAVE to use enum for the operations
-> you HAVe to use classes as an entity for the data you will store in the files. EG : (user,operation,result,operations history,etc)
-> validate input data and return appropiate error messages if the data is not valid.

-> go as far as you want.

-> BONUS :

  * Add unit testing
  * THink about possible edge cases
  * think about how you would implement composed operations. EG: (2 + 3) * 4/2 ,...
  add an /about endpoint with some info on how the app works
