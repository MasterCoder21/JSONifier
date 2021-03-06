# JSONifier

---
## [Github](https://github.com/MasterCoder21/JSONifier)
## [PyPI](https://pypi.org/project/JSONifier/)
### A package for reading, writing, and editing of JSON files, Python dictionaries, and such.

---

# Classes

### **JSONifier**
Build a JSONifier object from a dict or a readable file. (Params and usage below)

      ...

      Params
      ----------
      *These params are used in the initialization of an instance of this class.*

      mode : str
          Define the mode in which to read and parse the given `data`.

      data : Any
          The data for the JSONifier object.

      Attributes
      ----------
      mode : str
          *Set when a new instance of the class is made.*

      data : Any
          *Set when a new instance of the class is made.*

      valid_modes : list
          *List of valid modes for instantiating a new JSONifier object.*

      call_methods : list
          *List of valid methods for the call function.*

      call_return_methods : list
          *List of valid methods for specifying how to get the instance data back from the call method.*

      write_methods : list
          *List of valid methods for writing to a json file.*

      Methods
      -------
      call(self, ret) - _builtin_
          The call function (calling an instance as a function).  `ret` is the return method.

      init(self, mode: str = None, data: Any = None) - _builtin_
          *Make a new instance.  Refer to `params` for information on the parameters.*

      @classmethod
      create(cls, mode, data)
          *Alternative constructor for the class.*

      @classmethod
      fromFile(cls, file)
          *Alternative constructor from a file path.*

      @classmethod
      fromDict(cls, file)
          *Alternative constructor from a supplied dictionary.*

      get_data(self)
          *Return the instance's data.*

      replace(self, key=None, value=None)
          *Replace the specified key with the specified value.*

      @staticmethod
      write(method="json", file=None, data=None)
          *Write to a specific file the data supplied.